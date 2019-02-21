# -*- coding: utf-8 -*-

'''
    Covenant Add-on

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

sysaddon = sys.argv[0] ; syshandle = int(sys.argv[1]) ; control.moderator()

artPath = control.artPath() ; addonFanart = control.addonFanart()

imdbCredentials = False if control.setting('imdb.user') == '' else True

traktCredentials = trakt.getTraktCredentialsInfo()

traktIndicators = trakt.getTraktIndicatorsInfo()

queueMenu = control.lang(32065).encode('utf-8')


class navigator:
    def root(self):
        self.addDirectoryItem(32001, 'movieNavigator', 'movies.jpg', 'DefaultMovies.png')
        self.addDirectoryItem(32002, 'tvNavigator', 'tvshows.jpg', 'DefaultTVShows.png')

        if not control.setting('lists.widget') == '0':
            self.addDirectoryItem(32003, 'mymovieNavigator', 'mymovies.jpg', 'DefaultVideoPlaylists.png')
            self.addDirectoryItem(32004, 'mytvNavigator', 'mytvshows.jpg', 'DefaultVideoPlaylists.png')

        if not control.setting('movie.widget') == '0':
            self.addDirectoryItem(32005, 'movieWidget', 'latest-movies.jpg', 'DefaultRecentlyAddedMovies.png')

        if (traktIndicators == True and not control.setting('tv.widget.alt') == '0') or (traktIndicators == False and not control.setting('tv.widget') == '0'):
            self.addDirectoryItem(32006, 'tvWidget', 'latest-episodes.jpg', 'DefaultRecentlyAddedEpisodes.png')

        self.addDirectoryItem(32007, 'channels', 'channels.jpg', 'DefaultMovies.png')

        self.addDirectoryItem(32008, 'toolNavigator', 'tools.jpg', 'DefaultAddonProgram.png')

        downloads = True if control.setting('downloads') == 'true' and (len(control.listDir(control.setting('movie.download.path'))[0]) > 0 or len(control.listDir(control.setting('tv.download.path'))[0]) > 0) else False
        if downloads == True:
            self.addDirectoryItem(32009, 'downloadNavigator', 'downloads.jpg', 'DefaultFolder.png')

        self.addDirectoryItem(32010, 'searchNavigator', 'search.jpg', 'DefaultFolder.png')

        self.endDirectory()


    def movies(self, lite=False):
        self.addDirectoryItem(32011, 'movieGenres', 'genres.jpg', 'DefaultMovies.png')
        self.addDirectoryItem(32012, 'movieYears', 'years.jpg', 'DefaultMovies.png')
        self.addDirectoryItem(32013, 'moviePersons', 'people.jpg', 'DefaultMovies.png')
        self.addDirectoryItem(32014, 'movieLanguages', 'languages.jpg', 'DefaultMovies.png')
        self.addDirectoryItem(32015, 'movieCertificates', 'certificates.jpg', 'DefaultMovies.png')
        self.addDirectoryItem(32017, 'movies&url=trending', 'people-watching.jpg', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem(32018, 'movies&url=popular', 'most-popular.jpg', 'DefaultMovies.png')
        self.addDirectoryItem('Romantic Comedy', 'movies&url=romance', 'romance.jpg', 'DefaultMovies.png')	
        self.addDirectoryItem('Marvel Studios', 'movies&url=marvel', 'marvel.jpg', 'DefaultMovies.png')	
        self.addDirectoryItem('DC Movies', 'movies&url=dcmovies', 'dc.jpg', 'DefaultMovies.png')
        self.addDirectoryItem('DC Animated', 'movies&url=dcanimate', 'dc.jpg', 'DefaultMovies.png')
        self.addDirectoryItem('Horror 2018-2000', 'movies&url=tophorr', 'horror.jpg', 'DefaultMovies.png')
        self.addDirectoryItem('Horror 1999 & Under', 'movies&url=horror', 'horror.jpg', 'DefaultMovies.png')
        self.addDirectoryItem('Standup Comedy', 'movies&url=standup', 'standup.jpg', 'DefaultMovies.png')		
        self.addDirectoryItem(32019, 'movies&url=views', 'most-voted.jpg', 'DefaultMovies.png')
        self.addDirectoryItem(32020, 'movies&url=boxoffice', 'box-office.jpg', 'DefaultMovies.png')
        self.addDirectoryItem(32021, 'movies&url=oscars', 'oscar-winners.jpg', 'DefaultMovies.png')
        self.addDirectoryItem(32022, 'movies&url=theaters', 'in-theaters.jpg', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem(32005, 'movieWidget', 'latest-movies.jpg', 'DefaultRecentlyAddedMovies.png')

        if lite == False:
            if not control.setting('lists.widget') == '0':
                self.addDirectoryItem(32003, 'mymovieliteNavigator', 'mymovies.jpg', 'DefaultVideoPlaylists.png')

            self.addDirectoryItem(32028, 'moviePerson', 'people-search.jpg', 'DefaultMovies.png')
            self.addDirectoryItem(32010, 'movieSearch', 'search.jpg', 'DefaultMovies.png')

        self.endDirectory()


    def mymovies(self, lite=False):
        self.accountCheck()

        if traktCredentials == True and imdbCredentials == True:
            self.addDirectoryItem(32032, 'movies&url=traktcollection', 'trakt.jpg', 'DefaultMovies.png', queue=True, context=(32551, 'moviesToLibrary&url=traktcollection'))
            self.addDirectoryItem(32033, 'movies&url=traktwatchlist', 'trakt.jpg', 'DefaultMovies.png', queue=True, context=(32551, 'moviesToLibrary&url=traktwatchlist'))
            self.addDirectoryItem(32034, 'movies&url=imdbwatchlist', 'imdb.jpg', 'DefaultMovies.png', queue=True)

        elif traktCredentials == True:
            self.addDirectoryItem(32032, 'movies&url=traktcollection', 'trakt.jpg', 'DefaultMovies.png', queue=True, context=(32551, 'moviesToLibrary&url=traktcollection'))
            self.addDirectoryItem(32033, 'movies&url=traktwatchlist', 'trakt.jpg', 'DefaultMovies.png', queue=True, context=(32551, 'moviesToLibrary&url=traktwatchlist'))

        elif imdbCredentials == True:
            self.addDirectoryItem(32032, 'movies&url=imdbwatchlist', 'imdb.jpg', 'DefaultMovies.png', queue=True)
            self.addDirectoryItem(32033, 'movies&url=imdbwatchlist2', 'imdb.jpg', 'DefaultMovies.png', queue=True)

        if traktCredentials == True:
            self.addDirectoryItem(32035, 'movies&url=traktfeatured', 'trakt.jpg', 'DefaultMovies.png', queue=True)

        elif imdbCredentials == True:
            self.addDirectoryItem(32035, 'movies&url=featured', 'imdb.jpg', 'DefaultMovies.png', queue=True)

        if traktIndicators == True:
            self.addDirectoryItem(32036, 'movies&url=trakthistory', 'trakt.jpg', 'DefaultMovies.png', queue=True)

        self.addDirectoryItem(32039, 'movieUserlists', 'userlists.jpg', 'DefaultMovies.png')

        if lite == False:
            self.addDirectoryItem(32031, 'movieliteNavigator', 'movies.jpg', 'DefaultMovies.png')
            self.addDirectoryItem(32028, 'moviePerson', 'people-search.jpg', 'DefaultMovies.png')
            self.addDirectoryItem(32010, 'movieSearch', 'search.jpg', 'DefaultMovies.png')

        self.endDirectory()


    def tvshows(self, lite=False):
        self.addDirectoryItem(32011, 'tvGenres', 'genres.jpg', 'DefaultTVShows.png')
        self.addDirectoryItem(32016, 'tvNetworks', 'networks.jpg', 'DefaultTVShows.png')
        self.addDirectoryItem(32014, 'tvLanguages', 'languages.jpg', 'DefaultTVShows.png')
        self.addDirectoryItem(32015, 'tvCertificates', 'certificates.jpg', 'DefaultTVShows.png')
        self.addDirectoryItem(32017, 'tvshows&url=trending', 'people-watching.jpg', 'DefaultRecentlyAddedEpisodes.png')
        self.addDirectoryItem(32018, 'tvshows&url=popular', 'most-popular.jpg', 'DefaultTVShows.png')
        self.addDirectoryItem('Marvel TV', 'tvshows&url=marveltv', 'marvel.jpg', 'DefaultMovies.png')
        self.addDirectoryItem(32023, 'tvshows&url=rating', 'highly-rated.jpg', 'DefaultTVShows.png')
        self.addDirectoryItem(32019, 'tvshows&url=views', 'most-voted.jpg', 'DefaultTVShows.png')
        self.addDirectoryItem(32024, 'tvshows&url=airing', 'airing-today.jpg', 'DefaultTVShows.png')
        #self.addDirectoryItem(32025, 'tvshows&url=active', 'returning-tvshows.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32026, 'tvshows&url=premiere', 'new-tvshows.jpg', 'DefaultTVShows.png')
        self.addDirectoryItem(32006, 'calendar&url=added', 'latest-episodes.jpg', 'DefaultRecentlyAddedEpisodes.png', queue=True)
        self.addDirectoryItem(32027, 'calendars', 'calendar.jpg', 'DefaultRecentlyAddedEpisodes.png')

        if lite == False:
            if not control.setting('lists.widget') == '0':
                self.addDirectoryItem(32004, 'mytvliteNavigator', 'mytvshows.jpg', 'DefaultVideoPlaylists.png')

            self.addDirectoryItem(32028, 'tvPerson', 'people-search.jpg', 'DefaultTVShows.png')
            self.addDirectoryItem(32010, 'tvSearch', 'search.jpg', 'DefaultTVShows.png')

        self.endDirectory()


    def mytvshows(self, lite=False):
        self.accountCheck()

        if traktCredentials == True and imdbCredentials == True:
            self.addDirectoryItem(32032, 'tvshows&url=traktcollection', 'trakt.jpg', 'DefaultTVShows.png', context=(32551, 'tvshowsToLibrary&url=traktcollection'))
            self.addDirectoryItem(32033, 'tvshows&url=traktwatchlist', 'trakt.jpg', 'DefaultTVShows.png', context=(32551, 'tvshowsToLibrary&url=traktwatchlist'))
            self.addDirectoryItem(32034, 'tvshows&url=imdbwatchlist', 'imdb.jpg', 'DefaultTVShows.png')

        elif traktCredentials == True:
            self.addDirectoryItem(32032, 'tvshows&url=traktcollection', 'trakt.jpg', 'DefaultTVShows.png', context=(32551, 'tvshowsToLibrary&url=traktcollection'))
            self.addDirectoryItem(32033, 'tvshows&url=traktwatchlist', 'trakt.jpg', 'DefaultTVShows.png', context=(32551, 'tvshowsToLibrary&url=traktwatchlist'))

        elif imdbCredentials == True:
            self.addDirectoryItem(32032, 'tvshows&url=imdbwatchlist', 'imdb.jpg', 'DefaultTVShows.png')
            self.addDirectoryItem(32033, 'tvshows&url=imdbwatchlist2', 'imdb.jpg', 'DefaultTVShows.png')

        if traktCredentials == True:
            self.addDirectoryItem(32035, 'tvshows&url=traktfeatured', 'trakt.jpg', 'DefaultTVShows.png')

        elif imdbCredentials == True:
            self.addDirectoryItem(32035, 'tvshows&url=trending', 'imdb.jpg', 'DefaultMovies.png', queue=True)

        if traktIndicators == True:
            self.addDirectoryItem(32036, 'calendar&url=trakthistory', 'trakt.jpg', 'DefaultTVShows.png', queue=True)
            self.addDirectoryItem(32037, 'calendar&url=progress', 'trakt.jpg', 'DefaultRecentlyAddedEpisodes.png', queue=True)
            self.addDirectoryItem(32038, 'calendar&url=mycalendar', 'trakt.jpg', 'DefaultRecentlyAddedEpisodes.png', queue=True)

        self.addDirectoryItem(32040, 'tvUserlists', 'userlists.jpg', 'DefaultTVShows.png')

        if traktCredentials == True:
            self.addDirectoryItem(32041, 'episodeUserlists', 'userlists.jpg', 'DefaultTVShows.png')

        if lite == False:
            self.addDirectoryItem(32031, 'tvliteNavigator', 'tvshows.jpg', 'DefaultTVShows.png')
            self.addDirectoryItem(32028, 'tvPerson', 'people-search.jpg', 'DefaultTVShows.png')
            self.addDirectoryItem(32010, 'tvSearch', 'search.jpg', 'DefaultTVShows.png')

        self.endDirectory()


    def tools(self):
        self.addDirectoryItem(32043, 'openSettings&query=0.0', 'tools.jpg', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32044, 'openSettings&query=3.1', 'tools.jpg', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32045, 'openSettings&query=1.0', 'tools.jpg', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32046, 'openSettings&query=6.0', 'tools.jpg', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32047, 'openSettings&query=2.0', 'tools.jpg', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32556, 'libraryNavigator', 'tools.jpg', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32048, 'openSettings&query=5.0', 'tools.jpg', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32049, 'viewsNavigator', 'tools.jpg', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32050, 'clearSources', 'tools.jpg', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32604, 'clearCacheSearch', 'tools.jpg', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32052, 'clearCache', 'tools.jpg', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32073, 'authTrakt', 'trakt.jpg', 'DefaultAddonProgram.png')

        self.endDirectory()

    def library(self):
        self.addDirectoryItem(32557, 'openSettings&query=4.0', 'tools.jpg', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32558, 'updateLibrary&query=tool', 'library_update.jpg', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32559, control.setting('library.movie'), 'movies.jpg', 'DefaultMovies.png', isAction=False)
        self.addDirectoryItem(32560, control.setting('library.tv'), 'tvshows.jpg', 'DefaultTVShows.png', isAction=False)

        if trakt.getTraktCredentialsInfo():
            self.addDirectoryItem(32561, 'moviesToLibrary&url=traktcollection', 'trakt.jpg', 'DefaultMovies.png')
            self.addDirectoryItem(32562, 'moviesToLibrary&url=traktwatchlist', 'trakt.jpg', 'DefaultMovies.png')
            self.addDirectoryItem(32563, 'tvshowsToLibrary&url=traktcollection', 'trakt.jpg', 'DefaultTVShows.png')
            self.addDirectoryItem(32564, 'tvshowsToLibrary&url=traktwatchlist', 'trakt.jpg', 'DefaultTVShows.png')

        self.endDirectory()

    def downloads(self):
        movie_downloads = control.setting('movie.download.path')
        tv_downloads = control.setting('tv.download.path')

        if len(control.listDir(movie_downloads)[0]) > 0:
            self.addDirectoryItem(32001, movie_downloads, 'movies.jpg', 'DefaultMovies.png', isAction=False)
        if len(control.listDir(tv_downloads)[0]) > 0:
            self.addDirectoryItem(32002, tv_downloads, 'tvshows.jpg', 'DefaultTVShows.png', isAction=False)

        self.endDirectory()


    def search(self):
        self.addDirectoryItem(32001, 'movieSearch', 'search.jpg', 'DefaultMovies.png')
        self.addDirectoryItem(32002, 'tvSearch', 'search.jpg', 'DefaultTVShows.png')
        self.addDirectoryItem(32029, 'moviePerson', 'people-search.jpg', 'DefaultMovies.png')
        self.addDirectoryItem(32030, 'tvPerson', 'people-search.jpg', 'DefaultTVShows.png')

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


