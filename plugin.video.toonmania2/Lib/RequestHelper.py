# -*- coding: utf-8 -*-
import requests
from datetime import datetime

from xbmc import sleep

from Lib.SimpleCache import simpleCache as cache


# A requests helper class just for the Animetoon and Animeplus APIs.

class RequestHelper():

    URL_ANIMETOON_API = 'http://api.animetoon.tv'
    URL_ANIMETOON_IMAGES = 'http://www.animetoon.tv/images/series/small/' # Replace 'small' with 'big' to get larger thumbs.
    URL_ANIMETOON_SEARCH = 'http://www.animetoon.org/toon/search?key=%s'

    URL_ANIMEPLUS_API = 'http://api.animeplus.tv'
    URL_ANIMEPLUS_IMAGES = 'http://www.animeplus.tv/images/series/small/'
    URL_ANIMEPLUS_SEARCH = 'http://www.animeplus.tv/anime/search?key=%s'

    # API source constants, used with the setAPISource() function.
    API_ANIMETOON = '0'
    API_ANIMEPLUS = '1'

    # Persistent window properties holding the app versions obtained from
    # the '/GetVersion' API routes.
    PROPERTY_ANIMETOON_VERSION = 'rhelper.prop.toonVersion'
    PROPERTY_ANIMEPLUS_VERSION = 'rhelper.prop.plusVersion'
    
    # Stores a persistent random user-agent string, or empty if not used yet.
    # Used when name searching, it needs a desktop header for the website.
    PROPERTY_RANDOM_USERAGENT = 'rhelper.prop.randomUA'


    def __init__(self):
        self.animetoonHeaders = {
            'User-Agent': 'okhttp/2.3.0',
            'App-LandingPage': 'http://www.mobi24.net/toon.html',
            'App-Name': '#Toonmania',
            'App-Version': '8.0',
            'Accept': '*/*'
        }
        self.animeplusHeaders = {
            'User-Agent': 'okhttp/2.3.0',
            'App-LandingPage': 'http://www.mobi24.net/anime.html',
            'App-Name': '#Animania',
            'App-Version': '8.0',
            'Accept': '*/*'
        }        
        self.session = requests.Session()        
        self.checkAppVersions()


    def setAPISource(self, api):
        '''
        Called before doing requests to the app routes, it sets up the API URL
        which the route requests will go to, as well as search and thumb URLs.
        :param api: The API to change to, it's either RequestHelper.API_ANIMETOON
        or RequestHelper.API_ANIMEPLUS.
        '''
        if api == self.API_ANIMETOON:
            self.apiURL = self.URL_ANIMETOON_API
            self.imageURL = self.URL_ANIMETOON_IMAGES
            self.searchURL = self.URL_ANIMETOON_SEARCH
            self.session.headers.update(self.animetoonHeaders)
        else:
            self.apiURL = self.URL_ANIMEPLUS_API
            self.imageURL = self.URL_ANIMEPLUS_IMAGES
            self.searchURL = self.URL_ANIMEPLUS_SEARCH
            self.session.headers.update(self.animeplusHeaders)

            
    def checkAppVersions(self):
        '''
        Requests and caches the latest version from the apps.
        Probably avoids the 'Please update your app' reponse to route requests.

        On Kodi <= 17.6 this is called at every change of directory, so
        we cache the app version into persistent window memory properties.
        '''
        toonVersion = cache.getRawProperty(self.PROPERTY_ANIMETOON_VERSION)
        if not toonVersion:
            self.setAPISource(self.API_ANIMETOON)
            self.delayBegin()
            toonVersion = self.routeGET('/GetVersion').get('version', '8.0')
            self.delayEnd()
            cache.setRawProperty(self.PROPERTY_ANIMETOON_VERSION, toonVersion)
        self.animetoonHeaders.update({'App-Version': toonVersion})
        
        plusVersion = cache.getRawProperty(self.PROPERTY_ANIMEPLUS_VERSION)        
        if not plusVersion:
                self.setAPISource(self.API_ANIMEPLUS)
                self.delayBegin()
                plusVersion = self.routeGET('/GetVersion').get('version', '8.0')
                self.delayEnd()
                cache.setRawProperty(self.PROPERTY_ANIMEPLUS_VERSION, plusVersion)                
        self.animeplusHeaders.update({'App-Version': plusVersion})

        
    def setDesktopHeader(self):
        del self.session.headers['App-LandingPage'] # Delete these app header items, just for safety.
        del self.session.headers['App-Name']
        del self.session.headers['App-Version']
        self.session.headers.update(self.getRandomHeader())


    def GET(self, url):
        try:
            return self.session.get(url, timeout = 10)
        except:
            from xbmcgui import Dialog
            Dialog().notification('Toonmania2', 'Web request failed', xbmcgui.NOTIFICATION_INFO, 3000, True)
            class FakeResponse:
                ok = None             
            return FakeResponse # Just so other parts of the add-on don't break.


    def POST(self, url, data):
        '''
        This function is unused so far.
        '''
        return self.session.post(url, data = data, timeout = 10)


    def routeGET(self, routeURL):
        '''
        Convenience function to GET from a route path.
        Assumes 'routeURL' starts with a forward slash.
        
        :returns: The JSON of the response or None if it failed.
        '''
        r = self.GET(self.apiURL + routeURL)
        return r.json() if r.ok else None


    def searchGET(self, query):
        return self.GET(self.searchURL % query)


    def makeThumbURL(self, id):
        '''
        Returns the appropriate thumbnail image URL based on the current API.
        '''        
        return self.imageURL + str(id) + '.jpg' # 'imageURL' changes depending on the API set in setAPISource().


    def delayBegin(self):
        '''
        Called before a request or a code block that includes a request to
        grab the current time, used for some request delay logic for scraping.
        '''
        self.delayStartTime = datetime.now()


    def delayEnd(self, delayOverride = 200):
        '''
        Called after a request or a code block that included a request. This actually
        does the delay.        
        :param delayOverride: Custom delay time in milliseconds. Default: 200ms.
        '''
        elapsed = int((datetime.now() - self.delayStartTime).total_seconds() * 1000)
        if elapsed < delayOverride: # Only delay if we haven't waited the full time already.
            sleep(max(delayOverride - elapsed, 100))


    def getRandomHeader(self):
        '''
        Random user-agent logic, thanks to http://edmundmartin.com/random-user-agent-requests-python/
        
        :returns: A dictionary that is an incomplete desktop header, meant for updating self.session.headers.
        '''
        randomUA = cache.getRawProperty(self.PROPERTY_RANDOM_USERAGENT)
        if not randomUA:            
            from random import choice
            randomUA = choice(self._desktopUserAgents())
            cache.setRawProperty(self.PROPERTY_RANDOM_USERAGENT, randomUA)
        return {
            'User-Agent': randomUA,
            'Accept': 'text/html,application/xhtml+xml,application/xml,application/json;q=0.9,image/webp,*/*;q=0.8'
        }


    def _desktopUserAgents(self):
        desktop_agents = (
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14',
            'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
            'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'
        )
        return desktop_agents


requestHelper = RequestHelper()
