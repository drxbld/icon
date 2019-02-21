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
#------------------------------------------------------------



import urllib,json

from resources.lib.stemodules import cache
from resources.lib.stemodules import client


class tvMaze:
    def __init__(self, show_id = None):
        self.api_url = 'http://api.tvmaze.com/%s%s'
        self.show_id = show_id


    def showID(self, show_id = None):
        if (show_id != None):
            self.show_id = show_id
            return show_id

        return self.show_id


    def request(self, endpoint, query = None):
        try:
            # Encode the queries, if there is any...
            if (query != None):
                query = '?' + urllib.urlencode(query)
            else:
                query = ''

            # Make the request
            request = self.api_url % (endpoint, query)

            # Send the request and get the response
            # Get the results from cache if available
            response = cache.get(client.request, 24, request)

            # Retrun the result as a dictionary
            return json.loads(response)
        except:
            pass

        return {}


    def showLookup(self, type, id):
        try:
            result = self.request('lookup/shows', {type: id})

            # Storing the show id locally
            if ('id' in result):
                self.show_id = result['id']

            return result
        except:
            pass

        return {}


    def shows(self, show_id = None, embed = None):
        try:
            if (not self.showID(show_id)):
                raise Exception()

            result = self.request('shows/%d' % self.show_id)

            # Storing the show id locally
            if ('id' in result):
                self.show_id = result['id']

            return result
        except:
            pass

        return {}


    def showSeasons(self, show_id = None):
        try:
            if (not self.showID(show_id)):
                raise Exception()

            result = self.request('shows/%d/seasons' % int( self.show_id ))

            if (len(result) > 0 and 'id' in result[0]):
                return result
        except:
            pass

        return []


    def showSeasonList(self, show_id):
        return {}


    def showEpisodeList(self, show_id = None, specials = False):
        try:
            if (not self.showID(show_id)):
                raise Exception()

            result = self.request('shows/%d/episodes' % int( self.show_id ), 'specials=1' if specials else '')

            if (len(result) > 0 and 'id' in result[0]):
                return result
        except:
            pass

        return []


    def episodeAbsoluteNumber(self, thetvdb, season, episode):
        try:
            url = 'http://thetvdb.com/api/%s/series/%s/default/%01d/%01d' % ('MUQ2MkYyRjkwMDMwQzQ0NA=='.decode('base64'), thetvdb, int(season), int(episode))
            r = client.request(url)
            episode = client.parseDOM(r, 'absolute_number')[0]

            return int( episode )
        except:
            pass

        return episode


