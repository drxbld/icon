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


		self.addDirectoryItem(32001, 'astropmNavigator', 'astro.png', 'Defaultastro.png')
		self.addDirectoryItem(32002, 'astroptNavigator', 'astro.png', 'Defaultastro.png')




		#if not control.setting('lists.widget') == '0':
			#self.addDirectoryItem(32003, 'mymovieNavigator', 'astro.png', 'DefaultVideoPlaylists.jpg')
			#self.addDirectoryItem(32004, 'mytvNavigator', 'astro.png', 'DefaultVideoPlaylists.jpg')

		#self.addDirectoryItem(32008, 'toolNavigator', 'tools.jpg', 'DefaultAddonProgram.jpg')

		#downloads = True if control.setting('downloads') == 'true' and (len(control.listDir(control.setting('movie.download.path'))[0]) > 0 or len(control.listDir(control.setting('tv.download.path'))[0]) > 0) else False
		#if downloads == True:
			#self.addDirectoryItem(32009, 'downloadNavigator', 'dir.jpg', 'DefaultFolder.jpg')

		self.endDirectory()


	def astropm(self, lite=False):
		self.addDirectoryItem('Franchise', 'Franchise1Navigator', 'astro.png', 'Defaultastro.png')
		self.addDirectoryItem('Top Sci Fi Directors', 'namegenre', 'astro.png', 'Defaultastro.png')
		#self.addDirectoryItem('Anime', 'movies7&url=scifidir', 'astro.png', 'Defaultastro.png')
		self.addDirectoryItem(32011, 'movieGenres', 'astro.png', 'Defaultastro.png')

		self.addDirectoryItem(32012, 'movieYears', 'astro.png', 'Defaultastro.png')
		#self.addDirectoryItem('Popular', 'movies7&url=popular', 'astro.png', 'Defaultastro.png')
		self.addDirectoryItem('Highest Voted', 'movies7&url=views', 'astro.png', 'Defaultastro.png')
		self.addDirectoryItem('Featured', 'movies7&url=featured', 'astro.png', 'Defaultastro.png')
		self.addDirectoryItem(32021, 'movies7&url=oscars', 'astro.png', 'Defaultastro.png')
		self.addDirectoryItem('boxoffice', 'movies7&url=boxoffice', 'astro.png', 'Defaultastro.png')
		self.addDirectoryItem(32022, 'movies7&url=theaters', 'astro.png', 'DefaultRecentlyAddedastro.png')

		
		#if lite == False:
			#if not control.setting('lists.widget') == '0':
				#self.addDirectoryItem(32003, 'mymovieliteNavigator', 'astro.png', 'DefaultVideoPlaylists.jpg')

			#self.addDirectoryItem('Actor Search', 'moviePerson', 'actorsearch.jpg', 'Defaultastro.png')
			#self.addDirectoryItem(32010, 'movieSearch', 'search.jpg', 'Defaultastro.png')

		self.endDirectory()


	def Franchise1(self, lite=False):
		self.addDirectoryItem('STARTREK', 'movies7&url=STARTREK', 'astro.png', 'Defaultastro.png')
		self.addDirectoryItem('STARWARS', 'movies7&url=STARWARS', 'astro.png', 'Defaultastro.png')
		self.addDirectoryItem('THEOUTERLIMITS', 'movies7&url=THEOUTERLIMITS', 'astro.png', 'Defaultastro.png')
		self.addDirectoryItem('THETWILIGHTZONE', 'movies7&url=THETWILIGHTZONE', 'astro.png', 'Defaultastro.png')
		self.addDirectoryItem('DOCTORWHO', 'movies7&url=DOCTORWHO', 'astro.png', 'Defaultastro.png')
		self.addDirectoryItem('BATTLESTARGALACTICA', 'movies7&url=BATTLESTARGALACTICA', 'astro.png', 'Defaultastro.png')
		self.addDirectoryItem('PLANETOFTHEAPES', 'movies7&url=PLANETOFTHEAPES', 'astro.png', 'Defaultastro.png')
		self.addDirectoryItem('STARGATE', 'movies7&url=STARGATE', 'astro.png', 'Defaultastro.png')
		self.addDirectoryItem('FLASHGORDON', 'movies7&url=FLASHGORDON', 'astro.png', 'Defaultastro.png')
		self.addDirectoryItem('BACKTOTHEFUTURE', 'movies7&url=BACKTOTHEFUTURE', 'astro.png', 'Defaultastro.png')
		self.addDirectoryItem('THEXFILES', 'movies7&url=THEXFILES', 'astro.png', 'Defaultastro.png')
		self.addDirectoryItem('FIREFLY', 'movies7&url=FIREFLY', 'astro.png', 'Defaultastro.png')
		self.addDirectoryItem('GODZILLA', 'movies7&url=GODZILLA', 'astro.png', 'Defaultastro.png')
		self.addDirectoryItem('THETERMINATOR', 'movies7&url=THETERMINATOR', 'astro.png', 'Defaultastro.png')
		self.addDirectoryItem('JURASSICPARK', 'movies7&url=JURASSICPARK', 'astro.png', 'Defaultastro.png')
		self.addDirectoryItem('BABYLON', 'movies7&url=BABYLON', 'astro.png', 'Defaultastro.png')
		self.addDirectoryItem('MADMAX', 'movies7&url=MADMAX', 'astro.png', 'Defaultastro.png')
		self.addDirectoryItem('THEMATRIX', 'movies7&url=THEMATRIX', 'astro.png', 'Defaultastro.png')	
		self.endDirectory()


	def Franchise2(self, lite=False):
		self.addDirectoryItem('STARTREK', 'tvshows7&url=STARTREK', 'astro.png', 'Defaultastro.png')
		self.addDirectoryItem('STARWARS', 'tvshows7&url=STARWARS', 'astro.png', 'Defaultastro.png')
		self.addDirectoryItem('THEOUTERLIMITS', 'tvshows7&url=THEOUTERLIMITS', 'astro.png', 'Defaultastro.png')
		self.addDirectoryItem('THETWILIGHTZONE', 'tvshows7&url=THETWILIGHTZONE', 'astro.png', 'Defaultastro.png')
		self.addDirectoryItem('DOCTORWHO', 'tvshows7&url=DOCTORWHO', 'astro.png', 'Defaultastro.png')
		self.addDirectoryItem('BATTLESTARGALACTICA', 'tvshows7&url=BATTLESTARGALACTICA', 'astro.png', 'Defaultastro.png')
		self.addDirectoryItem('STARGATE', 'tvshows7&url=STARGATE', 'astro.png', 'Defaultastro.png')
		self.addDirectoryItem('FLASHGORDON', 'tvshows7&url=FLASHGORDON', 'astro.png', 'Defaultastro.png')
		self.addDirectoryItem('THEXFILES', 'tvshows7&url=THEXFILES', 'astro.png', 'Defaultastro.png')
		self.addDirectoryItem('FIREFLY', 'tvshows7&url=FIREFLY', 'astro.png', 'Defaultastro.png')
		self.addDirectoryItem('THETERMINATOR', 'tvshows7&url=THETERMINATOR', 'astro.png', 'Defaultastro.png')
		self.addDirectoryItem('BABYLON', 'tvshows7&url=BABYLON', 'astro.png', 'Defaultastro.png')
		self.endDirectory()	

	def mymovies(self, lite=False):
		self.accountCheck()

		if traktCredentials == True and imdbCredentials == True:
			self.addDirectoryItem(32032, 'movies7&url=traktcollection', 'astro.png', 'Defaultastro.png', queue=True, context=(32551, 'moviesToLibrary&url=traktcollection'))
			self.addDirectoryItem(32033, 'movies7&url=traktwatchlist', 'astro.png', 'Defaultastro.png', queue=True, context=(32551, 'moviesToLibrary&url=traktwatchlist'))
			self.addDirectoryItem(32034, 'movies7&url=imdbwatchlist', 'astro.png', 'Defaultastro.png', queue=True)

		elif traktCredentials == True:
			self.addDirectoryItem(32032, 'movies7&url=traktcollection', 'astro.png', 'Defaultastro.png', queue=True, context=(32551, 'moviesToLibrary&url=traktcollection'))
			self.addDirectoryItem(32033, 'movies7&url=traktwatchlist', 'astro.png', 'Defaultastro.png', queue=True, context=(32551, 'moviesToLibrary&url=traktwatchlist'))

		elif imdbCredentials == True:
			self.addDirectoryItem(32032, 'movies7&url=imdbwatchlist', 'astro.png', 'Defaultastro.png', queue=True)
			self.addDirectoryItem(32033, 'movies7&url=imdbwatchlist2', 'astro.png', 'Defaultastro.png', queue=True)

		if traktCredentials == True:
			self.addDirectoryItem(32035, 'movies7&url=traktfeatured', 'astro.png', 'Defaultastro.png', queue=True)

		elif imdbCredentials == True:
			self.addDirectoryItem(32035, 'movies7&url=featured', 'astro.png', 'Defaultastro.png', queue=True)

		if traktIndicators == True:
			self.addDirectoryItem(32036, 'movies7&url=trakthistory', 'astro.png', 'Defaultastro.png', queue=True)

		self.addDirectoryItem(32039, 'movieUserlists', 'astro.png', 'Defaultastro.png')

		if lite == False:
			self.addDirectoryItem(32031, 'movieliteNavigator', 'astro.png', 'Defaultastro.png')
			self.addDirectoryItem('Actor Search', 'moviePerson', 'actorsearch.jpg', 'Defaultastro.png')
			self.addDirectoryItem(32010, 'movieSearch', 'search.jpg', 'Defaultastro.png')

		self.endDirectory()


	def astropt(self, lite=False):
		self.addDirectoryItem('Franchise', 'Franchise2Navigator', 'astro.png', 'Defaultastro.png')
		#self.addDirectoryItem('Anime', 'tvshows7&url=anime', 'astro.png', 'Defaultastro.png')
		self.addDirectoryItem(32012, 'tvYears', 'astro.png', 'Defaultastro.png')
		#self.addDirectoryItem(32011, 'tvGenres', 'astro.png', 'Defaultastro.png')



		self.addDirectoryItem(32026, 'tvshows7&url=premiere', 'astro.png', 'Defaultastro.png')
		#self.addDirectoryItem('Popular', 'tvshows7&url=popular', 'astro.png', 'playlist.jpg')

		#if lite == False:
			#if not control.setting('lists.widget') == '0':
				#self.addDirectoryItem(32004, 'mytvliteNavigator', 'astro.png', 'DefaultVideoPlaylists.jpg')




		self.endDirectory()


	def mytvshows(self, lite=False):
		self.accountCheck()

		if traktCredentials == True and imdbCredentials == True:
			self.addDirectoryItem(32032, 'tvshows7&url=traktcollection', 'astro.png', 'Defaultastro.png', context=(32551, 'tvshowsToLibrary&url=traktcollection'))
			self.addDirectoryItem(32033, 'tvshows7&url=traktwatchlist', 'astro.png', 'Defaultastro.png', context=(32551, 'tvshowsToLibrary&url=traktwatchlist'))
			self.addDirectoryItem(32034, 'tvshows7&url=imdbwatchlist', 'astro.png', 'Defaultastro.png')

		elif traktCredentials == True:
			self.addDirectoryItem(32032, 'tvshows7&url=traktcollection', 'astro.png', 'Defaultastro.png', context=(32551, 'tvshowsToLibrary&url=traktcollection'))
			self.addDirectoryItem(32033, 'tvshows7&url=traktwatchlist', 'astro.png', 'Defaultastro.png', context=(32551, 'tvshowsToLibrary&url=traktwatchlist'))

		elif imdbCredentials == True:
			self.addDirectoryItem(32032, 'tvshows7&url=imdbwatchlist', 'astro.png', 'Defaultastro.png')
			self.addDirectoryItem(32033, 'tvshows7&url=imdbwatchlist2', 'astro.png', 'Defaultastro.png')

		if traktCredentials == True:
			self.addDirectoryItem(32035, 'tvshows7&url=traktfeatured', 'astro.png', 'Defaultastro.png')

		elif imdbCredentials == True:
			self.addDirectoryItem(32035, 'tvshows7&url=trending', 'astro.png', 'Defaultastro.png', queue=True)

		if traktIndicators == True:
			self.addDirectoryItem(32036, 'calendar&url=trakthistory', 'astro.png', 'Defaultastro.png', queue=True)
			self.addDirectoryItem(32037, 'calendar&url=progress', 'astro.png', 'DefaultRecentlyAddedEpisodes.jpg', queue=True)
			self.addDirectoryItem(32038, 'calendar&url=mycalendar', 'astro.png', 'DefaultRecentlyAddedEpisodes.jpg', queue=True)

		self.addDirectoryItem(32040, 'tvUserlists', 'astro.png', 'Defaultastro.png')

		if traktCredentials == True:
			self.addDirectoryItem(32041, 'episodeUserlists', 'myastro.png', 'Defaultastro.png')

		if lite == False:
			self.addDirectoryItem(32031, 'tvliteNavigator', 'astro.png', 'Defaultastro.png')
			self.addDirectoryItem('Actor Search', 'tvPerson', 'actorsearch.jpg', 'Defaultastro.png')
			self.addDirectoryItem(32010, 'tvSearch', 'search.jpg', 'Defaultastro.png')

		self.endDirectory()

		

	def tools(self):
		self.addDirectoryItem(32043, 'openSettings&query=0.0', 'tools.jpg', 'DefaultAddonProgram.jpg')
		self.addDirectoryItem(32044, 'openSettings&query=3.1', 'tools.jpg', 'DefaultAddonProgram.jpg')
		self.addDirectoryItem(32045, 'openSettings&query=1.0', 'tools.jpg', 'DefaultAddonProgram.jpg')
		self.addDirectoryItem(32046, 'openSettings&query=6.0', 'tools.jpg', 'DefaultAddonProgram.jpg')
		self.addDirectoryItem(32047, 'openSettings&query=2.0', 'tools.jpg', 'DefaultAddonProgram.jpg')
		self.addDirectoryItem(32556, 'libraryNavigator', 'tools.jpg', 'DefaultAddonProgram.jpg')
		self.addDirectoryItem(32048, 'openSettings&query=5.0', 'tools.jpg', 'DefaultAddonProgram.jpg')
		self.addDirectoryItem(32049, 'viewsNavigator', 'tools.jpg', 'DefaultAddonProgram.jpg')
		self.addDirectoryItem(32050, 'clearSources', 'tools.jpg', 'DefaultAddonProgram.jpg')
		self.addDirectoryItem(32052, 'clearCache', 'tools.jpg', 'DefaultAddonProgram.jpg')

		self.endDirectory()

	def library(self):
		self.addDirectoryItem(32557, 'openSettings&query=4.0', 'tools.jpg', 'DefaultAddonProgram.jpg')
		self.addDirectoryItem(32558, 'updateLibrary&query=tool', 'library_update.jpg', 'DefaultAddonProgram.jpg')
		self.addDirectoryItem(32559, control.setting('library.movie'), 'astro.png', 'Defaultastro.png', isAction=False)
		self.addDirectoryItem(32560, control.setting('library.tv'), 'astro.png', 'Defaultastro.png', isAction=False)

		if trakt.getTraktCredentialsInfo():
			self.addDirectoryItem(32561, 'moviesToLibrary&url=traktcollection', 'astro.png', 'Defaultastro.png')
			self.addDirectoryItem(32562, 'moviesToLibrary&url=traktwatchlist', 'astro.png', 'Defaultastro.png')
			self.addDirectoryItem(32563, 'tvshowsToLibrary&url=traktcollection', 'astro.png', 'Defaultastro.png')
			self.addDirectoryItem(32564, 'tvshowsToLibrary&url=traktwatchlist', 'astro.png', 'Defaultastro.png')

		self.endDirectory()

	def downloads(self):
		movie_downloads = control.setting('movie.download.path')
		tv_downloads = control.setting('tv.download.path')

		if len(control.listDir(movie_downloads)[0]) > 0:
			self.addDirectoryItem(32001, movie_downloads, 'astro.png', 'Defaultastro.png', isAction=False)
		if len(control.listDir(tv_downloads)[0]) > 0:
			self.addDirectoryItem(32002, tv_downloads, 'astro.png', 'Defaultastro.png', isAction=False)

		self.endDirectory()


	def search(self):
		self.addDirectoryItem(32001, 'movieSearch', 'astro.png', 'Defaultastro.png')
		self.addDirectoryItem(32002, 'tvSearch', 'astro.png', 'Defaultastro.png')
		self.addDirectoryItem('Actor Search', 'moviePerson', 'astro.png', 'Defaultastro.png')
		self.addDirectoryItem('TV Actor Search', 'tvPerson', 'astro.png', 'Defaultastro.png')

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


