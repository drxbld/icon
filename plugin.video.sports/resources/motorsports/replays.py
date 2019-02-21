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
fanart = xbmc.translatePath(os.path.join(path, "resources/motorsports/background.jpg"))
h = HTMLParser()
wp = 'http://fullmatchtv.com/index.php/wp-json/wp/v2/posts?categories=973'

def get_url(**kwargs):
    kwargs = {k: unicode(v).encode('ascii', 'ignore') for k,v in kwargs.iteritems()}
    return '{0}?{1}'.format(_url, urlencode(kwargs))

def show_qualities(link, title):
    if 'ok.ru' in link:
        quals = okru(link)
    elif 'vidoza' in link:
        quals = vidoza(link)
    for quality, link in quals:
        combined = '%s | %s' % (quality, title)
        list_item = xbmcgui.ListItem(label=combined, path=link)
        list_item.setArt({'fanart':fanart,'thumb':icon,'poster':icon})
        list_item.setInfo('video', {'title': combined})
        list_item.setProperty('IsPlayable','true')
        xbmcplugin.addDirectoryItem(_handle, link, list_item, False)
        
    xbmcplugin.addSortMethod(_handle, xbmcplugin.SORT_METHOD_TITLE)
    xbmcplugin.endOfDirectory(_handle)
    

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
    
def vidoza(link):
    qual_list = []
    vidoza_resp = requests.get(link).content
    if vidoza_resp == 'File was deleted':
        qual_list.append(('[COLOR red]File was deleted[/COLOR]', ''))
        return qual_list
    try:
        vidoza_re = re.compile('sources:\s*(\[.+?\]),')
        sources = eval(vidoza_re.findall(vidoza_resp)[0].replace('file','"file"').replace('label','"label"'))
        for source in sources:
            qual_list.append((source['label'], source['file']))
        return qual_list
    except:
        pass
    try:
        vidoza_re = re.compile('player\.updateSrc\((\[.+?\])\)', re.DOTALL)
        sources = eval(vidoza_re.findall(vidoza_resp)[0].replace('src','"src"').replace('type','"type"').replace('label','"label"').replace('res','"res"'))
        for source in sources:
            qual_list.append((source['res']+'p', source['src']))
        return qual_list
    except: 
        return qual_list
        
def get_races(page=1):
    iframes = re.compile('<(?:IFRAME.+?SRC=|iframe.+?src=)[\'"](?!.{0,8}openload)(.+?[^\s])[\'"]')
    resp = requests.get(wp + '&page=' + str(page))
    if resp.status_code != 400:
        currentCount = 0
        for game in resp.json():
            content = game['content']['rendered']
            title = game['title']['rendered'].replace('&#8211;','|').replace(' at ',' vs ')
            if title.count('|') > 1:
                title = title.replace('| Dual','Dual')
            description = re.compile('<h2>(.+?)</h2>').findall(game['content']['rendered'])[0]
            description = description.replace(' &#8211; ','\n')

            d = title.split(' | ')[1]
            parsed_date = time.strptime(d, '%b %d, %Y')
            d = str(time.strftime("%m.%d.%Y", parsed_date))
            t = title.split(' | ')[0]
            title = '%s | %s' % (d, t)
            
            sources = iframes.findall(content)
            for s, source in enumerate(sources):
                if not 'http' in source:
                    source = 'http:%s' % source
                list_item = xbmcgui.ListItem(label='%s (source #%s)' % (title, str(s+1)))
                list_item.setInfo('video', {'title': title, 'plot':description})
                list_item.setArt({'fanart':fanart,'thumb':icon,'poster':icon})
                url = get_url(sport='motorsports', endpoint='replays', link=source, title=title)
                xbmcplugin.addDirectoryItem(_handle, url, list_item, True)
                currentCount += 1
        if currentCount > 0:
            list_item = xbmcgui.ListItem(label='[B]<<< EARLIER RACES[/B]')
            list_item.setArt({'fanart':fanart,'thumb':icon,'poster':icon})
            url = get_url(sport='motorsports', endpoint='replays', page=int(page)+1)
            xbmcplugin.addDirectoryItem(_handle, url, list_item, True)
        
    xbmcplugin.addSortMethod(_handle, xbmcplugin.SORT_METHOD_NONE)
    xbmcplugin.endOfDirectory(_handle)