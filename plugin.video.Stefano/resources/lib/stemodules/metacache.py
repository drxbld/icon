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



import os,time,hashlib

try:
    from sqlite3 import dbapi2 as database
except:
    from pysqlite2 import dbapi2 as database

from resources.lib.stemodules import control


def fetch(items, lang):
    try:
        t2 = int(time.time())
        metacacheFile = os.path.join(control.dataPath, 'meta.5.db')
        dbcon = database.connect(metacacheFile)
        dbcur = dbcon.cursor()
    except:
        try: dbcon.close()
        except: pass
        return items

    for i in range(0, len(items)):
        try:
            dbcur.execute("SELECT * FROM meta WHERE (imdb = '%s' and lang = '%s' and not imdb = '0') or (tmdb = '%s' and lang = '%s' and not tmdb = '0') or (tvdb = '%s' and lang = '%s' and not tvdb = '0')" % (items[i]['imdb'], lang, items[i]['tmdb'], lang, items[i]['tvdb'], lang))
            match = dbcur.fetchone()

            t1 = int(match[5])
            update = (abs(t2 - t1) / 3600) >= 720
            if update == True: raise Exception()

            item = eval(match[4].encode('utf-8'))
            item = dict((k,v) for k, v in item.iteritems() if not v == '0')

            if items[i]['fanart'] == '0':
                try: items[i].update({'fanart': item['fanart']})
                except: pass

            item = dict((k,v) for k, v in item.iteritems() if not k == 'fanart')
            items[i].update(item)

            items[i].update({'metacache': True})
        except:
            pass

    try: dbcon.close()
    except: pass

    return items


def insert(meta):
    try:
        if not meta: return
        control.makeFile(control.dataPath)
        metacacheFile = os.path.join(control.dataPath, 'meta.5.db')

        dbcon = database.connect(metacacheFile)
        dbcur = dbcon.cursor()
        dbcur.execute("CREATE TABLE IF NOT EXISTS meta (""imdb TEXT, ""tmdb TEXT, ""tvdb TEXT, ""lang TEXT, ""item TEXT, ""time TEXT, ""UNIQUE(imdb, tmdb, tvdb, lang)"");")
        t = int(time.time())
        r = False
        for m in meta:
            try:
                i = repr(m['item'])
                try: dbcur.execute("DELETE * FROM meta WHERE (imdb = '%s' and lang = '%s' and not imdb = '0') or (tmdb = '%s' and lang = '%s' and not tmdb = '0') or (tvdb = '%s' and lang = '%s' and not tvdb = '0')" % (m['imdb'], m['lang'], m['tmdb'], m['lang'], m['tvdb'], m['lang']))
                except: pass
                try: dbcur.execute("INSERT INTO meta Values (?, ?, ?, ?, ?, ?)", (m['imdb'], m['tmdb'], m['tvdb'], m['lang'], i, t))
                except: r = True ; break
            except:
                pass
        dbcon.commit()
        dbcon.close()

        if r == False: return

        control.deleteFile(metacacheFile)
        dbcon = database.connect(metacacheFile)
        dbcur = dbcon.cursor()
        dbcur.execute("CREATE TABLE IF NOT EXISTS meta (""imdb TEXT, ""tmdb TEXT, ""tvdb TEXT, ""lang TEXT, ""item TEXT, ""time TEXT, ""UNIQUE(imdb, tmdb, tvdb, lang)"");")
        t = int(time.time())
        r = False
        for m in meta:
            try:
                i = repr(m['item'])
                try: dbcur.execute("DELETE * FROM meta WHERE (imdb = '%s' and lang = '%s' and not imdb = '0') or (tmdb = '%s' and lang = '%s' and not tmdb = '0') or (tvdb = '%s' and lang = '%s' and not tvdb = '0')" % (m['imdb'], m['lang'], m['tmdb'], m['lang'], m['tvdb'], m['lang']))
                except: pass
                dbcur.execute("INSERT INTO meta Values (?, ?, ?, ?, ?, ?)", (m['imdb'], m['tmdb'], m['tvdb'], m['lang'], i, t))
            except:
                pass
        dbcon.commit()
        dbcon.close()
    except:
        return


