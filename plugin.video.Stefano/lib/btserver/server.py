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

import traceback
import BaseHTTPServer
from SocketServer import ThreadingMixIn
from threading import Thread


class Server(ThreadingMixIn, BaseHTTPServer.HTTPServer):
    daemon_threads = True
    timeout = 1
    def __init__(self, address, handler, client):
        BaseHTTPServer.HTTPServer.__init__(self,address,handler)
        self._client = client
        self.file=None
        self.running=True
        self.request = None

    def stop(self):
        self.running=False

    def serve(self):
        while self.running:
            try:
                self.handle_request()
            except:
                print traceback.format_exc()

    def run(self):
        t=Thread(target=self.serve, name='HTTP Server')
        t.daemon=True
        t.start()
    def handle_error(self, request, client_address):
      if not "socket.py" in traceback.format_exc():
        print traceback.format_exc()