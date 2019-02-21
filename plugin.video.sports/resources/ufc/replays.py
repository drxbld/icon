# encoding: utf-8
# -*- coding: utf-8 -*-
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import wait
from concurrent.futures import as_completed
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
fanart = xbmc.translatePath(os.path.join(path, "resources/ufc/background.jpg"))
h = HTMLParser()
dBase = 'http://fight.mmashare.club'
direct = 'http://fight.mmashare.club/viewforum.php?f=35'
wp = 'http://mmaversus.com/wp-json/wp/v2/posts?categories=7'
blogger = 'https://www.googleapis.com/blogger/v3/blogs/8362146453809730236' + \
          '/posts?maxResults=10&view=READER' + \
          '&key=AIzaSyDvnYVff5NGrP8gJqfaz1SvHs8XTM8PEus'
nextpage = '&pageToken={token}'

api_call = 'http://rutube.ru/api/play/options/{mediaId}/?format=json&no_404=true'

def get_url(**kwargs):
    try:
        kwargs = {k: unicode(v).encode('ascii', 'ignore') for k,v in kwargs.iteritems()}
    except:
        pass
    return '{0}?{1}'.format(_url, urlencode(kwargs))

def resolve(link, title):
    if 'rutube' in link:
        if link.endswith('/'):
            link = link[:-1]
        id = link.split('/')[-1]
        resp = requests.get(api_call.format(mediaId=id))
        if resp.json().get('video_balancer').get('m3u8') is not None:
            link = resp.json()['video_balancer']['m3u8'] + '|Referer=https://rutube.ru&User-Agent=' + \
                   'Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36'
            play_item = xbmcgui.ListItem(title, path=link)
            play_item.setProperty('IsPlayable','true')
            xbmcplugin.setResolvedUrl(_handle, True, listitem=play_item)
        else:
            xbmcgui.Dialog().ok('Sports Guru', 'Whoops, sorry about that! It looks like this fight has been deleted. Please select a different fight.')
            list_item = xbmcgui.ListItem('')
            xbmcplugin.setResolvedUrl(_handle, False, list_item)
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
    elif link.startswith('#'):
        list_item = xbmcgui.ListItem('')
        xbmcgui.Dialog().ok('Sports Guru', 'Whoops, sorry about that! It looks like this file has been deleted. Please select a different link.')
        xbmcplugin.setResolvedUrl(_handle, False, list_item)
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

def scrapeDirect(post):
    import _strptime
    postvals = re.compile('<a href=[\'"](.+?)[\'"] class=[\'"]topictitle[\'"]>(.+?)</a>.+?&raquo;\s*(.+?),', re.DOTALL)
    total_links = []
    postDetails = postvals.findall(post)
    for link, title, pDate in postDetails:
        if 'vs' in title and 'inside the octagon' not in title.lower():
            parsed_date = time.strptime(pDate, '%b %d. %Y')
            d = str(time.strftime("%m.%d.%Y", parsed_date))
            premiered = str(time.strftime("%Y-%m-%d", parsed_date))
            title = '%s | %s (Source #1)' % (d, title.title())
            
            fullLink = dBase + link[1:]
            ready = fullLink.replace('&amp;','&')
            while 'fight.mmashare.club' in ready:
                orig = ready
                resp = requests.get(ready).content
                try:
                    ready = re.compile('<source.+?src=[\'"](.+?)[\'"]').findall(resp)[0]
                    if ready.startswith('.'):
                        ready = dBase + ready[1:]
                    ready = ready.replace(' ','%20').replace('&amp;','&')
                    ready += '|User-Agent=Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
                    if not 'fight.mmashare.club' in ready:
                        break
                except:
                    pass
                if orig != ready.split('|')[0]:
                    continue
                try:
                    ready = re.compile('<iframe src="(.+?)"').findall(resp)[0]
                    ready = ready.replace(' ','%20').replace('&amp;','&')
                    if ready.startswith('.'):
                        ready = dBase + ready[1:]
                    if not 'fight.mmashare.club' in ready:
                        break
                except:
                    pass
                if orig != ready:
                    continue
                try:
                    dataUrl = re.compile('<div class="content">.+?(?:<a href=[\'"]|data-url=[\'"])(.+?)[\'"]', re.DOTALL)
                    ready = dataUrl.findall(resp)[0]
                    if ready.startswith('.'):
                        ready = dBase + ready[1:]
                    ready = ready.replace(' ','%20').replace('&amp;','&')
                    if not 'fight.mmashare.club' in ready:
                        break
                except:
                    pass
            total_links.append((title, ready, title))
        else:
            continue
    return total_links
    
def get_games(directPage=None, wpPage=1, bloggerToken=None):
    total_links = []
    if directPage != '':
        if directPage is None: 
            directPage = direct
        resp = requests.get(directPage).content
        origResp = resp
        postObjects = re.compile('<dt title="No unread posts">(.+?)</dt>', re.DOTALL).findall(resp)
        
        pool = ThreadPoolExecutor(10)
        futures = [pool.submit(scrapeDirect, post) for post in postObjects]
        [total_links.extend(r.result()) for r in as_completed(futures)]
        
        try:
            newDirectPage = dBase + re.compile('<li class="next"><a href="(.+?)"').findall(origResp)[0].replace('&amp;','&')[1:]
        except:
            newDirectPage = ''
    newWPpage = 0
    nextBloggerToken = ''
    
    iframes = re.compile('<(?:IFRAME.+?SRC=|iframe.+?src=)[\'"](?!.{0,8}openload)(.+?[^\s])[\'"]')
    currentCount = 0
    if wpPage > 0:
        resp = requests.get(wp + '&page=' + str(wpPage))
        if resp.status_code != 400:
            for game in resp.json():
                title = game['title']['rendered']
                if any(['U@F' in title, 'UFC' in title]) and not any(['Vlog' in title, 'WWE' in title]):
                    content = game['content']['rendered']
                    description = re.compile('p style="text-align: center;">(.+?)(?:<div|<p><iframe)', re.DOTALL).findall(content)[0]
                    description = " ".join(description.split())
                    description = description.replace('<strong>','').replace('</strong></p> <p style="text-align: center;">','\n')
                    description = description.replace('<br /> ','\n').replace('</p> ','').replace(' Fight Video ',' \n').replace('; ','\n')
                    description = description[:-4]
                    
                    d = game['date'].split('T')[0]
                    parsed_date = time.strptime(d, '%Y-%m-%d')
                    d = str(time.strftime("%m.%d.%Y", parsed_date))
                    t = title.replace('U@F', 'UFC').split(' Fight Video ')
                    title = '%s | %s (Source #2)' % (d, t[0])
                    
                    sources = iframes.findall(content)
                    for source in sources:
                        if not 'http' in source: source = 'http:%s' % source
                        total_links.append((title, source, description))
                        currentCount += 1
            if currentCount > 0:
                newWPpage = int(wpPage)+1
            else:
                newWPpage = 0
        else:
            newWPpage = 0
    
    if bloggerToken != '':
        bUrl = blogger
        if bloggerToken is not None:
            bUrl += nextpage.format(token=bloggerToken)
        resp = requests.get(bUrl).json()
        if resp.get('nextPageToken') is not None:
            nextBloggerToken = resp['nextPageToken']
        else:
            nextBloggerToken = ''
        for video in resp['items']:
            if 'Fight Video' in video['title']:
                links = iframes.findall(video['content'])
                
                title = video['title']
                d = video['published'].split('T')[0]
                parsed_date = time.strptime(d, '%Y-%m-%d')
                d = str(time.strftime("%m.%d.%Y", parsed_date))
                t = title.split(' Fight Video - ')
                title = '%s | %s (Source #3)' % (d, t[0])
                for source in links:
                    if not 'http' in source: source = 'http:%s' % source
                    total_links.append((title, source, title))
            else:
                continue
    
    
    total_links.sort(key=lambda tup: unicode(tup[0], errors='replace') if isinstance(tup[0], str) else tup[0], reverse=True)
    for title, ready, description in total_links:
        list_item = xbmcgui.ListItem(label=title)
        list_item.setInfo('video', {'title': title, 'plot':description})
        list_item.setArt({'fanart':fanart,'thumb':icon,'poster':icon})
        url = get_url(sport='ufc', endpoint='replays', link=ready.replace('&amp;','&'), title=title)
        if any([site in ready for site in ['ok.ru','dailymotion']]):
            xbmcplugin.addDirectoryItem(_handle, url, list_item, True)
        else:
            list_item.setProperty('IsPlayable','true')
            xbmcplugin.addDirectoryItem(_handle, url, list_item, False)
            
    if any([newDirectPage != '', newWPpage > 0, nextBloggerToken != '']):
        list_item = xbmcgui.ListItem(label='[B]<<< EARLIER FIGHTS[/B]')
        list_item.setArt({'fanart':fanart,'thumb':icon,'poster':icon})
        url = get_url(sport='ufc', endpoint='replays', directPage=newDirectPage, wpPage=newWPpage, bloggerToken=nextBloggerToken)
        xbmcplugin.addDirectoryItem(_handle, url, list_item, True)
        
    xbmcplugin.addSortMethod(_handle, xbmcplugin.SORT_METHOD_NONE)#xbmcplugin.SORT_METHOD_DATE)
    xbmcplugin.endOfDirectory(_handle)