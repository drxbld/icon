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
fanart = xbmc.translatePath(os.path.join(path, "resources/lfl/background.jpg"))
h = HTMLParser()
current = 'PLfS4i_GXOfPxRFwON3hLqwBOoihg7eWqk'
past = 'PLfS4i_GXOfPzestgSDJlG2PWwCs1TTLmZ'
base = 'https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=24' + \
       '&key=AIzaSyDvnYVff5NGrP8gJqfaz1SvHs8XTM8PEus&playlistId={pid}'
searchquarters = base.replace('playlistItems', 'search').replace('maxResults=24', 'maxResults=12')
searchquarters += '&type=video&q={query}'
nextpage = '&pageToken={token}'
ytplay = 'plugin://plugin.video.youtube/?action=play_video&videoid={vid}'




#LFL | WEEK 6 | 2018 SEASON | NASHVILLE KNIGHTS vs SEATTLE | FULL GAME
fullgame = re.compile('^LFL\s\|\s((?:GAME|WEEK)\s\d{1,2})\s\|\s(\d{4}\sSEASON)\s\|\s(.+?(?:vs|AT).+?)\s\|\sFULL\sGAME$')

#LFL | 2017 SEASON | WEEK 6 | DENVER DREAM AT SEATTLE MIST | 1ST QUARTER
#LFL | WEEK 1 | 2018 SEASON | LOS ANGELES TEMPTATION vs CHICAGO BLISS | 1ST QUARTER
quarter = re.compile('^LFL\s\|\s((\d{4}\sSEASON)\s\|\s((?:GAME|WEEK)\s\d{1,2})|((?:GAME|WEEK)\s\d{1,2})\s\|\s(\d{4}\sSEASON))\s\|\s(.+?(?:vs|AT).+?)\s\|\s\d\w{2}\sQUARTER$')

#LFL | GAME 16 | CHICAGO BLISS vs ATLANTA STEAM | 3RD QUARTER
oldquarter = re.compile('^LFL\s\|\s((?:GAME|WEEK)\s\d{1,2})\s\|\s(.+?(?:vs|AT).+?)\s\|\s\d\w{2}\sQUARTER$')

def get_url(**kwargs):
    kwargs = {k: unicode(v).encode('ascii', 'ignore') for k,v in kwargs.iteritems()}
    return '{0}?{1}'.format(_url, urlencode(kwargs))
    
def find_quarters(age, gametitle, q, season, week, teams):
    check1 = season.replace(' ','')
    check2 = week.replace(' ','')
    check3 = teams.replace(' ','')
    
    pl = xbmc.PlayList(1)
    pl.clear()
    itemList = ['','','','']
    if age == 'mostrecent':
        url = searchquarters.format(pid=current, query=q)
    elif age == 'older':
        url = searchquarters.format(pid=past, query=q)
    resp = requests.get(url)
    for video in resp.json()['items']:
        t = video['snippet']['title']
        id = video['id']['videoId']
        nsTitle = t.replace(' ','')
        
        if all([any([check1 in nsTitle, check2 in nsTitle]), check3 in nsTitle]):
            if '1ST' in nsTitle:
                video_meta = xbmcgui.ListItem('1ST QUARTER', path=ytplay.format(vid=id))
                video_meta.setProperty('IsPlayable','true')
                itemList[0] = video_meta
                pl.add(url=ytplay.format(vid=id), listitem=video_meta, index=0)
            elif '2ND' in nsTitle:
                video_meta = xbmcgui.ListItem('2ND QUARTER', path=ytplay.format(vid=id))
                video_meta.setProperty('IsPlayable','true')
                itemList[1] = video_meta
                pl.add(url=ytplay.format(vid=id), listitem=video_meta, index=1)
            elif '3RD' in nsTitle:
                video_meta = xbmcgui.ListItem('3RD QUARTER', path=ytplay.format(vid=id))
                video_meta.setProperty('IsPlayable','true')
                itemList[2] = video_meta
                pl.add(url=ytplay.format(vid=id), listitem=video_meta, index=2)
            elif '4TH' in nsTitle:
                video_meta = xbmcgui.ListItem('4TH QUARTER', path=ytplay.format(vid=id))
                video_meta.setProperty('IsPlayable','true')
                itemList[3] = video_meta
                pl.add(url=ytplay.format(vid=id), listitem=video_meta, index=3)
    try:
        xbmcplugin.setResolvedUrl(_handle, True, itemList[0])
    except:
        xbmcgui.Dialog().ok('Sports Guru', 'Whoops, sorry about that! It looks like not all segments of this game are available to play. This sometimes happens with older videos. Please select a different game.')
        list_item = xbmcgui.ListItem('')
        xbmcplugin.setResolvedUrl(_handle, False, list_item)

def get_games(age, pageToken=None):
    if age == 'mostrecent':
        nexturl = base.format(pid=current)
    elif age == 'older':
        nexturl = base.format(pid=past)
    if pageToken is not None:
        nexturl += nextpage.format(token=pageToken)
    resp = requests.get(nexturl)
    print nexturl
    multipartGames = []
    for i, video in enumerate(resp.json()['items']):
        t = video['snippet']['title']
        d = video['snippet']['description']
        id = video['snippet']['resourceId']['videoId']
        full = fullgame.match(t)
        part = quarter.match(t)
        oldpart = oldquarter.match(t)
        
        if full is not None:
            moddedtitle = ' | '.join(t.split(' | ')[1:-1])
            list_item = xbmcgui.ListItem(label=moddedtitle)
            list_item.setProperty('IsPlayable','true')
            list_item.setInfo('video', {'title': moddedtitle, 'plot':d})
            list_item.setArt({'fanart':fanart,'thumb':icon,'poster':icon})
            url = ytplay.format(vid=id)
            xbmcplugin.addDirectoryItem(_handle, url, list_item, False)
        elif part is not None:
            #LFL | 2017 SEASON | WEEK 6 | DENVER DREAM AT SEATTLE MIST | 1ST QUARTER
            partialtitle = t.split(' | ')
            if 'SEASON' in partialtitle[2]:
                rebuilt = ' | '.join([partialtitle[1], partialtitle[2], partialtitle[3]])
            else:
                rebuilt = ' | '.join([partialtitle[2], partialtitle[1], partialtitle[3]])
            q = '+'.join(partialtitle[1:-1])
            if q not in multipartGames:
                multipartGames.append(q)
                list_item = xbmcgui.ListItem(label=rebuilt)
                list_item.setProperty('IsPlayable','true')
                list_item.setInfo('video', {'title': rebuilt, 'plot':d})
                list_item.setArt({'fanart':fanart,'thumb':icon,'poster':icon})
                url = get_url(sport='lfl', endpoint='replays', age=age, title=rebuilt, searchfor=q, season=partialtitle[1], week=partialtitle[2], teams=partialtitle[3])
                xbmcplugin.addDirectoryItem(_handle, url, list_item, isFolder=False)
        elif oldpart is not None:
            #LFL | GAME 16 | CHICAGO BLISS vs ATLANTA STEAM | 3RD QUARTER
            year = video['snippet']['publishedAt'].split('-')[0]
            partialtitle = t.split(' | ')
            rebuilt = ' | '.join([partialtitle[1], year+' SEASON', partialtitle[2]])
            q = '+'.join([partialtitle[1], year+' SEASON', partialtitle[2]])
            if q not in multipartGames:
                multipartGames.append(q)
                list_item = xbmcgui.ListItem(label=rebuilt)
                list_item.setProperty('IsPlayable','true')
                list_item.setInfo('video', {'title': rebuilt, 'plot':d})
                list_item.setArt({'fanart':fanart,'thumb':icon,'poster':icon})
                url = get_url(sport='lfl', endpoint='replays', age=age, title=rebuilt, searchfor=q, season=year+' SEASON', week=partialtitle[1], teams=partialtitle[2])
                xbmcplugin.addDirectoryItem(_handle, url, list_item, isFolder=False)
    if resp.json().get('nextPageToken') is not None and len(resp.json()['items']) > 0:
        list_item = xbmcgui.ListItem(label='[B]<<< EARLIER GAMES[/B]')
        list_item.setArt({'fanart':fanart,'thumb':icon,'poster':icon})
        url = get_url(sport='lfl', endpoint='replays', age=age, page=resp.json()['nextPageToken'])
        xbmcplugin.addDirectoryItem(_handle, url, list_item, isFolder=True)
    xbmcplugin.addSortMethod(_handle, xbmcplugin.SORT_METHOD_NONE)
    xbmcplugin.endOfDirectory(_handle)