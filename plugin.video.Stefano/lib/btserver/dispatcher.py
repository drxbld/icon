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


from monitor import Monitor
try:
    from python_libtorrent import get_libtorrent
    lt = get_libtorrent()
except Exception, e:
    import libtorrent as lt

class Dispatcher(Monitor):
    def __init__(self, client):
        super(Dispatcher,self).__init__(client)

    def do_start(self, th, ses):
        self._th = th
        self._ses=ses
        self.start()

    def run(self):
        if not self._ses:
            raise Exception('Invalid state, session is not initialized')

        while self.running:
            a=self._ses.wait_for_alert(1000)
            if a:
                alerts= self._ses.pop_alerts()
                for alert in alerts:
                    with self.lock:
                        for cb in self.listeners:
                            cb(lt.alert.what(alert), alert)
