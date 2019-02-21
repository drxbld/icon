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


import os

import config
import scrapertools


def get_current_plugin_version():
    return 4204


def get_current_plugin_version_tag():
    return "4.2.0-final"


def get_current_plugin_date():
    return "30/04/2017"


def get_current_channels_version():
    f = open(os.path.join(config.get_runtime_path(), "channels", "version.xml"))
    data = f.read()
    f.close()

    return int(scrapertools.find_single_match(data, "<version>([^<]+)</version>"))


def get_current_servers_version():
    f = open(os.path.join(config.get_runtime_path(), "servers", "version.xml"))
    data = f.read()
    f.close()

    return int(scrapertools.find_single_match(data, "<version>([^<]+)</version>"))
