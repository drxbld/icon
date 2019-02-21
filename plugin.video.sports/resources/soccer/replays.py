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
fanart = xbmc.translatePath(os.path.join(path, "resources/soccer/background.jpg"))
h = HTMLParser()
efm_wp = 'http://eplfootballmatch.com/wp-json/wp/v2/posts?categories=3'
ffm_wp = 'http://footballfullmatch.com/wp-json/wp/v2/posts?categories=%s'
eplfootballmatch = {'English Premier League': 6,
                    'Spain La Liga': 16,
                    'Italian Serie A': 118,
                    'German Bundesliga': 163,
                    'Scottish Premier League': 8,
                    'French Ligue 1': 182,
                    'International Friendlies':158,
                    'World Cup':407}
footballfullmatch = {"English Premier League": "40",
                     "UEFA Europa League": "304",
                     "UEFA Champions League": "287",
                     "Italian Serie A": "63",
                     "Spain La Liga": "32",
                     "Scottish Premier League": "380",
                     "French Ligue 1": "154",
                     "German Bundesliga": "52",
                     "International Friendlies": "470",
                     "World Cup": "1109"}
           
def get_url(**kwargs):
    kwargs = {k: unicode(v).encode('ascii', 'ignore') for k,v in kwargs.iteritems()}
    return '{0}?{1}'.format(_url, urlencode(kwargs))

def resolve(link, content, title):
    print link
    if content and '<iframe' in content:                    
        #We can extract 1st & 2nd Half links and add them to a playlist
        starter = re.compile('</p> <p>(.+?)</p> <p>').findall(content)
        if 'Pre-match' in starter:
            segments = re.compile('src=[\'"](.+?)[\'"]').findall(content)[1:]
        else:
            segments = re.compile('src=[\'"](.+?)[\'"]').findall(content)
            
        pl = xbmc.PlayList(1)
        pl.clear()
        itemList = []
        for s, segment in enumerate(segments):
            if segment.startswith('//'): 
                segment = 'http:%s' % segment
            if s == 0: 
                Itemtitle = '%s (1st half)' % title
            elif s == 1: 
                Itemtitle = '%s (2nd half)' % title
            else: 
                break
            if 'ok.ru' in segment: 
                segment = okru(segment)
            if segment == '':
                pl.clear()
                line1 = 'Sorry, one or both replay links were removed due to copyright infringement.'
                xbmcgui.Dialog().ok(addonname, line1)
                break
            video_meta = xbmcgui.ListItem(Itemtitle)
            video_meta.setProperty('IsPlayable','true')
            
            pl.add(url=segment, listitem=video_meta)
            itemList.append(video_meta)
        if pl.size() > 0:
            xbmcplugin.setResolvedUrl(_handle, True, itemList[0])
    elif 'eplfootballmatch' in link:
        #We need to visit post page to get hola_player source
        postResp = requests.get(link)
        holaPlayer = re.compile('window.hola_player\(\{.+?sources:\s*\[\{.+?src:\s*[\'"](.+?)[\'"]')
        link = holaPlayer.findall(postResp.content)[0]
        play_item = xbmcgui.ListItem(title, path=link)
        play_item.setProperty('IsPlayable','true')
        xbmcplugin.setResolvedUrl(_handle, True, listitem=play_item)
    elif 'footballfullmatch' in link:
        pl = xbmc.PlayList(1)
        pl.clear()
        itemList = []
        resp = requests.get(link).content
        stream_links = []
        match_image = re.compile('<div id="videoplayer".+?style="background-image:url\(\'(.+?)\'\)').findall(resp)[0]
        video_titles = re.compile("<li\sdata\-index='\d{1,2}'\s?[class='active']*>(.+?)</li>").findall(resp)
        iframes = re.compile("var\svideoSelector\s+=\s+(\[.+?\]);").findall(resp)[0]
        for i, iframe in enumerate(iframes.split(',')):
            if not 'half' in video_titles[i]: 
                continue
            decoded_iframe = iframe.decode('string_escape').replace('\/','/')
            segment = re.compile('<iframe.+?src="(.+?)"').findall(decoded_iframe)[0]
            if segment.startswith('//'): 
                segment = 'http:%s' % segment
            if 'openload' in segment or 'allplayer' in segment: 
                continue
            if 'ok.ru' in segment: 
                segment = okru(segment)
            if segment == '':
                pl.clear()
                line1 = 'Sorry, one or both replay links were removed due to copyright infringement.'
                xbmcgui.Dialog().ok(addonname, line1)
                break
            
            if len(itemList) == 0: 
                Itemtitle = '%s (1st Half)' % title
            else: 
                Itemtitle = '%s (2nd Half)' % title
            video_meta = xbmcgui.ListItem(Itemtitle)
            video_meta.setProperty('IsPlayable','true')
            
            pl.add(url=segment, listitem=video_meta)
            itemList.append(video_meta)
            if len(itemList) == 2: 
                break
        if pl.size() > 0:
            xbmcplugin.setResolvedUrl(_handle, True, itemList[0])

def okru(link):      
    okru_resp = requests.get(link).content
    if len(re.compile('OK\.VideoPlayer\.yandexError\(\'COPYRIGHTS_RESTRICTED\'\);').findall(okru_resp)) > 0:
        return ''
    try:
        okru_re = re.compile('data-module="OKVideo" data-options="(.+?)"')
        jumbled_json = okru_re.findall(okru_resp)[0]
        unjumbled = h.unescape(jumbled_json).decode("utf-8")
        j_obj = json.loads(unjumbled)
        metadata = j_obj['flashvars']['metadata']
        m_obj = json.loads(metadata)
        m_obj.pop('metadataEmbedded')
        qual_map = {'ultra': '2160', 'quad': '1440', 'full': '1080', 'hd': '720', 
                    'sd': '480', 'low': '360', 'lowest': '240', 'mobile': '144'}
        best_qual = 'mobile'
        for video in m_obj['videos']:
            if int(qual_map[video['name'].lower()]) > int(qual_map[best_qual]):
                link = video['url']
                best_qual = video['name'].lower()
        return link
    except: return ''
        
def get_matches(league, page=1):
    if eplfootballmatch.get(league) or footballfullmatch.get(league):
        #League category exists, collect games
        if eplfootballmatch.get(league):
            l = eplfootballmatch[league]
            resp = requests.get(efm_wp + '&page=' + str(page))
            if resp.status_code != 400:
                for game in resp.json():
                    if l in game['categories']:
                        try:
                            image_resp = requests.get(game['_links']['wp:featuredmedia'][0]['href'])
                            image_json = json.loads(image_resp.text)
                            image = image_json['guid']['rendered']
                        except: 
                            image = icon
                            
                        link = game['link']
                        content = game['content']['rendered']
                        title = h.unescape(game['title']['rendered'].replace('&#8211;','-').encode('ascii', 'ignore').replace('  ',' - '))
                        print title
                        title = title.replace(' - Full Match','').replace('|  Full Match','')
                        title = title.replace(' | International Football','').replace(' | International Friendly Match','')
                        title = title.replace(' | Full Match Replay','').replace(' | Full Match','')
                        title = title.replace(' | EPL','').replace(' | Premier League','')
                        title = title.replace(' | Friday Night Football','').replace(' | Skysports','')
                        title = title.replace(' | La Liga','').replace(' | El Clasico','')
                        title = title.replace(' | Serie A','').replace(' |  Serie A','')
                        title = title.replace(' | Bundesliga','').replace(' | Scottish Premiership','')
                        title = title.replace(' | Ligue 1','').replace(' |  Ligue 1','')
                        title = title.replace(' v ',' vs ')
                        try:
                            d = title.split(' | ')[1]
                            if '.' in d:
                                parsed_date = time.strptime(d, '%d.%m.%Y')
                            elif '-' in d:
                                parsed_date = time.strptime(d, '%d-%m-%Y')
                            elif 'day' in d:
                                parsed_date = time.strptime(d, '%A %d %B %Y')
                            d = str(time.strftime("%m.%d.%Y", parsed_date))
                            t = title.split(' | ')[0]
                            title = '%s | %s' % (d, t)
                        except:
                            try:
                                d = game['date'].split('T')[0]
                                parsed_date = time.strptime(d, '%Y-%m-%d')
                                d = str(time.strftime("%m.%d.%Y", parsed_date))
                                title = '%s | %s' % (d, title)
                            except:
                                pass
                        list_item = xbmcgui.ListItem(label=title)
                        list_item.setInfo('video', {'title': title})
                        list_item.setArt({'fanart':fanart,'thumb':icon,'poster':icon})
                        list_item.setProperty('IsPlayable','true')
                        url = get_url(sport='soccer', endpoint='replays', link=link, data=content, title=title)
                        xbmcplugin.addDirectoryItem(_handle, url, list_item, False)
        if footballfullmatch.get(league):
            l = footballfullmatch[league]
            resp = requests.get(ffm_wp % l + '&page=' + str(page))
            if resp.status_code != 400: 
                for game in resp.json():
                    try:
                        image_resp = requests.get(game['_links']['wp:featuredmedia'][0]['href'])
                        image_json = json.loads(image_resp.text)
                        image = image_json['guid']['rendered']
                    except: 
                        image = icon
                    title = game['title']['rendered']
                    excerpt = game['excerpt']['rendered']
                    dre = re.compile('>[\s\n]*(?!.*<br /)(.+?)</p>\s*$').findall(excerpt)[0]
                    parsed_date = time.strptime(dre, '%A, %d %B %Y')
                    d = str(time.strftime("%m.%d.%Y", parsed_date))
                    title = '%s | %s' % (d, title)
                    link = game['link']
                    list_item = xbmcgui.ListItem(label=title)
                    list_item.setInfo('video', {'title': title})
                    list_item.setArt({'fanart':fanart,'thumb':icon,'poster':icon})
                    list_item.setProperty('IsPlayable','true')
                    url = get_url(sport='soccer', endpoint='replays', link=link, title=title)
                    xbmcplugin.addDirectoryItem(_handle, url, list_item, False)
                    
                list_item = xbmcgui.ListItem(label='[B]<<< EARLIER MATCHES[/B]')
                list_item.setArt({'fanart':fanart,'thumb':icon,'poster':icon})
                url = get_url(sport='soccer', league=league, endpoint='replays', page=int(page)+1)
                xbmcplugin.addDirectoryItem(_handle, url, list_item, True)
        xbmcplugin.addSortMethod(_handle, xbmcplugin.SORT_METHOD_NONE)
        xbmcplugin.endOfDirectory(_handle)
    else:
        line1 = 'The current Full-Game Replay Source(s) do not cover this league yet.'
        xbmcgui.Dialog().ok(addonname, line1)