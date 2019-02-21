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


def get(version):
    try:
        import xbmc,xbmcgui,xbmcaddon,xbmcvfs

        f = xbmcvfs.File(xbmcaddon.Addon().getAddonInfo('changelog'))
        text = f.read() ; f.close()

        label = '%s - %s' % (xbmc.getLocalizedString(24054), xbmcaddon.Addon().getAddonInfo('name'))

        id = 10147

        xbmc.executebuiltin('ActivateWindow(%d)' % id)
        xbmc.sleep(100)

        win = xbmcgui.Window(id)

        retry = 50
        while (retry > 0):
            try:
                xbmc.sleep(10)
                win.getControl(1).setLabel(label)
                win.getControl(5).setText(text)
                retry = 0
            except:
                retry -= 1

        return '1'
    except:
        return '1'


