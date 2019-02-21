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


import urllib

import config
import jsontools
from core import logger
import scrapertools

MAIN_URL = "http://api.tvalacarta.info/v2"
API_KEY = "nzgJy84P9w54H2w"
DEFAULT_HEADERS = [ ["User-Agent",config.PLUGIN_NAME+" "+config.get_platform()] ]

# ---------------------------------------------------------------------------------------------------------
#  Common function for API calls
# ---------------------------------------------------------------------------------------------------------

# Make a remote call using post, ensuring api key is here
def remote_call(url,parameters={},require_session=True):
    logger.info("url=" + url + ", parameters=" + repr(parameters))

    if not url.startswith("http"):
        url = MAIN_URL + "/" + url

    if not "api_key" in parameters:
        parameters["api_key"] = API_KEY

    # Add session token if not here
    #if not "s" in parameters and require_session:
    #    parameters["s"] = get_session_token()

    headers = DEFAULT_HEADERS
    post = urllib.urlencode(parameters)

    response_body = scrapertools.downloadpage(url,post,headers)

    return jsontools.load_json(response_body)

# ---------------------------------------------------------------------------------------------------------
#  Plugin service calls
# ---------------------------------------------------------------------------------------------------------

def plugins_get_all_packages():
    logger.info()

    parameters = { "plugin" : config.PLUGIN_NAME , "platform" : config.get_platform() }
    return remote_call( "plugins/get_all_packages.php" , parameters )

def plugins_get_latest_packages():
    logger.info()

    parameters = { "plugin" : config.PLUGIN_NAME , "platform" : config.get_platform() }
    return remote_call( "plugins/get_latest_packages.php" , parameters )
