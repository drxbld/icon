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


import glob
import os
import threading
from threading import Thread

from core import config
from core import updater

DEBUG = config.get_setting("debug")
MAX_THREADS = 16


# Procedures
def update_servers():
    server_path = os.path.join(config.get_runtime_path(), "servers", '*.xml')

    server_files = sorted(glob.glob(server_path))

    # ----------------------------
    import xbmc
    import xbmcgui
    progress = xbmcgui.DialogProgressBG()
    progress.create("Update servers list")
    # ----------------------------

    for index, server in enumerate(server_files):
        # ----------------------------
        percentage = index * 100 / len(server_files)
        # ----------------------------
        server_name = os.path.basename(server)[:-4]
        t = Thread(target=updater.update_server, args=[server_name])
        t.setDaemon(True)
        t.start()
        # ----------------------------
        progress.update(percentage, ' Update server: ' + server_name)
        # ----------------------------
        while threading.active_count() >= MAX_THREADS:
            xbmc.sleep(500)

    # ----------------------------
    progress.close()
    # ----------------------------


# Run
Thread(target=update_servers).start()
