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
		self.addDirectoryItem('Nightmare Movies', 'nightmaremovNavigator', 'night.png', 'Defaultnight.png')
		self.addDirectoryItem('Nightmare TV Shows', 'nightmaretvNavigator', 'night.png', 'Defaultnight.png')




		#if not control.setting('lists.widget') == '0':
			#self.addDirectoryItem(32003, 'mymovieNavigator', 'night.png', 'DefaultVideoPlaylists.jpg')
			#self.addDirectoryItem(32004, 'mytvNavigator', 'night.png', 'DefaultVideoPlaylists.jpg')

		#self.addDirectoryItem(32008, 'toolNavigator', 'tools.gif', 'DefaultAddonProgram.jpg')

		#downloads = True if control.setting('downloads') == 'true' and (len(control.listDir(control.setting('movie.download.path'))[0]) > 0 or len(control.listDir(control.setting('tv.download.path'))[0]) > 0) else False
		#if downloads == True:
			#self.addDirectoryItem(32009, 'downloadNavigator', 'dir.gif', 'DefaultFolder.jpg')

		self.endDirectory()


	def nightmaremov(self, lite=False):
		self.addDirectoryItem('Franchise', 'FranchiseNavigator', 'night.png', 'Defaultnight.png')
		self.addDirectoryItem('Scream Queens', 'screamq', 'night.png', 'Defaultnight.png')
		self.addDirectoryItem('Top Fifty Horror Directors', 'namegenre', 'night.png', 'Defaultnight.png')
		self.addDirectoryItem('Anime', 'movies4&url=anime', 'night.png', 'Defaultnight.png')
		#self.addDirectoryItem(32011, 'movieGenres', 'night.png', 'Defaultnight.png')

		self.addDirectoryItem(32012, 'movieYears', 'night.png', 'Defaultnight.png')
		#self.addDirectoryItem('Certificates', 'movieCertificates', 'night.png', 'Defaultnight.png')
		self.addDirectoryItem('Popular', 'movies4&url=popular', 'night.png', 'Defaultnight.png')
		self.addDirectoryItem('Highest Voted', 'movies4&url=views', 'night.png', 'Defaultnight.png')
		self.addDirectoryItem('Featured', 'movies4&url=featured', 'night.png', 'Defaultnight.png')
		self.addDirectoryItem(32021, 'movies4&url=oscars', 'night.png', 'Defaultnight.png')
		self.addDirectoryItem('boxoffice', 'movies4&url=boxoffice', 'night.png', 'Defaultnight.png')
		self.addDirectoryItem(32022, 'movies4&url=theaters', 'night.png', 'DefaultRecentlyAddednight.png')

		
		#if lite == False:
			#if not control.setting('lists.widget') == '0':
				#self.addDirectoryItem(32003, 'mymovieliteNavigator', 'night.png', 'DefaultVideoPlaylists.jpg')

			#self.addDirectoryItem('Actor Search', 'moviePerson', 'actorsearch.jpg', 'Defaultnight.png')
			#self.addDirectoryItem(32010, 'movieSearch', 'search.jpg', 'Defaultnight.png')

		self.endDirectory()


	def Franchise(self, lite=False):
		self.addDirectoryItem('A Nightmare on Elm Street Franchise', 'movies4&url=ANightmareonElmStreet', 'nightmare-on-elm-street-ranked-slice-600x200.jpg', 'Defaultnight.png')
		self.addDirectoryItem('Halloween Franchise', 'movies4&url=HalloweenFranchise', 'halloween.jpg', 'Defaultnight.png')
		self.addDirectoryItem('Friday the 13th Franchise', 'movies4&url=FridaythethFranchise', 'f13th.jpg', 'Defaultnight.png')
		self.addDirectoryItem('Scream Franchise', 'movies4&url=ScreamFranchise', 'ScreamFranchise.jpg', 'Defaultnight.png')
		self.addDirectoryItem('Saw Franchise', 'movies4&url=SawFranchise', 'saw.jpg', 'Defaultnight.png')
		self.addDirectoryItem('Aliens and Predators Franchise', 'movies4&url=AliensAndPredatorsFranchise', 'AliensAndPredatorsFranchise.png', 'Defaultnight.png')
		self.addDirectoryItem('Texas Chainsaw Massacre Franchise', 'movies4&url=TexasChainsawMassacreFranchise', 'TexasChainsawMassacreFranchise.jpg', 'Defaultnight.png')
		self.addDirectoryItem('Evil Dead Franchise', 'movies4&url=EvilDeadFranchise', 'evildead.jpg', 'Defaultnight.png')
		self.addDirectoryItem('Childs Play Franchise', 'movies4&url=ChildsPlayFranchise', 'chucky.jpg', 'Defaultnight.png')
		self.addDirectoryItem('Romeros Dead Zombie Franchise', 'movies4&url=RomerosDeadZombieFranchise', 'george.jpg', 'Defaultnight.png')
		self.addDirectoryItem('Final Destination Franchise', 'movies4&url=FinalDestinationFranchise', 'Final_Destination.jpg', 'Defaultnight.png')
		self.addDirectoryItem('Jaws Franchise', 'movies4&url=JawsFranchise', 'jaws-posters-all.jpg', 'Defaultnight.png')
		self.addDirectoryItem('Jeepers Creepers Franchise', 'movies4&url=JeepersCreepersFranchise', 'jeepers-creepers.jpg', 'Defaultnight.png')
		self.addDirectoryItem('Hellraiser Franchise', 'movies4&url=HellraiserFranchise', 'hellraiser.jpg', 'Defaultnight.png')
		self.addDirectoryItem('Insidious Franchise', 'movies4&url=InsidiousFranchise', 'Insidious_05072014_1.jpg', 'Defaultnight.png')
		self.addDirectoryItem('The Exorcist Franchise', 'movies4&url=TheExorcistFranchise', 'the-exorcist-one.jpg', 'Defaultnight.png')
		self.addDirectoryItem('The Hills Have Eyes Franchise', 'movies4&url=TheHillsHaveEyesFranchise', 'the-hills-have-eyes-franchise-u2.jpg', 'Defaultnight.png')
		self.addDirectoryItem('The Ring Franchise', 'movies4&url=TheRingFranchise', 'ring.jpg', 'Defaultnight.png')
		self.addDirectoryItem('Jurassic Park Franchise', 'movies4&url=JurassicParkFranchise', 'park.jpg', 'Defaultnight.png')
		self.addDirectoryItem('Poltergeist Franchise', 'movies4&url=PoltergeistFranchise', 'poltergeist-clown-poster-bg.jpg', 'Defaultnight.png')
		self.addDirectoryItem('Psycho Franchise', 'movies4&url=PsychoFranchise', 'Psycho_logos.JPG', 'Defaultnight.png')
		self.addDirectoryItem('Candyman Franchise', 'movies4&url=CandymanFranchise', 'Candyman.jpg', 'Defaultnight.png')
		self.addDirectoryItem('Resident Evil Franchise', 'movies4&url=ResidentEvilFranchise', 'Resident-Evil-750x401.jpg', 'Defaultnight.png')
		self.addDirectoryItem('Amityville Franchise', 'movies4&url=AmityvilleFranchise', 'amityville.jpg', 'Defaultnight.png')
		self.addDirectoryItem('I Know What You Did Last Summer Franchise', 'movies4&url=IKnowWhatYouDidLastSummerFranchise', 'I_know_what_you_did_last_summer.jpg', 'Defaultnight.png')
		self.addDirectoryItem('The Purge Franchise', 'movies4&url=ThePurgeFranchise', 'purge.jpg', 'Defaultnight.png')
		self.addDirectoryItem('Creepshow Franchise', 'movies4&url=CreepshowFranchise', 'creepshow-7.jpg', 'Defaultnight.png')
		self.addDirectoryItem('Gremlins Franchise', 'movies4&url=GremlinsFranchise', 'grimlins.jpg', 'Defaultnight.png')
		self.addDirectoryItem('The Omen Franchise', 'movies4&url=TheOmenFranchise', 'the-omen.jpg', 'Defaultnight.png') 
		self.addDirectoryItem('Silent Hill Franchise', 'movies4&url=SilentHillFranchise', 'Silent_Hill_film_logo.png', 'Defaultnight.png')
		self.addDirectoryItem('Wrong Turn Franchise', 'movies4&url=WrongTurnFranchise', 'wrong-turn-5-bloodlines-review.jpg', 'Defaultnight.png')
		self.addDirectoryItem('Children of the Corn Franchise', 'movies4&url=ChildrenoftheCornFranchise', 'children.jpg', 'Defaultnight.png')
		self.addDirectoryItem('Blade Franchise', 'movies4&url=BladeFranchise', 'blade.png', 'Defaultnight.png')
		self.addDirectoryItem('The Mummy Franchise', 'movies4&url=TheMummyFranchise', 'the-mummy-franchise-1024x983.jpg', 'Defaultnight.png')
		self.addDirectoryItem('From Dusk till Dawn Franchise', 'movies4&url=FromDusktillDawnFranchise', 'fromdusk.jpg', 'Defaultnight.png')
		self.addDirectoryItem('Tremors Franchise', 'movies4&url=TremorsFranchise', 'tremors-movie-poster.jpg', 'Defaultnight.png')
		self.addDirectoryItem('The Conjuring Franchise', 'movies4&url=TheConjuringFranchise', 'conj.jpg', 'Defaultnight.png')
		self.addDirectoryItem('Cube Franchise', 'movies4&url=CubeFranchise', 'cube.jpg', 'Defaultnight.png')
		self.addDirectoryItem('The Thing Franchise', 'movies4&url=TheThingFranchise', 'thing.jpg', 'Defaultnight.png')
		self.addDirectoryItem('Paranormal Activity Franchise', 'movies4&url=ParanormalActivityFranchise', 'marked-ones.jpg', 'Defaultnight.png')
		self.addDirectoryItem('Phantasm Franchise', 'movies4&url=PhantasmFranchise', 'Phantasm_Simple.jpg', 'Defaultnight.png')
		self.addDirectoryItem('Scary Movie Franchise', 'movies4&url=ScaryMovieFranchise', 'scary-movie-5-1.jpg', 'Defaultnight.png')
		self.addDirectoryItem('Return of the Living Dead Franchise', 'movies4&url=ReturnoftheLivingDeadFranchise', 'return-of-the-living-dead-series.jpg', 'Defaultnight.png')
		self.addDirectoryItem('Carrie Franchise', 'movies4&url=CarrieFranchise_link', 'crit.jpg', 'Defaultnight.png')
		self.addDirectoryItem('Sinister Franchise', 'movies4&url=SinisterFranchise', 'sinister-2.jpg', 'Defaultnight.png')
		self.addDirectoryItem('Underworld Franchise', 'movies4&url=UnderworldFranchise', 'under.jpg', 'Defaultnight.png')
		self.addDirectoryItem('Puppet Master Franchise', 'movies4&url=PuppetMasterFranchise', 'puppetmaster.jpg', 'Defaultnight.png')
		self.addDirectoryItem('The Grudge Franchise', 'movies4&url=TheGrudgeFranchise', 'The_Grudge_logo.jpg', 'Defaultnight.png')
		self.addDirectoryItem('Joy Ride Franchise', 'movies4&url=JoyRideFranchise', 'joyride3.jpg', 'Defaultnight.png')
		self.addDirectoryItem('Goulies Franchise', 'movies4&url=GouliesFranchise', 'GhouliesF.jpg', 'Defaultnight.png')
		self.addDirectoryItem('Critters Franchise', 'movies4&url=CrittersFranchise', 'crit.jpg', 'Defaultnight.png')
		self.addDirectoryItem('Wishmaster Franchise', 'movies4&url=WishmasterFranchise', 'wish.jpg', 'Defaultnight.png')
		self.addDirectoryItem('Pumpkin head Franchise', 'movies4&url=PumpkinheadFranchise', 'pumpkinhead-in-church.jpg', 'Defaultnight.png')
		self.addDirectoryItem('Demonic toys Franchise', 'movies4&url=DemonictoysFranchise', 'Demonic-Toys.jpg', 'Defaultnight.png')		
		self.addDirectoryItem('Gate Franchise', 'movies4&url=GateFranchise', 'gate.jpg', 'Defaultnight.png')		
		self.addDirectoryItem('C H U D Franchise', 'movies4&url=CHUDFranchise', 'CHUD.jpg', 'Defaultnight.png')		
		self.addDirectoryItem('House the movies Franchise', 'movies4&url=HouseFranchise', 'house.jpg', 'Defaultnight.png')
		self.addDirectoryItem('Faces of death ', 'movies4&url=Facesofdeath', 'fod.jpg', 'Defaultnight.png')
		self.addDirectoryItem('Hatchet', 'movies4&url=Hatchet', 'Victor-Crowley-Hatchet-4-700x300.jpg', 'Defaultnight.png')
		self.addDirectoryItem('leprechaun', 'movies4&url=leprechaun', 'leprechaun-original102611.jpg', 'Defaultnight.png')
		self.addDirectoryItem('Alone in the Dark‎', 'movies4&url=Alone', 'alone.jpg', 'Defaultnight.png')
		self.addDirectoryItem('Anaconda', 'movies4&url=Anaconda', 'anaconda.jpg', 'Defaultnight.png')
		self.addDirectoryItem('Blair Witch', 'movies4&url=BlairWitch', 'blair.jpg', 'Defaultnight.png')
		self.endDirectory()	


	def mymovies(self, lite=False):
		self.accountCheck()

		if traktCredentials == True and imdbCredentials == True:
			self.addDirectoryItem(32032, 'movies4&url=traktcollection', 'night.png', 'Defaultnight.png', queue=True, context=(32551, 'moviesToLibrary&url=traktcollection'))
			self.addDirectoryItem(32033, 'movies4&url=traktwatchlist', 'night.png', 'Defaultnight.png', queue=True, context=(32551, 'moviesToLibrary&url=traktwatchlist'))
			self.addDirectoryItem(32034, 'movies4&url=imdbwatchlist', 'night.png', 'Defaultnight.png', queue=True)

		elif traktCredentials == True:
			self.addDirectoryItem(32032, 'movies4&url=traktcollection', 'night.png', 'Defaultnight.png', queue=True, context=(32551, 'moviesToLibrary&url=traktcollection'))
			self.addDirectoryItem(32033, 'movies4&url=traktwatchlist', 'night.png', 'Defaultnight.png', queue=True, context=(32551, 'moviesToLibrary&url=traktwatchlist'))

		elif imdbCredentials == True:
			self.addDirectoryItem(32032, 'movies4&url=imdbwatchlist', 'night.png', 'Defaultnight.png', queue=True)
			self.addDirectoryItem(32033, 'movies4&url=imdbwatchlist2', 'night.png', 'Defaultnight.png', queue=True)

		if traktCredentials == True:
			self.addDirectoryItem(32035, 'movies4&url=traktfeatured', 'night.png', 'Defaultnight.png', queue=True)

		elif imdbCredentials == True:
			self.addDirectoryItem(32035, 'movies4&url=featured', 'night.png', 'Defaultnight.png', queue=True)

		if traktIndicators == True:
			self.addDirectoryItem(32036, 'movies4&url=trakthistory', 'night.png', 'Defaultnight.png', queue=True)

		self.addDirectoryItem(32039, 'movieUserlists', 'night.png', 'Defaultnight.png')

		#if lite == False:
			#self.addDirectoryItem(32031, 'movieliteNavigator', 'night.png', 'Defaultnight.png')
			#self.addDirectoryItem('Actor Search', 'moviePerson', 'actorsearch.jpg', 'Defaultnight.png')
			#self.addDirectoryItem(32010, 'movieSearch', 'search.jpg', 'Defaultnight.png')

		self.endDirectory()


	def nightmaretv(self, lite=False):
		self.addDirectoryItem('Anime', 'tvshows4&url=anime', 'night.png', 'Defaultnight.png')
		self.addDirectoryItem(32012, 'tvYears', 'night.png', 'Defaultnight.png')
		#self.addDirectoryItem(32011, 'tvGenres', 'night.png', 'Defaultnight.png')


		#self.addDirectoryItem('Certificates', 'tvCertificates', 'night.png', 'playlist.jpg')
		#self.addDirectoryItem(32026, 'tvshows4&url=premiere', 'night.png', 'Defaultnight.png')
		self.addDirectoryItem('Popular', 'tvshows4&url=popular', 'night.png', 'playlist.jpg')

		#if lite == False:
			#if not control.setting('lists.widget') == '0':
				#self.addDirectoryItem(32004, 'mytvliteNavigator', 'night.png', 'DefaultVideoPlaylists.jpg')




		self.endDirectory()


	def mytvshows(self, lite=False):
		self.accountCheck()

		if traktCredentials == True and imdbCredentials == True:
			self.addDirectoryItem(32032, 'tvshows4&url=traktcollection', 'night.png', 'Defaultnight.png', context=(32551, 'tvshowsToLibrary&url=traktcollection'))
			self.addDirectoryItem(32033, 'tvshows4&url=traktwatchlist', 'night.png', 'Defaultnight.png', context=(32551, 'tvshowsToLibrary&url=traktwatchlist'))
			self.addDirectoryItem(32034, 'tvshows4&url=imdbwatchlist', 'night.png', 'Defaultnight.png')

		elif traktCredentials == True:
			self.addDirectoryItem(32032, 'tvshows4&url=traktcollection', 'night.png', 'Defaultnight.png', context=(32551, 'tvshowsToLibrary&url=traktcollection'))
			self.addDirectoryItem(32033, 'tvshows4&url=traktwatchlist', 'night.png', 'Defaultnight.png', context=(32551, 'tvshowsToLibrary&url=traktwatchlist'))

		elif imdbCredentials == True:
			self.addDirectoryItem(32032, 'tvshows4&url=imdbwatchlist', 'night.png', 'Defaultnight.png')
			self.addDirectoryItem(32033, 'tvshows4&url=imdbwatchlist2', 'night.png', 'Defaultnight.png')

		if traktCredentials == True:
			self.addDirectoryItem(32035, 'tvshows4&url=traktfeatured', 'night.png', 'Defaultnight.png')

		elif imdbCredentials == True:
			self.addDirectoryItem(32035, 'tvshows4&url=trending', 'night.png', 'Defaultnight.png', queue=True)

		if traktIndicators == True:
			self.addDirectoryItem(32036, 'calendar&url=trakthistory', 'night.png', 'Defaultnight.png', queue=True)
			self.addDirectoryItem(32037, 'calendar&url=progress', 'night.png', 'DefaultRecentlyAddedEpisodes.jpg', queue=True)
			self.addDirectoryItem(32038, 'calendar&url=mycalendar', 'night.png', 'DefaultRecentlyAddedEpisodes.jpg', queue=True)

		self.addDirectoryItem(32040, 'tvUserlists', 'mynight.png', 'Defaultnight.png')

		if traktCredentials == True:
			self.addDirectoryItem(32041, 'episodeUserlists', 'mynight.png', 'Defaultnight.png')

		if lite == False:
			self.addDirectoryItem(32031, 'tvliteNavigator', 'night.png', 'Defaultnight.png')
			self.addDirectoryItem('Actor Search', 'tvPerson', 'actorsearch.jpg', 'Defaultnight.png')
			self.addDirectoryItem(32010, 'tvSearch', 'search.jpg', 'Defaultnight.png')

		self.endDirectory()

		

	def tools(self):
		self.addDirectoryItem(32043, 'openSettings&query=0.0', 'tools.gif', 'DefaultAddonProgram.jpg')
		self.addDirectoryItem(32044, 'openSettings&query=3.1', 'tools.gif', 'DefaultAddonProgram.jpg')
		self.addDirectoryItem(32045, 'openSettings&query=1.0', 'tools.gif', 'DefaultAddonProgram.jpg')
		self.addDirectoryItem(32046, 'openSettings&query=6.0', 'tools.gif', 'DefaultAddonProgram.jpg')
		self.addDirectoryItem(32047, 'openSettings&query=2.0', 'tools.gif', 'DefaultAddonProgram.jpg')
		self.addDirectoryItem(32556, 'libraryNavigator', 'tools.gif', 'DefaultAddonProgram.jpg')
		self.addDirectoryItem(32048, 'openSettings&query=5.0', 'tools.gif', 'DefaultAddonProgram.jpg')
		self.addDirectoryItem(32049, 'viewsNavigator', 'tools.gif', 'DefaultAddonProgram.jpg')
		self.addDirectoryItem(32050, 'clearSources', 'tools.gif', 'DefaultAddonProgram.jpg')
		self.addDirectoryItem(32052, 'clearCache', 'tools.gif', 'DefaultAddonProgram.jpg')

		self.endDirectory()

	def library(self):
		self.addDirectoryItem(32557, 'openSettings&query=4.0', 'tools.gif', 'DefaultAddonProgram.jpg')
		self.addDirectoryItem(32558, 'updateLibrary&query=tool', 'library_update.jpg', 'DefaultAddonProgram.jpg')
		self.addDirectoryItem(32559, control.setting('library.movie'), 'night.png', 'Defaultnight.png', isAction=False)
		self.addDirectoryItem(32560, control.setting('library.tv'), 'night.png', 'Defaultnight.png', isAction=False)

		if trakt.getTraktCredentialsInfo():
			self.addDirectoryItem(32561, 'moviesToLibrary&url=traktcollection', 'night.png', 'Defaultnight.png')
			self.addDirectoryItem(32562, 'moviesToLibrary&url=traktwatchlist', 'night.png', 'Defaultnight.png')
			self.addDirectoryItem(32563, 'tvshowsToLibrary&url=traktcollection', 'night.png', 'Defaultnight.png')
			self.addDirectoryItem(32564, 'tvshowsToLibrary&url=traktwatchlist', 'night.png', 'Defaultnight.png')

		self.endDirectory()

	def downloads(self):
		movie_downloads = control.setting('movie.download.path')
		tv_downloads = control.setting('tv.download.path')

		if len(control.listDir(movie_downloads)[0]) > 0:
			self.addDirectoryItem(32001, movie_downloads, 'night.png', 'Defaultnight.png', isAction=False)
		if len(control.listDir(tv_downloads)[0]) > 0:
			self.addDirectoryItem(32002, tv_downloads, 'night.png', 'Defaultnight.png', isAction=False)

		self.endDirectory()


	def search(self):
		self.addDirectoryItem(32001, 'movieSearch', 'night.png', 'Defaultnight.png')
		self.addDirectoryItem(32002, 'tvSearch', 'night.png', 'Defaultnight.png')
		self.addDirectoryItem('Actor Search', 'moviePerson', 'night.png', 'Defaultnight.png')
		self.addDirectoryItem('TV Actor Search', 'tvPerson', 'night.png', 'Defaultnight.png')

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


