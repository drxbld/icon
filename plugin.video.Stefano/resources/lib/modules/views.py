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


try: from sqlite3 import dbapi2 as database
except: from pysqlite2 import dbapi2 as database

from resources.lib.modules import control


def addView(content):
    try:
        skin = control.skin
        record = (skin, content, str(control.getCurrentViewId()))
        control.makeFile(control.dataPath)
        dbcon = database.connect(control.viewsFile)
        dbcur = dbcon.cursor()
        dbcur.execute("CREATE TABLE IF NOT EXISTS views (""skin TEXT, ""view_type TEXT, ""view_id TEXT, ""UNIQUE(skin, view_type)"");")
        dbcur.execute("DELETE FROM views WHERE skin = '%s' AND view_type = '%s'" % (record[0], record[1]))
        dbcur.execute("INSERT INTO views Values (?, ?, ?)", record)
        dbcon.commit()

        viewName = control.infoLabel('Container.Viewmode')
        skinName = control.addon(skin).getAddonInfo('name')
        skinIcon = control.addon(skin).getAddonInfo('icon')

        control.infoDialog(viewName, heading=skinName, sound=True, icon=skinIcon)
    except:
        return


def setView(content, viewDict=None):
    for i in range(0, 200):
        if control.condVisibility('Container.Content(%s)' % content):
            try:
                skin = control.skin
                record = (skin, content)
                dbcon = database.connect(control.viewsFile)
                dbcur = dbcon.cursor()
                dbcur.execute("SELECT * FROM views WHERE skin = '%s' AND view_type = '%s'" % (record[0], record[1]))
                view = dbcur.fetchone()
                view = view[2]
                if view == None: raise Exception()
                return control.execute('Container.SetViewMode(%s)' % str(view))
            except:
                try: return control.execute('Container.SetViewMode(%s)' % str(viewDict[skin]))
                except: return

        control.sleep(100)


