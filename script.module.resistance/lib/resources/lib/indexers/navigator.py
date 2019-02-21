# -*- coding: UTF-8 -*-
#           ________
#          _,.-Y  |  |  Y-._
#      .-~"   ||  |  |  |   "-.
#      I" ""=="|" !""! "|"[]""|     _____
#      L__  [] |..------|:   _[----I" .-{"-.
#     I___|  ..| l______|l_ [__L]_[I_/r(=}=-P
#    [L______L_[________]______j~  '-=c_]/=-^
#     \_I_j.--.\==I|I==_/.--L_]
#       [_((==)[`-----"](==)j
#          I--I"~~"""~~"I--I
#          |[]|         |[]|
#          l__j         l__j
#         |!!|         |!!|
#          |..|         |..|
#          ([])         ([])
#          ]--[         ]--[
#          [_L]         [_L]
#         /|..|\       /|..|\
#        `=}--{='     `=}--{='
#       .-^--r-^-.   .-^--r-^-.
# Resistance is futile @lock_down... 



import os,sys,urlparse
import xbmc, xbmcaddon, xbmcgui, xbmcplugin
import time

from resources.lib.modules import control
from resources.lib.modules import trakt
from resources.lib.modules import cache
from resources.lib.indexers import sports_streams
from resources.lib.indexers import arconaitv

sysaddon = sys.argv[0] ; syshandle = int(sys.argv[1])

artPath = control.artPath() ; addonFanart = control.addonFanart()

imdbCredentials = False if control.setting('imdb.user') == '' else True

traktCredentials = trakt.getTraktCredentialsInfo()

traktIndicators = trakt.getTraktIndicatorsInfo()

queueMenu = control.lang(32065).encode('utf-8')


class navigator:
    def root(self):
        self.addDirectoryItem(32001, 'movieNavigator', '2.png', 'DefaultMovies.png')
        self.addDirectoryItem(32002, 'tvNavigator', '3.png', 'DefaultTVShows.png')
        #self.addDirectoryItem('Sports', 'lists', 'icon.png', 'DefaultTVShows.png')
        self.addDirectoryItem('Resistance Extra', 'resistdNavigator', 'extra.png', 'DefaultTVShows.png')
        #self.addDirectoryItem('Testings', 'oneclickNavigator', 'icon.png', 'DefaultTVShows.png')
        #self.addDirectoryItem('Resistance Direct2', 'oneclick2Navigator', 'icon.png', 'DefaultTVShows.png')
        
        if not control.setting('lists.widget') == '0':
            self.addDirectoryItem(32003, 'mymovieNavigator', '9.png', 'DefaultVideoPlaylists.png')
            self.addDirectoryItem(32004, 'mytvNavigator', '10.png', 'DefaultVideoPlaylists.png')

        if not control.setting('movie.widget') == '0':
            self.addDirectoryItem(32005, 'movieWidget', '8.png', 'DefaultRecentlyAddedMovies.png')

        if (traktIndicators == True and not control.setting('tv.widget.alt') == '0') or (traktIndicators == False and not control.setting('tv.widget') == '0'):
            self.addDirectoryItem(32006, 'tvWidget', '7.png', 'DefaultRecentlyAddedEpisodes.png')

        #self.addDirectoryItem(32007, 'channels', '6.png', 'DefaultMovies.png')
        #if not control.setting('furk.api') == '':
            #self.addDirectoryItem('Furk.net', 'furkNavigator', 'movies.png', 'movies.png')
        self.addDirectoryItem(32008, 'toolNavigator', '4.png', 'DefaultAddonProgram.png')

        downloads = True if control.setting('downloads') == 'true' and (len(control.listDir(control.setting('movie.download.path'))[0]) > 0 or len(control.listDir(control.setting('tv.download.path'))[0]) > 0) else False
        if downloads == True:
            self.addDirectoryItem(32009, 'downloadNavigator', 'downloads.png', 'DefaultFolder.png')

        self.addDirectoryItem(32010, 'searchNavigator', '5.png', 'DefaultFolder.png')
        self.addDirectoryItem('Resolve Url Settings', 'ruSettings', 'ru.png', 'DefaultFolder.png')

        self.endDirectory()

    def furk(self):
        self.addDirectoryItem('User Files', 'furkUserFiles', 'mytvnavigator.png', 'mytvnavigator.png')
        self.addDirectoryItem('Search', 'furkSearch', 'search.png', 'search.png')
        self.endDirectory()

    def movies(self, lite=False):
        self.addDirectoryItem(32011, 'movieGenres', '2.png', 'DefaultMovies.png')
        self.addDirectoryItem(32012, 'movieYears', '2.png', 'DefaultMovies.png')
        self.addDirectoryItem(32013, 'moviePersons', '2.png', 'DefaultMovies.png')
        self.addDirectoryItem(32014, 'movieLanguages', '2.png', 'DefaultMovies.png')
        self.addDirectoryItem(32015, 'movieCertificates', '2.png', 'DefaultMovies.png')
        self.addDirectoryItem(32017, 'movies&url=trending', '2.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem(32018, 'movies&url=popular', '2.png', 'DefaultMovies.png')
        self.addDirectoryItem(32019, 'movies&url=views', '2.png', 'DefaultMovies.png')
        self.addDirectoryItem(32020, 'movies&url=boxoffice', '2.png', 'DefaultMovies.png')
        self.addDirectoryItem(32021, 'movies&url=oscars', '2.png', 'DefaultMovies.png')
        self.addDirectoryItem(32022, 'movies&url=theaters', '2.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem(32005, 'movieWidget', '2.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('IMDB Top 100', 'movies&url=top3', '2.png', 'DefaultMovies.png')
        self.addDirectoryItem('IMDB Top 250', 'movies&url=top2', '2.png', 'DefaultMovies.png')
        self.addDirectoryItem('IMDB Top 1000', 'movies&url=top4', '2.png', 'DefaultMovies.png')
        self.addDirectoryItem('IMDB Best Director Winning', 'movies&url=bestd', '2.png', 'DefaultMovies.png')
        self.addDirectoryItem('National Film Board Preserved ', 'movies&url=nfb', '2.png', 'DefaultMovies.png')
        self.addDirectoryItem('Fox', 'movies&url=fox', '2.png', 'DefaultTVShows.png')
        self.addDirectoryItem('Paramount', 'movies&url=para', '2.png', 'DefaultTVShows.png')
        self.addDirectoryItem('MGM', 'movies&url=pmgm', '2.png', 'DefaultTVShows.png')
        self.addDirectoryItem('Disney', 'movies&url=disney1', '2.png', 'DefaultTVShows.png')
        self.addDirectoryItem('Universal', 'movies&url=uni', '2.png', 'DefaultTVShows.png')
        self.addDirectoryItem('Sony', 'movies&url=sony', '2.png', 'DefaultTVShows.png')
        self.addDirectoryItem('Warner Bros', 'movies&url=warb', '2.png', 'DefaultTVShows.png')
        self.addDirectoryItem('IMDB Prime Video', 'movies&url=primev', '2.png', 'DefaultTVShows.png')
        self.addDirectoryItem('Classic', 'movies&url=classmov', '2.png', 'DefaultTVShows.png')
        self.addDirectoryItem('Classic Horror', 'movies&url=classhor', '2.png', 'DefaultTVShows.png')
        self.addDirectoryItem('Classic Fantasy', 'movies&url=classfant', '2.png', 'DefaultTVShows.png')
        self.addDirectoryItem('Classic Western', 'movies&url=classwest', '2.png', 'DefaultTVShows.png')
        self.addDirectoryItem('Classic Animation', 'movies&url=classani', '2.png', 'DefaultTVShows.png')
        self.addDirectoryItem('Classic War', 'movies&url=classwar', '2.png', 'DefaultTVShows.png')
        self.addDirectoryItem('Classic Sci-fi', 'movies&url=classsci', '2.png', 'DefaultTVShows.png')
        self.addDirectoryItem('Eighties', 'movies&url=eighties', '2.png', 'DefaultTVShows.png')
        self.addDirectoryItem('Nineties', 'movies&url=nineties', '2.png', 'DefaultTVShows.png')
        self.addDirectoryItem('Noughties', 'movies&url=noughties', '2.png', 'DefaultTVShows.png')
        self.addDirectoryItem('Twenty Tens', 'movies&url=twentyten', '2.png', 'DefaultTVShows.png')

        if lite == False:
            if not control.setting('lists.widget') == '0':
                self.addDirectoryItem(32003, 'mymovieliteNavigator', '9.png', 'DefaultVideoPlaylists.png')

            self.addDirectoryItem(32028, 'moviePerson', '5.png', 'DefaultMovies.png')
            self.addDirectoryItem(32010, 'movieSearch', '5.png', 'DefaultMovies.png')

        self.endDirectory()


    def mymovies(self, lite=False):
        self.accountCheck()

        if traktCredentials == True and imdbCredentials == True:
            self.addDirectoryItem(32032, 'movies&url=traktcollection', 'trakt.png', 'DefaultMovies.png', queue=True, context=(32551, 'moviesToLibrary&url=traktcollection'))
            self.addDirectoryItem(32033, 'movies&url=traktwatchlist', 'trakt.png', 'DefaultMovies.png', queue=True, context=(32551, 'moviesToLibrary&url=traktwatchlist'))
            self.addDirectoryItem(32034, 'movies&url=imdbwatchlist', 'imdb.png', 'DefaultMovies.png', queue=True)

        elif traktCredentials == True:
            self.addDirectoryItem(32032, 'movies&url=traktcollection', 'trakt.png', 'DefaultMovies.png', queue=True, context=(32551, 'moviesToLibrary&url=traktcollection'))
            self.addDirectoryItem(32033, 'movies&url=traktwatchlist', 'trakt.png', 'DefaultMovies.png', queue=True, context=(32551, 'moviesToLibrary&url=traktwatchlist'))

        elif imdbCredentials == True:
            self.addDirectoryItem(32032, 'movies&url=imdbwatchlist', 'imdb.png', 'DefaultMovies.png', queue=True)
            self.addDirectoryItem(32033, 'movies&url=imdbwatchlist2', 'imdb.png', 'DefaultMovies.png', queue=True)

        if traktCredentials == True:
            self.addDirectoryItem(32035, 'movies&url=traktfeatured', 'trakt.png', 'DefaultMovies.png', queue=True)

        elif imdbCredentials == True:
            self.addDirectoryItem(32035, 'movies&url=featured', '9.png', 'DefaultMovies.png', queue=True)

        if traktIndicators == True:
            self.addDirectoryItem(32036, 'movies&url=trakthistory', 'trakt.png', 'DefaultMovies.png', queue=True)

        self.addDirectoryItem(32039, 'movieUserlists', '9.png', 'DefaultMovies.png')

        if lite == False:
            self.addDirectoryItem(32031, 'movieliteNavigator', '9.png', 'DefaultMovies.png')
            self.addDirectoryItem(32028, 'moviePerson', '9.png', 'DefaultMovies.png')
            self.addDirectoryItem(32010, 'movieSearch', '5.png', 'DefaultMovies.png')

        self.endDirectory()


    def tvshows(self, lite=False):
        self.addDirectoryItem(32011, 'tvGenres', '3.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32016, 'tvNetworks', '3.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32014, 'tvLanguages', '3.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32015, 'tvCertificates', '3.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32017, 'tvshows&url=trending', '3.png', 'DefaultRecentlyAddedEpisodes.png')
        self.addDirectoryItem(32018, 'tvshows&url=popular', '3.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32023, 'tvshows&url=rating', '3.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32019, 'tvshows&url=views', '3.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32024, 'tvshows&url=airing', '3.png', 'DefaultTVShows.png')
        self.addDirectoryItem('IMDB Prime Video', 'tvshows&url=usprime', '3.png', 'DefaultTVShows.png')
        self.addDirectoryItem('Documentaries', 'tvshows&url=docsa', '3.png', 'DefaultTVShows.png')
        self.addDirectoryItem('Mystery', 'tvshows&url=myst', '3.png', 'DefaultTVShows.png')
        self.addDirectoryItem('Sci-Fi', 'tvshows&url=scifi1', '3.png', 'DefaultTVShows.png')
        self.addDirectoryItem('User Rating 7 to 10', 'tvshows&url=userr', '3.png', 'DefaultTVShows.png')
        self.addDirectoryItem('Mini-Series', 'tvshows&url=mini', '3.png', 'DefaultTVShows.png')
        self.addDirectoryItem('Classic', 'tvshows&url=classtv', '3.png', 'DefaultTVShows.png')
        self.addDirectoryItem('Paranormal', 'paranormalNavigator', '3.png', 'DefaultTVShows.png')
        self.addDirectoryItem('PG-PG13', 'tvshows&url=pg', '3.png', 'DefaultTVShows.png')
        self.addDirectoryItem('Sci-Fi Animation', 'tvshows&url=scian', '3.png', 'DefaultTVShows.png')
        self.addDirectoryItem('Global Animation', 'tvshows&url=ani1', '3.png', 'DefaultTVShows.png')
        self.addDirectoryItem('Reality TV', 'tvshows&url=rtv', '3.png', 'DefaultTVShows.png')
        self.addDirectoryItem('Walt Disney', 'tvshows&url=waltd', '3.png', 'DefaultTVShows.png')
        self.addDirectoryItem('Dream Works', 'tvshows&url=dreamw', '3.png', 'DefaultTVShows.png')
        self.addDirectoryItem('Sony', 'tvshows&url=sony3', '3.png', 'DefaultTVShows.png')
        self.addDirectoryItem('Warner Bros', 'tvshows&url=warnerbro1', '3.png', 'DefaultTVShows.png')
        self.addDirectoryItem('Universal', 'tvshows&url=uni1', '3.png', 'DefaultTVShows.png')
        self.addDirectoryItem('Fox', 'tvshows&url=fox11', '3.png', 'DefaultTVShows.png')
        self.addDirectoryItem('Paramount', 'tvshows&url=para4', '3.png', 'DefaultTVShows.png')
        self.addDirectoryItem('MGM', 'tvshows&url=mgm5', '3.png', 'DefaultTVShows.png')
        #self.addDirectoryItem(32025, 'tvshows&url=active', 'returning-tvshows.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32026, 'tvshows&url=premiere', '3.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32006, 'calendar&url=added', '3.png', 'DefaultRecentlyAddedEpisodes.png', queue=True)
        self.addDirectoryItem(32027, 'calendars', '3.png', 'DefaultRecentlyAddedEpisodes.png')

        if lite == False:
            if not control.setting('lists.widget') == '0':
                self.addDirectoryItem(32004, 'mytvliteNavigator', '10.png', 'DefaultVideoPlaylists.png')

            self.addDirectoryItem(32028, 'tvPerson', '5.png', 'DefaultTVShows.png')
            self.addDirectoryItem(32010, 'tvSearch', '5.png', 'DefaultTVShows.png')

        self.endDirectory()

    def paranormal(self, lite=False):
        self.addDirectoryItem('Ghost Adventures', 'tvshows&url=ghostadv', 'p.png', 'DefaultTVShows.png')
        self.addDirectoryItem('Deadly Possessions', 'tvshows&url=deadp', 'p.png', 'DefaultTVShows.png')
        self.addDirectoryItem('Most Haunted', 'tvshows&url=mosth', 'p.png', 'DefaultTVShows.png')
        self.addDirectoryItem('Ghost Hunters', 'tvshows&url=ghosth', 'p.png', 'DefaultTVShows.png')
        self.addDirectoryItem('Paranormal Witness', 'tvshows&url=paraw', 'p.png', 'DefaultTVShows.png')
        self.addDirectoryItem('Paranormal Lockdown', 'tvshows&url=paral', 'p.png', 'DefaultTVShows.png')
        self.addDirectoryItem('A Haunting', 'tvshows&url=haunt', 'p.png', 'DefaultTVShows.png')
        self.addDirectoryItem('Haunted Collector', 'tvshows&url=hauntc', 'p.png', 'DefaultTVShows.png')
        self.addDirectoryItem('Ghost Asylum', 'tvshows&url=ghosta', 'p.png', 'DefaultTVShows.png')
        self.addDirectoryItem('Ghost Inside My Child', 'tvshows&url=ghosti', 'p.png', 'DefaultTVShows.png')
        self.addDirectoryItem('My Ghost Story', 'tvshows&url=paran', 'p.png', 'DefaultTVShows.png')

        self.endDirectory()

    def resistd(self, lite=False):
        self.addDirectoryItem('Resistance Direct', 'lists', 'direct.png', 'DefaultTVShows.png')
        #self.addDirectoryItem('[COLOR pink]Adult Only XXX[/COLOR]', 'lists2', 'xxx.png', 'DefaultTVShows.png')
        self.addDirectoryItem('Bonecrusher', 'bonecNavigator', 'bc.png', 'DefaultTVShows.png')
        self.addDirectoryItem('Toontown', 'toontownNavigator', 'toont.png', 'DefaultTVShows.png')
        self.addDirectoryItem('Nightmare', 'nightmareNavigator', 'night.png', 'DefaultTVShows.png')
        self.addDirectoryItem('Action Packed', 'actionpNavigator', 'ac.jpg', 'DefaultTVShows.png')
        self.addDirectoryItem('Wild West', 'wildwestNavigator', 'ww.jpg', 'DefaultTVShows.png')
        self.addDirectoryItem('Astroplane', 'astroplaneNavigator', 'astro.png', 'DefaultTVShows.png')
        self.addDirectoryItem('Laughing Hour', 'laughNavigator', 'll.png', 'DefaultTVShows.png')
        self.addDirectoryItem('Dark Love', 'darkloveNavigator', 'dl.png', 'DefaultTVShows.png')
        self.addDirectoryItem('Zim', 'zimNavigator', 'zz.png', 'DefaultTVShows.png')
        self.addDirectoryItem('Resolve Url Settings', 'ruSettings', 'ru.png', 'DefaultFolder.png')
        self.addDirectoryItem(32008, 'toolNavigator', '4.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem('TV Person Search', 'tvPerson', '5.png', 'DefaultTVShows.png')
        self.addDirectoryItem('TV Search', 'tvSearch', '5.png', 'DefaultTVShows.png')
        self.addDirectoryItem('Movie Person Search', 'moviePerson', '5.png', 'DefaultMovies.png')
        self.addDirectoryItem('Movie Search', 'movieSearch', '5.png', 'DefaultMovies.png')
        #self.addDirectoryItem('Search', 'searchdirect', '5.png', 'DefaultTVShows.png')

        self.endDirectory()

    def zim(self, lite=False):
        self.addDirectoryItem('Kids Movies', 'kidmovieNavigator', 'zz.png', 'Defaultzz.png')
        self.addDirectoryItem('Kids TV Shows', 'kidstvNavigator', 'zz.png', 'Defaultzz.png')
        self.addDirectoryItem('Anime Movies', 'animemovieNavigator', 'zz.png', 'Defaultzz.png')
        self.addDirectoryItem('Anime TV Shows', 'animetvNavigator', 'zz.png', 'Defaulzz.png')
        self.addDirectoryItem('Little Tikes', 'toddlerNavigator', 'zz.png', 'Defaulzz.png')

        self.endDirectory()    
    

    def darklove(self, lite=False):
        self.addDirectoryItem('Romance Movies', 'movieromNavigator', 'dl.png', 'Defaultdl.png')
        self.addDirectoryItem('Drama Movies', 'moviedramaNavigator', 'dl.png', 'Defaultdl.png')
        self.addDirectoryItem('Drama T.V', 'tvdramaNavigator', 'dl.png', 'Defaultdl.png')
        self.addDirectoryItem('Romance T.v', 'tvromNavigator', 'dl.png', 'Defaultdl.png')

        self.endDirectory()    

    def laugh(self, lite=False):
        self.addDirectoryItem('Astroplane Movies', 'astropmNavigator', 'astro.png', 'Defaultastro.png')
        self.addDirectoryItem('Astroplane TV Shows', 'astroptNavigator', 'astro.png', 'Defaultastro.png')

        self.endDirectory()     

    def astroplane(self, lite=False):
        self.addDirectoryItem('Astroplane Movies', 'astropmNavigator', 'astro.png', 'Defaultastro.png')
        self.addDirectoryItem('Astroplane TV Shows', 'astroptNavigator', 'astro.png', 'Defaultastro.png')

        self.endDirectory()     

    def wildwest(self, lite=False):
        self.addDirectoryItem('Wild West Movies', 'wildmovieNavigator', 'ww.jpg', 'DefaultMovies.png')
        self.addDirectoryItem('Wild West TV Shows', 'wildshowsNavigator', 'ww.jpg', 'DefaultTVShows.png')

        self.endDirectory()    

    def action(self, lite=False):
        self.addDirectoryItem('Action Packed Movies', 'moviesapNavigator', 'ac.jpg', 'DefaultMovies.png')
        self.addDirectoryItem('Action Packed TV Shows', 'tvshowsapNavigator', 'ac.jpg', 'DefaultTVShows.png')

        self.endDirectory()    

    def nightmare(self, lite=False):
        self.addDirectoryItem('Nightmare Movies', 'nightmaremovNavigator', 'night.png', 'Defaultmovies.gif')
        self.addDirectoryItem('Nightmare TV Shows', 'nightmaretvNavigator', 'night.png', 'Defaulttvshows.gif')

        self.endDirectory()         

    def toontown(self, lite=False):
        self.addDirectoryItem('Anime Tv Shows', 'animetvNavigator', 'toont.png', 'DefaultMovies.jpg')
        self.addDirectoryItem('Anime Movies', 'animemovieNavigator', 'toont.png', 'DefaultMovies.jpg')
        self.addDirectoryItem('Toons Movies', 'toonmovieNavigator', 'toont.png', 'DefaultMovies.jpg')
        self.addDirectoryItem('Toons Tv Shows', 'toonstvNavigator', 'toont.png', 'DefaultTVShows.jpg')

        self.endDirectory()     

    def bonec(self, lite=False):
        self.addDirectoryItem('Developers', 'teamNavigator', 'bc.png', 'decepticons.png')
        self.addDirectoryItem('Classic', 'classicsNavigator', 'bc.png', 'decepticons.png')
        self.addDirectoryItem('Box Sets', 'boxsetsNavigator', 'bc.png', 'decepticons.png')
        self.addDirectoryItem('Kids', 'kids2Navigator', 'bc.png', 'decepticons.png')
        self.addDirectoryItem('Documentaries', 'docs2navNavigator', 'bc.png', 'decepticons.png')

        self.endDirectory()       

    def oneclick(IDdoADDON):
        file_path = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.odin/odin.py')) 
        xbmc.executebuiltin("XBMC.RunScript("+file_path+")")

    def oneclick2(IDdoADDON2):
        file_path = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.resistance/resources/plugin.py')) 
        xbmc.executebuiltin("XBMC.RunScript("+file_path+")")    

    def mytvshows(self, lite=False):
        try:
            self.accountCheck()

            if traktCredentials == True and imdbCredentials == True:

                self.addDirectoryItem(32032, 'tvshows&url=traktcollection', '10.png', 'DefaultTVShows.png', context=(32551, 'tvshowsToLibrary&url=traktcollection'))
                self.addDirectoryItem(32033, 'tvshows&url=traktwatchlist', '10.png', 'DefaultTVShows.png', context=(32551, 'tvshowsToLibrary&url=traktwatchlist'))
                self.addDirectoryItem(32034, 'tvshows&url=imdbwatchlist', '10.png', 'DefaultTVShows.png')

            elif traktCredentials == True:
                self.addDirectoryItem("Trakt On Deck", 'calendar&url=onDeck', '10.png', 'DefaultTVShows.png')
                self.addDirectoryItem(32032, 'tvshows&url=traktcollection', '10.png', 'DefaultTVShows.png', context=(32551, 'tvshowsToLibrary&url=traktcollection'))
                self.addDirectoryItem(32033, 'tvshows&url=traktwatchlist', '10.png', 'DefaultTVShows.png', context=(32551, 'tvshowsToLibrary&url=traktwatchlist'))

            elif imdbCredentials == True:
                self.addDirectoryItem(32032, 'tvshows&url=imdbwatchlist', '10.png', 'DefaultTVShows.png')
                self.addDirectoryItem(32033, 'tvshows&url=imdbwatchlist2', '10.png', 'DefaultTVShows.png')

            if traktCredentials == True:
                self.addDirectoryItem(32035, 'tvshows&url=traktfeatured', '10.png', 'DefaultTVShows.png')

            elif imdbCredentials == True:
                self.addDirectoryItem(32035, 'tvshows&url=trending', '10.png', 'DefaultMovies.png', queue=True)

            if traktIndicators == True:
                self.addDirectoryItem(32036, 'calendar&url=trakthistory', '10.png', 'DefaultTVShows.png', queue=True)
                self.addDirectoryItem(32037, 'calendar&url=progress', '10.png', 'DefaultRecentlyAddedEpisodes.png', queue=True)
                self.addDirectoryItem(32038, 'calendar&url=mycalendar', '10.png', 'DefaultRecentlyAddedEpisodes.png', queue=True)

            self.addDirectoryItem(32040, 'tvUserlists', '10.png', 'DefaultTVShows.png')

            if traktCredentials == True:
                self.addDirectoryItem(32041, 'episodeUserlists', '10.png', 'DefaultTVShows.png')

            if lite == False:
                self.addDirectoryItem(32031, 'tvliteNavigator', '10.png', 'DefaultTVShows.png')
                self.addDirectoryItem(32028, 'tvPerson', '10.png', 'DefaultTVShows.png')
                self.addDirectoryItem(32010, 'tvSearch', '10.png', 'DefaultTVShows.png')

            self.endDirectory()
        except:
            print("ERROR")


    def tools(self):
        self.addDirectoryItem(32043, 'openSettings&query=0.0', 'tools.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32044, 'openSettings&query=3.1', 'tools.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32045, 'openSettings&query=1.0', 'tools.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32046, 'openSettings&query=6.0', 'tools.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32047, 'openSettings&query=2.0', 'tools.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32556, 'libraryNavigator', 'tools.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32048, 'openSettings&query=5.0', 'tools.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32049, 'viewsNavigator', 'tools.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32050, 'clearSources', 'tools.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32604, 'clearCacheSearch', 'tools.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32052, 'clearCache', 'tools.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32073, 'authTrakt', 'trakt.png', 'DefaultAddonProgram.png')

        self.endDirectory()

    def library(self):
        self.addDirectoryItem(32557, 'openSettings&query=4.0', 'tools.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32558, 'updateLibrary&query=tool', 'library_update.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32559, control.setting('library.movie'), 'movies.png', 'DefaultMovies.png', isAction=False)
        self.addDirectoryItem(32560, control.setting('library.tv'), 'tvshows.png', 'DefaultTVShows.png', isAction=False)

        if trakt.getTraktCredentialsInfo():
            self.addDirectoryItem(32561, 'moviesToLibrary&url=traktcollection', 'trakt.png', 'DefaultMovies.png')
            self.addDirectoryItem(32562, 'moviesToLibrary&url=traktwatchlist', 'trakt.png', 'DefaultMovies.png')
            self.addDirectoryItem(32563, 'tvshowsToLibrary&url=traktcollection', 'trakt.png', 'DefaultTVShows.png')
            self.addDirectoryItem(32564, 'tvshowsToLibrary&url=traktwatchlist', 'trakt.png', 'DefaultTVShows.png')

        self.endDirectory()

    def downloads(self):
        movie_downloads = control.setting('movie.download.path')
        tv_downloads = control.setting('tv.download.path')

        if len(control.listDir(movie_downloads)[0]) > 0:
            self.addDirectoryItem(32001, movie_downloads, 'movies.png', 'DefaultMovies.png', isAction=False)
        if len(control.listDir(tv_downloads)[0]) > 0:
            self.addDirectoryItem(32002, tv_downloads, 'tvshows.png', 'DefaultTVShows.png', isAction=False)

        self.endDirectory()


    def search(self):
        self.addDirectoryItem(32001, 'movieSearch', 'search.png', 'DefaultMovies.png')
        self.addDirectoryItem(32002, 'tvSearch', 'search.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32029, 'moviePerson', 'people-search.png', 'DefaultMovies.png')
        self.addDirectoryItem(32030, 'tvPerson', 'people-search.png', 'DefaultTVShows.png')

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


    def infoCheck(self, version):
        try:
            control.infoDialog('', control.lang(32074).encode('utf-8'), time=5000, sound=False)
            return '1'
        except:
            return '1'

    def freeview(self):    
        xbmc.RunAddon("pluin.video.youtube")
    
    def clearCache(self):
        control.idle()
        yes = control.yesnoDialog(control.lang(32056).encode('utf-8'), '', '')
        if not yes: return
        from resources.lib.modules import cache
        cache.cache_clear()
        control.infoDialog(control.lang(32057).encode('utf-8'), sound=True, icon='INFO')

    def clearCacheMeta(self):
        control.idle()
        yes = control.yesnoDialog(control.lang(32056).encode('utf-8'), '', '')
        if not yes: return
        from resources.lib.modules import cache
        cache.cache_clear_meta()
        control.infoDialog(control.lang(32057).encode('utf-8'), sound=True, icon='INFO')

    def clearCacheProviders(self):
        control.idle()
        yes = control.yesnoDialog(control.lang(32056).encode('utf-8'), '', '')
        if not yes: return
        from resources.lib.modules import cache
        cache.cache_clear_providers()
        control.infoDialog(control.lang(32057).encode('utf-8'), sound=True, icon='INFO')

    def clearCacheSearch(self):
        control.idle()
        yes = control.yesnoDialog(control.lang(32056).encode('utf-8'), '', '')
        if not yes: return
        from resources.lib.modules import cache
        cache.cache_clear_search()
        control.infoDialog(control.lang(32057).encode('utf-8'), sound=True, icon='INFO')

    def clearCacheAll(self):
        control.idle()
        yes = control.yesnoDialog(control.lang(32056).encode('utf-8'), '', '')
        if not yes: return
        from resources.lib.modules import cache
        cache.cache_clear_all()
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
