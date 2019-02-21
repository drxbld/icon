# -*- coding: UTF-8 -*-
# -Cleaned and Checked on 11-23-2018 by JewBMX in Scrubs.

import re,urllib,urlparse
from resources.lib.modules import cleantitle,client


class source:
    def __init__(self):
        self.priority = 1
        self.language = ['fr']
        self.domains = ['cinemay.ws'] # Old cinemay.com
        self.base_link = 'https://cinemay.ws'
        self.key_link = '?'
        self.search_link = 's=%s'


    def movie(self, imdb, title, localtitle, aliases, year):
        try:
            url = {'imdb': imdb, 'title': title, 'localtitle': localtitle, 'year': year}
            url = urllib.urlencode(url)
            return url
        except:
            return


    def tvshow(self, imdb, tvdb, tvshowtitle, localtvshowtitle, aliases, year):
        try:
            url = {'imdb': imdb, 'tvdb': tvdb, 'tvshowtitle': tvshowtitle, 'localtvshowtitle': localtvshowtitle, 'year': year}
            url = urllib.urlencode(url)
            return url
        except:
            return


    def episode(self, url, imdb, tvdb, title, premiered, season, episode):
        try:
            if url == None: return
            url = urlparse.parse_qs(url)
            url = dict([(i, url[i][0]) if url[i] else (i, '') for i in url])
            url['title'], url['premiered'], url['season'], url['episode'] = title, premiered, season, episode
            url = urllib.urlencode(url)
            return url
        except:
            return


    def sources(self, url, hostDict, hostprDict):
        try:
            print '-------------------------------    -------------------------------'
            sources = []
            print url
            data = urlparse.parse_qs(url)
            data = dict([(i, data[i][0]) if data[i] else (i, '') for i in data])
            print data
            title = data['title']
            year = data['year'] if 'year' in data else data['year']
            season = data['season'] if 'season' in data else False
            episode = data['episode'] if 'episode' in data else False
            localtitle = data['localtitle'] if 'localtitle' in data else False
            if season and episode:
                localtitle = data['localtvshowtitle'] if 'localtvshowtitle' in data else False
            t = cleantitle.get(title)
            tq = cleantitle.query(localtitle)
            tq2 =  re.sub(' ', '', cleantitle.query(localtitle).lower())
            tq = re.sub(' ', '%20', tq)
            y = ['%s' % str(year), '%s' % str(int(year) + 1), '%s' % str(int(year) - 1), '0']
            query = 'https://cinemay.ws'
            r = client.request('https://cinemay.ws/?s=%s' % tq)
            print 'https://cinemay.ws/?s=%s' % tq
            r = client.parseDOM(r, 'div', attrs={'class': 'unfilm'})
            r = [(client.parseDOM(i, 'a', ret='href'), client.parseDOM(i, 'a', ret='title')) for i in r]
            r = [(i[0][0], re.sub('(film| en streaming vf| en streaming vostfr|&rsquo;| )', '', i[1][0]).lower()) for i in r if len(i[0]) > 0 and len(i[1]) > 0]
            r = [(i[0], i[1], re.findall('(.+?) \(*(\d{4})', i[1])) for i in r]
            r = [(i[0], i[2][0][0] if len(i[2]) > 0 else i[1], i[2][0][1] if len(i[2]) > 0 else '0') for i in r]
            r = [(i[0], i[1], i[2], re.findall('(.+?)\s+(?:saison|s)\s+(\d+)', i[1])) for i in r]
            r = [(i[0], i[3][0][0] if len(i[3]) > 0 else i[1], i[2], i[3][0][1] if len(i[3]) > 0 else '0') for i in r]
            r = [(i[0], re.sub(' \&\#[0-9]{4,6};', '', i[1]), i[2], i[3]) for i in r]
            r = [i[0] for i in r if tq2 == cleantitle.get(i[1])][0]
            url = re.findall('(?://.+?|)(/.+)', r)[0]
            url = client.replaceHTMLCodes(url)
            url = url.encode('utf-8')
            r = client.request('https://cinemay.ws' + url)
            print 'https://cinemay.ws' + url
            r = client.parseDOM(r, 'div', attrs={'class': 'module-actionbar'})
            r = client.parseDOM(r, 'a', ret='href')
            for i in r:
                if i =='#':
                    continue
                url = client.request('https://cinemay.ws' + i)
                url = client.parseDOM(url, 'div', attrs={'class': 'wbox2 video dark'})
                url = client.parseDOM(url, 'iframe', ret='src')[0]
                host = re.findall('([\w]+[.][\w]+)$', urlparse.urlparse(url.strip().lower()).netloc)[0]
                if not host in hostDict: continue
                host = client.replaceHTMLCodes(host)
                host = host.encode('utf-8')
                sources.append({'source': host, 'quality': 'SD', 'language': 'FR', 'url': url, 'direct': False, 'debridonly': False})
            return sources
        except:
            return sources


    def resolve(self, url):
        return url

