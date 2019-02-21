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

import requests.sessions
from BeautifulSoup import BeautifulSoup

def get_source_info(url):
    source_info = {}
    if 'thevideo' in url:
        source_info['source'] = 'thevideo.me'
        with requests.session() as s:
            p = s.get(url)
            soup = BeautifulSoup(p.text, 'html.parser')
            title = soup.findAll('script', src=False, type=False)
            for i in title:
                if "title" in i.prettify():
                    for line in i.prettify().split('\n'):
                        if " title" in line:
                            line = line.replace("title: '", '').replace("',", '')
                            if "720" in line:
                                source_info['qual'] = "720p"
                            elif "1080" in line:
                                source_info['qual'] = "1080p"
                            else:
                                source_info['qual'] = "SD"
        return source_info
    elif 'vidzi' in url:
        #Not completed
        return "SD"