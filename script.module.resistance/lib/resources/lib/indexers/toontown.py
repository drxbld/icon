# -*- coding: utf-8 -*-




import os,sys,urlparse

from resources.lib.modules import control
from resources.lib.modules import trakt
from resources.lib.modules import cache
import xbmc
import xbmcaddon
import xbmcgui

sysaddon = sys.argv[0] ; syshandle = int(sys.argv[1])

artPath = control.artPath() ; addonFanart = control.addonFanart()

imdbCredentials = False if control.setting('imdb.user') == '' else True

traktCredentials = trakt.getTraktCredentialsInfo()

traktIndicators = trakt.getTraktIndicatorsInfo()

queueMenu = control.lang(32065).encode('utf-8')

class navigator:
	def root(self):

		self.addDirectoryItem('Anime Tv Shows', 'animetvNavigator', 'toont.png', 'Defaulttoont.png')
		self.addDirectoryItem('Anime Movies', 'animemovieNavigator', 'toont.png', 'Defaulttoont.png')
		self.addDirectoryItem('Toons Movies', 'toonmovieNavigator', 'toont.png', 'Defaulttoont.png')
		self.addDirectoryItem('Toons Tv Shows', 'toonstvNavigator', 'toont.png', 'Defaulttoont.png')




		#if not control.setting('lists.widget') == '0':
			#self.addDirectoryItem(32003, 'mymovieNavigator', 'toont.png', 'DefaultVideoPlaylists.jpg')
			#self.addDirectoryItem(32004, 'mytvNavigator', 'toont.png', 'DefaultVideoPlaylists.jpg')

		#self.addDirectoryItem(32008, 'toolNavigator', 'toont.png', 'DefaultAddonProgram.jpg')

		#downloads = True if control.setting('downloads') == 'true' and (len(control.listDir(control.setting('movie.download.path'))[0]) > 0 or len(control.listDir(control.setting('tv.download.path'))[0]) > 0) else False
		#if downloads == True:
			#self.addDirectoryItem(32009, 'downloadNavigator', 'dir.jpg', 'DefaultFolder.jpg')

		self.endDirectory()


	def toonsmov(self, lite=False):
		self.addDirectoryItem(32011, 'movieGenres', 'toont.png', 'Defaulttoont.png')

		self.addDirectoryItem(32012, 'movieYears', 'toont.png', 'Defaulttoont.png')
		self.addDirectoryItem('Popular', 'movies3&url=popular', 'toont.png', 'Defaulttoont.png')
		self.addDirectoryItem('Highest Voted', 'movies3&url=views', 'toont.png', 'Defaulttoont.png')
		self.addDirectoryItem('Featured', 'movies3&url=featured', 'toont.png', 'Defaulttoont.png')
		self.addDirectoryItem(32021, 'movies3&url=oscars', 'toont.png', 'Defaulttoont.png')
		self.addDirectoryItem('boxoffice', 'movies3&url=boxoffice', 'toont.png', 'Defaulttoont.png')
		self.addDirectoryItem(32022, 'movies3&url=theaters', 'toont.png', 'DefaultRecentlyAddedtoont.png')

		
		#if lite == False:
			#if not control.setting('lists.widget') == '0':
				#self.addDirectoryItem(32003, 'mymovieliteNavigator', 'toont.png', 'DefaultVideoPlaylists.jpg')

			#self.addDirectoryItem('Actor Search', 'moviePerson', 'actorsearch.jpg', 'Defaulttoont.png')
			#self.addDirectoryItem(32010, 'movieSearch', 'search.jpg', 'Defaulttoont.png')

		self.endDirectory()

	def animemov(self, lite=False):

		self.addDirectoryItem(32011, 'animegenres', 'toont.png', 'Defaulttoont.png')
		#self.addDirectoryItem('certifications', 'movieanimecertifications', 'toont.png', 'Defaulttoont.png')
		self.addDirectoryItem(32012, 'animemovyears', 'toont.png', 'Defaulttoont.png')
		self.addDirectoryItem('Popular', 'movies3&url=animepopular', 'toont.png', 'Defaulttoont.png')
		self.addDirectoryItem('Highest Voted', 'movies3&url=animeviews', 'toont.png', 'Defaulttoont.png')
		self.addDirectoryItem(32022, 'movies3&url=animetheaters', 'toont.png', 'DefaultRecentlyAddedtoont.png')

		
		if lite == False:
			if not control.setting('lists.widget') == '0':
				self.addDirectoryItem(32003, 'mymovieliteNavigator', 'toont.png', 'DefaultVideoPlaylists.jpg')

			#self.addDirectoryItem('Actor Search', 'moviePerson', 'actorsearch.jpg', 'Defaulttoont.png')
			#self.addDirectoryItem(32010, 'movieSearch', 'search.jpg', 'Defaulttoont.png')

		self.endDirectory()


	def mymovies(self, lite=False):
		self.accountCheck()

		if traktCredentials == True and imdbCredentials == True:
			self.addDirectoryItem(32032, 'movies3&url=traktcollection', 'toont.png', 'Defaulttoont.png', queue=True, context=(32551, 'moviesToLibrary&url=traktcollection'))
			self.addDirectoryItem(32033, 'movies3&url=traktwatchlist', 'toont.png', 'Defaulttoont.png', queue=True, context=(32551, 'moviesToLibrary&url=traktwatchlist'))
			self.addDirectoryItem(32034, 'movies3&url=imdbwatchlist', 'toont.png', 'Defaulttoont.png', queue=True)

		elif traktCredentials == True:
			self.addDirectoryItem(32032, 'movies3&url=traktcollection', 'toont.png', 'Defaulttoont.png', queue=True, context=(32551, 'moviesToLibrary&url=traktcollection'))
			self.addDirectoryItem(32033, 'movies3&url=traktwatchlist', 'toont.png', 'Defaulttoont.png', queue=True, context=(32551, 'moviesToLibrary&url=traktwatchlist'))

		elif imdbCredentials == True:
			self.addDirectoryItem(32032, 'movies3&url=imdbwatchlist', 'toont.png', 'Defaulttoont.png', queue=True)
			self.addDirectoryItem(32033, 'movies3&url=imdbwatchlist2', 'toont.png', 'Defaulttoont.png', queue=True)

		if traktCredentials == True:
			self.addDirectoryItem(32035, 'movies3&url=traktfeatured', 'toont.png', 'Defaulttoont.png', queue=True)

		elif imdbCredentials == True:
			self.addDirectoryItem(32035, 'movies3&url=featured', 'toont.png', 'Defaulttoont.png', queue=True)

		if traktIndicators == True:
			self.addDirectoryItem(32036, 'movies3&url=trakthistory', 'toont.png', 'Defaulttoont.png', queue=True)

		self.addDirectoryItem(32039, 'movieUserlists', 'toont.png', 'Defaulttoont.png')

		if lite == False:
			self.addDirectoryItem(32031, 'movieliteNavigator', 'toont.png', 'Defaulttoont.png')
			self.addDirectoryItem('Actor Search', 'moviePerson', 'actorsearch.jpg', 'Defaulttoont.png')
			self.addDirectoryItem(32010, 'movieSearch', 'search.jpg', 'Defaulttoont.png')

		self.endDirectory()


	def toonstvshows(self, lite=False):

		self.addDirectoryItem(32012, 'tvYears', 'toont.png', 'Defaulttoont.png')
		self.addDirectoryItem(32011, 'tvGenres', 'toont.png', 'Defaulttoont.png')
		self.addDirectoryItem('Most Viewed', 'tvshows3&url=views', 'toont.png', 'playlist.jpg')
		#self.addDirectoryItem('Certifications', 'tvCertificates', 'toont.png', 'playlist.jpg')


		self.addDirectoryItem(32026, 'tvshows3&url=premiere', 'toont.png', 'Defaulttoont.png')
		self.addDirectoryItem('Popular', 'tvshows3&url=popular', 'toont.png', 'playlist.jpg')

		#if lite == False:
			#if not control.setting('lists.widget') == '0':
				#self.addDirectoryItem(32004, 'mytvliteNavigator', 'toont.png', 'DefaultVideoPlaylists.jpg')




		self.endDirectory()

	def animetvshows(self, lite=False):

		self.addDirectoryItem(32012, 'tvYears', 'toont.png', 'Defaulttoont.png')
		self.addDirectoryItem(32011, 'animeGenres', 'toont.png', 'Defaulttoont.png')
		self.addDirectoryItem('Most Viewed', 'tvshows3&url=animeviews', 'toont.png', 'playlist.jpg')
		#self.addDirectoryItem('Certifications', 'tvshows3&url=tvanimecertifications', 'toont.png', 'playlist.jpg')
		#self.addDirectoryItem('Active', 'tvshows3&url=animeactive', 'toont.png', 'playlist.jpg')

		#self.addDirectoryItem('Airing', 'tvshows3&url=animeairing', 'toont.png', 'playlist.jpg')

		self.addDirectoryItem(32026, 'tvshows3&url=animepremiere', 'toont.png', 'Defaulttoont.png')
		self.addDirectoryItem('Popular', 'tvshows3&url=animepopular', 'toont.png', 'playlist.jpg')

		#if lite == False:
			#if not control.setting('lists.widget') == '0':
				#self.addDirectoryItem(32004, 'mytvliteNavigator', 'toont.png', 'DefaultVideoPlaylists.jpg')




		self.endDirectory()

	def mytvshows(self, lite=False):
		self.accountCheck()

		if traktCredentials == True and imdbCredentials == True:
			self.addDirectoryItem(32032, 'tvshows3&url=traktcollection', 'toont.png', 'Defaulttoont.png', context=(32551, 'tvshowsToLibrary&url=traktcollection'))
			self.addDirectoryItem(32033, 'tvshows3&url=traktwatchlist', 'toont.png', 'Defaulttoont.png', context=(32551, 'tvshowsToLibrary&url=traktwatchlist'))
			self.addDirectoryItem(32034, 'tvshows3&url=imdbwatchlist', 'toont.png', 'Defaulttoont.png')

		elif traktCredentials == True:
			self.addDirectoryItem(32032, 'tvshows3&url=traktcollection', 'toont.png', 'Defaulttoont.png', context=(32551, 'tvshowsToLibrary&url=traktcollection'))
			self.addDirectoryItem(32033, 'tvshows3&url=traktwatchlist', 'toont.png', 'Defaulttoont.png', context=(32551, 'tvshowsToLibrary&url=traktwatchlist'))

		elif imdbCredentials == True:
			self.addDirectoryItem(32032, 'tvshows3&url=imdbwatchlist', 'toont.png', 'Defaulttoont.png')
			self.addDirectoryItem(32033, 'tvshows3&url=imdbwatchlist2', 'toont.png', 'Defaulttoont.png')

		if traktCredentials == True:
			self.addDirectoryItem(32035, 'tvshows3&url=traktfeatured', 'toont.png', 'Defaulttoont.png')

		elif imdbCredentials == True:
			self.addDirectoryItem(32035, 'tvshows3&url=trending', 'toont.png', 'Defaulttoont.png', queue=True)

		if traktIndicators == True:
			self.addDirectoryItem(32036, 'calendar&url=trakthistory', 'toont.png', 'Defaulttoont.png', queue=True)
			self.addDirectoryItem(32037, 'calendar&url=progress', 'toont.png', 'DefaultRecentlyAddedEpisodes.jpg', queue=True)
			self.addDirectoryItem(32038, 'calendar&url=mycalendar', 'toont.png', 'DefaultRecentlyAddedEpisodes.jpg', queue=True)

		self.addDirectoryItem(32040, 'tvUserlists', 'toont.png', 'Defaulttoont.png')

		if traktCredentials == True:
			self.addDirectoryItem(32041, 'episodeUserlists', 'toont.png', 'Defaulttoont.png')

		if lite == False:
			self.addDirectoryItem(32031, 'tvliteNavigator', 'toont.png', 'Defaulttoont.png')
			self.addDirectoryItem('Actor Search', 'tvPerson', 'actorsearch.jpg', 'Defaulttoont.png')
			self.addDirectoryItem(32010, 'tvSearch', 'search.jpg', 'Defaulttoont.png')

		self.endDirectory()

		

	def tools(self):
		self.addDirectoryItem(32043, 'openSettings&query=0.0', 'toont.png', 'DefaultAddonProgram.jpg')
		self.addDirectoryItem(32044, 'openSettings&query=3.1', 'toont.png', 'DefaultAddonProgram.jpg')
		self.addDirectoryItem(32045, 'openSettings&query=1.0', 'toont.png', 'DefaultAddonProgram.jpg')
		self.addDirectoryItem(32046, 'openSettings&query=6.0', 'toont.png', 'DefaultAddonProgram.jpg')
		self.addDirectoryItem(32047, 'openSettings&query=2.0', 'toont.png', 'DefaultAddonProgram.jpg')
		self.addDirectoryItem(32556, 'libraryNavigator', 'toont.png', 'DefaultAddonProgram.jpg')
		self.addDirectoryItem(32048, 'openSettings&query=5.0', 'toont.png', 'DefaultAddonProgram.jpg')
		self.addDirectoryItem(32049, 'viewsNavigator', 'toont.png', 'DefaultAddonProgram.jpg')
		self.addDirectoryItem(32050, 'clearSources', 'toont.png', 'DefaultAddonProgram.jpg')
		self.addDirectoryItem(32052, 'clearCache', 'toont.png', 'DefaultAddonProgram.jpg')

		self.endDirectory()

	def library(self):
		self.addDirectoryItem(32557, 'openSettings&query=4.0', 'toont.png', 'DefaultAddonProgram.jpg')
		self.addDirectoryItem(32558, 'updateLibrary&query=tool', 'library_update.jpg', 'DefaultAddonProgram.jpg')
		self.addDirectoryItem(32559, control.setting('library.movie'), 'toont.png', 'Defaulttoont.png', isAction=False)
		self.addDirectoryItem(32560, control.setting('library.tv'), 'toont.png', 'Defaulttoont.png', isAction=False)

		if trakt.getTraktCredentialsInfo():
			self.addDirectoryItem(32561, 'moviesToLibrary&url=traktcollection', 'toont.png', 'Defaulttoont.png')
			self.addDirectoryItem(32562, 'moviesToLibrary&url=traktwatchlist', 'toont.png', 'Defaulttoont.png')
			self.addDirectoryItem(32563, 'tvshowsToLibrary&url=traktcollection', 'toont.png', 'Defaulttoont.png')
			self.addDirectoryItem(32564, 'tvshowsToLibrary&url=traktwatchlist', 'toont.png', 'Defaulttoont.png')

		self.endDirectory()

	def downloads(self):
		movie_downloads = control.setting('movie.download.path')
		tv_downloads = control.setting('tv.download.path')

		if len(control.listDir(movie_downloads)[0]) > 0:
			self.addDirectoryItem(32001, movie_downloads, 'toont.png', 'Defaulttoont.png', isAction=False)
		if len(control.listDir(tv_downloads)[0]) > 0:
			self.addDirectoryItem(32002, tv_downloads, 'toont.png', 'Defaulttoont.png', isAction=False)

		self.endDirectory()


	def search(self):
		self.addDirectoryItem(32001, 'movieSearch', 'toont.png', 'Defaulttoont.png')
		self.addDirectoryItem(32002, 'tvSearch', 'toont.png', 'Defaulttoont.png')
		self.addDirectoryItem('Actor Search', 'moviePerson', 'toont.png', 'Defaulttoont.png')
		self.addDirectoryItem('TV Actor Search', 'tvPerson', 'toont.png', 'Defaulttoont.png')

		self.endDirectory()


	def views(self):
		try:
			control.idle()

			items = [ (control.lang(32001).encode('utf-8'), 'movies'), (control.lang(32002).encode('utf-8'), 'tvshows'), (control.lang(32054).encode('utf-8'), 'seasons'), (control.lang(32038).encode('utf-8'), 'episodes') ]

			select = control.selectDialog([i[0] for i in items], control.lang(32049).encode('utf-8'))

			if select == -1: return

			content = items[select][1]

			title = control.lang(32059).encode('utf-8')
			url = '%s?action=addView&content=%s' % (sys.argv[0], content)

			poster, banner, fanart = control.addonPoster(), control.addonBanner(), control.addonFanart()

			item = control.item(label=title)
			item.setInfo(type='Video', infoLabels = {'title': title})
			item.setArt({'icon': poster, 'thumb': poster, 'poster': poster, 'banner': banner})
			item.setProperty('Fanart_Image', fanart)

			control.addItem(handle=int(sys.argv[1]), url=url, listitem=item, isFolder=False)
			control.content(int(sys.argv[1]), content)
			control.directory(int(sys.argv[1]), cacheToDisc=True)

			from resources.lib.modules import views
			views.setView(content, {})
		except:
			return


	def accountCheck(self):
		if traktCredentials == False and imdbCredentials == False:
			control.idle()
			control.infoDialog(control.lang(32042).encode('utf-8'), sound=True, icon='WARNING')
			sys.exit()




	def clearCache(self):
		control.idle()
		yes = control.yesnoDialog(control.lang(32056).encode('utf-8'), '', '')
		if not yes: return
		from resources.lib.modules import cache
		cache.cache_clear()
		control.infoDialog(control.lang(32057).encode('utf-8'), sound=True, icon='INFO')


	def addDirectoryItem(self, name, query, thumb, icon, context=None, queue=False, isAction=True, isFolder=True):
		try: name = control.lang(name).encode('utf-8')
		except: pass
		url = '%s?action=%s' % (sysaddon, query) if isAction == True else query
		thumb = os.path.join(artPath, thumb) if not artPath == None else icon
		cm = []
		if queue == True: cm.append((queueMenu, 'RunPlugin(%s?action=queueItem)' % sysaddon))
		if not context == None: cm.append((control.lang(context[0]).encode('utf-8'), 'RunPlugin(%s?action=%s)' % (sysaddon, context[1])))
		item = control.item(label=name)
		item.addContextMenuItems(cm)
		item.setArt({'icon': thumb, 'thumb': thumb})
		if not addonFanart == None: item.setProperty('Fanart_Image', addonFanart)
		control.addItem(handle=syshandle, url=url, listitem=item, isFolder=isFolder)


	def endDirectory(self):
		control.content(syshandle, 'addons')
		control.directory(syshandle, cacheToDisc=True)


