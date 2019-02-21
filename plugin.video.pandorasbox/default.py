# -*- coding: cp1252 -*-

'''
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

import sys
import urlparse
import urllib,urllib2,datetime,re,os,base64,xbmc,xbmcplugin,xbmcgui,xbmcaddon
from lib import process
import urlresolver

Dialog = xbmcgui.Dialog()
Decode = base64.decodestring
CAT=Decode('LnBocA==')
Base_Pand = (Decode('aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9QYW5zQm94L09SSUdJTlMv'))
addon_id='plugin.video.pandorasbox'
base_url = sys.argv[0]
addon_handle = int(sys.argv[1])
args = urlparse.parse_qs(sys.argv[2][1:])
PATH = "Pandoras Box"
VERSION = "1.0.1"
ADDON_PATH = xbmc.translatePath('special://home/addons/plugin.video.pandorasbox/')
USERDATA_PATH = xbmc.translatePath('special://home/userdata/addon_data')
ADDON_DATA = USERDATA_PATH + '/Pandora\'sBox/'
if not os.path.exists(ADDON_DATA):
    os.makedirs(ADDON_DATA)
FANART      =  xbmc.translatePath('special://home/addons/plugin.video.pandorasbox/fanart.jpg')



def Home_Menu():
    
    process.Menu('[COLOR darkgoldenrod][I]Open Pandora\'s Box[/I][/COLOR]',Base_Pand +Decode('c3BvbmdlbWFpbi5waHA='),400,'https://s32.postimg.org/ov9s6ipf9/icon.png',FANART,'','')
    process.Menu('[COLOR darkgoldenrod][I]Search[/I][/COLOR]','',1,'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png',FANART,'','')
    process.Menu('[COLOR darkgoldenrod][I]Favourites[/I][/COLOR]','',10,'http://icons.iconarchive.com/icons/colorflow/colorflow_1/256/32-Favorites-icon.png',FANART,'','')

    xbmcplugin.setContent(addon_handle, 'movies')
		
def Search_Menu():
	process.Menu('[COLOR darkgoldenrod][I]Search Pandoras Films[/I][/COLOR]','Movies',9,'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png',FANART,'','')
	process.Menu('[COLOR darkgoldenrod][I]Search Pandoras TV[/I][/COLOR]','TV',9,'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png',FANART,'','')

        xbmcplugin.setContent(addon_handle, 'movies')

	
def Pandoras_Box(url):

    List = []
    html=process.OPEN_URL(url)
    match = re.compile('<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?</item>',re.DOTALL).findall(html)
    for name,desc,url,img,fanart in match:
        if 'php' in url:
            if name == '[COLOR darkgoldenrod][I]Movies[/I][/COLOR]':
                process.Menu(name,url,3,img,fanart,desc,'')
            elif name == '[COLOR darkgoldenrod][I]TV Shows[/I][/COLOR]':
                process.Menu(name,url,2,img,fanart,desc,'')
            elif name == '[COLOR darkgoldenrod][I]Recently Added TV[/I][/COLOR]':
                process.Menu(name,url,19,img,fanart,desc,'')
            elif name == '[COLOR darkgoldenrod][I]Recently Added Movies[/I][/COLOR]':
                process.Menu(name,url,19,img,fanart,desc,'')
            else:
                process.Menu(name,url,400,img,fanart,desc,'')
    match2=re.compile('<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>').findall(html)
    for url,iconimage,desc,fanart,name in match2:
        if 'php' in url:
            process.Menu(name,url.replace(' ','%20'),400,iconimage,fanart,desc,'')
        elif not 'http' in url:
            if len(url) == 11:
                url = 'plugin://plugin.video.youtube/play/?video_id='+ url
                process.Play(name,url,401,iconimage,fanart,desc,'')			
        elif 'utube' in url and 'playlist' in url:
            process.Menu(name,url,18,iconimage,fanart,desc,'')	
        elif 'sportsdevil:' in url:
            url = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url='+url.replace('sportsdevil:','')
            process.Play(name,url,401,iconimage,fanart,desc,'')			
        elif 'f4mtester:' in url:
            if '.f4m' in i.string:
                url = 'plugin://plugin.video.f4mTester/?url='+url
            elif '.m3u8' in i.string:
                url = 'plugin://plugin.video.f4mTester/?url='+url+'&amp;streamtype=HLS'
            else:
                url = 'plugin://plugin.video.f4mTester/?url='+url+'&amp;streamtype=SIMPLE'
            process.Play(name,url,401,iconimage,fanart,desc,'')
        elif 'sublink:' in url:
            process.Play(name,url,15,iconimage,fanart,desc,'')
        elif name == '[COLOR darkgoldenrod][I]Recently Added TV[/I][/COLOR]':
			process.Play(name,url.replace(' ','%20'),401,iconimage,fanart,desc,'')
        elif name == '[COLOR darkgoldenrod][I]Recently Added Movies[/I][/COLOR]':
			process.Play(name,url.replace(' ','%20'),401,iconimage,fanart,desc,'')
        else:
            process.Play(name,url.replace(' ','%20'),401,iconimage,fanart,desc,'')			

    xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_TITLE)
    xbmcplugin.setContent(addon_handle, 'movies')
	
def open_normal(name,url,iconimage,fanart,description):
	html = process.OPEN_URL(url)
	match2=re.compile('<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>').findall(html)
	for url,iconimage,desc,fanart,name in match2:
		process.Play(name,url.replace(' ','%20'),401,iconimage,fanart,description,'')

def Youtube_Playlist_Grab_Duration(url):
   
    #Need to view the playlist to use this one (as a list on page) max 100 vids
    HTML = OPEN_URL(url)
    block_set = re.compile('<tr class="pl-video yt-uix-tile(.+?)</tr>',re.DOTALL).findall(HTML)
    for block in block_set:
        image = re.compile('data-thumb="(.+?)"').findall(str(block))
        for image in image:
            image = image
        name = re.compile('data-title="(.+?)"').findall(str(block))
        for name in name:
            name = (name).replace('&quot;','').replace('&#39;','\'').replace('&amp;','&')
        duration = re.compile('<div class="timestamp"><span aria-label=".+?">(.+?)</span>').findall(str(block))
        for duration in duration:
            duration = duration
        url = re.compile('data-video-ids="(.+?)"').findall(str(block))
        for url in url:
            url = url
        if 'elete' in name:
            pass
        elif 'rivate Vid' in name:
            pass
        else:
    	    process.PLAY('[COLORred]'+str(duration)+'[/COLOR] : '+str(name),'plugin://plugin.video.youtube/play/?video_id='+str(url),906,str(image),'','','' )		
	
def TV_Calender_Day(url):
	from datetime import datetime
	today = datetime.now().strftime("%d")
	this_month = datetime.now().strftime("%m")
	this_year = datetime.now().strftime("%y")
	todays_number = (int(this_year)*100)+(int(this_month)*31)+(int(today))
	HTML = process.OPEN_URL(url)
	match = re.compile('<span class="dayofmonth">.+?<span class=".+?">(.+?)</span>(.+?)</span>(.+?)</div>',re.DOTALL).findall(HTML)
	for Day_Month,Date,Block in match:
		Date = Date.replace('\n','').replace('  ','').replace('	','')
		Day_Month = Day_Month.replace('\n','').replace('  ','').replace('	','')
		Final_Name = Day_Month.replace(',',' '+Date+' ')
		split_month = Day_Month+'>'
		Month_split = re.compile(', (.+?)>').findall(str(split_month))
		for item in Month_split:
			month_one = item.replace('January','1').replace('February','2').replace('March','3').replace('April','4').replace('May','5').replace('June','6')
			month = month_one.replace('July','7').replace('August','8').replace('September','9').replace('October','10').replace('November','11').replace('December','12')
		show_day = Date.replace('st','').replace('th','').replace('nd','').replace('rd','')
		shows_number = (int(this_year)*100)+(int(month)*31)+(int(show_day))
		if shows_number>= todays_number:
			process.Menu('[COLORred]*'+'[COLORwhite]'+Final_Name+'[/COLOR]','',7,'','','',Block)
		else:
			process.Menu('[COLORgreen]*'+'[COLORwhite]'+Final_Name+'[/COLOR]','',7,'','','',Block)

def TV_Calender_Prog(extra):
	match = re.compile('<span class="show">.+?<a href=".+?">(.+?)</a>:.+?</span>.+?<a href=".+?" title=".+?">(.+?)</a>',re.DOTALL).findall(str(extra))
	for prog, ep in match:
		process.Menu(prog+' - Season '+ep.replace('x',' Episode '),'',8,'','','',prog)
	
						
def send_to_search(name,extra):
	if 'COLOR' in name:
		name = re.compile('- (.+?)>').findall(str(name)+'>')
		for name in name:
			name = name
	dp =  xbmcgui.DialogProgress()
	dp.create('Checking for stream')
	from lib import search
	search.TV(name)
	
def Youtube_Playlist_Grab_Duration(url):
   
    #Need to view the playlist to use this one (as a list on page) max 100 vids
    HTML = process.OPEN_URL(url)
    block_set = re.compile('<tr class="pl-video yt-uix-tile(.+?)</tr>',re.DOTALL).findall(HTML)
    for block in block_set:
        image = re.compile('data-thumb="(.+?)"').findall(str(block))
        for image in image:
            image = image
        name = re.compile('data-title="(.+?)"').findall(str(block))
        for name in name:
            name = (name).replace('&quot;','').replace('&#39;','\'').replace('&amp;','&')
        duration = re.compile('<div class="timestamp"><span aria-label=".+?">(.+?)</span>').findall(str(block))
        for duration in duration:
            duration = duration
        url = re.compile('data-video-ids="(.+?)"').findall(str(block))
        for url in url:
            url = url
        if 'elete' in name:
            pass
        elif 'rivate Vid' in name:
            pass
        else:
    	    process.Play('[COLORred]'+str(duration)+'[/COLOR] : '+str(name),'plugin://plugin.video.youtube/play/?video_id='+str(url),401,str(image),'','','' )	

		
def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2: 
                params=sys.argv[2] 
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}    
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]
                                
        return param
        
params=get_params()
url=None
name=None
iconimage=None
mode=None
description=None
extra=None
fav_mode=None

try:
    fav_mode=int(params["fav_mode"])
except:
    pass
	
try:
    extra=urllib.unquote_plus(params["extra"])
except:
    pass

try:
        url=urllib.unquote_plus(params["url"])
except:
        pass
try:
        name=urllib.unquote_plus(params["name"])
except:
        pass
try:
        iconimage=urllib.unquote_plus(params["iconimage"])
except:
        pass
try:        
        mode=int(params["mode"])
except:
        pass
try:        
        fanart=urllib.unquote_plus(params["fanart"])
except:
        pass
try:        
        description=urllib.unquote_plus(params["description"])
except:
        pass
        
        
print str(PATH)+': '+str(VERSION)
print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)
print "IconImage: "+str(iconimage)

 

if mode == None : Home_Menu()
elif mode == 1 	: Search_Menu()
elif mode == 2 	: from lib import multitv;multitv.multiv_Main_Menu()
elif mode == 3 	: from lib import Movies;Movies.Movie_Main()
elif mode == 4  : from lib import search;search.Clear_Search(url)
elif mode == 5  : Youtube_Playlist_Grab_Duration(url)
elif mode == 6  : TV_Calender_Day(url)
elif mode == 7  : TV_Calender_Prog(extra)
elif mode == 8  : send_to_search(name,extra)
elif mode == 9  : from lib import search;search.Search_Input(name,url,extra)
elif mode == 10: from lib import process;process.getFavourites()
elif mode==11:
    try:
        name = name.split('\\ ')[1]
    except:
        pass
    try:
        name = name.split('  - ')[0]
    except:
        pass
    process.addFavorite(name, url, fav_mode, iconimage, fanart, description, extra)
elif mode==12:
    try:
        name = name.split('\\ ')[1]
    except:
        pass
    try:
        name = name.split('  - ')[0]
    except:
        pass
    process.rmFavorite(name)
elif mode == 13  : Youtube_Playlist(url)
elif mode == 14  : process.queueItem()
elif mode == 15  : process.GetSublinks(name,url,iconimage,fanart)
elif mode == 16  : from lib import search;search.Search_Input(name,url,extra)
elif mode == 17  : process.check_for_episode()
elif mode == 18  : Youtube_Playlist_Grab_Duration(url)
elif mode == 19  : open_normal(name,url,iconimage,fanart,description)
elif mode == 202 : from lib import Movies;Movies.Movie_Genre(url)
elif mode == 203 : from lib import Movies;Movies.IMDB_Grab(url)
elif mode == 204 : from lib import Movies;Movies.Check_Link(name,url,image)
elif mode == 205 : from lib import Movies;Movies.Get_playlink(url)
elif mode == 206 : from lib import Movies;Movies.IMDB_Top250(url)
elif mode == 207 : from lib import Movies;Movies.search_movies()
elif mode == 208 : from lib import Movies;Movies.movie_channels()
elif mode == 209 : from lib import Movies;Movies.split_for_search(extra)
elif mode == 300 : from lib import multitv;multitv.multiv_Main_Menu()
elif mode == 301 : from lib import multitv;multitv.IMDB_TOP_100_EPS(url)
elif mode == 302 : from lib import multitv;multitv.Popular(url)
elif mode == 303 : from lib import multitv;multitv.Genres()
elif mode == 304 : from lib import multitv;multitv.Genres_Page(url)
elif mode == 305 : from lib import multitv;multitv.IMDB_Get_Season_info(url,iconimage,extra)
elif mode == 306 : from lib import multitv;multitv.IMDB_Get_Episode_info(url,extra)
elif mode == 307 : from lib import multitv;multitv.SPLIT(extra)
elif mode == 308 : from lib import multitv;multitv.Search_TV()
elif mode == 400 : Pandoras_Box(url)
elif mode == 401 : process.Resolve(name,url)
elif mode == 423 : open_Menu(url)

xbmcplugin.endOfDirectory(int(sys.argv[1]))