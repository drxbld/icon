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


import datetime
import imp
import math
import re
import threading

from core import config, scrapertools, logger
from core import filetools
from core import jsontools
from core import library
from core.item import Item
from platformcode import platformtools


def convert_old_to_v4():
    logger.info()
    path_series_xml = filetools.join(config.get_data_path(), "series.xml")
    path_series_json = filetools.join(config.get_data_path(), "series.json")
    series_insertadas = 0
    series_fallidas = 0
    version = 'v?'

    # Rename and create Series directory
    import time
    new_name = str(time.time())
    path_series_old = filetools.join(library.LIBRARY_PATH, "SERIES_OLD_" + new_name)
    if filetools.rename(library.TVSHOWS_PATH, "SERIES_OLD_" + new_name):
        if not filetools.mkdir(library.TVSHOWS_PATH):
            logger.error("ERROR, impossibile creare la directory SERIES")
            return False
    else:
        logger.error("ERROR,impossibile rinominare la directory SERIES")
        return False

    path_cine_old = filetools.join(library.LIBRARY_PATH, "CINE_OLD_" + new_name)
    if filetools.rename(library.MOVIES_PATH, "CINE_OLD_" + new_name):
        if not filetools.mkdir(library.MOVIES_PATH):
            logger.error("ERROR, impossibile creare la directory CINE")
            return False
    else:
        logger.error("ERROR, impossibile rinominare la directory CINE")
        return False

    # Convert library from v1 to v4 (xml)
    if filetools.exists(path_series_xml):
        try:
            data = filetools.read(path_series_xml)
            for line in data.splitlines():
                try:
                    aux = line.rstrip('\n').split(",")
                    tvshow = aux[0].strip()
                    url = aux[1].strip()
                    channel = aux[2].strip()

                    serie = Item(contentSerieName=tvshow, url=url, channel=channel, action="episodios",
                                 title=tvshow, active=True)

                    patron = "^(.+)[\s]\((\d{4})\)$"
                    matches = re.compile(patron, re.DOTALL).findall(serie.contentSerieName)

                    if matches:
                        serie.infoLabels['title'] = matches[0][0]
                        serie.infoLabels['year'] = matches[0][1]
                    else:
                        serie.infoLabels['title'] = tvshow

                    insertados, sobreescritos, fallidos = library.save_library_tvshow(serie, list())
                    if fallidos == 0:
                        series_insertadas += 1
                        platformtools.dialog_notification("Serie aggiornata", serie.infoLabels['title'])
                    else:
                        series_fallidas += 1
                except:
                    series_fallidas += 1

            filetools.rename(path_series_xml, "series.xml.old")
            version = 'v4'

        except EnvironmentError:
            logger.error("ERROR al leer el archivo: %s" % path_series_xml)
            return False

    # Convert library from v2 to v4 (json)
    if filetools.exists(path_series_json):
        try:
            data = jsontools.load_json(filetools.read(path_series_json))
            for tvshow in data:
                for channel in data[tvshow]["channels"]:
                    try:
                        serie = Item(contentSerieName=data[tvshow]["channels"][channel]["tvshow"],
                                     url=data[tvshow]["channels"][channel]["url"], channel=channel, action="episodios",
                                     title=data[tvshow]["name"], active=True)
                        if not tvshow.startswith("t_"):
                            serie.infoLabels["tmdb_id"] = tvshow

                        insertados, sobreescritos, fallidos = library.save_library_tvshow(serie, list())
                        if fallidos == 0:
                            series_insertadas += 1
                            platformtools.dialog_notification("Serie aggiornata", serie.infoLabels['title'])
                        else:
                            series_fallidas += 1
                    except:
                        series_fallidas += 1

            filetools.rename(path_series_json, "series.json.old")
            version = 'v4'

        except EnvironmentError:
            logger.error("ERROR al leer el archivo: %s" % path_series_json)
            return False

    # Convert library from v2 to v4
    if version != 'v4':
        # Get old Series recursively
        for raiz, subcarpetas, ficheros in filetools.walk(path_series_old):
            for f in ficheros:
                if f == "tvshow.json":
                    try:
                        serie = Item().fromjson(filetools.read(filetools.join(raiz, f)))
                        insertados, sobreescritos, fallidos = library.save_library_tvshow(serie, list())
                        if fallidos == 0:
                            series_insertadas += 1
                            platformtools.dialog_notification("Serie aggiornata", serie.infoLabels['title'])
                        else:
                            series_fallidas += 1
                    except:
                        series_fallidas += 1

        movies_insertadas = 0
        movies_fallidas = 0
        for raiz, subcarpetas, ficheros in filetools.walk(path_cine_old):
            for f in ficheros:
                if f.endswith(".strm.json"):
                    try:
                        movie = Item().fromjson(filetools.read(filetools.join(raiz, f)))
                        insertados, sobreescritos, fallidos = library.save_library_movie(movie)
                        if fallidos == 0:
                            movies_insertadas += 1
                            platformtools.dialog_notification("Film aggiornato", movie.infoLabels['title'])
                        else:
                            movies_fallidas += 1
                    except:
                        movies_fallidas += 1

    config.set_setting("library_version", 'v4')

    platformtools.dialog_notification("Libreria aggiornata con il nuovo formato",
                                      "%s serie convertite e %s serie scaricate. Continuare per"
                                      "ottenere le info sugli episodi" %
                                      (series_insertadas, series_fallidas), time=12000)

    # Cleanup library of empty records
    if config.is_xbmc():
        from platformcode import xbmc_library
        xbmc_library.clean()

    return True


def update(path, p_dialog, i, t, serie, overwrite):
    logger.info("Actualizando " + path)
    insertados_total = 0

    # logger.debug("%s: %s" %(serie.contentSerieName,str(list_canales) ))
    for channel, url in serie.library_urls.items():
        serie.channel = channel
        serie.url = url

        heading = 'Aggiornamento della libreria...'
        p_dialog.update(int(math.ceil((i + 1) * t)), heading, "%s: %s" % (serie.contentSerieName,
                                                                          serie.channel.capitalize()))
        pathchannels = filetools.join(config.get_runtime_path(), "channels", serie.channel + '.py')
        logger.info("Caricando il canale: " + pathchannels + " " +
                    serie.channel)

        if serie.library_filter_show:
            serie.show = serie.library_filter_show.get(channel, serie.contentSerieName)

        obj = imp.load_source(serie.channel, pathchannels)

        itemlist = ""
        try:
            itemlist = obj.episodios(serie)
        except Exception as ex:
            pass
        try:
            if itemlist == "":
                itemlist = obj.serietv(serie)

            try:
                if int(overwrite) == 3:
                    # Overwrite all files (tvshow.nfo, 1x01.nfo, 1x01 [canal].json, 1x01.strm, etc...)
                    insertados, sobreescritos, fallidos = library.save_library_tvshow(serie, itemlist)
                else:
                    insertados, sobreescritos, fallidos = library.save_library_episodes(path, itemlist, serie,
                                                                                        silent=True,
                                                                                        overwrite=overwrite)
                insertados_total += insertados

            except Exception as ex:
                logger.error("Errore nei capitoli delle serie")
                template = "An exception of type %s occured. Arguments:\n%r"
                message = template % (type(ex).__name__, ex.args)
                logger.error(message)

        except Exception as ex:
            pass

        if itemlist == "":
            logger.error("Errore nel ricavare gli episodi di %s. Verificare il metodo utilizzato dal canale %s." % (
            serie.show, serie.channel))

    return insertados_total > 0


def check_for_update(overwrite=True):
    logger.info("Aggiornamento series...")
    p_dialog = None
    serie_actualizada = False
    update_when_finished = False
    hoy = datetime.date.today()

    try:
        if config.get_setting("updatelibrary", "biblioteca") != 0 or overwrite:
            config.set_setting("updatelibrary_last_check", hoy.strftime('%Y-%m-%d'), "biblioteca")

            heading = 'Aggiornamento della libreria...'
            p_dialog = platformtools.dialog_progress_bg('Stefano', heading)
            p_dialog.update(0, '')

            show_list = []
            for path, folders, files in filetools.walk(library.TVSHOWS_PATH):
                show_list.extend([filetools.join(path, f) for f in files if f == "tvshow.sod"])

            if show_list:
                t = float(100) / len(show_list)

            for i, tvshow_file in enumerate(show_list):
                head_nfo, serie = library.read_nfo(tvshow_file)
                path = filetools.dirname(tvshow_file)

                logger.info("serie=" + serie.contentSerieName)
                p_dialog.update(int(math.ceil((i + 1) * t)), heading, serie.contentSerieName)

                interval = int(serie.active)  # Can be bool type

                if not serie.active:
                    # Unload if the Serie is not active
                    continue

                # Update next
                update_next = serie.update_next
                if update_next:
                    y, m, d = update_next.split('-')
                    update_next = datetime.date(int(y), int(m), int(d))
                else:
                    update_next = hoy

                update_last = serie.update_last
                if update_last:
                    y, m, d = update_last.split('-')
                    update_last = datetime.date(int(y), int(m), int(d))
                else:
                    update_last = hoy

                # if the Serie is active ...
                if overwrite or config.get_setting("updatetvshows_interval", "biblioteca") == 0:
                    # ... force autonomus update
                    serie_actualizada = update(path, p_dialog, i, t, serie, overwrite)

                elif interval == 1 and update_next <= hoy:
                    # ...weekly update
                    serie_actualizada = update(path, p_dialog, i, t, serie, overwrite)
                    if not serie_actualizada and update_last <= hoy - datetime.timedelta(days=7):
                        # raise the interval
                        interval = 7
                        update_next = hoy + datetime.timedelta(days=interval)

                elif interval == 7 and update_next <= hoy:
                    # ...14days update
                    serie_actualizada = update(path, p_dialog, i, t, serie, overwrite)
                    if not serie_actualizada:
                        if update_last <= hoy - datetime.timedelta(days=14):
                            # raise the interval
                            interval = 30

                        update_next += datetime.timedelta(days=interval)

                elif interval == 30 and update_next <= hoy:
                    # ...monthly update
                    serie_actualizada = update(path, p_dialog, i, t, serie, overwrite)
                    if not serie_actualizada:
                        update_next += datetime.timedelta(days=interval)

                if interval != int(serie.active) or update_next.strftime('%Y-%m-%d') != serie.update_next:
                    serie.active = interval
                    serie.update_next = update_next.strftime('%Y-%m-%d')
                    serie.channel = "biblioteca"
                    serie.action = "get_temporadas"
                    filetools.write(tvshow_file, head_nfo + serie.tojson())

                if serie_actualizada:
                    if config.get_setting("search_new_content", "biblioteca") == 0:
                        # Update Kodi library: Search contents in the Serie directory
                        if config.is_xbmc():
                            from platformcode import xbmc_library
                            xbmc_library.update(folder=filetools.basename(path))
                    else:
                        update_when_finished = True

            if config.get_setting("search_new_content", "biblioteca") == 1 and update_when_finished:
                # Update Kodi library: Search contents for every Serie
                if config.is_xbmc():
                    from platformcode import xbmc_library
                    xbmc_library.update()

            p_dialog.close()

        else:
            logger.info("Libreria non aggiornata, opzione disattiva nella configurazione di Stefano")

    except Exception as ex:
        logger.error("Si è verificato un errore nell'aggiornamento")
        template = "An exception of type %s occured. Arguments:\n%r"
        message = template % (type(ex).__name__, ex.args)
        logger.error(message)

        if p_dialog:
            p_dialog.close()


def start(thread=True):
    if thread:
        t = threading.Thread(target=start, args=[False])
        t.setDaemon(True)
        t.start()
    else:
        import xbmc

        updatelibrary_wait = [0, 10000, 20000, 30000, 60000]
        try:
            confval = int(config.get_setting("updatelibrary_wait", "biblioteca"))
        except:
            confval = 0
        wait = updatelibrary_wait[confval]
        if wait > 0:
            xbmc.sleep(wait)

        # Compare the library and update it if necessary
        library_version = config.get_setting("library_version")
        if library_version != None and library_version != 'v4' and library_version != 'v5':
            platformtools.dialog_ok(config.PLUGIN_NAME.capitalize(), "Aggiornamento della libreria al nuovo formato",
                                    "Selezionare correttamente il nome della serie, se non sicuro seleziona 'Annulla'.")

            if not convert_old_to_v4():
                platformtools.dialog_ok(config.PLUGIN_NAME.capitalize(),
                                        "ERROR, nella conversione al nuovo formato")
            else:
                # Option 2 "Once per day"
                if not config.get_setting("updatelibrary", "biblioteca") == 2:
                    check_for_update(overwrite=False)
        else:
            if not config.get_setting("updatelibrary", "biblioteca") == 2:
                check_for_update(overwrite=False)

        # Cycling update
        while True:
            monitor_update()
            xbmc.sleep(3600 * 1000)


def monitor_update():
    update_setting = config.get_setting("updatelibrary", "biblioteca")
    if update_setting == 2 or update_setting == 3:
        hoy = datetime.date.today()
        last_check = config.get_setting("updatelibrary_last_check", "biblioteca")
        if last_check:
            y, m, d = last_check.split('-')
            last_check = datetime.date(int(y), int(m), int(d))
        else:
            last_check = hoy - datetime.timedelta(days=1)

        update_start = config.get_setting("everyday_delay", "biblioteca") * 4

        if last_check < hoy and datetime.datetime.now().hour >= int(update_start):
            logger.info("Inizio update programmato: %s" % datetime.datetime.now())
            check_for_update(overwrite=False)


if __name__ == "__main__":
    version = config.__settings__.getAddonInfo("version")
    config.set_setting("plugin_version_number", version.replace(".", "") + "0")
    config.set_setting("plugin_version_tag", version)

    if scrapertools.wait_for_internet(retry=10):

        # disable update channel/server
        if config.get_setting("check_for_channel_updates") == "true":
            # -- Update channels from repository Stefano ------
            try:
                from core import update_channels
            except:
                logger.info("Stefano.library_service Error in update_channels")
            # ----------------------------------------------------------------------

            # -- Update servertools and servers from repository Stefano ------
            try:
                from core import update_servers
            except:
                logger.info("Stefano.library_service Error in update_servers")
            # ----------------------------------------------------------------------
    '''

        # Start from the beginning
        import xbmc

        # adult mode:
        # Change from False to True to the system 0: Never, 1:Always, 2:Only on Kodi restart
        # if == 2 inactive.
        if config.get_setting("adult_mode") == False or config.get_setting("adult_mode") == 2:
            config.set_setting("adult_mode", 0)
        elif config.get_setting("adult_mode") == True:
            config.set_setting("adult_mode", 1)

        updatelibrary_wait = [0, 10000, 20000, 30000, 60000]
        try:
            confval = int(config.get_setting("updatelibrary_wait", "biblioteca"))
        except:
            confval = 0
        wait = updatelibrary_wait[confval]
        if wait > 0:
            xbmc.sleep(wait)

        # Compare the library and update it if necessary
        library_version = config.get_setting("library_version")
        if library_version != None and library_version != 'v4' and library_version != 'v5':
            platformtools.dialog_ok(config.PLUGIN_NAME.capitalize(), "Aggiornamento della libreria al nuovo formato", "Seleziona il nome corretto di serie o film, se non sicuro seleziona 'Cancel'.")

            if not convert_old_to_v4():
                platformtools.dialog_ok(config.PLUGIN_NAME.capitalize(), "ERROR, al actualizar la biblioteca al nuevo formato")
            else:
                # Option 2 "Once per day"
                if not config.get_setting("updatelibrary", "biblioteca") == 2:
                    check_for_update(overwrite=False)
        else:
            if not config.get_setting("updatelibrary", "biblioteca") == 2:
                check_for_update(overwrite=False)

        # Cycle execution
        if config.get_platform(True)['num_version'] >= 14:
            monitor = xbmc.Monitor()  # For Kodi >= 14
        else:
            monitor = None  # For Kodi < 14

        if monitor:
            while not monitor.abortRequested():
                monitor_update()
                if monitor.waitForAbort(3600 * 1000):
                    break
        else:
            while not xbmc.abortRequested:
                monitor_update()
                xbmc.sleep(3600 * 1000)'''
