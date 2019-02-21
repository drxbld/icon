# ------------------------------------------------------------
# -*- coding: utf-8 -*-
# ------------------------------------------------------------
# Stefano Thegroove 360
# Copyright 2018 https://stefanoaddon.info
#
# Distribuito sotto i termini di GNU General Public License v3 (GPLv3)
# http://www.gnu.org/licenses/gpl-3.0.html
# ------------------------------------------------- -----------
# Questo file fa parte di Stefano Thegroove 360.
#
# Stefano Thegroove 360 ​​è un software gratuito: puoi ridistribuirlo e / o modificarlo
# è sotto i termini della GNU General Public License come pubblicata da
# la Free Software Foundation, o la versione 3 della licenza, o
# (a tua scelta) qualsiasi versione successiva.
#
# Stefano Thegroove 360 ​​è distribuito nella speranza che possa essere utile,
# ma SENZA ALCUNA GARANZIA; senza nemmeno la garanzia implicita di
# COMMERCIABILITÀ o IDONEITÀ PER UN PARTICOLARE SCOPO. Vedere il
# GNU General Public License per maggiori dettagli.
#
# Dovresti aver ricevuto una copia della GNU General Public License
# insieme a Stefano Thegroove 360. In caso contrario, vedi <http://www.gnu.org/licenses/>.
# ------------------------------------------------- -----------
# Client for Stefano Thegroove 360
# ------------------------------------------------------------


import os
import sys
import urllib
import urllib2
import urlparse
from HTMLParser import HTMLParser

import xbmc
import xbmcaddon
import xbmcgui

from core import config, logger
from core.item import Item
from platformcode import launcher

logger.info("init...")

__addon__ = xbmcaddon.Addon()
__addonname__ = __addon__.getAddonInfo('name')

librerias = xbmc.translatePath(os.path.join(config.get_runtime_path(), 'lib'))
sys.path.append(librerias)

item = None
params = dict(urlparse.parse_qsl(sys.argv[2].replace('?', '')))

action = params.get('action')

if action == "serverdir":
    unparams = sys.argv[2].encode('utf-8').replace('?', '')
    unparams = urllib2.unquote(unparams).decode('utf-8')
    unparams = HTMLParser().unescape(unparams).encode('utf-8')
    params = dict(urlparse.parse_qsl(unparams))

if action is None and params.get('params'):
    p = eval(params.get('params'))
    action = p.get('action')

if action is None:
    item = Item().fromurl(sys.argv[2])
    if type(item) is Item and item.action != "":
        action = "sod"

subid = params.get('subid')

docu_category = params.get('docuCat')

docu_watch = params.get('docuPlay')

podcast_show = params.get('podcastshow')

podcast_cat = params.get('podcastlist')

podcast_cats = params.get('podcastcategories')

podcast_episode = params.get('podcastepisode')

name = params.get('name')

title = params.get('title')

year = params.get('year')

imdb = params.get('imdb')

tvdb = params.get('tvdb')

tmdb = params.get('tmdb')

season = params.get('season')

episode = params.get('episode')

tvshowtitle = params.get('tvshowtitle')

premiered = params.get('premiered')

url = params.get('url')

image = params.get('image')

meta = params.get('meta')

select = params.get('select')

query = params.get('query')

source = params.get('source')

content = params.get('content')

if action is None:
    from resources.lib.indexers import thegroove360_ext

    thegroove360_ext.indexer_ext().updatecheck(title)


elif action == 'serverdir':
    from resources.lib.indexers import thegroove360_ext

    thegroove360_ext.indexer_ext().getServer(url)

elif action == 'directory':
    custom_ua = False
    parts = url.split("|")

    if len(parts) > 1:
        url = parts[0]
        custom_ua = parts[1] == 'custom_ua'

    from resources.lib.indexers import thegroove360_ext

    thegroove360_ext.indexer_ext().get(url, custom_ua)

elif action == 'qdirectory':
    from resources.lib.indexers import thegroove360_ext

    thegroove360_ext.indexer_ext().getq(url)

elif action == 'xdirectory':
    from resources.lib.indexers import thegroove360_ext

    thegroove360_ext.indexer_ext().getx(url)

elif action == 'developer':
    from resources.lib.indexers import thegroove360_ext

    thegroove360_ext.indexer_ext().developer()

elif action == "adult":
    kb = xbmc.Keyboard('', 'Enter Your Password', True)
    kb.doModal()
    if kb.isConfirmed():
        pw = kb.getText()

        import hashlib

        hashpw = hashlib.sha256(pw).hexdigest()
        hashed = "7fde5144eba56d1a85e0b5ff9d5946fb65812022ee610be341e4561519497ef6"

        if hashed == hashpw:
            from resources.lib.stemodules import regex
            from resources.lib.indexers import thegroove360_ext

            regex.clear()
            thegroove360_ext.indexer_ext().getServer('xxx')
        else:
            xbmcgui.Dialog().ok('[COLOR red][B]Stefano Addon Area Adulti Sezione[/B][/COLOR]',
                                'Incorrect Password, Please Try Again')


elif action == 'rsi':
    from resources.lib.indexers import thegroove360_ext

    thegroove360_ext.indexer_ext().rsilist(subid, url, title)

elif action == 'tap':
    from resources.lib.indexers import thegroove360_ext

    thegroove360_ext.indexer_ext().taplist_channels(cat_id=subid)

elif action == 'taplay':
    from resources.lib.indexers import thegroove360_ext

    thegroove360_ext.indexer_ext().taplay(ch_id=subid)

elif action == 'sport365a':
    execfile(os.path.dirname(os.path.realpath(__file__)) + os.sep + 'main.py')

elif action == 'sod':
    launcher.start()
    if item is Item:
        launcher.run(item)
    else:
        launcher.run()

elif action == 'tvtuner':
    from resources.lib.indexers import thegroove360_ext

    thegroove360_ext.indexer_ext().tvtuner(url)

elif 'youtube' in str(action):
    from resources.lib.indexers import thegroove360_ext

    thegroove360_ext.indexer_ext().youtube(url, action)

elif action == 'play3':
    from resources.lib.indexers import thegroove360_ext

    thegroove360_ext.player().play3(url, content)

elif action == 'browser':
    from resources.lib.indexers import thegroove360

    thegroove360.resolver().browser(url)

elif action == 'search':
    from resources.lib.indexers import thegroove360_ext

    thegroove360_ext.indexer_ext().search(url=None)

elif action == 'addSearch':
    from resources.lib.indexers import thegroove360_ext

    thegroove360_ext.indexer_ext().addSearch(url)

elif action == 'delSearch':
    from resources.lib.indexers import thegroove360_ext

    thegroove360_ext.indexer_ext().delSearch()

elif action == 'queueItem':
    from resources.lib.modules import control

    control.queueItem()

elif action == 'urlresolverSettings':
    from resources.lib.modules import control

    control.openSettings(id='script.module.urlresolver')

elif action == 'addView1':
    from resources.lib.stemodules import views

    views.addView1(content)

elif action == 'downloader1':
    from resources.lib.stemodules import downloader

    downloader.downloader1()

elif action == 'addDownload':
    from resources.lib.stemodules import downloader

    downloader.addDownload(name, url, image)

elif action == 'removeDownload':
    from resources.lib.stemodules import downloader

    downloader.removeDownload(url)

elif action == 'startDownload':
    from resources.lib.stemodules import downloader

    downloader.startDownload()

elif action == 'startDownloadThread':
    from resources.lib.stemodules import downloader

    downloader.startDownloadThread()

elif action == 'stopDownload':
    from resources.lib.stemodules import downloader

    downloader.stopDownload()

elif action == 'statusDownload':
    from resources.lib.stemodules import downloader

    downloader.statusDownload()

elif action == 'clearCache1':
    from resources.lib.stemodules import cache

    cache.clear()

elif action == 'radios':
    from resources.lib.indexers import phradios

    phradios.radios()

elif action == 'radioResolve':
    from resources.lib.indexers import phradios

    phradios.radioResolve(url)

elif action == 'radio1fm':
    from resources.lib.indexers import phradios

    phradios.radio1fm()

elif action == 'radio181fm':
    from resources.lib.indexers import phradios

    phradios.radio181fm()

elif action == 'radiocast':
    from resources.lib.indexers import phradios

    phradios.kickinradio()

elif action == 'kickinradiocats':
    from resources.lib.indexers import phradios

    phradios.kickinradiocats(url)

elif action == 'home':
    from resources.lib.indexers import navigator
    from resources.lib.modules import cache

    cache.cache_version_check()
    navigator.navigator().root()

elif action == 'newsNavigator':
    from resources.lib.indexers import navigator

    navigator.navigator().news()

elif action == 'movieNavigator':
    from resources.lib.indexers import navigator

    navigator.navigator().movies()

elif action == 'movieliteNavigator':
    from resources.lib.indexers import navigator

    navigator.navigator().movies(lite=True)

elif action == 'mymovieNavigator':
    from resources.lib.indexers import navigator

    navigator.navigator().mymovies()

elif action == 'mymovieliteNavigator':
    from resources.lib.indexers import navigator

    navigator.navigator().mymovies(lite=True)

elif action == 'tvNavigator':
    from resources.lib.indexers import navigator

    navigator.navigator().tvshows()

elif action == 'tvliteNavigator':
    from resources.lib.indexers import navigator

    navigator.navigator().tvshows(lite=True)

elif action == 'mytvNavigator':
    from resources.lib.indexers import navigator

    navigator.navigator().mytvshows()

elif action == 'mytvliteNavigator':
    from resources.lib.indexers import navigator

    navigator.navigator().mytvshows(lite=True)

elif action == 'downloadNavigator':
    from resources.lib.indexers import navigator

    navigator.navigator().downloads()

elif action == 'libraryNavigator':
    from resources.lib.indexers import navigator

    navigator.navigator().library()

elif action == 'toolNavigator':
    from resources.lib.indexers import navigator

    navigator.navigator().tools()

elif action == 'searchNavigator':
    from resources.lib.indexers import navigator

    navigator.navigator().search()

elif action == 'viewsNavigator':
    from resources.lib.indexers import navigator

    navigator.navigator().views()

elif action == 'clearCache':
    from resources.lib.indexers import navigator

    navigator.navigator().clearCache()

elif action == 'clearCacheSearch':
    from resources.lib.indexers import navigator

    navigator.navigator().clearCacheSearch()

elif action == 'clearAllCache':
    from resources.lib.indexers import navigator

    navigator.navigator().clearCacheAll()

elif action == 'clearMetaCache':
    from resources.lib.indexers import navigator

    navigator.navigator().clearCacheMeta()

elif action == 'infoCheck':
    from resources.lib.indexers import navigator

    navigator.navigator().infoCheck('')

elif action == 'movies':
    from resources.lib.indexers import movies

    movies.movies().get(url)

elif action == 'moviePage':
    from resources.lib.indexers import movies

    movies.movies().get(url)

elif action == 'movieWidget':
    from resources.lib.indexers import movies

    movies.movies().widget()

elif action == 'movieSearch':
    from resources.lib.indexers import movies

    movies.movies().search()

elif action == 'movieSearchnew':
    from resources.lib.indexers import movies

    movies.movies().search_new()

elif action == 'movieSearchterm':
    from resources.lib.indexers import movies

    movies.movies().search_term(name)

elif action == 'moviePerson':
    from resources.lib.indexers import movies

    movies.movies().person()

elif action == 'movieGenres':
    from resources.lib.indexers import movies

    movies.movies().genres()

elif action == 'movieLanguages':
    from resources.lib.indexers import movies

    movies.movies().languages()

elif action == 'movieCertificates':
    from resources.lib.indexers import movies

    movies.movies().certifications()

elif action == 'movieYears':
    from resources.lib.indexers import movies

    movies.movies().years()

elif action == 'moviePersons':
    from resources.lib.indexers import movies

    movies.movies().persons(url)

elif action == 'movieUserlists':
    from resources.lib.indexers import movies

    movies.movies().userlists()

elif action == 'channels':
    from resources.lib.indexers import channels

    channels.channels().get()

elif action == 'tvshows':
    from resources.lib.indexers import tvshows

    tvshows.tvshows().get(url)

elif action == 'tvshowPage':
    from resources.lib.indexers import tvshows

    tvshows.tvshows().get(url)

elif action == 'tvSearch':
    from resources.lib.indexers import tvshows

    tvshows.tvshows().search()

elif action == 'tvSearchnew':
    from resources.lib.indexers import tvshows

    tvshows.tvshows().search_new()

elif action == 'tvSearchterm':
    from resources.lib.indexers import tvshows

    tvshows.tvshows().search_term(name)

elif action == 'tvPerson':
    from resources.lib.indexers import tvshows

    tvshows.tvshows().person()

elif action == 'tvGenres':
    from resources.lib.indexers import tvshows

    tvshows.tvshows().genres()

elif action == 'tvReviews':
    from resources.lib.indexers import youtube

    if subid is None:
        youtube.yt_index().root(action)
    else:
        youtube.yt_index().get(action, subid)

elif action == 'movieReviews':
    from resources.lib.indexers import youtube

    if subid is None:
        youtube.yt_index().root(action)
    else:
        youtube.yt_index().get(action, subid)

elif action == 'tvNetworks':
    from resources.lib.indexers import tvshows

    tvshows.tvshows().networks()

elif action == 'tvLanguages':
    from resources.lib.indexers import tvshows

    tvshows.tvshows().languages()

elif action == 'tvCertificates':
    from resources.lib.indexers import tvshows

    tvshows.tvshows().certifications()

elif action == 'tvPersons':
    from resources.lib.indexers import tvshows

    tvshows.tvshows().persons(url)

elif action == 'tvUserlists':
    from resources.lib.indexers import tvshows

    tvshows.tvshows().userlists()

elif action == 'seasons':
    from resources.lib.indexers import episodes

    episodes.seasons().get(tvshowtitle, year, imdb, tvdb)

elif action == 'episodes':
    from resources.lib.indexers import episodes

    episodes.episodes().get(tvshowtitle, year, imdb, tvdb, season, episode)

elif action == 'calendar':
    from resources.lib.indexers import episodes

    episodes.episodes().calendar(url)

elif action == 'tvWidget':
    from resources.lib.indexers import episodes

    episodes.episodes().widget()

elif action == 'calendars':
    from resources.lib.indexers import episodes

    episodes.episodes().calendars()

elif action == 'episodeUserlists':
    from resources.lib.indexers import episodes

    episodes.episodes().userlists()

elif action == 'refresh':
    from resources.lib.modules import control

    control.refresh()

elif action == 'queueItem':
    from resources.lib.modules import control

    control.queueItem()

elif action == 'openSettings':
    from resources.lib.modules import control

    control.openSettings(query)

elif action == 'artwork':
    from resources.lib.modules import control

    control.artwork()

elif action == 'addView':
    from resources.lib.modules import views

    views.addView(content)

elif action == 'moviePlaycount':
    from resources.lib.modules import playcount

    playcount.movies(imdb, query)

elif action == 'episodePlaycount':
    from resources.lib.modules import playcount

    playcount.episodes(imdb, tvdb, season, episode, query)

elif action == 'tvPlaycount':
    from resources.lib.modules import playcount

    playcount.tvshows(name, imdb, tvdb, season, query)

elif action == 'trailer':
    from resources.lib.modules import trailer

    trailer.trailer().play(name, url)

elif action == 'traktManager':
    from resources.lib.modules import trakt

    trakt.manager(name, imdb, tvdb, content)

elif action == 'authTrakt':
    from resources.lib.modules import trakt

    trakt.authTrakt()

elif action == 'urlResolver':
    try:
        import resolveurl
    except:
        pass
    resolveurl.display_settings()

elif action == 'download':
    import json
    from resources.lib.modules import sources
    from resources.lib.modules import downloader

    try:
        downloader.download(name, image, sources.sources().sourcesResolve(json.loads(source)[0], True))
    except:
        pass

elif action == 'kidscorner':
    from resources.lib.indexers import youtube

    if subid is None:
        youtube.yt_index().root(action)
    else:
        youtube.yt_index().get(action, subid)

elif action == 'fitness':
    from resources.lib.indexers import youtube

    if subid is None:
        youtube.yt_index().root(action)
    else:
        youtube.yt_index().get(action, subid)

elif action == 'legends':
    from resources.lib.indexers import youtube

    if subid is None:
        youtube.yt_index().root(action)
    else:
        youtube.yt_index().get(action, subid)

elif action == 'podcastNavigator':
    from resources.lib.indexers import podcast

    podcast.podcast().root()

elif action == 'podcastOne':
    from resources.lib.indexers import podcast

    if podcast_show is not None:
        podcast.podcast().pco_show(podcast_show)
    elif podcast_cat is not None:
        podcast.podcast().pco_cat(podcast_cat)
    elif podcast_cats is not None:
        podcast.podcast().pcocats_list()
    elif podcast_episode is not None:
        podcast.podcast().podcast_play(action, podcast_episode)
    else:
        podcast.podcast().pco_root()

elif action == 'docuHeaven':
    from resources.lib.indexers import docu

    if docu_category is not None:
        docu.documentary().docu_list(docu_category)
    elif docu_watch is not None:
        docu.documentary().docu_play(docu_watch)
    else:
        docu.documentary().root()

elif action == 'podbay':
    from resources.lib.indexers import podcast

    if podcast_show is not None:
        podcast.podcast().pb_show(podcast_show)
    elif podcast_cat is not None:
        podcast.podcast().pb_cat(podcast_cat)
    elif podcast_cats is not None:
        podcast.podcast().pb_root()
    elif podcast_episode is not None:
        podcast.podcast().podcast_play(action, podcast_episode)
    else:
        podcast.podcast().pb_root()

elif action == 'sectionItem':
    pass  # Placeholder. This is a non-clickable menu item for notes, etc.

elif action == 'play':
    from resources.lib.modules import sources

    sources.sources().play(title, year, imdb, tvdb, season, episode, tvshowtitle, premiered, meta, select)

elif action == 'addItem':
    from resources.lib.modules import sources

    sources.sources().addItem(title)

elif action == 'playItem':
    from resources.lib.modules import sources

    sources.sources().playItem(title, source)

elif action == 'alterSources':
    from resources.lib.modules import sources

    sources.sources().alterSources(url, meta)

elif action == 'clearSources':
    from resources.lib.modules import sources

    sources.sources().clearSources()

elif action == 'random':
    rtype = params.get('rtype')
    rlist = None
    r = None
    if rtype == 'movie':
        from resources.lib.indexers import movies

        rlist = movies.movies().get(url, create_directory=False)
        r = sys.argv[0] + "?action=play"
    elif rtype == 'episode':
        from resources.lib.indexers import episodes

        rlist = episodes.episodes().get(tvshowtitle, year, imdb, tvdb, season, create_directory=False)
        r = sys.argv[0] + "?action=play"
    elif rtype == 'season':
        from resources.lib.indexers import episodes

        rlist = episodes.seasons().get(tvshowtitle, year, imdb, tvdb, create_directory=False)
        r = sys.argv[0] + "?action=random&rtype=episode"
    elif rtype == 'show':
        from resources.lib.indexers import tvshows

        rlist = tvshows.tvshows().get(url, create_directory=False)
        r = sys.argv[0] + "?action=random&rtype=season"
    from resources.lib.modules import control
    from random import randint
    import json

    try:
        rand = randint(1, len(rlist)) - 1
        for p in ['title', 'year', 'imdb', 'tvdb', 'season', 'episode', 'tvshowtitle', 'premiered', 'select']:
            if rtype == "show" and p == "tvshowtitle":
                try:
                    r += '&' + p + '=' + urllib.quote_plus(rlist[rand]['title'])
                except:
                    pass
            else:
                try:
                    r += '&' + p + '=' + urllib.quote_plus(rlist[rand][p])
                except:
                    pass
        try:
            r += '&meta=' + urllib.quote_plus(json.dumps(rlist[rand]))
        except:
            r += '&meta=' + urllib.quote_plus("{}")
        if rtype == "movie":
            try:
                control.infoDialog(rlist[rand]['title'], control.lang(32536).encode('utf-8'), time=30000)
            except:
                pass
        elif rtype == "episode":
            try:
                control.infoDialog(
                    rlist[rand]['tvshowtitle'] + " - Season " + rlist[rand]['season'] + " - " + rlist[rand]['title'],
                    control.lang(32536).encode('utf-8'), time=30000)
            except:
                pass
        control.execute('RunPlugin(%s)' % r)
    except:
        control.infoDialog(control.lang(32537).encode('utf-8'), time=8000)

elif action == 'movieToLibrary':
    from resources.lib.modules import libtools

    libtools.libmovies().add(name, title, year, imdb, tmdb)

elif action == 'moviesToLibrary':
    from resources.lib.modules import libtools

    libtools.libmovies().range(url)

elif action == 'tvshowToLibrary':
    from resources.lib.modules import libtools

    libtools.libtvshows().add(tvshowtitle, year, imdb, tvdb)

elif action == 'tvshowsToLibrary':
    from resources.lib.modules import libtools

    libtools.libtvshows().range(url)

elif action == 'updateLibrary':
    from resources.lib.modules import libtools

    libtools.libepisodes().update(query)

elif action == 'service':
    from resources.lib.modules import libtools

    libtools.libepisodes().service()

else:
    if 'search' in action:
        url = action.split('search=')[1]
        url = url + '|SECTION|'
        from resources.lib.indexers import thegroove360_ext

        thegroove360_ext.indexer_ext().search(url)
    else:
        quit()
