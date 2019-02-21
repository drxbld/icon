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



import json,urlparse

from resources.lib.stemodules import client


def getTrakt(url, post=None):
    try:
        url = urlparse.urljoin('http://api-v2launch.trakt.tv', url)

        headers = {'Content-Type': 'application/json', 'trakt-api-key': 'c029c80fd3d3a5284ee820ba1cf7f0221da8976b8ee5e6c4af714c22fc4f46fa', 'trakt-api-version': '2'}

        if not post == None: post = json.dumps(post)

        result = client.request(url, post=post, headers=headers)
        return result
    except:
        pass


def getMovieTranslation(id, lang):
    url = '/movies/%s/translations/%s' % (id, lang)
    try: return json.loads(getTrakt(url))[0]['title'].encode('utf-8')
    except: pass


def getTVShowTranslation(id, lang):
    url = '/shows/%s/translations/%s' % (id, lang)
    try: return json.loads(getTrakt(url))[0]['title'].encode('utf-8')
    except: pass


