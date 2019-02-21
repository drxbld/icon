# -*- coding: utf-8 -*-
#
# Copyright (C) 2016 RACC
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import unicode_literals

import xbmc
import xbmcgui
import xbmcaddon
import xbmcplugin
from xbmcgui import ListItem
from routing import Plugin

import sys
import os
import traceback

import requests
from base64 import urlsafe_b64encode
from datetime import timedelta
from requests_cache import CachedSession

try:
    from urllib.parse import quote_from_bytes as orig_quote
except ImportError:
    from urllib import quote as orig_quote
try:
    from urllib.parse import unquote_to_bytes as orig_unquote
except ImportError:
    from urllib import unquote as orig_unquote


addon = xbmcaddon.Addon()
plugin = Plugin()
plugin.name = addon.getAddonInfo("name")
user_agent = "Dalvik/2.1.0 (Linux; U; Android 5.1.1; AFTS Build/LVY48F)"
USER_DATA_DIR = xbmc.translatePath(addon.getAddonInfo("profile")).decode("utf-8")  # !!
CACHE_TIME = int(addon.getSetting("cache_time"))
CACHE_FILE = os.path.join(USER_DATA_DIR, "cache")
expire_after = timedelta(hours=CACHE_TIME)

if not os.path.exists(USER_DATA_DIR):
    os.makedirs(USER_DATA_DIR)

s = CachedSession(CACHE_FILE, allowable_methods="GET", expire_after=expire_after, old_data_on_error=True)
s.hooks = {"response": lambda r, *args, **kwargs: r.raise_for_status()}
s.headers.update({"User-Agent": user_agent})

data_url = "http://swiftstreamz.com/SwiftLive/swiftlive.php"
api_url = "http://swiftstreamz.com/SwiftLive/api.php"
list_url = "http://swiftstreamz.com/SwiftLive/api.php?cat_id={0}"
thumb_url = "http://swiftstreamz.com/SwiftLive/images/thumbs/{0}|User-Agent={1}"

USER = "SwiftStreamz"
PASS = "@SwiftStreamz@"

def quote(s, safe=""):
    return orig_quote(s.encode("utf-8"), safe.encode("utf-8"))


def unquote(s):
    return orig_unquote(s).decode("utf-8")


@plugin.route("/refresh")
def refresh():
    s.cache.clear()
    xbmc.executebuiltin("Container.Refresh")


@plugin.route("/")
def root():
    r = s.get(api_url, headers={"User-Agent": user_agent}, timeout=10)
    res = r.json(strict=False)

    list_items = []
    for cat in res["LIVETV"]:
        li = ListItem(cat["category_name"])
        li.setArt({"thumb": thumb_url.format(cat["category_image"], quote(user_agent))})
        url = plugin.url_for(list_channels, cat_id=cat["cid"])
        list_items.append((url, li, True))

    xbmcplugin.addDirectoryItems(plugin.handle, list_items)
    xbmcplugin.endOfDirectory(plugin.handle)


@plugin.route("/list_channels/<cat_id>")
def list_channels(cat_id=None):
    list_items = []
    r = s.get(list_url.format(cat_id), headers={"User-Agent": user_agent}, timeout=10)
    res = r.json(strict=False)

    refresh_streams = "RunPlugin({0})".format(plugin.url_for(refresh))
    for ch in res["LIVETV"]:
        image = thumb_url.format(ch["channel_thumbnail"], quote(user_agent))
        li = ListItem(ch["channel_title"])
        li.setProperty("IsPlayable", "true")
        li.addContextMenuItems([("Refresh Streams", refresh_streams)])
        li.setArt({"thumb": image, "icon": image})
        li.setInfo(type="Video", infoLabels={"Title": ch["channel_title"], "mediatype": "video", "playcount": 0})
        try:
            li.setContentLookup(False)
        except AttributeError:
            pass
        url = plugin.url_for(play, cat_id=cat_id, channel_id=ch.get("id"))
        list_items.append((url, li, False))

    xbmcplugin.addDirectoryItems(plugin.handle, list_items)
    xbmcplugin.endOfDirectory(plugin.handle)


@plugin.route("/play/<cat_id>/<channel_id>/play.pvr")
def play(cat_id, channel_id):
    r = s.get(list_url.format(cat_id), headers={"User-Agent": user_agent}, timeout=10)
    res = r.json(strict=False)

    for ch in res["LIVETV"]:
        if ch.get("id") == channel_id:
            title = ch.get("channel_title")
            image = thumb_url.format(ch.get("channel_thumbnail"), quote(user_agent))
            channel_url = ch.get("channel_url")

    fix_token = ""
    r = s.get(data_url, headers={"User-Agent": user_agent}, auth=(USER, PASS), timeout=10)
    data = r.json(strict=False)

    if data["DATA"][0]["HelloUrl"] in channel_url or data["DATA"][0]["HelloUrl1"] in channel_url:
        auth_url = data["DATA"][0]["HelloLogin"]
        auth_auth = tuple(data["DATA"][0]["PasswordHello"].split(":"))
    elif data["DATA"][0]["LiveTvUrl"] in channel_url:
        auth_url = data["DATA"][0]["LiveTvLogin"]
        auth_auth = tuple(data["DATA"][0]["PasswordLiveTv"].split(":"))
        fix_token = "y"
    elif data["DATA"][0]["nexgtvUrl"] in channel_url:
        auth_url = data["DATA"][0].get("nexgtvToken", data["DATA"][0].get("nexgtvtoken1"))
        auth_auth = tuple(data["DATA"][0]["nexgtvPass"].split(":"))
    else:
        auth_url = data["DATA"][0]["loginUrl"]
        auth_auth = tuple(data["DATA"][0]["Password"].split(":"))
        fix_token = "y"

    with s.cache_disabled():
        r = s.get(auth_url, headers={"User-Agent": user_agent}, auth=auth_auth, timeout=10)
        auth_token = r.text.partition("=")[2]

    if fix_token:
        auth_token = "".join([auth_token[:-59], auth_token[-58:-47], auth_token[-46:-35], auth_token[-34:-23], auth_token[-22:-11], auth_token[-10:]])

    if "playlist.m3u8" in channel_url:
        media_url = "{0}?wmsAuthSign={1}|User-Agent={2}".format(channel_url, auth_token, quote(data["DATA"][0].get("Agent", user_agent)))
        if addon.getSetting("inputstream") == "true":
            li = ListItem(title, path=media_url)
            li.setArt({"thumb": image, "icon": image})
            li.setMimeType("application/vnd.apple.mpegurl")
            li.setProperty("inputstreamaddon", "inputstream.adaptive")
            li.setProperty("inputstream.adaptive.manifest_type", "hls")
            li.setProperty("inputstream.adaptive.stream_headers", media_url.split("|")[-1])
        elif addon.getSetting("livestreamer") == "true":
            serverPath = os.path.join(xbmc.translatePath(addon.getAddonInfo("path")), "livestreamerXBMCLocalProxy.py")
            runs = 0
            while not runs > 10:
                try:
                    requests.get("http://127.0.0.1:19001/version")
                    break
                except Exception:
                    xbmc.executebuiltin("RunScript(" + serverPath + ")")
                    runs += 1
                    xbmc.sleep(600)
            livestreamer_url = "http://127.0.0.1:19001/livestreamer/" + urlsafe_b64encode("hlsvariant://" + media_url)
            li = ListItem(title, path=livestreamer_url)
            li.setArt({"thumb": image, "icon": image})
            li.setMimeType("video/x-mpegts")
        else:
            li = ListItem(title, path=media_url)
            li.setArt({"thumb": image, "icon": image})
            li.setMimeType("application/vnd.apple.mpegurl")
    else:
        media_url = "{0}?wmsAuthSign={1}|User-Agent={2}".format(channel_url, auth_token, quote(data["DATA"][0].get("Agent", user_agent)))
        li = ListItem(title, path=media_url)
        li.setArt({"thumb": image, "icon": image})
        li.setMimeType("video/x-mpegts")

    try:
        li.setContentLookup(False)
    except AttributeError:
        pass

    xbmcplugin.setResolvedUrl(plugin.handle, True, li)


if __name__ == "__main__":
    try:
        plugin.run(sys.argv)
    except requests.exceptions.RequestException as e:
        dialog = xbmcgui.Dialog()
        dialog.notification(plugin.name, str(e), xbmcgui.NOTIFICATION_ERROR)
        traceback.print_exc()
        xbmcplugin.endOfDirectory(plugin.handle, False)
