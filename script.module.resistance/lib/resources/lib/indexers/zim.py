# -*- coding: utf-8 -*-

'''
    Zim Add-on

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


import os,sys,urlparse

from resources.lib.modules import control
from resources.lib.modules import trakt
from resources.lib.modules import cache

sysaddon = sys.argv[0] ; syshandle = int(sys.argv[1])

artPath = control.artPath() ; addonFanart = control.addonFanart()

imdbCredentials = False if control.setting('imdb.user') == '' else True

traktCredentials = trakt.getTraktCredentialsInfo()

traktIndicators = trakt.getTraktIndicatorsInfo()

queueMenu = control.lang(32065).encode('utf-8')


class navigator:
    def root(self):
        self.addDirectoryItem('Kids Movies', 'kidmovieNavigator', 'zz.png', 'Defaultzz.png')
        self.addDirectoryItem('Kids TV Shows', 'kidstvNavigator', 'zz.png', 'Defaultzz.png')
        self.addDirectoryItem('Anime Movies', 'animemovieNavigator', 'zz.png', 'Defaultzz.png')
        self.addDirectoryItem('Anime TV Shows', 'animetvNavigator', 'zz.png', 'Defaulzz.png')
        self.addDirectoryItem('Little Tikes', 'toddlertvNavigator', 'zz.png', 'Defaulzz.png')
		
	
        #self.addDirectoryItem(32008, 'toolNavigator', 'tools.png', 'DefaultAddonProgram.png')

        #downloads = True if control.setting('downloads') == 'true' and (len(control.listDir(control.setting('movie.download.path'))[0]) > 0 or len(control.listDir(control.setting('tv.download.path'))[0]) > 0) else False
        #if downloads == True:
            #self.addDirectoryItem(32009, 'downloadNavigator', 'downloads.png', 'DefaultFolder.png')

        #self.addDirectoryItem(32010, 'searchNavigator', 'search.png', 'DefaultFolder.png')

        self.endDirectory()

    def furk(self):
        self.addDirectoryItem('User Files', 'furkUserFiles', 'mytvnavigator.png', 'mytvnavigator.png')
        self.addDirectoryItem('Search', 'furkSearch', 'search.png', 'search.png')
        self.endDirectory()
		

    def kidmovie(self, lite=False):		
        self.addDirectoryItem('Zims Holiday Favs', 'movies10&url=christmas', 'zz.png', 'Defaultzz.png')
        self.addDirectoryItem('Ultimate Movie List', 'movies10&url=ultimate', 'zz.png', 'Defaultzz.png')
        self.addDirectoryItem('Walt Disney Pictures', 'disneymovieNavigator', 'zz.png', 'Defaultzz.png')
        self.addDirectoryItem('Dreamworks', 'movies10&url=dreamworks', 'zz.png', 'Defaultzz.png')
        self.addDirectoryItem('Superhero Movies', 'superheroNavigator', 'zz.png', 'Defaultzz.png')
        self.addDirectoryItem('Tim Burton Films', 'movies10&url=timburton', 'zz.png', 'Defaultzz.png')
        self.addDirectoryItem('Lego Movies', 'movies10&url=lego', 'zz.png', 'Defaultzz.png')
        self.addDirectoryItem('Transformers Movies', 'movies10&url=robots', 'zz.png', 'Defaultzz.png')
        self.addDirectoryItem('Harry Potter Films', 'movies10&url=harry', 'zz.png', 'Defaultzz.png')
        		
        self.endDirectory()


    def animemovie(self, lite=False):
        self.addDirectoryItem('Popular', 'movies10&url=animepopular', 'zz.png', 'Defaultzz.png')
        self.addDirectoryItem('Highest Voted', 'movies10&url=animeviews', 'zz.png', 'Defaultzz.png')
        #self.addDirectoryItem('Certifications', 'movieanimecertifications', 'zz.png', 'Defaultzz.png')
        self.addDirectoryItem(32011, 'animegenres', 'zz.png', 'Defaultzz.png')
		
        self.endDirectory()
		
		
    def disneymov(self, lite=False):
        self.addDirectoryItem('Disney Animation', 'movies10&url=disneycollection' , 'zz.png', 'DefaultRecentlyAddedzz.png')
        self.addDirectoryItem('Disney Pixar', 'movies10&url=disneypixar', 'zz.png', 'Defaultzz.png')
        self.addDirectoryItem('Disney Live Action', 'movies10&url=disneyliveaction', 'zz.png', 'DefaultRecentlyAddedzz.png')
        self.addDirectoryItem('Disney Nature', 'movies10&url=disneynature', 'zz.png', 'DefaultRecentlyAddedzz.png')

        self.endDirectory()
		
					
    def supermov(self, lite=False):
        self.addDirectoryItem('DC & Marvel Movies', 'movies10&url=superheromovies', 'zz.png', 'Defaultzz.png')
        self.addDirectoryItem('Marvel Movies', 'movies10&url=marvelmovies', 'zz.png', 'Defaultzz.png')
        self.addDirectoryItem('DC Movies', 'movies10&url=dcmovies', 'zz.png', 'Defaultzz.png')
        self.addDirectoryItem('Marvel Animated Movies', 'movies10&url=marvelanimate', 'zz.png', 'Defaultzz.png')
        self.addDirectoryItem('DC Animated Movies', 'movies10&url=dcanimate', 'zz.png', 'Defaultzz.png')

        self.endDirectory()


    def mymovies(self, lite=False):
        self.accountCheck()

        if traktCredentials == True and imdbCredentials == True:
            self.addDirectoryItem(32032, 'movies10&url=traktcollection', 'trakt.png', 'Defaultzz.png', queue=True, context=(32551, 'moviesToLibrary&url=traktcollection'))
            self.addDirectoryItem(32033, 'movies10&url=traktwatchlist', 'trakt.png', 'Defaultzz.png', queue=True, context=(32551, 'moviesToLibrary&url=traktwatchlist'))
            self.addDirectoryItem(32034, 'movies10&url=imdbwatchlist', 'imdb.png', 'Defaultzz.png', queue=True)

        elif traktCredentials == True:
            self.addDirectoryItem(32032, 'movies10&url=traktcollection', 'trakt.png', 'Defaultzz.png', queue=True, context=(32551, 'moviesToLibrary&url=traktcollection'))
            self.addDirectoryItem(32033, 'movies10&url=traktwatchlist', 'trakt.png', 'Defaultzz.png', queue=True, context=(32551, 'moviesToLibrary&url=traktwatchlist'))

        elif imdbCredentials == True:
            self.addDirectoryItem(32032, 'movies10&url=imdbwatchlist', 'imdb.png', 'Defaultzz.png', queue=True)
            self.addDirectoryItem(32033, 'movies10&url=imdbwatchlist2', 'imdb.png', 'Defaultzz.png', queue=True)

        if traktCredentials == True:
            self.addDirectoryItem(32035, 'movies10&url=traktfeatured', 'trakt.png', 'Defaultzz.png', queue=True)

        elif imdbCredentials == True:
            self.addDirectoryItem(32035, 'movies10&url=featured', 'imdb.png', 'Defaultzz.png', queue=True)

        if traktIndicators == True:
            self.addDirectoryItem(32036, 'movies10&url=trakthistory', 'trakt.png', 'Defaultzz.png', queue=True)

        self.addDirectoryItem(32039, 'movieUserlists', 'userlists.png', 'Defaultzz.png')

        if lite == False:
            self.addDirectoryItem(32031, 'movieliteNavigator', 'zz.png', 'Defaultzz.png')
            self.addDirectoryItem(32028, 'moviePerson', 'people-search.png', 'Defaultzz.png')
            self.addDirectoryItem(32010, 'movieSearch', 'search.png', 'Defaultzz.png')

        self.endDirectory()


    def kidstv(self, lite=False):
        self.addDirectoryItem('Popular Cartoons', 'tvshows10&url=popular', 'zz.png', 'Defaultzz.png')
        self.addDirectoryItem('Trending Shows', 'tvshows10&url=views', 'zz.png', 'Defaultzz.png')
        self.addDirectoryItem('Teen TV Networks', 'teentvNavigator', 'zz.png', 'Defaulzz.png')
        self.addDirectoryItem('Popular Networks', 'kidNetworks', 'zz.png', 'Defaulzz.png')
        self.addDirectoryItem('Throwbackback TV', 'tvshows10&url=retrotv', 'zz.png', 'Defaultzz.png')
        self.addDirectoryItem('Lego TV', 'tvshows10&url=lego', 'zz.png', 'Defaulzz.png')
        self.addDirectoryItem('Transformers TV', 'tvshows10&url=robots', 'zz.png', 'Defaulzz.png')
			
        self.endDirectory()
	
			
    def animetv(self, lite=False):
        self.addDirectoryItem('Popular Anime', 'tvshows10&url=animepop', 'zz.png', 'Defaultzz.png')
        self.addDirectoryItem('Most Viewed', 'tvshows10&url=animeviews', 'zz.png', 'Defaultzz.png')
        #self.addDirectoryItem('Active', 'tvshows10&url=animeactive', 'zz.png', 'playlist.png')
        self.addDirectoryItem('Popular Mini-Series', 'tvshows10&url=animepremiere', 'zz.png', 'Defaultzz.png')
        #self.addDirectoryItem('Certifications', 'tvanimecertifications', 'zz.png', 'Defaultzz.png')
        #self.addDirectoryItem(32011, 'animeGenres', 'zz.png', 'Defaultzz.png')
		
        self.endDirectory()
	
	
    def toddlertv(self, lite=False):
        self.addDirectoryItem('Disney Jr Shows', 'tvshows10&url=disneyjr', 'zz.png', 'Defaulzz.png')
        self.addDirectoryItem('Nick Jr Shows', 'tvshows10&url=nickjr', 'zz.png', 'Defaulzz.png')
        self.addDirectoryItem('Netflix Shows', 'tvshows10&url=netflixkid', 'zz.png', 'Defaulzz.png')
        self.addDirectoryItem('Random Toddler Shows', 'tvshows10&url=toddler', 'zz.png', 'Defaultzz.png')
		
        self.endDirectory()

		
    def teentv(self, lite=False):
        self.addDirectoryItem('Disney Channel', 'tvshows10&url=disneychannel', 'zz.png', 'Defaulzz.png')
        self.addDirectoryItem('Teen Nick', 'tvshows10&url=teennick', 'zz.png', 'Defaulzz.png')
        self.addDirectoryItem('Freeform', 'tvshows10&url=freeform', 'zz.png', 'Defaulzz.png')
        self.addDirectoryItem('Teen TV Shows', 'tvshows10&url=teentv', 'zz.png', 'Defaulzz.png')
				
        self.endDirectory()


    def kidnetworks(self, lite=False):
        self.addDirectoryItem('Nickelodeon', 'tvshows10&url=nick', 'zz.png', 'Defaultzz.png')
        self.addDirectoryItem('Cartoon Network', 'tvshows10&url=cartoonnetwork', 'zz.png', 'Defaulzz.png')
        self.addDirectoryItem('Nicktoons', 'tvshows10&url=nicktoons', 'zz.png', 'Defaulzz.png')
        self.addDirectoryItem('Disney XD', 'tvshows10&url=disneyxd', 'zz.png', 'Defaulzz.png')

        self.endDirectory()


    def mytvshows(self, lite=False):
        try:
            self.accountCheck()

            if traktCredentials == True and imdbCredentials == True:

                self.addDirectoryItem(32032, 'tvshows10&url=traktcollection', 'trakt.png', 'Defaultzz.png', context=(32551, 'tvshowsToLibrary&url=traktcollection'))
                self.addDirectoryItem(32033, 'tvshows10&url=traktwatchlist', 'trakt.png', 'Defaultzz.png', context=(32551, 'tvshowsToLibrary&url=traktwatchlist'))
                self.addDirectoryItem(32034, 'tvshows10&url=imdbwatchlist', 'imdb.png', 'Defaultzz.png')

            elif traktCredentials == True:
                self.addDirectoryItem("Trakt On Deck", 'calendar&url=onDeck', 'trakt.png', 'Defaultzz.png')
                self.addDirectoryItem(32032, 'tvshows10&url=traktcollection', 'trakt.png', 'Defaultzz.png', context=(32551, 'tvshowsToLibrary&url=traktcollection'))
                self.addDirectoryItem(32033, 'tvshows10&url=traktwatchlist', 'trakt.png', 'Defaultzz.png', context=(32551, 'tvshowsToLibrary&url=traktwatchlist'))

            elif imdbCredentials == True:
                self.addDirectoryItem(32032, 'tvshows10&url=imdbwatchlist', 'imdb.png', 'Defaultzz.png')
                self.addDirectoryItem(32033, 'tvshows10&url=imdbwatchlist2', 'imdb.png', 'Defaultzz.png')

            if traktCredentials == True:
                self.addDirectoryItem(32035, 'tvshows10&url=traktfeatured', 'trakt.png', 'Defaultzz.png')

            elif imdbCredentials == True:
                self.addDirectoryItem(32035, 'tvshows10&url=trending', 'imdb.png', 'Defaultzz.png', queue=True)

            if traktIndicators == True:
                self.addDirectoryItem(32036, 'calendar&url=trakthistory', 'trakt.png', 'Defaultzz.png', queue=True)
                self.addDirectoryItem(32037, 'calendar&url=progress', 'trakt.png', 'DefaultRecentlyAddedEpisodes.png', queue=True)
                self.addDirectoryItem(32038, 'calendar&url=mycalendar', 'trakt.png', 'DefaultRecentlyAddedEpisodes.png', queue=True)

            self.addDirectoryItem(32040, 'tvUserlists', 'userlists.png', 'Defaultzz.png')

            if traktCredentials == True:
                self.addDirectoryItem(32041, 'episodeUserlists', 'userlists.png', 'Defaultzz.png')

            if lite == False:
                self.addDirectoryItem(32031, 'tvliteNavigator', 'zz.png', 'Defaultzz.png')
                self.addDirectoryItem(32028, 'tvPerson', 'people-search.png', 'Defaultzz.png')
                self.addDirectoryItem(32010, 'tvSearch', 'search.png', 'Defaultzz.png')

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
        self.addDirectoryItem(32559, control.setting('library.movie'), 'zz.png', 'Defaultzz.png', isAction=False)
        self.addDirectoryItem(32560, control.setting('library.tv'), 'zz.png', 'Defaultzz.png', isAction=False)

        if trakt.getTraktCredentialsInfo():
            self.addDirectoryItem(32561, 'moviesToLibrary&url=traktcollection', 'trakt.png', 'Defaultzz.png')
            self.addDirectoryItem(32562, 'moviesToLibrary&url=traktwatchlist', 'trakt.png', 'Defaultzz.png')
            self.addDirectoryItem(32563, 'tvshowsToLibrary&url=traktcollection', 'trakt.png', 'Defaultzz.png')
            self.addDirectoryItem(32564, 'tvshowsToLibrary&url=traktwatchlist', 'trakt.png', 'Defaultzz.png')

        self.endDirectory()

    def downloads(self):
        movie_downloads = control.setting('movie.download.path')
        tv_downloads = control.setting('tv.download.path')

        if len(control.listDir(movie_downloads)[0]) > 0:
            self.addDirectoryItem(32001, movie_downloads, 'zz.png', 'Defaultzz.png', isAction=False)
        if len(control.listDir(tv_downloads)[0]) > 0:
            self.addDirectoryItem(32002, tv_downloads, 'zz.png', 'Defaultzz.png', isAction=False)

        self.endDirectory()


    def search(self):
        self.addDirectoryItem(32001, 'movieSearch', 'search.png', 'Defaultzz.png')
        self.addDirectoryItem(32002, 'tvSearch', 'search.png', 'Defaultzz.png')
        self.addDirectoryItem(32029, 'moviePerson', 'people-search.png', 'Defaultzz.png')
        self.addDirectoryItem(32030, 'tvPerson', 'people-search.png', 'Defaultzz.png')

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
