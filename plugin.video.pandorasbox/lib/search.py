import re, process, urllib, urllib2, xbmc, xbmcgui, base64, sys, xbmcplugin, threading, xbmcaddon, os

addon_id = 'plugin.video.pandorasbox'
ADDON = xbmcaddon.Addon(id=addon_id)
Dialog = xbmcgui.Dialog()
dp =  xbmcgui.DialogProgress()
Decode = base64.decodestring
addon_handle = int(sys.argv[1])
Base_Pand = (Decode('aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9QYW5zQm94L09SSUdJTlMv'))
watched_list = xbmc.translatePath('special://home/userdata/addon_data/plugin.video.pandorasbox/watched.txt')
pans = xbmc.translatePath('special://home/userdata/addon_data/plugin.video.pandorasbox/')

def Search_Input(name,url,extra):
    if extra == 'NEW':
		Dialog = xbmcgui.Dialog()
		Search_title = Dialog.input('Search', type=xbmcgui.INPUT_ALPHANUM)
		Search_name = Search_title.lower()
		if Search_name == '':
			pass
		else:
			xbmc.log('SEARCH NAME ='+Search_name+'    URL= '+url)
			write_to_file(Search_name,url)
			if url == 'TV':
				TV(Search_name)
			elif url == 'Movies':
				Movies(Search_name)
			else:
				process.Menu('Search failed - '+url,'','','','','','')
    elif extra == 'OLD':
		Search_name = name
		if Search_name == '':
			pass
		else:
			if url == 'TV':
				TV(Search_name)
			elif url == 'Movies':
				Movies(Search_name)
    elif extra == 'ALL':
		read_from_file('full')
    else:
		process.Menu('[COLOR darkgoldenrod][B]New Search[/B][/COLOR]',url,9,'','','','NEW')
		read_from_file(url)
			
class Thread(threading.Thread):
    def __init__(self, target, *args):
        self._target = target
        self._args = args
        threading.Thread.__init__(self)
    def run(self):
        self._target(*self._args)
		
def Movies(Search_name):
    if '(' in Search_name:
		Search_name = re.compile('(.+?)\(').findall(str(Search_name))
		for thing in Search_name:
			Search_name = thing
    Thread(target=Pans_Search_Movies(Search_name))
	

def write_to_file(Search_name,file_name):
	full_file = pans + 'full.txt'
	Stream_file = pans+file_name+'.txt'
	if not os.path.exists(Stream_file):
		print_text_file = open(Stream_file,"w")
		print_text_file.write('<NAME=>'+Search_name+'</NAME><URL=>'+file_name+'</URL>\n')
	else:
		print_text_file = open(Stream_file,"a")
		print_text_file.write('<NAME=>'+Search_name+'</NAME><URL=>'+file_name+'</URL>\n')
	if not os.path.exists(full_file):
		print_text_file = open(full_file,"w")
		print_text_file.write('<NAME=>'+Search_name+'</NAME><URL=>'+file_name+'</URL>\n')
	else:
		print_text_file = open(full_file,"a")
		print_text_file.write('<NAME=>'+Search_name+'</NAME><URL=>'+file_name+'</URL>\n')
	
def read_from_file(file_name):
	Stream_file = pans+file_name+'.txt'
	if not os.path.exists(Stream_file):
		print_text_file = open(Stream_file,"w")
	html = open(Stream_file).read()
	match = re.compile('<NAME=>(.+?)</NAME><URL=>(.+?)</URL>').findall(html)
	for result,type in match:
		process.Menu(result,type,9,'','','','OLD')
	process.Menu('[COLORred][B]Clear previous search\'s[/B][/COLOR]',file_name,4,'','','','')
	
def Clear_Search(file_name):
	Stream_file = pans+file_name+'.txt'
	if os.path.exists(Stream_file):
		print_text_file = open(Stream_file,"w")
	
def TV(Search_name):
    dp.create('Checking for streams')
    if 'season' in Search_name.lower():
        Type = 'single_ep'
        name_splitter = Search_name + '<>'
        name_split = re.compile('(.+?) - season (.+?) episode (.+?)<>').findall(str(name_splitter).lower())
        for name,season,episode in name_split:
            title = name
            season = season
            episode = episode
    else:
        title = Search_name
        season = ''
        episode = ''
    dp.update(100,'',"Checking Pandoras Box",'Please Wait')
    Thread(target=Pans_Search_TV(Search_name))
    dp.update(100,'',"Checking Origin Cartoons",'Please Wait')
    Thread(target=animetoon_search(Search_name))
    process.rmWatched(title)
    process.Addwatched(title,season,episode)
    dp.update(100,'',"Finished checking",'Please Wait')
    dp.close()

def animetoon_search(Search_name):
	List = []
	if 'season' in Search_name.lower():
		Type = 'single_ep'
		name_splitter = Search_name + '<>'
		name_split = re.compile('(.+?) - season (.+?) episode (.+?)<>').findall(str(name_splitter).lower())
		for name,season,episode in name_split:
			title = name
			season = season
			episode = episode
		year = ''
		if season == '1':
			url = 'http://www.animetoon.org/' + title.replace(' ', '-').replace('!', '') + '-episode-' + episode
		elif season == '01':
			url = 'http://www.animetoon.org/' + title.replace(' ', '-').replace('!', '') + '-episode-' + episode
		else:
			url = 'http://www.animetoon.org/' + title.replace(' ','-').replace('!', '') +'-season-'+season+'-episode-'+episode
		html=process.OPEN_URL(url)
		match = re.compile('"playlist">.+?</span></div><div><iframe src="(.+?)"').findall(html)
		for url2 in match:
			if 'panda' in url2:
				HTML = process.OPEN_URL(url2)
				match2 = re.compile("url: '(.+?)'").findall(HTML)
				for url3 in match2:
					if 'http' in url3:
						if url3 not in List:
							process.Play('[COLORwhite]Origin[/COLOR] | Playpanda | '+title,url3,401,'','','','')
							List.append(url3)
			elif 'easy' in url2:
				HTML2 = process.OPEN_URL(url2)
				match3 = re.compile("url: '(.+?)'").findall(HTML2)
				for url3 in match3:
					if 'http' in url3:
						if url3 not in List:
							process.Play('[COLORwhite]Origin[/COLOR] | Easyvideo | '+title,url3,401,'','','','')
							List.append(url3)
			elif 'zoo' in url2:
				HTML3 = process.OPEN_URL(url2)
				match4 = re.compile("url: '(.+?)'").findall(HTML3)
				for url3 in match4:
					if 'http' in url3:
						if url3 not in List:
							process.Play('[COLORwhite]Origin[/COLOR] | Videozoo | '+title,url3,401,'','','','')
							List.append(url3)

	else:
		pass
	
				
def Pans_Search_Movies(Search_name):
	Pans_files_Movies = ['hey1080p','hey3D','hey','mov'+Search_name[0].lower()]
	for file_name in Pans_files_Movies:
		search_URL = Base_Pand + file_name + '.php'
		HTML = process.OPEN_URL(search_URL)
		if HTML != 'Opened':
			match=re.compile('<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>').findall(HTML)
			for url,iconimage,desc,fanart,name in match:
				if Search_name.lower().replace(' ','') in (name).replace(' ','').lower():
					name = '[COLOR darkgoldenrod]Pandora [/COLOR]| ' + name
					process.Play(name,url,401,iconimage,fanart,desc,'')

def Pans_Search_TV (Search_name):
	if 'season' in Search_name.lower():
		Type = 'single_ep'
		name_splitter = Search_name + '<>'
		name_split = re.compile('(.+?) - season (.+?) episode (.+?)<>').findall(str(name_splitter).lower())
		for name,season,episode in name_split:
			title = name
			season = season
			episode = episode
		year = ''
	else:
		Type = 'full_show'
		title = Search_name
	if Search_name[0].lower() in 'abcdefghijklmnopqrstuvwxyz':
		url_extra = Search_name[0].lower()
	else:
		url_extra = 'tvnum'
	search_URL2 = Base_Pand + url_extra + '.php'
	HTML = process.OPEN_URL(search_URL2)
	if HTML != 'Opened':
		match = re.compile('<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>',re.DOTALL).findall(HTML)
		for name,desc,url,img,fanart,mode in match:
			if Type == 'full_show':
				if (Search_name).replace(' ','') in (name).replace(' ','').lower():
					name = '[COLOR darkgoldenrod]Pandora [/COLOR]' + name
					process.Menu(name,url,mode,img,fanart,desc,'')
			elif Type == 'single_ep':
				if title.replace(' ','').lower() in name.replace(' ','').lower():
					HTML5 = process.OPEN_URL(url)
					match5=re.compile('<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>').findall(HTML5)
					for url5,iconimage,desc5,background,name5 in match5:
						if len(episode) == 1:
							episode = '0'+episode
						if 'E'+episode in name5:
							process.Play('[COLOR darkgoldenrod]Pandora | [/COLOR]' + name5,url5,401,iconimage,background,desc5,'')
					HTML2 = process.OPEN_URL(url)
					match2 = re.compile('<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>',re.DOTALL).findall(HTML2)
					for name2,desc2,url2,img2,fanart2,mode2 in match2:
						if 's' in name2.lower() and season in name2.lower():
							HTML3 = process.OPEN_URL(url2)
							match3=re.compile('<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>').findall(HTML3)
							for url3,iconimage,desc3,background,name3 in match3:
								if len(episode) == 1:
									episode = '0'+episode
								if 'E'+episode in name3:
									process.Play('[COLOR darkgoldenrod]Pandora | [/COLOR]' + name3,url3,401,iconimage,background,desc3,'')
	if Type == 'single_ep':
		HTML4 = process.OPEN_URL(Base_Pand + 'recenttv.php')
		match4=re.compile('<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>').findall(HTML4)
		for url4,iconimage,desc4,background,name4 in match4:
			if len(episode) == 1:
				episode = '0'+episode
			if 'E'+episode in name4 and title.lower().replace(' ','') in name4.lower().replace(' ',''):
				process.Play('[COLOR darkgoldenrod]Pandora Recent | [/COLOR]' + name4,url4,401,iconimage,background,desc4,'')
			
