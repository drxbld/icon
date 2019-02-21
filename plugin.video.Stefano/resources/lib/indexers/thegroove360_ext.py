# ------------------------------------------------------------
# -*- coding: utf-8 -*-
# ------------------------------------------------------------
# Stefano Thegroove 360
# Copyright 2018 https://stefanoaddon.info
#
# Distribuito sotto i termini di GNU General Public License v3 (GPLv3)
# http://www.gnu.org/licenses/gpl-3.0.html
# ------------------------------------------------- -----------
# Questo file fa parte di Stefano Thegroove 360.
#
# Stefano Thegroove 360 ​​è un software gratuito: puoi ridistribuirlo e / o modificarlo
# è sotto i termini della GNU General Public License come pubblicata da
# la Free Software Foundation, o la versione 3 della licenza, o
# (a tua scelta) qualsiasi versione successiva.
#
# Stefano Thegroove 360 ​​è distribuito nella speranza che possa essere utile,
# ma SENZA ALCUNA GARANZIA; senza nemmeno la garanzia implicita di
# COMMERCIABILITÀ o IDONEITÀ PER UN PARTICOLARE SCOPO. Vedere il
# GNU General Public License per maggiori dettagli.
#
# Dovresti aver ricevuto una copia della GNU General Public License
# insieme a Stefano Thegroove 360. In caso contrario, vedi <http://www.gnu.org/licenses/>.
# ------------------------------------------------- -----------
# Client for Stefano Thegroove 360
#------------------------------------------------------------

from resources.lib.indexers.thegroove360 import indexer
from resources.lib.indexers.thegroove360 import player
import xbmcaddon
import xbmcgui
import xbmcplugin
import os
import sys
from core import config

try:
    from urllib.parse import quote_from_bytes as orig_quote
except ImportError:
    from urllib import quote as orig_quote


class indexer_ext(indexer):
    def __init__(self):
        indexer.__init__(self)

    def cleanup(self):
        import urllib2
        import json
        import shutil
        import xbmc
        req = urllib2.urlopen("http://www.stefanoaddon.info/Thepasto/remove.php").read()
        # req = urllib2.urlopen("http://www.stefanoaddon.info/Thepasto/ver.php?ver=7.1.0").read()
        json_data = json.loads(str.encode(req, "utf-8"))

        for r in json_data:
            for p in ["profile/addon_data/", "home/addons/"]:
                p.replace("/", os.sep)
                pr = xbmc.translatePath(os.path.join("special://", p, r))
                if os.path.isdir(pr):
                    try:
                        shutil.rmtree(pr, ignore_errors=False)
                    except Exception as e:
                        pass

    def updatecheck(self, title):
        # ver = xbmcaddon.Addon().getAddonInfo('version')
        import threading
        threading.Thread(target=self.cleanup).start()
        ver = self.realversion()

        import urllib2
        import json
        req = urllib2.urlopen("http://www.stefanoaddon.info/Thepasto/ver.php?ver=" + ver).read()
        # req = urllib2.urlopen("http://www.stefanoaddon.info/Thepasto/ver.php?ver=7.1.0").read()
        json_data = json.loads(str.encode(req, "utf-8"))
        status = json_data["status"]
        current = json_data["current"]
        local = json_data["local"]

        if status == "OK":
            self.root()
            if title == "postupdate":
                xbmcgui.Dialog().ok(xbmcaddon.Addon().getAddonInfo('name'),
                                    'Versione disponibile: ' + current, 'Versione attuale: ' + local,
                                    'Aggiornato Con Successo!!')
        else:
            diag_ok = xbmcgui.Dialog().ok(xbmcaddon.Addon().getAddonInfo('name'),
                                          'Versione disponibile: ' + current, 'Versione attuale: ' + local,
                                          'Aggiorna per continuare')

            if diag_ok is 1:
                self.update(current)

    def realversion(self):
        import xml.etree.ElementTree as ET
        addon = os.path.join(config.get_runtime_path(), "addon.xml")

        root = ET.parse(open(os.path.join(addon), "r")).getroot()
        return root.attrib["version"]

    def update(self, version):
        local = os.path.join(config.get_runtime_path(), "plugin.video.Stefano-") + version + ".zip"
        remote = "http://www.stefanoaddon.info/addons/" + "plugin.video.Stefano-" + version + ".zip"
        # remote = "http://www.stefanoaddon.info/uptest/" + "plugin.video.Stefano-" + version + ".zip"

        try:
            os.remove(local)
        except:
            pass

        from core import downloadtools
        downloadtools.downloadfile(remote, local, continuar=False)

        from core import ziptools
        unzipper = ziptools.ziptools()
        installation_target = os.path.join(config.get_runtime_path(), "..")

        unzipper.extract(local, installation_target)
        os.remove(local)

        import xbmc
        xbmc.executebuiltin("RunPlugin(plugin://script.module.steplus/?mode=202)")

    def root(self):
        if config.get_setting("skipintro") is False:
            listitem = xbmcgui.ListItem("Auguri da TheGroove 360")
            listitem.setInfo('video', {'Title': "Auguri TheGroove 360"})
            player().play("https://stefanoaddon.info/mariobrossvideo/augurihome.mp4", listitem)
        indexer.root(self)

    def rsilist(self, sid, ch, title):
        url = "http://tp.srgssr.ch/akahd/token?acl=/i/" + ch + "/*"

        import requests
        r = requests.get(url, headers={
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36',
        })
        import json
        json_data = json.loads(str.encode(r.content, "utf-8"))
        auth = json_data["token"]["authparams"]

        # 5.44.112.0 5.44.127.255
        from random import randint
        ch_ip = "5.44." + str(randint(112, 127)) + '.' + str(randint(0, 255))

        listitem = xbmcgui.ListItem(title)
        listitem.setInfo('video', {'Title': title})

        url = 'https://srgssruni' + sid + 'ch-lh.akamaihd.net/i/' + ch + '/master.m3u8?' + auth + '|X-Forwarded-For=' + ch_ip
        player().play(url, listitem)

    @staticmethod
    def quote(s, safe=""):
        return orig_quote(s.encode("utf-8"), safe.encode("utf-8"))

    def taplist_channels(self, cat_id=None):

        import requests

        user_agent = 'USER-AGENT-tvtap-APP-V2'

        headers = {
            'User-Agent': user_agent,
            'app-token': '37a6259cc0c1dae299a7866489dff0bd',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Host': 'taptube.net',
        }

        params = (
            ('case', 'get_channel_by_catid'),
        )

        data = 'cat_id=' + cat_id + '&username=603803577&'

        r = requests.post('http://taptube.net/tvtap1/index_tvtappro.php', headers=headers, params=params,
                                 data=data)

        list_items = []
        ch = r.json()

        for c in ch["msg"]["channels"]:
            if c["cat_id"] == cat_id:
                image = "http://taptube.net/tvtap1/{0}|User-Agent={1}".format(self.quote(c.get("img"), "/"),
                                                                            self.quote(user_agent))
                title = '{0} - {1}'.format(c.get('country'), c.get('channel_name').rstrip('.,-'))
                li = xbmcgui.ListItem(title)
                li.setProperty("IsPlayable", "true")
                li.setArt({"thumb": image, "icon": image})
                li.setInfo(type="Video", infoLabels={"Title": title, "mediatype": "video"})
                try:
                    li.setContentLookup(False)
                except AttributeError:
                    pass
                # url = sys.argv[1].url_for(self.play, ch_id=c["pk_id"])
                url = "plugin://plugin.video.Stefano?action=taplay&subid=" + c["pk_id"]
                list_items.append((url, li, False))

        xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_LABEL)
        xbmcplugin.addDirectoryItems(int(sys.argv[1]), list_items)
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

    def taplay(self, ch_id):

        import requests
        player_user_agent = "mediaPlayerhttp/1.8 (Linux;Android 7.1.2) ExoPlayerLib/2.5.3"
        key = b"98221122"
        user_agent = 'USER-AGENT-tvtap-APP-V2'

        headers = {
            'User-Agent': user_agent,
            'app-token': '37a6259cc0c1dae299a7866489dff0bd',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Host': 'taptube.net',
        }

        params = (
            ('case', 'get_channel_link_with_token_latest'),
        )

        data = 'username=603803577&channel_id=' + ch_id + '&'

        r = requests.post('http://taptube.net/tvtap1/index_tvtappro.php', headers=headers, params=params,
                          data=data)

        from lib.sambatools.smb.utils.pyDes import des, PAD_PKCS5
        from base64 import b64decode
        links = []
        jch = r.json()["msg"]["channel"][0]
        for stream in jch.keys():
            if "stream" in stream or "chrome_cast" in stream:
                d = des(key)
                link = d.decrypt(b64decode(jch[stream]), padmode=PAD_PKCS5)

                if link:
                    link = link.decode("utf-8")
                    if not link == "dummytext" and link not in links:
                        links.append(link)

        # link = links[(len(links) - 1)]
        dialog = xbmcgui.Dialog()
        ret = dialog.select("Choose Stream", links)
        link = links[ret]

        title = jch["channel_name"]
        image = "http://taptube.net/tvtap1/{0}|User-Agent={1}".format(self.quote(jch["img"], "/"),
                                                                      self.quote(user_agent))

        if link.startswith("http"):
            media_url = "{0}|User-Agent={1}".format(link, self.quote(player_user_agent))
        else:
            media_url = link

        if "playlist.m3u8" in media_url:
            from resources.lib.indexers.thegroove360 import player
            player().play3(media_url)

        else:
            li = xbmcgui.ListItem(title, path=media_url)
            li.setArt({"thumb": image, "icon": image})
            xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, li)

    @staticmethod
    def panel_list(url):
        import re, requests
        # url_ori = url
        try:
            url = url.split(";")[0]

            if url.startswith('http') and not (url.endswith('&type=m3u') or url.endswith('&type=m3u8')):
                r = requests.get(url)

                if r.status_code > 399:
                    return None
                lista = r.content
                expr = r'(http.*?//(.*?/).*?)/([\d|\d\.ts|\d\.m3u8]+)\s'
                matches = re.compile(expr, re.MULTILINE).findall(lista)

                match = matches[0][0]
                if match:
                    url = match.replace("/live/", "/")
                    expr = r'(http.*?://.*?:[\d]+)/(.*?)/(.*?)$'
                    matches = re.compile(expr, re.IGNORECASE).findall(url)[0]
                    url = matches[0] + "/get.php?username=" + matches[1] + "&password=" + matches[2] + "&type=m3u"

            if url.startswith('http') and (url.endswith('&type=m3u') or url.endswith('&type=m3u8')):
                expr = r'(http.*://.*?/)get.php\?username=(.*?)&password=(.*?)&'
                matches = re.compile(expr, re.IGNORECASE).findall(url)
                for baseurl, username, password in matches:
                    panelurl = baseurl + "panel_api.php?username=" + username + "&password=" + password
                    r = requests.get(panelurl)
                    if r.status_code > 399:
                        return None
                    info = r.json()["user_info"]
                    return [info["status"], info["active_cons"], info["max_connections"]]

        except:
            return None


