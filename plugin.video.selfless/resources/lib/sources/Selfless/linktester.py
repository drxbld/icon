# -*- coding: UTF-8 -*-
#######################################################################
 # ----------------------------------------------------------------------------
 # # -*- coding: UTF-8 -*-
'''
    A scraper for SelflessLive.

    Updated and refactored by someone.
    Originally created by others.
'''

 # ----------------------------------------------------------------------------
#######################################################################

# Addon Name: Selfless Live
# Addon id: plugin.video.selfless
# Addon Provider: Kodi Ghost

from resources.lib.modules import directstream

class source:
    def __init__(self):
        self.priority = 0
        self.language = ['en']
        self.domain = 'chillax.ws'
        self.base_link = 'http://chillax.ws'
        self.search_link = 'http://chillax.ws/search/auto?q='
        self.movie_link = "http://chillax.ws/movies/getMovieLink?"
        self.login_link = 'http://chillax.ws/session/loginajax'
        self.tv_link = 'http://chillax.ws/series/getTvLink?'
        self.login_payload = {'username': '', 'password': ''}

    def tvshow(self, imdb, tvdb, tvshowtitle, localtvshowtitle, aliases, year):
        url = []
        return url

    def episode(self, url, imdb, tvdb, title, premiered, season, episode):
        url = []
        return url

    def sources(self, url, hostDict, hostprDict):
        sources = []
        sources.append({'source': "openload", 'quality': "HD", 'language': "en",
                        'url': ' https://openload.co/f/IYt5Vk18WdE/Malcolm.in.the.Middle.S07E21.DVDRip.x264-TASTETV.mkv.mp4',
                        'info' : i['type'],
                        'direct': False, 'debridonly': False})
        return sources


    def resolve(self, url):
        if 'google' in url:
            return directstream.googlepass(url)
        else:
            return url