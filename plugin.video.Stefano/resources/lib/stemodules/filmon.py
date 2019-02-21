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




import re,urlparse,json
from resources.lib.stemodules import client

def resolve(url):
    try:
        if '/vod/' in url:
            url = re.compile('/(\d+)').findall(url)[-1]
            url = 'http://www.filmon.com/vod/info/%s' % url
        elif '/tv/' in url:
            url = url.replace('/tv/', '/channel/')
        elif not '/channel/' in url:
            raise Exception()


        headers = {'X-Requested-With': 'XMLHttpRequest'}

        cookie = client.request(url, output='cookie')

        cid = client.request(url, headers=headers)
        cid = json.loads(cid)['id']
        

        headers = {'X-Requested-With': 'XMLHttpRequest', 'Referer': url}

        url = 'http://www.filmon.com/ajax/getChannelInfo?channel_id=%s' % cid

        result = client.request(url, cookie=cookie, headers=headers)

        result = json.loads(result)
        try:
            result = result['streams']
        except:
            result = result['data']['streams']
            result = [i[1] for i in result.items()]

        url = [(i['url'], int(i['watch-timeout'])) for i in result]
        url = [i for i in url if '.m3u8' in i[0]]
        
        url.sort()
        url = url[-1][0]

        return url
    except:
        return

