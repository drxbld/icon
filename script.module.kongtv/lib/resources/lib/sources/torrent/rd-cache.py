import xbmc
import xbmcaddon
import re
import urllib
import urlparse
from resources.lib.modules import cleantitle
from resources.lib.modules import client
from resources.lib.modules import proxy
from resources.lib.modules import torrent

class source:
	def __init__(self):
		self.priority = 1
		self.language = ['en']
		self.domains = ['real-debrid.com']
		self.base_link = 'https://real-debrid.com'
		
		privateToken = xbmcaddon.Addon('plugin.video.kongtv').getSetting('private.rd.enable')
		if privateToken == 'true':
			self.token = xbmcaddon.Addon('plugin.video.kongtv').getSetting('private.rd.api')
		else:
			self.token = xbmcaddon.Addon('script.realdebrid.mod').getSetting('rd_access')

	def movie(self, imdb, title, localtitle, aliases, year):
		if xbmc.getCondVisibility('System.HasAddon(script.realdebrid.mod)'):
			try:
				url = title
				return url
			except:
				return
			
	def tvshow(self, imdb, tvdb, tvshowtitle, localtvshowtitle, aliases, year):
		if xbmc.getCondVisibility('System.HasAddon(script.realdebrid.mod)'):
			try:
				url = tvshowtitle
				return url
			except:
				return
 
	def episode(self, url, imdb, tvdb, title, premiered, season, episode):
		try:
			if not url: return
			season = '%02d' % int(season)
			episode = '%02d' % int(episode)
			url = '%s S%sE%s' % (url,str(season),str(episode))
			return url
		except:
			return

	def sources(self, url, hostDict, hostprDict):
		try:
			sources = []
			q = url
			
			try: # No .
				q = q
				url = 'https://api.real-debrid.com/rest/1.0/torrents?auth_token=%s' % self.token
				r = client.request(url)
				match = re.compile('"filename": "(.+?)"').findall(r)
				for filename in match: 
					if q in filename:
						quality = torrent.qualityCheck(filename)
						
						if '.mkv' in filename: 
							url = filename
							sources.append({'source': 'Torrent','info': filename,'quality': quality,'language': 'en','url': url,'direct': False,'debridonly': False})
						if '.mp4' in filename: 
							url = filename
							sources.append({'source': 'Torrent','info': filename,'quality': quality,'language': 'en','url': url,'direct': False,'debridonly': False})
						if '.avi' in filename: 
							url = filename
							sources.append({'source': 'Torrent','info': filename,'quality': quality,'language': 'en','url': url,'direct': False,'debridonly': False})
						if '.flv' in filename: 
							url = filename
							sources.append({'source': 'Torrent','info': filename,'quality': quality,'language': 'en','url': url,'direct': False,'debridonly': False})
			except: return
			
			try: # No space
				q = q.replace(' ','.')
				url = 'https://api.real-debrid.com/rest/1.0/torrents?auth_token=%s' % self.token
				r = client.request(url)
				match = re.compile('"filename": "(.+?)"').findall(r)
				for filename in match: 
					if q in filename:
						quality = torrent.qualityCheck(filename)
						
						if '.mkv' in filename: 
							url = filename
							sources.append({'source': 'Torrent','info': filename,'quality': quality,'language': 'en','url': url,'direct': False,'debridonly': False})
						if '.mp4' in filename: 
							url = filename
							sources.append({'source': 'Torrent','info': filename,'quality': quality,'language': 'en','url': url,'direct': False,'debridonly': False})
						if '.avi' in filename: 
							url = filename
							sources.append({'source': 'Torrent','info': filename,'quality': quality,'language': 'en','url': url,'direct': False,'debridonly': False})
						if '.flv' in filename: 
							url = filename
							sources.append({'source': 'Torrent','info': filename,'quality': quality,'language': 'en','url': url,'direct': False,'debridonly': False})
			except: return

		except Exception:
			return
		return sources

	def resolve(self, url):
		filename = url
		# Fetch magnet link
		
		import time
		time.sleep(5)
				
		api = 'https://api.real-debrid.com/rest/1.0/torrents?auth_token=%s' % self.token
		r = client.request(api)
		r = r.replace('	','').replace('\n','').replace('[','').replace(']','').replace('\/','/').replace('(','').replace(')','')
		match = re.compile('"filename": ".+?","hash": ".+?","bytes": .+?,"host": ".+?","split": .+?,"progress": 100,"status": "downloaded","added": ".+?","links": "https://real-debrid\.com/d/(.+?)"').findall(r)
		for url in match: 
			url = 'plugin://script.realdebrid.mod/?url=https://real-debrid.com/d/%s&mode=5&name=Real-Debrid&icon=none&fanart=none&poster=none' % url
			return url
			
			