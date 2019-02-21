# -*- coding: utf-8 -*-




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
        self.addDirectoryItem('Wild West Movies', 'wildmovieNavigator', 'ww.jpg', 'Defaultww.jpg')
        self.addDirectoryItem('Wild West TV Shows', 'wildshowsNavigator', 'ww.jpg', 'Defaultww.jpg')
        #if not control.setting('lists.widget') == '0':
            #self.addDirectoryItem(32003, 'mymovieNavigator', 'ww.jpg', 'DefaultVideoPlaylists.png')
            #self.addDirectoryItem(32004, 'mytvNavigator', 'ww.jpg', 'DefaultVideoPlaylists.png')

        #if not control.setting('movie.widget') == '0':
            #self.addDirectoryItem(32005, 'movieWidget', 'latest-ww.jpg', 'DefaultRecentlyAddedww.jpg')

        #if (traktIndicators == True and not control.setting('tv.widget.alt') == '0') or (traktIndicators == False and not control.setting('tv.widget') == '0'):
            #self.addDirectoryItem(32006, 'tvWidget', 'latest-episodes.png', 'DefaultRecentlyAddedEpisodes.png')

        #self.addDirectoryItem(32007, 'channels', 'channels.png', 'Defaultww.jpg')
        #self.addDirectoryItem(32008, 'toolNavigator', 'tools.png', 'DefaultAddonProgram.png')

        #downloads = True if control.setting('downloads') == 'true' and (len(control.listDir(control.setting('movie.download.path'))[0]) > 0 or len(control.listDir(control.setting('tv.download.path'))[0]) > 0) else False
        #if downloads == True:
            #self.addDirectoryItem(32009, 'downloadNavigator', 'downloads.png', 'DefaultFolder.png')

        #self.addDirectoryItem(32010, 'searchNavigator', 'search.png', 'DefaultFolder.png')

        self.endDirectory()
    def wildmovie(self, lite=False):
        #self.addDirectoryItem(32011, 'movieGenres', 'ww.jpg', 'Defaultww.jpg')
        self.addDirectoryItem('Resistance Classic Westerns', 'movies6&url=classwest', 'ww.jpg', 'Defaultww.jpg')
        self.addDirectoryItem(32012, 'movieYears', 'ww.jpg', 'Defaultww.jpg')
        #self.addDirectoryItem(32013, 'moviePersons', 'ww.jpg', 'Defaultww.jpg')
        #self.addDirectoryItem(32014, 'movieLanguages', 'ww.jpg', 'Defaultww.jpg')
        #self.addDirectoryItem(32015, 'movieCertificates', 'ww.jpg', 'Defaultww.jpg')
        #self.addDirectoryItem(32017, 'movies6&url=trending', 'ww.jpg', 'DefaultRecentlyAddedww.jpg')
        self.addDirectoryItem(32018, 'movies6&url=popular', 'ww.jpg', 'Defaultww.jpg')
        self.addDirectoryItem(32019, 'movies6&url=views', 'ww.jpg', 'Defaultww.jpg')
        self.addDirectoryItem(32020, 'movies6&url=boxoffice', 'ww.jpg', 'Defaultww.jpg')
        self.addDirectoryItem(32021, 'movies6&url=oscars', 'ww.jpg', 'Defaultww.jpg')
        #self.addDirectoryItem(32022, 'movies6&url=theaters', 'ww.jpg', 'DefaultRecentlyAddedww.jpg')
        self.addDirectoryItem(32005, 'movieWidget', 'ww.jpg', 'DefaultRecentlyAddedww.jpg')

        #if lite == False:
            #if not control.setting('lists.widget') == '0':
                #self.addDirectoryItem(32003, 'mymovieliteNavigator', 'ww.jpg', 'DefaultVideoPlaylists.png')


        self.endDirectory()


    def mymovies(self, lite=False):
        self.accountCheck()

        if traktCredentials == True and imdbCredentials == True:
            self.addDirectoryItem(32032, 'movies6&url=traktcollection', 'trakt.png', 'Defaultww.jpg', queue=True, context=(32551, 'moviesToLibrary&url=traktcollection'))
            self.addDirectoryItem(32033, 'movies6&url=traktwatchlist', 'trakt.png', 'Defaultww.jpg', queue=True, context=(32551, 'moviesToLibrary&url=traktwatchlist'))
            self.addDirectoryItem(32034, 'movies6&url=imdbwatchlist', 'imdb.png', 'Defaultww.jpg', queue=True)

        elif traktCredentials == True:
            self.addDirectoryItem(32032, 'movies6&url=traktcollection', 'trakt.png', 'Defaultww.jpg', queue=True, context=(32551, 'moviesToLibrary&url=traktcollection'))
            self.addDirectoryItem(32033, 'movies6&url=traktwatchlist', 'trakt.png', 'Defaultww.jpg', queue=True, context=(32551, 'moviesToLibrary&url=traktwatchlist'))

        elif imdbCredentials == True:
            self.addDirectoryItem(32032, 'movies6&url=imdbwatchlist', 'imdb.png', 'Defaultww.jpg', queue=True)
            self.addDirectoryItem(32033, 'movies6&url=imdbwatchlist2', 'imdb.png', 'Defaultww.jpg', queue=True)

        if traktCredentials == True:
            self.addDirectoryItem(32035, 'movies6&url=traktfeatured', 'trakt.png', 'Defaultww.jpg', queue=True)

        elif imdbCredentials == True:
            self.addDirectoryItem(32035, 'movies6&url=featured', 'imdb.png', 'Defaultww.jpg', queue=True)

        if traktIndicators == True:
            self.addDirectoryItem(32036, 'movies6&url=trakthistory', 'trakt.png', 'Defaultww.jpg', queue=True)

        self.addDirectoryItem(32039, 'movieUserlists', 'userlists.png', 'Defaultww.jpg')

        if lite == False:
            self.addDirectoryItem(32031, 'movieliteNavigator', 'ww.jpg', 'Defaultww.jpg')
            self.addDirectoryItem(32028, 'moviePerson', 'people-search.png', 'Defaultww.jpg')
            self.addDirectoryItem(32010, 'movieSearch', 'search.png', 'Defaultww.jpg')

        self.endDirectory()


    def wildshows(self, lite=False):
        #self.addDirectoryItem(32011, 'tvGenres', 'ww.jpg', 'Defaultww.jpg')
        #self.addDirectoryItem(32016, 'tvNetworks', 'networks.png', 'Defaultww.jpg')
        #self.addDirectoryItem(32014, 'tvLanguages', 'ww.jpg', 'Defaultww.jpg')
        #self.addDirectoryItem(32015, 'tvCertificates', 'ww.jpg', 'Defaultww.jpg')
        #self.addDirectoryItem(32017, 'tvshows6&url=trending', 'ww.jpg', 'DefaultRecentlyAddedEpisodes.png')
        self.addDirectoryItem(32018, 'tvshows6&url=popular', 'ww.jpg', 'Defaultww.jpg')
        self.addDirectoryItem(32023, 'tvshows6&url=rating', 'ww.jpg', 'Defaultww.jpg')
        self.addDirectoryItem(32019, 'tvshows6&url=views', 'ww.jpg', 'Defaultww.jpg')
        #self.addDirectoryItem(32024, 'tvshows6&url=airing', 'ww.jpg', 'Defaultww.jpg')
        #self.addDirectoryItem(32025, 'tvshows6&url=active', 'ww.jpg', 'Defaultww.jpg')
        #self.addDirectoryItem(32026, 'tvshows6&url=premiere', 'ww.jpg', 'Defaultww.jpg')
        #self.addDirectoryItem(32006, 'calendar&url=added', 'ww.jpg', 'DefaultRecentlyAddedEpisodes.png', queue=True)
        #self.addDirectoryItem(32027, 'calendars', 'ww.jpg', 'DefaultRecentlyAddedEpisodes.png')

        #if lite == False:
            #if not control.setting('lists.widget') == '0':
                #self.addDirectoryItem(32004, 'mytvliteNavigator', 'ww.jpg', 'DefaultVideoPlaylists.png')

        self.endDirectory()


    def mytvshows(self, lite=False):
        try:
            self.accountCheck()

            if traktCredentials == True and imdbCredentials == True:

                self.addDirectoryItem(32032, 'tvshows6&url=traktcollection', 'trakt.png', 'Defaultww.jpg', context=(32551, 'tvshowsToLibrary&url=traktcollection'))
                self.addDirectoryItem(32033, 'tvshows6&url=traktwatchlist', 'trakt.png', 'Defaultww.jpg', context=(32551, 'tvshowsToLibrary&url=traktwatchlist'))
                self.addDirectoryItem(32034, 'tvshows6&url=imdbwatchlist', 'imdb.png', 'Defaultww.jpg')

            elif traktCredentials == True:
                self.addDirectoryItem("Trakt On Deck", 'calendar&url=onDeck', 'trakt.png', 'Defaultww.jpg')
                self.addDirectoryItem(32032, 'tvshows6&url=traktcollection', 'trakt.png', 'Defaultww.jpg', context=(32551, 'tvshowsToLibrary&url=traktcollection'))
                self.addDirectoryItem(32033, 'tvshows6&url=traktwatchlist', 'trakt.png', 'Defaultww.jpg', context=(32551, 'tvshowsToLibrary&url=traktwatchlist'))

            elif imdbCredentials == True:
                self.addDirectoryItem(32032, 'tvshows6&url=imdbwatchlist', 'imdb.png', 'Defaultww.jpg')
                self.addDirectoryItem(32033, 'tvshows6&url=imdbwatchlist2', 'imdb.png', 'Defaultww.jpg')

            if traktCredentials == True:
                self.addDirectoryItem(32035, 'tvshows6&url=traktfeatured', 'trakt.png', 'Defaultww.jpg')

            elif imdbCredentials == True:
                self.addDirectoryItem(32035, 'tvshows6&url=trending', 'imdb.png', 'Defaultww.jpg', queue=True)

            if traktIndicators == True:
                self.addDirectoryItem(32036, 'calendar&url=trakthistory', 'trakt.png', 'Defaultww.jpg', queue=True)
                self.addDirectoryItem(32037, 'calendar&url=progress', 'trakt.png', 'DefaultRecentlyAddedEpisodes.png', queue=True)
                self.addDirectoryItem(32038, 'calendar&url=mycalendar', 'trakt.png', 'DefaultRecentlyAddedEpisodes.png', queue=True)

            self.addDirectoryItem(32040, 'tvUserlists', 'userlists.png', 'Defaultww.jpg')

            if traktCredentials == True:
                self.addDirectoryItem(32041, 'episodeUserlists', 'userlists.png', 'Defaultww.jpg')

            if lite == False:
                self.addDirectoryItem(32031, 'tvliteNavigator', 'ww.jpg', 'Defaultww.jpg')
                self.addDirectoryItem(32028, 'tvPerson', 'people-search.png', 'Defaultww.jpg')
                self.addDirectoryItem(32010, 'tvSearch', 'search.png', 'Defaultww.jpg')

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
        self.addDirectoryItem(32559, control.setting('library.movie'), 'ww.jpg', 'Defaultww.jpg', isAction=False)
        self.addDirectoryItem(32560, control.setting('library.tv'), 'ww.jpg', 'Defaultww.jpg', isAction=False)

        if trakt.getTraktCredentialsInfo():
            self.addDirectoryItem(32561, 'moviesToLibrary&url=traktcollection', 'trakt.png', 'Defaultww.jpg')
            self.addDirectoryItem(32562, 'moviesToLibrary&url=traktwatchlist', 'trakt.png', 'Defaultww.jpg')
            self.addDirectoryItem(32563, 'tvshowsToLibrary&url=traktcollection', 'trakt.png', 'Defaultww.jpg')
            self.addDirectoryItem(32564, 'tvshowsToLibrary&url=traktwatchlist', 'trakt.png', 'Defaultww.jpg')

        self.endDirectory()

    def downloads(self):
        movie_downloads = control.setting('movie.download.path')
        tv_downloads = control.setting('tv.download.path')

        if len(control.listDir(movie_downloads)[0]) > 0:
            self.addDirectoryItem(32001, movie_downloads, 'ww.jpg', 'Defaultww.jpg', isAction=False)
        if len(control.listDir(tv_downloads)[0]) > 0:
            self.addDirectoryItem(32002, tv_downloads, 'ww.jpg', 'Defaultww.jpg', isAction=False)

        self.endDirectory()


    def search(self):
        self.addDirectoryItem(32001, 'movieSearch', 'search.png', 'Defaultww.jpg')
        self.addDirectoryItem(32002, 'tvSearch', 'search.png', 'Defaultww.jpg')
        self.addDirectoryItem(32029, 'moviePerson', 'people-search.png', 'Defaultww.jpg')
        self.addDirectoryItem(32030, 'tvPerson', 'people-search.png', 'Defaultww.jpg')

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
