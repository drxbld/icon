# -*- coding: UTF-8 -*-
#######################################################################
 # ----------------------------------------------------------------------------
 # "THE BEER-WARE LICENSE" (Revision 42):
 # @Daddy_Blamo wrote this file.  As long as you retain this notice you
 # can do whatever you want with this stuff. If we meet some day, and you think
 # this stuff is worth it, you can buy me a beer in return. - Muad'Dib
 # ----------------------------------------------------------------------------
#######################################################################

# Addon Name: Exodus
# Addon id: plugin.video.exodus
# Addon Provider: Exodus

import re
import urllib
import urlparse

from resources.lib.modules import cleantitle
from resources.lib.modules import client
from resources.lib.modules import source_utils
from resources.lib.modules import dom_parser


class source:
    def __init__(self):
        self.priority = 1
        self.language = ['de']
        self.domains = ['kinoking.to']
        self.base_link = 'https://kinoking.to'
        self.search_link = '/?s=%s'
        self.get_link = '/links/%s'

    def movie(self, imdb, title, localtitle, aliases, year):        
        try:
            url = self.__search([localtitle] + source_utils.aliases_to_array(aliases))
            if not url and title != localtitle: url = self.__search([title] + source_utils.aliases_to_array(aliases))
            return url
        except:
            return

    def tvshow(self, imdb, tvdb, tvshowtitle, localtvshowtitle, aliases, year):
        try:
            url = self.__search([localtvshowtitle] + source_utils.aliases_to_array(aliases))
            if not url and tvshowtitle != localtvshowtitle: url = self.__search([tvshowtitle] + source_utils.aliases_to_array(aliases))
            return url
        except:
            return

    def episode(self, url, imdb, tvdb, title, premiered, season, episode):
        try:
            if not url:
                return

            s = '-%sx%s/' % (season, episode)

            url = url.rstrip('/')
            url = url + s
            url = urlparse.urljoin(self.base_link, url)

            return url
        except:
            return

    def sources(self, url, hostDict, hostprDict):        
        sources = []

        try:
            if not url:
                return sources

            query = urlparse.urljoin(self.base_link, url)

            r = client.request(query)

            r = dom_parser.parse_dom(r, 'div', attrs={'id': 'downloads'})
            r = dom_parser.parse_dom(r, 'table')
            r = dom_parser.parse_dom(r, 'tbody')
            r = dom_parser.parse_dom(r, 'tr')

            for i in r:

                if re.search('German', i[1]):

                    hoster = re.search('(?<=domain=)(.*?)(?=\")', i[1])
                    hoster = hoster.group().lower()

                    valid, hoster = source_utils.is_host_valid(hoster, hostDict)
                    if not valid: continue

                    link = re.search('(?<=links/)(.*?)(?=/)', i[1])
                    link = link.group()

                    if re.search('<td>HD</td>', i[1]):
                        quality = 'HD'
                    else:
                        quality = 'SD'

                    url = self.__get_link(link)

                    sources.append({'source': hoster, 'quality': quality, 'language': 'de', 'url': url, 'direct': False, 'debridonly': False})

            return sources
        except:
            return sources

    def resolve(self, url):
        return url

    def __search(self, titles):        
        try:
            query = self.search_link % (urllib.quote_plus(cleantitle.query(titles[0])))
            query = urlparse.urljoin(self.base_link, query)

            t = [cleantitle.get(i) for i in set(titles) if i]

            r = client.request(query)

            r = dom_parser.parse_dom(r, 'article')
            r = dom_parser.parse_dom(r, 'div', attrs={'class': 'title'})
            r = dom_parser.parse_dom(r, 'a', req='href')

            for i in r:
                title = client.replaceHTMLCodes(r[0][1])
                title = cleantitle.get(title)

                if title in t:
                    return source_utils.strip_domain(i[0]['href'])
            
            return
        except:
            return

    def __get_link(self, link):
        try:
            if not link:
                return

            query = self.get_link % link
            query = urlparse.urljoin(self.base_link, query)

            r = client.request(query)

            r = dom_parser.parse_dom(r, 'div', attrs={'class': 'boton'})
            r = dom_parser.parse_dom(r, 'a', req='href')
            r = r[0].attrs['href']

            return r
        except:
            return