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

from threading import Thread, Lock, Event


class Monitor(Thread):
        def __init__(self, client):
            Thread.__init__(self)
            self.daemon=True
            self.listeners=[]
            self.lock = Lock()
            self.wait_event= Event()
            self.running=True
            self.client=client
            self.ses=None
            self.client=client

        def stop(self):
            self.running=False
            self.wait_event.set()

        def add_listener(self, cb):
            with self.lock:
                if not cb in self.listeners:
                    self.listeners.append(cb)
        def remove_listener(self,cb):
            with self.lock:
                try:
                    self.listeners.remove(cb)
                except ValueError:
                    pass

        def remove_all_listeners(self):
            with self.lock:
                self.listeners=[]

        def run(self):
            while (self.running):
                with self.lock:
                    for cb in self.listeners:
                        cb()

                self.wait_event.wait(1.0)