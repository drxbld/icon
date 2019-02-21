# -*- coding: utf-8 -*-

import os,base64,sys,urllib2,urlparse,xbmc,xbmcaddon,xbmcgui
from resources.lib.modules import control,cache,trakt

sysaddon = sys.argv[0] ; syshandle = int(sys.argv[1]) ; control.moderator()
artPath = control.artPath() ; addonFanart = control.addonFanart()
imdbCredentials = False if control.setting('imdb.user') == '' else True
traktCredentials = trakt.getTraktCredentialsInfo()
traktIndicators = trakt.getTraktIndicatorsInfo()
queueMenu = control.lang(32065).encode('utf-8')


class navigator:
    ADDON_ID      = xbmcaddon.Addon().getAddonInfo('id')
    HOMEPATH      = xbmc.translatePath('special://home/')
    ADDONSPATH    = os.path.join(HOMEPATH, 'addons')
    THISADDONPATH = os.path.join(ADDONSPATH, ADDON_ID)
    NEWSFILE      = base64.b64decode(b'')
    LOCALNEWS     = os.path.join(THISADDONPATH, 'whatsnew.txt')
    
    def root(self):
        self.addDirectoryItem(32001, 'movieNavigator', 'movies.png', 'DefaultMovies.png')
        self.addDirectoryItem(32002, 'tvNavigator', 'tvshows.png', 'DefaultTVShows.png')
        if not control.setting('lists.widget') == '0':
            self.addDirectoryItem(32003, 'mymovieNavigator', 'mymovies.png', 'DefaultVideoPlaylists.png')
            self.addDirectoryItem(32004, 'mytvNavigator', 'mytvshows.png', 'DefaultVideoPlaylists.png')
        if not control.setting('movie.widget') == '0':
            self.addDirectoryItem(32005, 'movieWidget', 'latest-movies.png', 'DefaultRecentlyAddedMovies.png')
        if (traktIndicators == True and not control.setting('tv.widget.alt') == '0') or (traktIndicators == False and not control.setting('tv.widget') == '0'):
            self.addDirectoryItem(32006, 'tvWidget', 'latest-episodes.png', 'DefaultRecentlyAddedEpisodes.png')
        if self.getMenuEnabled('navi.userlists') == True:
            self.addDirectoryItem(42003, 'wtfNavigator', 'imdb.png', 'DefaultVideoPlaylists.png')
            self.addDirectoryItem('TMDB Lists', 'JewNavigator', 'tmdb.png', 'DefaultVideoPlaylists.png')
        if self.getMenuEnabled('navi.morestuff') == True:
            self.addDirectoryItem(42004, 'moreplugs', 'movies.png', 'DefaultMovies.png')
        downloads = True if control.setting('downloads') == 'true' and (len(control.listDir(control.setting('movie.download.path'))[0]) > 0 or len(control.listDir(control.setting('tv.download.path'))[0]) > 0) else False
        if downloads == True:
            self.addDirectoryItem(32009, 'downloadNavigator', 'downloads.png', 'DefaultFolder.png')
        self.addDirectoryItem('Search Kong Tv', 'searchNavigator', 'search.png', 'DefaultFolder.png')
        self.addDirectoryItem(32008, 'toolNavigator', 'tools.png', 'DefaultAddonProgram.png')
        if self.getMenuEnabled('navi.changeLog') == True:
            self.addDirectoryItem('Show Changelog',  'ShowChangelog',  'icon.png',  'DefaultFolder.png')
        if self.getMenuEnabled('navi.dev') == True:
            self.addDirectoryItem('Dev Menu', 'devtoolNavigator', 'tools.png', 'DefaultAddonProgram.png')
        self.endDirectory()

    def getMenuEnabled(self, menu_title):
        is_enabled = control.setting(menu_title).strip()
        if (is_enabled == '' or is_enabled == 'false'): return False
        return True

    def news(self):
            message=self.open_news_url(self.NEWSFILE)
            r = open(self.LOCALNEWS)
            compfile = r.read()       
            if len(message)>1:
                    if compfile == message:pass
                    else:
                            text_file = open(self.LOCALNEWS, "w")
                            text_file.write(message)
                            text_file.close()
                            compfile = message
            self.showText('[B][I][COLOR orange]Kong Tv News[/B][/I][/COLOR]', compfile)
        
    def open_news_url(self, url):
            req = urllib2.Request(url)
            req.add_header('User-Agent', 'klopp')
            response = urllib2.urlopen(req)
            link=response.read()
            response.close()
            print link
            return link

    def showText(self, heading, text):
        id = 10147
        xbmc.executebuiltin('ActivateWindow(%d)' % id)
        xbmc.sleep(500)
        win = xbmcgui.Window(id)
        retry = 50
        while (retry > 0):
            try:
                xbmc.sleep(10)
                retry -= 1
                win.getControl(1).setLabel(heading)
                win.getControl(5).setText(text)
                quit()
                return
            except: pass
            
            
    def movies(self, lite=False):
        if self.getMenuEnabled('navi.moviegenre') == True:
            self.addDirectoryItem(32011, 'movieGenres', 'genres.png', 'DefaultMovies.png')
        if self.getMenuEnabled('navi.movieyears') == True:
            self.addDirectoryItem(32012, 'movieYears', 'years.png', 'DefaultMovies.png')
        if self.getMenuEnabled('navi.moviepersons') == True:
            self.addDirectoryItem(32013, 'moviePersons', 'people.png', 'DefaultMovies.png')
        if self.getMenuEnabled('navi.movielanguages') == True:
            self.addDirectoryItem(32014, 'movieLanguages', 'languages.png', 'DefaultMovies.png')
        if self.getMenuEnabled('navi.moviecerts') == True:
            self.addDirectoryItem(32015, 'movieCertificates', 'certificates.png', 'DefaultMovies.png')
        self.addDirectoryItem('BoxSets', 'boxesNavigator', 'tmdb.png', 'DefaultVideoPlaylists.png')
        self.addDirectoryItem('Movie Mosts', 'movieMosts', 'people-watching.png', 'DefaultMovies.png')
        if self.getMenuEnabled('navi.moviefeat') == True:
            self.addDirectoryItem(32035, 'movies&url=featured', 'imdb.png', 'imdb.png')
            self.addDirectoryItem('Featured(TMDB)', 'movies2&url=featured', 'featured.png', 'DefaultMovies.png')
            self.addDirectoryItem('Featured(Trakt)', 'movies&url=traktfeatured', 'featured.png', 'DefaultMovies.png')
        if self.getMenuEnabled('navi.movietrending') == True:
            self.addDirectoryItem(32017, 'movies&url=trending', 'people-watching.png', 'DefaultRecentlyAddedMovies.png')
        if self.getMenuEnabled('navi.moviepopular') == True:
            self.addDirectoryItem(32018, 'movies&url=popular', 'most-popular.png', 'DefaultMovies.png')
            self.addDirectoryItem('Popular(TMDB)', 'movies2&url=popular', 'most-popular.png', 'DefaultMovies.png')
        if self.getMenuEnabled('navi.movieviews') == True:
            self.addDirectoryItem(32019, 'movies&url=views', 'most-voted.png', 'DefaultMovies.png')
            self.addDirectoryItem('Top Rated', 'movies2&url=toprated', 'movies.png', 'DefaultMovies.png')
        if self.getMenuEnabled('navi.movieboxoffice') == True:
            self.addDirectoryItem(32020, 'movies&url=boxoffice', 'box-office.png', 'DefaultMovies.png')
        self.addDirectoryItem('Premiere', 'movies2&url=premiere', 'movies.png', 'DefaultMovies.png')
        if self.getMenuEnabled('navi.movietheaters') == True:
            self.addDirectoryItem(32022, 'movies&url=theaters', 'in-theaters.png', 'DefaultRecentlyAddedMovies.png')
            self.addDirectoryItem('In Theaters(Old Style)', 'movies&url=theatersOld', 'in-theaters.png', 'DefaultRecentlyAddedMovies.png')
            self.addDirectoryItem('In Theaters(TMDB)', 'movies2&url=theaters', 'movies.png', 'DefaultRecentlyAddedMovies.png')
        if self.getMenuEnabled('navi.movieoscars') == True:
            self.addDirectoryItem(32021, 'movies&url=oscars', 'oscar-winners.png', 'DefaultMovies.png')
        if lite == False:
            if not control.setting('lists.widget') == '0':
                self.addDirectoryItem(32003, 'mymovieliteNavigator', 'mymovies.png', 'DefaultVideoPlaylists.png')
            self.addDirectoryItem(32028, 'moviePerson', 'people-search.png', 'DefaultMovies.png')
            self.addDirectoryItem(32010, 'movieSearch', 'search.png', 'DefaultMovies.png')
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
        if traktIndicators == True:
            self.addDirectoryItem(32036, 'movies&url=trakthistory', 'trakt.png', 'DefaultMovies.png', queue=True)
        self.addDirectoryItem(32039, 'movieUserlists', 'userlists.png', 'DefaultMovies.png')
        if lite == False:
            self.addDirectoryItem(32031, 'movieliteNavigator', 'movies.png', 'DefaultMovies.png')
            self.addDirectoryItem(32028, 'moviePerson', 'people-search.png', 'DefaultMovies.png')
            self.addDirectoryItem(32010, 'movieSearch', 'search.png', 'DefaultMovies.png')
        self.endDirectory()

    def tvshows(self, lite=False):
        if self.getMenuEnabled('navi.tvGenres') == True:
            self.addDirectoryItem(32011, 'tvGenres', 'genres.png', 'DefaultTVShows.png')
        if self.getMenuEnabled('navi.tvNetworks') == True:
            self.addDirectoryItem(32016, 'tvNetworks', 'networks.png', 'DefaultTVShows.png')
        if self.getMenuEnabled('navi.tvLanguages') == True:
            self.addDirectoryItem(32014, 'tvLanguages', 'languages.png', 'DefaultTVShows.png')
        if self.getMenuEnabled('navi.tvCertificates') == True:
            self.addDirectoryItem(32015, 'tvCertificates', 'certificates.png', 'DefaultTVShows.png')
        if self.getMenuEnabled('navi.tvfeat') == True:
            self.addDirectoryItem('Featured(TMDB)', 'tvshows2&url=featured', 'featured.png', 'DefaultTVShows.png')
            self.addDirectoryItem(32035, 'tvshows&url=traktfeatured', 'featured.png', 'DefaultTVShows.png')
        if self.getMenuEnabled('navi.tvTrending') == True:
            self.addDirectoryItem(32017, 'tvshows&url=trending', 'people-watching.png', 'DefaultRecentlyAddedEpisodes.png')
        if self.getMenuEnabled('navi.tvPopular') == True:
            self.addDirectoryItem('Popular(TMDB)', 'tvshows2&url=popular', 'most-popular.png', 'DefaultTVShows.png')
            self.addDirectoryItem(32018, 'tvshows&url=popular', 'most-popular.png', 'DefaultTVShows.png')
        if self.getMenuEnabled('navi.tvRating') == True:
            self.addDirectoryItem('Top Rated(TMDB)', 'tvshows2&url=rating', 'highly-rated.png', 'DefaultTVShows.png')
            self.addDirectoryItem(32023, 'tvshows&url=rating', 'highly-rated.png', 'DefaultTVShows.png')
        if self.getMenuEnabled('navi.tvViews') == True:
            self.addDirectoryItem('Most Views(TMDB)', 'tvshows2&url=views', 'movies.png', 'DefaultVideoPlaylists.png')
            self.addDirectoryItem(32019, 'tvshows&url=views', 'most-voted.png', 'DefaultTVShows.png')
        self.addDirectoryItem('TV Show Mosts', 'showMosts', 'people-watching.png', 'DefaultTVShows.png')
        if self.getMenuEnabled('navi.tvAiring') == True:
            self.addDirectoryItem('Airing Today(TMDB)', 'tvshows2&url=airing', 'airing-today.png', 'DefaultTVShows.png')
            self.addDirectoryItem(32024, 'tvshows&url=airing', 'airing-today.png', 'DefaultTVShows.png')
        if self.getMenuEnabled('navi.tvActive') == True:
            self.addDirectoryItem('On The Air(TMDB)', 'tvshows2&url=active', 'returning-tvshows.png', 'DefaultTVShows.png')
            self.addDirectoryItem(32025, 'tvshows&url=active', 'returning-tvshows.png', 'DefaultTVShows.png')
        if self.getMenuEnabled('navi.tvPremier') == True:
            self.addDirectoryItem('Premiere(TMDB)', 'tvshows2&url=premiere', 'movies.png', 'DefaultVideoPlaylists.png')
            self.addDirectoryItem(32026, 'tvshows&url=premiere', 'new-tvshows.png', 'DefaultTVShows.png')
        if self.getMenuEnabled('navi.tvAdded') == True:
            self.addDirectoryItem(32006, 'calendar&url=added', 'latest-episodes.png', 'DefaultRecentlyAddedEpisodes.png', queue=True)
        if self.getMenuEnabled('navi.tvCalendar') == True:
            self.addDirectoryItem(32027, 'calendars', 'calendar.png', 'DefaultRecentlyAddedEpisodes.png')
        if lite == False:
            if not control.setting('lists.widget') == '0':
                self.addDirectoryItem(32004, 'mytvliteNavigator', 'mytvshows.png', 'DefaultVideoPlaylists.png')
            self.addDirectoryItem(32028, 'tvPerson', 'people-search.png', 'DefaultTVShows.png')
            self.addDirectoryItem(32010, 'tvSearch', 'search.png', 'DefaultTVShows.png')
        self.endDirectory()

    def mytvshows(self, lite=False):
        self.accountCheck()
        if traktCredentials == True and imdbCredentials == True:
            self.addDirectoryItem(32032, 'tvshows&url=traktcollection', 'trakt.png', 'DefaultTVShows.png', context=(32551, 'tvshowsToLibrary&url=traktcollection'))
            self.addDirectoryItem(32033, 'tvshows&url=traktwatchlist', 'trakt.png', 'DefaultTVShows.png', context=(32551, 'tvshowsToLibrary&url=traktwatchlist'))
            self.addDirectoryItem(32034, 'tvshows&url=imdbwatchlist', 'imdb.png', 'DefaultTVShows.png')
        elif traktCredentials == True:
            self.addDirectoryItem(32032, 'tvshows&url=traktcollection', 'trakt.png', 'DefaultTVShows.png', context=(32551, 'tvshowsToLibrary&url=traktcollection'))
            self.addDirectoryItem(32033, 'tvshows&url=traktwatchlist', 'trakt.png', 'DefaultTVShows.png', context=(32551, 'tvshowsToLibrary&url=traktwatchlist'))
        elif imdbCredentials == True:
            self.addDirectoryItem(32032, 'tvshows&url=imdbwatchlist', 'imdb.png', 'DefaultTVShows.png')
            self.addDirectoryItem(32033, 'tvshows&url=imdbwatchlist2', 'imdb.png', 'DefaultTVShows.png')
        if traktIndicators == True:
            self.addDirectoryItem(32036, 'calendar&url=trakthistory', 'trakt.png', 'DefaultTVShows.png', queue=True)
            self.addDirectoryItem(32037, 'calendar&url=progress', 'trakt.png', 'DefaultRecentlyAddedEpisodes.png', queue=True)
            self.addDirectoryItem(32038, 'calendar&url=mycalendar', 'trakt.png', 'DefaultRecentlyAddedEpisodes.png', queue=True)
        self.addDirectoryItem(32040, 'tvUserlists', 'userlists.png', 'DefaultTVShows.png')
        if traktCredentials == True:
            self.addDirectoryItem(32041, 'episodeUserlists', 'userlists.png', 'DefaultTVShows.png')
        if lite == False:
            self.addDirectoryItem(32031, 'tvliteNavigator', 'tvshows.png', 'DefaultTVShows.png')
            self.addDirectoryItem(32028, 'tvPerson', 'people-search.png', 'DefaultTVShows.png')
            self.addDirectoryItem(32010, 'tvSearch', 'search.png', 'DefaultTVShows.png')
        self.endDirectory()

    def wtf(self):
        self.addDirectoryItem(42002, 'tvshows&url=soaps', 'userlists.png', 'DefaultVideoPlaylists.png')
        self.addDirectoryItem('Dr Faustus Lists', 'spikeNavigator', 'userlists.png', 'DefaultVideoPlaylists.png')
        self.addDirectoryItem('The Ultimate Lists', 'critterLists', 'userlists.png', 'DefaultVideoPlaylists.png')
        self.addDirectoryItem('Top Movies Lists', 'playlistNavigator', 'userlists.png', 'DefaultVideoPlaylists.png')
        self.addDirectoryItem('IMDb-Editors (Movies)', 'wtfMovies', 'userlists.png', 'DefaultVideoPlaylists.png')
        self.addDirectoryItem('IMDb-Editors (Shows)', 'wtfShows', 'userlists.png', 'DefaultVideoPlaylists.png')
        self.addDirectoryItem('Hella Lists Book1', 'customNavigator', 'userlists.png', 'DefaultVideoPlaylists.png')
        self.addDirectoryItem('Hella Lists Book2', 'imdbLists', 'userlists.png', 'DefaultVideoPlaylists.png')
        self.endDirectory()		

    def wtfMovies(self):
		self.addDirectoryItem('New and Recent DVD/Blu-ray Releases', 'movies&url=imdbeditor1', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Popular Sci-Fi Movies to Stream Now With Prime', 'movies&url=imdbeditor2', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Trending Movies on Amazon Video', 'movies&url=imdbeditor24', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Horror Titles on Amazon Video', 'movies&url=imdbeditor25', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Comedy Titles to Discover on Amazon Video', 'movies&url=imdbeditor6', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Action and Adventure Titles to Discover on Amazon Video', 'movies&url=imdbeditor7', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Drama Movies to Discover on Amazon Video', 'movies&url=imdbeditor8', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Classic Movies on Amazon Video', 'movies&url=imdbeditor10', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Movies by Oscar-Winning Directors on Amazon Video', 'movies&url=imdbeditor11', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Popular Indie Movies on Amazon Video', 'movies&url=imdbeditor12', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Holiday Classics on Amazon Video', 'movies&url=imdbeditor13', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Trending Horror Movies on Amazon Video', 'movies&url=imdbeditor14', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Trending Titles on Amazon Video', 'movies&url=imdbeditor15', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Trending New Releases on Amazon Video', 'movies&url=imdbeditor16', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Most Popular Titles on Amazon Video', 'movies&url=imdbeditor17', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Popular Fathers Day Movies on Amazon Video', 'movies&url=imdbeditor22', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Valentines Day Suggestions on Amazon Video', 'movies&url=imdbeditor27', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('New Releases on Amazon Video', 'movies&url=imdbeditor28', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Binge-Watch Star Wars on Amazon Video', 'movies&url=imdbeditor29', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('The Marvel Universe on Amazon Instant Video', 'movies&url=imdbeditor33', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Top 20 Most Awesome Streaming Family Movies', 'movies&url=imdbeditor32', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('80 of the Best Horror Movies to Stream Today', 'movies&url=imdbeditor5', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('On TV: Holiday Specials and Movies', 'movies&url=imdbeditortvsp1', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Holiday TV Specials and Movies', 'movies&url=imdbeditortvsp2', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Holiday TV Viewing Guide', 'movies&url=imdbeditortvsp3', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Top-Rated Movies for a Solar Eclipse', 'movies&url=imdbeditor9', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Top 12 Holiday Movies with Families More Dysfunctional than Yours', 'movies&url=imdbeditor34', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('12 Top War Movies', 'movies&url=imdbeditor35', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Top 25 Movies by User Rating From the Last 25 Years', 'movies&url=imdbeditor30', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('15 Best Live Action Kids Movies', 'movies&url=imdbeditor31', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('10 Most Popular Lifetime Movies on IMDb', 'movies&url=imdbeditor23', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Top 100 Movies as Rated by Women on IMDb in 2016', 'movies&url=imdbeditor3', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('The Top 200 Movies as Rated by Women on IMDb in 2018', 'movies&url=imdbeditor4', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Beyond the Top 250: IMDb Staffs Favorite Movies', 'movies&url=imdbeditor26', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Best Charles Bronson Movies as Rated by IMDb Users', 'movies&url=imdbeditor18', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('All Kubrick Movies Ranked by IMDb Users', 'movies&url=imdbeditor19', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('All Woody Allen Movies Ranked by IMDb User Ratings', 'movies&url=imdbeditor20', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Nicolas Winding Refn Movies by IMDb User Ratings', 'movies&url=imdbeditor21', 'imdb.png', 'imdb.png')
		self.endDirectory()	

    def movieMosts(self):
		self.addDirectoryItem('Most Played This Week', 'movies&url=played1', 'most-popular.png', 'DefaultMovies.png')
		self.addDirectoryItem('Most Played This Month', 'movies&url=played2', 'most-popular.png', 'DefaultMovies.png')
		self.addDirectoryItem('Most Played This Year', 'movies&url=played3', 'most-popular.png', 'DefaultMovies.png')
		self.addDirectoryItem('Most Played All Time', 'movies&url=played4', 'most-popular.png', 'DefaultMovies.png')
		self.addDirectoryItem('Most Collected This Week', 'movies&url=collected1', 'most-popular.png', 'DefaultMovies.png')
		self.addDirectoryItem('Most Collected This Month', 'movies&url=collected2', 'most-popular.png', 'DefaultMovies.png')
		self.addDirectoryItem('Most Collected This Year', 'movies&url=collected3', 'most-popular.png', 'DefaultMovies.png')
		self.addDirectoryItem('Most Collected All Time', 'movies&url=collected4', 'most-popular.png', 'DefaultMovies.png')
		self.addDirectoryItem('Most Watched This Week', 'movies&url=watched1', 'most-popular.png', 'DefaultMovies.png')
		self.addDirectoryItem('Most Watched This Month', 'movies&url=watched2', 'most-popular.png', 'DefaultMovies.png')
		self.addDirectoryItem('Most Watched This Year', 'movies&url=watched3', 'most-popular.png', 'DefaultMovies.png')
		self.addDirectoryItem('Most Watched All Time', 'movies&url=watched4', 'most-popular.png', 'DefaultMovies.png')
		self.endDirectory()	

    def wtfShows(self):
		self.addDirectoryItem('Best Shows on Prime Video', 'tvshows&url=imdbeditortv5', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('20 Top-Rated Shows on Prime Video', 'tvshows&url=imdbeditortv4', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Animated TV Shows to Stream Now With Prime Video', 'tvshows&url=imdbeditortv2', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Popular on Amazon Video: Top TV Shows', 'tvshows&url=imdbeditortv11', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Binge-Worthy TV Shows on Amazon Video', 'tvshows&url=imdbeditortv9', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('GoldenGlobe-Nominated TV Shows on Amazon Video', 'tvshows&url=imdbeditortv10', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Great Late-Night TV on Amazon Instant Video', 'tvshows&url=imdbeditortv16', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Streaming TV Trending Title List', 'tvshows&url=imdbeditortv6', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Top 25 TV Shows by User Rating From the Last 25 Years', 'tvshows&url=imdbeditortv13', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Top 100 TV Shows as Rated by Women on IMDb in 2016', 'tvshows&url=imdbeditortv7', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Top 200 TV Shows as Rated by Women on IMDb in 2018', 'tvshows&url=imdbeditortv8', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Top Picks for Weekend Binge-Watching', 'tvshows&url=imdbeditortv3', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Favorite TV Shows to Binge-Watch', 'tvshows&url=imdbeditortv18', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('12 Binge-worthy TV Series for the Entire Family', 'tvshows&url=imdbeditortv15', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Holiday TV Viewing Guide', 'tvshows&url=imdbeditortvsp4', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Where to Watch Your Favorite DC, Marvel, and Other Superhero TV Shows', 'tvshows&url=imdbeditortv1', 'imdb.png', 'imdb.png')
		self.endDirectory()	

    def showMosts(self):
		self.addDirectoryItem('Most Played This Week', 'tvshows&url=played1', 'most-popular.png', 'DefaultTVShows.png')
		self.addDirectoryItem('Most Played This Month', 'tvshows&url=played2', 'most-popular.png', 'DefaultTVShows.png')
		self.addDirectoryItem('Most Played This Year', 'tvshows&url=played3', 'most-popular.png', 'DefaultTVShows.png')
		self.addDirectoryItem('Most Played All Time', 'tvshows&url=played4', 'most-popular.png', 'DefaultTVShows.png')
		self.addDirectoryItem('Most Collected This Week', 'tvshows&url=collected1', 'most-popular.png', 'DefaultTVShows.png')
		self.addDirectoryItem('Most Collected This Month', 'tvshows&url=collected2', 'most-popular.png', 'DefaultTVShows.png')
		self.addDirectoryItem('Most Collected This Year', 'tvshows&url=collected3', 'most-popular.png', 'DefaultTVShows.png')
		self.addDirectoryItem('Most Collected All Time', 'tvshows&url=collected4', 'most-popular.png', 'DefaultTVShows.png')
		self.addDirectoryItem('Most Watched This Week', 'tvshows&url=watched1', 'most-popular.png', 'DefaultTVShows.png')
		self.addDirectoryItem('Most Watched This Month', 'tvshows&url=watched2', 'most-popular.png', 'DefaultTVShows.png')
		self.addDirectoryItem('Most Watched This Year', 'tvshows&url=watched3', 'most-popular.png', 'DefaultTVShows.png')
		self.addDirectoryItem('Most Watched All Time', 'tvshows&url=watched4', 'most-popular.png', 'DefaultTVShows.png')
		self.endDirectory()


    def moreplugs(self):
        self.addDirectoryItem('IPTV', 'iptvChannels', 'channels.png', 'DefaultTVShows.png')
        self.addDirectoryItem('MusicChoice', 'jewMC', 'highly-rated.png', 'DefaultTVShows.png')
        self.addDirectoryItem('Tunes', 'radios', 'highly-rated.png', 'DefaultTVShows.png')
        self.addDirectoryItem(326232, 'tvReviews', 'highly-rated.png', 'DefaultVideoPlaylists.png')
        self.addDirectoryItem(32623, 'movieReviews', 'highly-rated.png', 'DefaultVideoPlaylists.png')
        self.addDirectoryItem(32631, 'docuHeaven', 'highly-rated.png', 'DefaultVideoPlaylists.png')
        self.addDirectoryItem(32610, 'kidscorner', 'highly-rated.png', 'DefaultVideoPlaylists.png')
        self.addDirectoryItem(32611, 'fitness', 'highly-rated.png', 'DefaultVideoPlaylists.png')
        self.addDirectoryItem(32612, 'legends', 'highly-rated.png', 'DefaultVideoPlaylists.png')
        self.addDirectoryItem(32620, 'podcastNavigator', 'highly-rated.png', 'DefaultVideoPlaylists.png')
        if self.getMenuEnabled('navi.xxx') == True:
            self.addDirectoryItem('[COLOR black]xxx[/COLOR]', 'navXXX', 'highly-rated.png', 'DefaultTVShows.png')
        self.endDirectory()


    def custom(self):
		self.addDirectoryItem('Anime', 'movies&url=anime', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Avant Garde', 'movies&url=avant', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Based On A True Story', 'movies&url=true', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Biker', 'movies&url=biker', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('B Movies', 'movies&url=bmovie', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Breaking The Fourth Wall', 'movies&url=breaking', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Business', 'movies&url=business', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Capers', 'movies&url=caper', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Car Chases', 'movies&url=car', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Chick Flix', 'movies&url=chick', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Coming to Age', 'movies&url=coming', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Competition', 'movies&url=competition', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Cult', 'movies&url=cult', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Cyberpunk', 'movies&url=cyber', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Dead Of Night', 'movies&url=deadofnight', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Drug Addiction', 'movies&url=drugs', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Dystopia', 'movies&url=dystopia', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Epic', 'movies&url=epic', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Espionage', 'movies&url=espionage', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Experimental', 'movies&url=expiremental', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Fairy Tale', 'movies&url=fairytale', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Farce', 'movies&url=farce', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Femme Fatale', 'movies&url=femme', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Futuristic', 'movies&url=futuristic', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Heist', 'movies&url=heist', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('High School', 'movies&url=highschool', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Horror Movie Remakes', 'movies&url=remakes', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('James Bond', 'movies&url=bond', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Kidnapping', 'movies&url=kidnapped', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Kung Fu', 'movies&url=kungfu', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Monster', 'movies&url=monster', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Movie Loners', 'movies&url=loners', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Mockumentaries', 'movies&url=mock', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Neo Noir', 'movies&url=neo', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Parenthood', 'movies&url=parenthood', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Parody', 'movies&url=parody', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Post Apocalypse', 'movies&url=apocalypse', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Remakes', 'movies&url=remake', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Road Movies', 'movies&url=road', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Robots', 'movies&url=robot', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Satire', 'movies&url=satire', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Serial Killers', 'movies&url=serial', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Slasher', 'movies&url=slasher', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Spiritual', 'movies&url=spiritual', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Spoofs', 'movies&url=spoof', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Star Wars', 'movies&url=star', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Steampunk', 'movies&url=steampunk', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Superheros', 'movies&url=superhero', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Supernatural', 'movies&url=supernatural', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Tech Noir', 'movies&url=tech', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Time Travel', 'movies&url=time', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Vampires', 'movies&url=vampire', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Virtual Reality', 'movies&url=vr', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Wilhelm Scream', 'movies&url=wilhelm', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Zombies', 'movies&url=zombie', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('New Years', 'movies&url=newyear', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Easter', 'movies&url=easter', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Halloween', 'movies&url=halloween', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Thanksgiving', 'movies&url=thanx', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Christmas', 'movies&url=xmass', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('DC', 'movies&url=dc', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Marvel Universe', 'movies&url=marvel', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Disney and Pixar', 'movies&url=disney', 'imdb.png', 'imdb.png')
		self.endDirectory()		

    def playlist(self):
		self.addDirectoryItem('I Love The 80s', 'movies&url=eighties', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('IMDB Top 1000', 'movies&url=thousand', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Top Documentaries 00-17', 'movies&url=docs', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Top Action Movies 00-17', 'movies&url=action', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Top Animated 00-17', 'movies&url=animated', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Top Gangster Movies', 'movies&url=gangster', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Top Horror Movies 00-17', 'movies&url=horror', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Top Action Movies 60-99', 'movies&url=action2', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Greatest Horror Films of All Time', 'movies&url=horror2', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Greatest Sci-Fi Films of All Time', 'movies&url=scifi', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Greatest Westerns of All Time', 'movies&url=western', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Top Cop Movies', 'movies&url=cop', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Greatest War Movies', 'movies&url=war', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('The Most Romantic Movies', 'movies&url=romance', 'imdb.png', 'imdb.png')
		self.endDirectory()

    def spike(self):
		self.addDirectoryItem('TOP SCIENCE-FICTION MOVIES: 2000-2018', 'movies&url=imdbdrf1', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('TOP HORROR MOVIES: 2000-2018', 'movies&url=imdbdrf2', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('TOP COMEDY MOVIES', 'movies&url=imdbdrf3', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('TOP HORROR MOVIES: PRE-2000', 'movies&url=imdbdrf4', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('TOP POLITICAL MOVIES', 'movies&url=imdbdrf5', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('TOP DOCUMENTARY MOVIES: 2000-2018', 'movies&url=imdbdrf6', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('TOP ACTION AND ADVENTURE MOVIES: 1980s', 'movies&url=imdbdrf7', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('TOP ACTION MOVIES: 2000-2018', 'movies&url=imdbdrf8', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('TOP ANIMATED MOVIES: 2000-2018', 'movies&url=imdbdrf9', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('TOP WESTERNS', 'movies&url=imdbdrf10', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('TOP WAR MOVIES', 'movies&url=imdbdrf11', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('TOP ANIMATED MOVIES: PRE-2000', 'movies&url=imdbdrf12', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('TOP ACTION AND ADVENTURE MOVIES: 1990s', 'movies&url=imdbdrf13', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('TOP ACTION AND ADVENTURE MOVIES: 1970s', 'movies&url=imdbdrf14', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('ACTUAL ONE-SHOT MOVIES', 'movies&url=imdbdrf15', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('2018: A MOVIE ODYSSEY', 'movies&url=imdbdrf16', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('100 Greatest Worst Movies', 'movies&url=imdbdrf17', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('HORROR FILM SERIES AND FRANCHISES', 'movies&url=imdbdrf18', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('James Bond: 50 Years of Main Title Design', 'movies&url=imdbdrf19', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('EXISTENTIAL FILMS', 'movies&url=imdbdrf20', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('MOVIE LONERS', 'movies&url=imdbdrf21', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('MOVIES AND RACISM', 'movies&url=imdbdrf22', 'imdb.png', 'imdb.png')
		self.endDirectory()

    def imdbLists(self):
		self.addDirectoryItem('Greatest Movies: 2000-2017', 'movies&url=imdb1', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Horror Movie Series', 'movies&url=imdb2', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Horror Of The Skull Posters', 'movies&url=imdb3', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Top Satirical Movies', 'movies&url=imdb4', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Greatest Science Fiction', 'movies&url=imdb5', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Top Private Eye Movies', 'movies&url=imdb7', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Sleeper Hit Movies', 'movies&url=imdb8', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Cult Horror Movies', 'movies&url=imdb9', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Heist Caper Movies', 'movies&url=imdb10', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Artificial Intelligence', 'movies&url=imdb11', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Stephen King Movies and Adaptations', 'movies&url=imdb12', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Alien Invasion', 'movies&url=imdb13', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Contract Killers', 'movies&url=imdb14', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Heroic Bloodshed', 'movies&url=imdb15', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Conspiracy', 'movies&url=imdb16', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Top Kung Fu', 'movies&url=imdb17', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Movies Based In One Room', 'movies&url=imdb18', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Movies For Intelligent People', 'movies&url=imdb19', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Inspirational Movies', 'movies&url=imdb20', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Tech Geeks', 'movies&url=imdb21', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Movie Clones', 'movies&url=imdb22', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Obscure Underrated Movies', 'movies&url=imdb23', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Smut and Trash', 'movies&url=imdb24', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Revenge', 'movies&url=imdb25', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Motivational', 'movies&url=imdb26', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Disaster & Apocalyptic', 'movies&url=imdb27', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Music or Musical Movies', 'movies&url=imdb28', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Mental, Physical Illness and Disability Movies', 'movies&url=imdb29', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Best Twist Ending Movies', 'movies&url=imdb30', 'imdb.png', 'playlist.png')
		self.addDirectoryItem('Heists, Cons, Scams & Robbers', 'movies&url=imdb31', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Road Trip & Travel', 'movies&url=imdb32', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Spy - CIA - MI5 - MI6 - KGB', 'movies&url=imdb33', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Prison & Escape', 'movies&url=imdb34', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Courtroom', 'movies&url=imdb35', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Father - Son', 'movies&url=imdb36', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Based on a True Story', 'movies&url=imdb37', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Man Vs. Nature', 'movies&url=imdb38', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Gangster', 'movies&url=imdb39', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Teenage', 'movies&url=imdb40', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Old Age', 'movies&url=imdb41', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Serial Killers', 'movies&url=imdb42', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Addiction', 'movies&url=imdb43', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Time Travel', 'movies&url=imdb44', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Puff Puff Pass', 'movies&url=imdb45', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Artists , Painters , Writers', 'movies&url=imdb46', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Love', 'movies&url=imdb47', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Winter Is Here', 'movies&url=imdb48', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Suicide', 'movies&url=imdb49', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Alchoholic', 'movies&url=imdb50', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Video Games', 'movies&url=imdb51', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Shocking Movie Scenes', 'movies&url=imdb52', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Biographical', 'movies&url=imdb53', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Movies to Teach You a Thing or Two', 'movies&url=imdb54', 'imdb.png', 'imdb.png')
		self.endDirectory()	

    def critterLists(self):
		self.addDirectoryItem('Best Detective Films and TV series', 'tvshows&url=imdbtultv1', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Best TV Drama', 'tvshows&url=imdbtultv2', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Best Animated TV Series', 'tvshows&url=imdbtultv3', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Best War Films', 'movies&url=imdbtul1', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('World War II Movies', 'movies&url=imdbtul2', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Best Spy Movies', 'movies&url=imdbtul3', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Superhero Movies', 'movies&url=imdbtul4', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Modern Westerns', 'movies&url=imdbtul5', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Best Dirty Cop Movies', 'movies&url=imdbtul6', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Best Crime Movies', 'movies&url=imdbtul7', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Best Psychological Thriller', 'movies&url=imdbtul8', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Science Fiction', 'movies&url=imdbtul9', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Best Thrillers', 'movies&url=imdbtul10', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Hitman Movies', 'movies&url=imdbtul11', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Best Legal Drama', 'movies&url=imdbtul12', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Best Documentary', 'movies&url=imdbtul13', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Biography Films', 'movies&url=imdbtul14', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Vampire Movies', 'movies&url=imdbtul15', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Best Short Movies', 'movies&url=imdbtul16', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Best Teen Movies', 'movies&url=imdbtul17', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Best Coming of Age Films', 'movies&url=imdbtul18', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Prison Films', 'movies&url=imdbtul19', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Sports Movies', 'movies&url=imdbtul20', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Best Revenge & Vigilante Movies', 'movies&url=imdbtul21', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Best TV Movies', 'movies&url=imdbtul22', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Best Family Movies', 'movies&url=imdbtul23', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Asian Crime Films', 'movies&url=imdbtul24', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Best Silent Films', 'movies&url=imdbtul25', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Best Fantasy Movies', 'movies&url=imdbtul26', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Best animated films', 'movies&url=imdbtul27', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Samourai Films', 'movies&url=imdbtul28', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Best Dark Comedies', 'movies&url=imdbtul29', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Blaxplotation', 'movies&url=imdbtul30', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Heist Films', 'movies&url=imdbtul31', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('HORROR of Slasher Films', 'movies&url=imdbtul32', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Best Giallo Films (Italian Horror)', 'movies&url=imdbtul33', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Best BUDDY Movies', 'movies&url=imdbtul34', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Best Costume Drama', 'movies&url=imdbtul35', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Best Westerns', 'movies&url=imdbtul36', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Classic Horror Films', 'movies&url=imdbtul37', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Disturbing,Controversial,Shocking and Unique', 'movies&url=imdbtul38', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Most Visually Beautiful Movies', 'movies&url=imdbtul39', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Top British Crime Movies', 'movies&url=imdbtul40', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('My favorite UNDERRATED movie gems', 'movies&url=imdbtul41', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Best of Croatian Cinema', 'movies&url=imdbtul42', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Best character study films', 'movies&url=imdbtul43', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Badass chicks/Girls with guns movies', 'movies&url=imdbtul44', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('French Action Cinema', 'movies&url=imdbtul45', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Italian Crime Films:Polizioteschi', 'movies&url=imdbtul46', 'imdb.png', 'imdb.png')
		self.addDirectoryItem('Shakespeare in Cinema', 'movies&url=imdbtul47', 'imdb.png', 'imdb.png')
		self.endDirectory()


    def tools(self):
        self.addDirectoryItem(32043, 'openSettings&query=0.0', 'tools.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32047, 'openSettings&query=3.0', 'tools.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32556, 'libraryNavigator', 'tools.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32049, 'viewsNavigator', 'tools.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32050, 'clearSources', 'tools.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32604, 'clearCacheSearch', 'tools.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32052, 'clearCache', 'tools.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32614, 'clearMetaCache', 'tools.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32613, 'clearAllCache', 'tools.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem('Pair Em',  'PairEm',  'tools.png',  'DefaultAddonProgram.png')
        self.addDirectoryItem(32073, 'authTrakt', 'trakt.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32609, 'urlResolver', 'urlresolver.png', 'DefaultAddonProgram.png')
        self.endDirectory()


    def devtools(self):
        self.addDirectoryItem('Test Movies(TMDB)', 'movies2&url=tmdbjewtestmovies', 'movies.png', 'DefaultMovies.png')
        self.addDirectoryItem('Test Shows(TMDB)', 'tvshows2&url=tmdbjewtestshows', 'tvshows.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32043, 'openSettings&query=0.0', 'tools.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32047, 'openSettings&query=3.0', 'tools.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32050, 'clearSources', 'tools.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32613, 'clearAllCache', 'tools.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32609, 'urlResolver', 'urlresolver.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem('[COLOR green]TurnOn RealDebridResolver[/COLOR]',  'TurnOnDbird', 'urlresolver.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem('[COLOR red]TurnOff RealDebridResolver[/COLOR]',  'TurnOffDbird',  'urlresolver.png',  'DefaultAddonProgram.png')
        self.addDirectoryItem('[COLOR green]TurnOn PremiumizeMeResolver[/COLOR]',  'TurnOnPreMe', 'urlresolver.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem('[COLOR red]TurnOff PremiumizeMeResolver[/COLOR]',  'TurnOffPreMe',  'urlresolver.png',  'DefaultAddonProgram.png')
        self.endDirectory()


    def library(self):
        self.addDirectoryItem(32557, 'openSettings&query=5.0', 'tools.png', 'DefaultAddonProgram.png')
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
        if control.yesnoDialog(control.lang(32056).encode('utf-8'), '', ''):
            control.setSetting('tvsearch', '')
            control.setSetting('moviesearch', '')
            control.refresh()

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

