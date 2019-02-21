# -*- coding: utf-8 -*-
import urllib,re,xbmcgui,xbmcplugin,xbmc,sys,process
addon_handle = int(sys.argv[1])


def Movie_Main():
    process.Menu('[COLOR slateblue]Search IMDB[/COLOR]','',207,'','','','')
    process.Menu('[COLOR slateblue]IMDB top 250 Films[/COLOR]','http://www.imdb.com/chart/top',206,'','','','')
    Pandoras_Box('http://genietvcunts.co.uk/PansBox/ORIGINS/moviecat.php')
    xbmcplugin.endOfDirectory(int(sys.argv[1]))
			
def split_for_search(extra):
	year = re.compile('\((.+?)\)').findall(str(extra))
	for item in year:
		year = item
	name = extra.replace('\(','').replace('\)','').replace(year,'')
	import Scrape_Nan;Scrape_Nan.scrape_movie(name,year)

def search_movies():
	Search_title = xbmcgui.Dialog().input('Search', type=xbmcgui.INPUT_ALPHANUM)
	url = 'http://www.imdb.com/find?ref_=nv_sr_fn&q='+Search_title.replace(' ','+')+'&s=all'
	html = process.OPEN_URL(url)
	match = re.compile('<tr class="findResult.+?"> <td class="primary_photo"> <a href=".+?" ><img src="(.+?)" /></a> </td> <td class="result_text"> <a href=".+?" >(.+?)</a>(.+?)</td>').findall(html)
	for image,title,year in match:
		if '<' in year:
			pass
		else:
			if '(TV Series)' in year:
				pass
			else:
				image = image.replace('32,44','174,256').replace('UY67','UY256').replace('UX32','UX175').replace('UY44','UY256')
				process.Menu(title,'Movies',16,image,'','','OLD')
				process.setView('movies', 'INFO')
	
def Movie_Genre(url):
	html = process.OPEN_URL('http://www.imdb.com/genre/')
	match = re.compile('<h3><a href="(.+?)">(.+?)<span class="normal">').findall(html)
	for url, name in match:
		url = 'http://www.imdb.com/search/title?genres='+name.replace(' ','').lower()+'&title_type=feature&sort=moviemeter,asc'
		process.Menu(name,url,203,'','','','')
		process.setView('movies', 'INFO')
		
def IMDB_Top250(url):
	html = process.OPEN_URL(url)
	film = re.compile('<td class="posterColumn">.+?<img src="(.+?)".+?<td class="titleColumn">(.+?)<a.+?title=".+?" >(.+?)</a>.+?<span class="secondaryInfo">(.+?)</span>',re.DOTALL).findall(html)
	for img,no,title,year in film:
		no = no.replace('\n','').replace('	','').replace('  ','')
		try:
			img = img.replace('45,67','174,256').replace('UY67','UY256').replace('UX45','UX175')
			process.Menu(title + ' ' + year,'Movies',16,img,'','','OLD')
		except:
			pass
		
def IMDB_Grab(url):
	try:
		List = []
		xbmc.log(url)
		html = process.OPEN_URL(url)
		match = re.compile('<div class="lister-item-image float-left">.+?<a href="(.+?)".+?<img alt="(.+?)".+?loadlate="(.+?)".+?<span class="lister-item-year text-muted unbold">(.+?)</span>.+?<p class="text-muted">\n(.+?)</p>',re.DOTALL).findall(html)
		for url,name,image,year,desc in match:
			image = image.replace('45,67','174,256').replace('UY67','UY256').replace('UX67','UX175').replace('UY98','UY256').replace('SX54','SX170').replace('54,74','174,256').replace('67,98','174,256')
			try:
				if '(2017)' in year:
					pass
				else:
					xbmc.log(image)
					year = year.replace('(I) ','').replace('II','')
					process.Menu(name + ' ' + year,'Movies',16,image,'',desc,'OLD')
					process.setView('movies', 'INFO')
			except:
				pass
		next_page = re.compile('<a href="(.+?)"\nclass="lister-page-next next-page" ref-marker=adv_nxt>Next &#187;</a>').findall(html)
		for item in next_page:
			if item not in List:
				process.Menu('Next Page','http://imdb.com/search/title'+item,203,'','','','')
				List.append(item)
	except:
		pass
		
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
			else:
				process.Menu(name,url,400,img,fanart,desc,'')
	match2=re.compile('<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>').findall(html)
	for url,iconimage,desc,fanart,name in match2:
		if not 'http' in url:
			if len(url) == 11:
				url = 'plugin://plugin.video.youtube/play/?video_id='+ url
			elif url.startswith('PL') and not '&order=' in url :
				url = 'plugin://plugin.video.youtube/play/?&order=default&playlist_id=' + url
			else:
				url = 'plugin://plugin.video.youtube/play/?playlist_id=' + url
			process.Play(name,url,401,iconimage,fanart,desc,'')			
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
		else:
			process.Play(name,url,401,iconimage,fanart,desc,'')			

	xbmcplugin.setContent(addon_handle, 'movies')
	xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_TITLE)