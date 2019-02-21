# -*- coding: utf-8 -*-
from HTMLParser import HTMLParser
from urllib import urlencode
from urllib import unquote
import xbmcplugin
import xbmcaddon
import requests
import xbmcgui
import xbmc
import time
import json
import sys
import re
import os

_url = sys.argv[0]
_handle = int(sys.argv[1])
addon_id = 'plugin.video.sports'
addon = xbmcaddon.Addon(id=addon_id)
addonname = addon.getAddonInfo('name')
icon = addon.getAddonInfo('icon')
path = 'special://home/addons/%s/' % addon_id
fanart = xbmc.translatePath(os.path.join(path, "resources/xgames/background.jpg"))
h = HTMLParser()
channel = 'PLGSIEmIEDaU_otfvgAbbcwHS-L1_cMlD4'
base = 'https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=25' + \
       '&key=AIzaSyDvnYVff5NGrP8gJqfaz1SvHs8XTM8PEus&type=video&channelId=' + \
       'UCxFt75OIIvoN4AaL7lJxtTg&order=date'
events = '&q="FULL+BROADCAST"'
shows = '&q="FULL+SHOW"|"FULL+EPISODE"'
nextpage = '&pageToken={token}'
ytplay = 'plugin://plugin.video.youtube/?action=play_video&videoid={vid}'

def get_url(**kwargs):
    kwargs = {k: unicode(v).encode('ascii', 'ignore') for k,v in kwargs.iteritems()}
    return '{0}?{1}'.format(_url, urlencode(kwargs))

def get_videos(content, pageToken=None):
    if content == 'events':
        nexturl = base + events
        lookingfor = 'FULL BROADCAST'
    elif content == 'shows':
        nexturl = base + shows
        lookingfor = 'FULL SHOW'
    if pageToken is not None:
        nexturl += nextpage.format(token=pageToken)
    print nexturl
    resp = requests.get(nexturl)
    for i, video in enumerate(resp.json()['items']):
        t = video['snippet']['title']
        d = video['snippet']['description']
        d = d[:d.find('SUBSCRIBE')]
        id = video['id']['videoId']
        print t.encode('utf-8')
        if all([content == 'events', lookingfor in t]) or \
           all([content == 'shows', any([lookingfor in t, 'FULL EPISODE' in t])]):
            if not ':' in t and '-' in t:
                #Best of Aspen 2017 - FULL SHOW | World of X Games
                t = ' | '.join([t.split(' | ')[1], t.split(' - ')[0]])
            elif not ':' in t:
                #FULL BROADCAST | X Games Real Wake 2017
                t = t.split(' | ')[1]
            elif any([t.startswith('FULL BROADCAST:'), 
                      t.startswith('FULL SHOW:'), 
                      t.startswith('FULL EPISODE:')]):
                #FULL BROADCAST: The Real Cost Moto X QuarterPipe High Air Final | X Games Minneapolis 2017
                #FULL SHOW: Real Street 2018 | World of X Games
                #FULL EPISODE: Real BMX 2017 | X Games
                t = ' | '.join([t.split(' | ')[1], t.split(': ')[1].split(' | ')[0]])
            elif ':' in t and '|' in t:
                #Men’s Skateboard Street: FULL BROADCAST | X Games Norway 2018
                t = ' | '.join([t.split(' | ')[1], t.split(': ')[0]])
            list_item = xbmcgui.ListItem(label=t)
            list_item.setProperty('IsPlayable','true')
            list_item.setInfo('video', {'title': t, 'plot':d})
            list_item.setArt({'fanart':fanart,'thumb':icon,'poster':icon})
            url = ytplay.format(vid=id)
            xbmcplugin.addDirectoryItem(_handle, url, list_item, False)
    if resp.json().get('nextPageToken') is not None and len(resp.json()['items']) > 0:
        list_item = xbmcgui.ListItem(label='[B]<<< EARLIER EVENTS[/B]')
        list_item.setArt({'fanart':fanart,'thumb':icon,'poster':icon})
        url = get_url(sport='xgames', endpoint='replays', content=content, page=resp.json()['nextPageToken'])
        xbmcplugin.addDirectoryItem(_handle, url, list_item, isFolder=True)
    xbmcplugin.addSortMethod(_handle, xbmcplugin.SORT_METHOD_NONE)
    xbmcplugin.endOfDirectory(_handle)