# encoding: utf-8
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
fanart = xbmc.translatePath(os.path.join(path, "resources/boxing/background.jpg"))
h = HTMLParser()
wp = 'http://allthebestfights.com/wp-json/wp/v2/posts?categories=7'
ytplay = 'plugin://plugin.video.youtube/?action=play_video&videoid={vid}'

def get_url(**kwargs):
    try:
        kwargs = {k: unicode(v).encode('ascii', 'ignore') for k,v in kwargs.iteritems()}
    except:
        pass
    return '{0}?{1}'.format(_url, urlencode(kwargs))

def show_qualities(link, title):
    if 'youtube' in link:
        id = link.split('embed/')[1].split('?')[0]
        url = ytplay.format(vid=id)
        list_item = xbmcgui.ListItem(label=title, path=url)
        list_item.setProperty('IsPlayable','true')
        list_item.setInfo('video', {'title': title})
        list_item.setArt({'fanart':fanart,'thumb':icon,'poster':icon})
        xbmcplugin.setResolvedUrl(_handle, True, listitem=list_item)
    elif 'streamable' in link:
        resp = requests.get(link).content
        link = re.compile('<video.+?src=[\'"](.+?)[\'"]', re.DOTALL).findall(resp)[0]
        if link.startswith('//'): link = 'https:%s' % link
        link = link.replace('&amp;','&')
        play_item = xbmcgui.ListItem(title, path=link)
        play_item.setProperty('IsPlayable','true')
        xbmcplugin.setResolvedUrl(_handle, True, listitem=play_item)
    elif 'dailymotion' in link:
        quals = dailymotion(link)
        for quality, vlink in quals:
            combined = '%s | %s' % (quality, title)
            list_item = xbmcgui.ListItem(label=combined, path=vlink)
            list_item.setArt({'fanart':fanart,'thumb':icon,'poster':icon})
            list_item.setInfo('video', {'title': combined})
            list_item.setProperty('IsPlayable','true')
            xbmcplugin.addDirectoryItem(_handle, vlink, list_item, False)
        xbmcplugin.addSortMethod(_handle, xbmcplugin.SORT_METHOD_TITLE)
        xbmcplugin.endOfDirectory(_handle)
    elif 'sendvid' in link:
        resp = requests.get(link).content
        link = re.compile('<source.+?src=[\'"](.+?)[\'"]').findall(resp)[0].replace(' ','%20')
        play_item = xbmcgui.ListItem(title, path=link)
        play_item.setProperty('IsPlayable','true')
        xbmcplugin.setResolvedUrl(_handle, True, listitem=play_item)
    elif 'ok.ru' in link:
        quals = okru(link)
        for quality, link in quals:
            combined = '%s | %s' % (quality, title)
            list_item = xbmcgui.ListItem(label=combined, path=link)
            list_item.setArt({'fanart':fanart,'thumb':icon,'poster':icon})
            list_item.setInfo('video', {'title': combined})
            list_item.setProperty('IsPlayable','true')
            xbmcplugin.addDirectoryItem(_handle, link, list_item, False)
        xbmcplugin.addSortMethod(_handle, xbmcplugin.SORT_METHOD_TITLE)
        xbmcplugin.endOfDirectory(_handle)
    elif 'mp4' in link:
        play_item = xbmcgui.ListItem(title, path=link)
        play_item.setProperty('IsPlayable','true')
        xbmcplugin.setResolvedUrl(_handle, True, listitem=play_item)
    else:
        print 'Unresolved link is ' + link
        xbmcgui.Dialog().ok('Sports Guru', 'Whoops, sorry about that! It looks like this provider is not yet supported. Please select a different fight.')
        list_item = xbmcgui.ListItem('')
        xbmcplugin.setResolvedUrl(_handle, False, list_item)
        
def okru(link):      
    qual_list = []
    okru_resp = requests.get(link).content
    if len(re.compile('OK\.VideoPlayer\.yandexError\(\'COPYRIGHTS_RESTRICTED\'\);').findall(okru_resp)) > 0:
        qual_list.append(('[COLOR red]File was deleted[/COLOR]', ''))
        return qual_list
    try:
        okru_re = re.compile('data-module="OKVideo" data-options="(.+?)"')
        jumbled_json = okru_re.findall(okru_resp)[0]
        unjumbled = h.unescape(jumbled_json).decode("utf-8")
        j_obj = json.loads(unjumbled)
        metadata = j_obj['flashvars']['metadata']
        m_obj = json.loads(metadata)
        m_obj.pop('metadataEmbedded')
        qual_map = {'ultra': '2160p', 'quad': '1440p', 'full': '1080p', 'hd': '720p', 
                    'sd': '480p', 'low': '360p', 'lowest': '240p', 'mobile': '144p'}
        for video in m_obj['videos']:
            qual_list.append((qual_map[video['name'].lower()], video['url']))
        return qual_list
    except: return qual_list
    
def dailymotion(link):
    if not '/embed/' in link:
        link = 'http://www.dailymotion.com/embed/video/%s' % link.split('/')[-1]
    qual_list = []
    resp = requests.get(link, headers={'Cookie':'family_filter=off; ff=off'}).content
    jsonStr = re.compile('var\s*(?:config|__PLAYER_CONFIG__)\s*\=\s*(\{.+?\}\});', re.DOTALL).findall(resp)[0]
    j_obj = json.loads(jsonStr)
    if j_obj.get('metadata').get('error') is not None:
        qual_list.append(('[COLOR red]File was deleted[/COLOR]', ''))
        return qual_list
    try:
        for qual, links in j_obj['metadata']['qualities'].iteritems():
            for form in links:
                if form['type'] == 'video/mp4':
                    t = '%sp' % qual
                else:
                    continue
                final = form['url'] + '|User-Agent=Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36'
                qual_list.append((t, final))
        return qual_list
    except: return qual_list
    
def get_games(page=1):
    iframes = re.compile('<(?:IFRAME.+?SRC=|iframe.+?src=)[\'"](?!.{0,8}openload)(.+?[^\s])[\'"]')
    resp = requests.get(wp + '&page=' + str(page))
    if resp.status_code != 400:
        currentCount = 0
        for game in resp.json():
            content = game['content']['rendered']
            title = game['title']['rendered'].replace('&#8211;','|').replace(' at ',' vs ')
            if not 'full fight' in title.lower():
                continue

            d = game['date'].split('T')[0]
            parsed_date = time.strptime(d, '%Y-%m-%d')
            d = str(time.strftime("%m.%d.%Y", parsed_date))
            t = title.split(' | full fight')[0]
            title = '%s | %s' % (d, t)
            
            source = iframes.findall(content)[0]
            if source.startswith('//'):
                source = 'http:' + source
            list_item = xbmcgui.ListItem(label=title)
            list_item.setInfo('video', {'title': title})
            list_item.setArt({'fanart':fanart,'thumb':icon,'poster':icon})
            url = get_url(sport='boxing', endpoint='replays', link=source, title=title)
            if any([site in source for site in ['ok.ru','dailymotion']]):
                xbmcplugin.addDirectoryItem(_handle, url, list_item, True)
            else:
                list_item.setProperty('IsPlayable','true')
                xbmcplugin.addDirectoryItem(_handle, url, list_item, False)
            currentCount += 1
        if currentCount > 0:
            list_item = xbmcgui.ListItem(label='[B]<<< EARLIER FIGHTS[/B]')
            list_item.setArt({'fanart':fanart,'thumb':icon,'poster':icon})
            url = get_url(sport='boxing', endpoint='replays', page=int(page)+1)
            xbmcplugin.addDirectoryItem(_handle, url, list_item, True)
        
    xbmcplugin.addSortMethod(_handle, xbmcplugin.SORT_METHOD_NONE)
    xbmcplugin.endOfDirectory(_handle)