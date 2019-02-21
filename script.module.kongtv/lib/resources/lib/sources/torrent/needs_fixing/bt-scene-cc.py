import xbmc
import xbmcaddon
import re
import urllib
import urlparse
from resources.lib.modules import cleantitle
from resources.lib.modules import client
from resources.lib.modules import proxy


class source:
	def __init__(self):
		self.priority = 1
		self.language = ['en']
		self.domains = ['btdb.to']
		self.base_link = 'https://bt-scene.cc'
		#self.base_link = 'https://btscene.bypassed.org'
		self.search_link = '/results_.php?q=%s&page=%s'
		
		privateToken = xbmcaddon.Addon('plugin.video.kongtv').getSetting('private.rd.enable')
		if privateToken == 'true':
			self.token = xbmcaddon.Addon('plugin.video.kongtv').getSetting('private.rd.api')
		else:
			self.token = xbmcaddon.Addon('script.realdebrid.mod').getSetting('rd_access')

	def movie(self, imdb, title, localtitle, aliases, year):
		if xbmc.getCondVisibility('System.HasAddon(script.realdebrid.mod)'):
			try:
				title = cleantitle.geturl(title)
				title = title.replace('-','.')
				url = '%s.%s' % (title,year)
				return url
			except:
				return
			
	def tvshow(self, imdb, tvdb, tvshowtitle, localtvshowtitle, aliases, year):
		if xbmc.getCondVisibility('System.HasAddon(script.realdebrid.mod)'):
			try:
				url = cleantitle.geturl(tvshowtitle)
				url = url.replace('-','.')
				return url
			except:
				return
 
	def episode(self, url, imdb, tvdb, title, premiered, season, episode):
		try:
			if not url: return
			season = '%02d' % int(season)
			episode = '%02d' % int(episode)
			url = '%s.s%se%s' % (url,str(season),str(episode))
			return url
		except:
			return

	def sources(self, url, hostDict, hostprDict):
		try:
			sources = []
			q = url

			try: # Page 1
				page = '1'
				url = self.base_link + self.search_link % (q,page)
				r = client.request(url)
				match = re.compile('<a href="(.+?)">(.+?)</a>	<div class="subinfo">').findall(r)
				for url,info in match: 
					torrenturl = 'https://bt-scene.cc%s' % (url)
					
					# Find infohash
					r = client.request(torrenturl)
					match = re.compile('onclick="update_once\(\'(.+?)\'\)').findall(r)
					for hash in match:
						hash = hash
						url = 'https://api.real-debrid.com/rest/1.0/torrents/instantAvailability/%s?auth_token=%s' % (hash,self.token)
						torrenturl = torrenturl
						# Check availability
						r = client.request(url)
						r = r.replace('	','').replace('\n','').replace('[','').replace(']','').replace('\/','/').replace('{','')
						r = r.replace('"rd": ',',')
						match = re.compile(',"(.+?)": "filename": "(.+?)"').findall(r)
						for id,filename in match:
							if '2160' in filename: quality = '4K'
							elif 'DVDSCR' in filename: quality = 'SD'
							elif 'DVDScr' in filename: quality = 'SD'
							elif 'HD-TS' in filename: quality = 'SD'
							elif '480' in filename: quality = 'SD'
							elif '720' in filename: quality = 'HD'
							elif '1080' in filename: quality = '1080p'
							elif 'HDRip' in filename: quality = 'SD'
							elif 'HDTV' in filename: quality = 'SD'
							elif 'WebRip' in filename: quality = 'SD'
							elif 'WEBRIP' in filename: quality = 'SD'
							elif 'WEBRip' in filename: quality = 'SD'
							elif 'BDRip' in filename: quality = '1080p'
							torrenturl = torrenturl
							# Check video isn't sample
							if '2160' not in filename: pass
							if 'DVDSCR' not in filename: pass
							if 'HDRip' not in filename: pass
							if '480' not in filename: pass
							if '720' not in filename: pass
							if '1080' not in filename: pass
							if 'HDTV' not in filename: pass
							if '.jpg' in filename: pass
							if '.jpeg' in filename: pass
							if '.png' in filename: pass
							if '.mkv' in filename: 
								url = 'url="%s"&filename="%s"&id="%s"' % (torrenturl,filename,id)
								sources.append({'source': 'Torrent','info': filename,'quality': quality,'language': 'en','url': url,'direct': False,'debridonly': False})
							if '.mp4' in filename: 
								url = 'url="%s"&filename="%s"&id="%s"' % (torrenturl,filename,id)
								sources.append({'source': 'Torrent','info': filename,'quality': quality,'language': 'en','url': url,'direct': False,'debridonly': False})
							if '.avi' in filename: 
								url = 'url="%s"&filename="%s"&id="%s"' % (torrenturl,filename,id)
								sources.append({'source': 'Torrent','info': filename,'quality': quality,'language': 'en','url': url,'direct': False,'debridonly': False})
							if '.flv' in filename: 
								url = 'url="%s"&filename="%s"&id="%s"' % (torrenturl,filename,id)
								sources.append({'source': 'Torrent','info': filename,'quality': quality,'language': 'en','url': url,'direct': False,'debridonly': False})
			except: return

		except Exception:
			return
		return sources

	def resolve(self, url):
		match = re.compile('url="(.+?)"&filename="(.+?)"&id="(.+?)"').findall(url)
		# Fetch magnet link
		for url,filename,id in match:
			r = client.request(url)
			match = re.compile('href="(.+?)">Magnet Link</a>').findall(r)
			for magnetLink in match:
				id = id
				filename = filename.replace('[','').replace(']','').replace('(','').replace(')','')
				magnetLink = urllib.quote_plus(magnetLink)
				
				# Pass on to script.realdebrid.mod...
				import xbmc
				if id == '1': xbmc.executebuiltin('RunPlugin(plugin://script.realdebrid.mod/?fanart=na&icon=na&mode=4&name=na&poster=na&link='+magnetLink+'&url)')
				if id == '2': xbmc.executebuiltin('RunPlugin(plugin://script.realdebrid.mod/?fanart=na&icon=na&mode=14&name=na&poster=na&link='+magnetLink+'&url)')
				if id == '3': xbmc.executebuiltin('RunPlugin(plugin://script.realdebrid.mod/?fanart=na&icon=na&mode=15&name=na&poster=na&link='+magnetLink+'&url)')
				if id == '4': xbmc.executebuiltin('RunPlugin(plugin://script.realdebrid.mod/?fanart=na&icon=na&mode=16&name=na&poster=na&link='+magnetLink+'&url)')
				if id == '5': xbmc.executebuiltin('RunPlugin(plugin://script.realdebrid.mod/?fanart=na&icon=na&mode=17&name=na&poster=na&link='+magnetLink+'&url)')
				if id == '6': xbmc.executebuiltin('RunPlugin(plugin://script.realdebrid.mod/?fanart=na&icon=na&mode=18&name=na&poster=na&link='+magnetLink+'&url)')
				if id == '7': xbmc.executebuiltin('RunPlugin(plugin://script.realdebrid.mod/?fanart=na&icon=na&mode=19&name=na&poster=na&link='+magnetLink+'&url)')
				if id == '8': xbmc.executebuiltin('RunPlugin(plugin://script.realdebrid.mod/?fanart=na&icon=na&mode=20&name=na&poster=na&link='+magnetLink+'&url)')
				if id == '9': xbmc.executebuiltin('RunPlugin(plugin://script.realdebrid.mod/?fanart=na&icon=na&mode=21&name=na&poster=na&link='+magnetLink+'&url)')
				if id == '10': xbmc.executebuiltin('RunPlugin(plugin://script.realdebrid.mod/?fanart=na&icon=na&mode=22&name=na&poster=na&link='+magnetLink+'&url)')
				
				import time
				time.sleep(3)
						
				api = 'https://api.real-debrid.com/rest/1.0/torrents?auth_token=%s' % self.token
				r = client.request(api)
				r = r.replace('	','').replace('\n','').replace('[','').replace(']','').replace('\/','/').replace('(','').replace(')','')
				match = re.compile('"filename": "'+filename+'","hash": ".+?","bytes": .+?,"host": ".+?","split": .+?,"progress": 100,"status": "downloaded","added": ".+?","links": "https://real-debrid\.com/d/(.+?)"').findall(r)
				for url in match: 
					url = 'plugin://script.realdebrid.mod/?url=https://real-debrid.com/d/%s&mode=5&name=Real-Debrid&icon=none&fanart=none&poster=none' % url
					return url
			
			