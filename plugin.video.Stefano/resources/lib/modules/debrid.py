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



from resources.lib.modules import log_utils

try:
    import resolveurl

    debrid_resolvers = [resolver() for resolver in resolveurl.relevant_resolvers(order_matters=True) if resolver.isUniversal()]

    if len(debrid_resolvers) == 0:
        # Support Rapidgator accounts! Unfortunately, `sources.py` assumes that rapidgator.net is only ever
        # accessed via a debrid service, so we add rapidgator as a debrid resolver and everything just works.
        # As a bonus(?), rapidgator links will be highlighted just like actual debrid links
        debrid_resolvers = [resolver() for resolver in resolveurl.relevant_resolvers(order_matters=True,include_universal=False) if 'rapidgator.net' in resolver.domains]

except:
    debrid_resolvers = []


def status():
    return debrid_resolvers != []


def resolver(url, debrid):
    try:
        debrid_resolver = [resolver for resolver in debrid_resolvers if resolver.name == debrid][0]

        debrid_resolver.login()
        _host, _media_id = debrid_resolver.get_host_and_id(url)
        stream_url = debrid_resolver.get_media_url(_host, _media_id)

        return stream_url
    except Exception as e:
        log_utils.log('%s Resolve Failure: %s' % (debrid, e), log_utils.LOGWARNING)
        return None
