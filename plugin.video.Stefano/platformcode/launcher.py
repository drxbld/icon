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


import os
import pprint
import sys
import urllib2
import urlparse

from core import channeltools, logger
from core import config
from core import library
from core import scrapertools
from core import servertools
from core.item import Item
from platformcode import platformtools


def start():
    """ Primera funcion que se ejecuta al entrar en el plugin.
    Dentro de esta funcion deberian ir todas las llamadas a las
    funciones que deseamos que se ejecuten nada mas abrir el plugin.
    """
    logger.info()

    # Test if all the required directories are created
    config.verify_directories_created()


def run(item=None):
    logger.info()


    print "UUUUUUUUUUUUUUUUUUUUU"
    print sys.argv

    params = dict(urlparse.parse_qsl(sys.argv[2].replace('?', '')))
    action = params.get('action')

    if not item:
        # Extract item from sys.argv
        if sys.argv[2] and action != "sod":
            item = Item().fromurl(sys.argv[2])

        # If no item, this is mainlist
        else:
            item = Item(channel="channelselector", action="getmainlist", viewmode="movie")
    logger.info(item.tostring())

    try:

        # If item has no action, stops here
        if item.action == "":
            logger.info("Item sin accion")
            return

        # Action for main menu in channelselector
        if item.action == "getmainlist":
            import channelselector

            # Check for updates only on first screen
            # if config.get_setting("check_for_plugin_updates") == True:
            #     logger.info("Check for plugin updates enabled")
            #     from core import updater
            #
            #     try:
            #         config.set_setting("plugin_updates_available", 0)
            #         version = updater.checkforupdates()
            #         itemlist = channelselector.getmainlist()
            #
            #         if version:
            #             config.set_setting("plugin_updates_available",1)
            #
            #             platformtools.dialog_ok("Versione "+version+" disponible",
            #                                     "E' possibile fare il download della nuova versione\n"
            #                                     "selezionare la relativa voce nel menu principale")
            #
            #             itemlist = channelselector.getmainlist()
            #             itemlist.insert(0, Item(title="Download versione "+version, version=version, channel="updater",
            #                                     action="update", thumbnail=os.path.join(config.get_runtime_path() , "resources" , "images", "service_update.png")))
            #     except:
            #         import traceback
            #         logger.info(traceback.format_exc())
            #         platformtools.dialog_ok("Impossibile connettersi", "Non è stato possibile verificare",
            #                                 "aggiornamenti")
            #         logger.info("Fallo al verificar la actualización")
            #         config.set_setting("plugin_updates_available","0")
            #         itemlist = channelselector.getmainlist()
            #
            # else:
            #     logger.info("Check for plugin updates disabled")
            #     config.set_setting("plugin_updates_available", 0)
            #     itemlist = channelselector.getmainlist()

            # Check for updates only on first screen
            if config.get_setting("check_for_plugin_updates"):
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

            itemlist = channelselector.getmainlist()
            platformtools.render_items(itemlist, item)

        # Action for updating plugin
        elif item.action == "update":

            from core import updater
            updater.update(item)
            config.set_setting("plugin_updates_available", 0)
            if config.get_system_platform() != "xbox":
                import xbmc
                xbmc.executebuiltin("Container.Refresh")

        # Action for channel types on channelselector: movies, series, etc.
        elif item.action == "getchanneltypes":
            import channelselector
            itemlist = channelselector.getchanneltypes()

            platformtools.render_items(itemlist, item)

        # Action for channel listing on channelselector
        elif item.action == "filterchannels":
            import channelselector
            itemlist = channelselector.filterchannels(item.channel_type)

            platformtools.render_items(itemlist, item)

        # Special action for playing a video from the library
        elif item.action == "play_from_library":
            play_from_library(item)
            return

        # Action in certain channel specified in "action" and "channel" parameters
        else:

            # Entry point for a channel is the "mainlist" action, so here we check parental control
            if item.action == "mainlist":

                # Parental control
                # If it is an adult channel, and user has configured pin, asks for it
                if channeltools.is_adult(item.channel) and config.get_setting("adult_pin") != "":
                    tecleado = platformtools.dialog_input("", "PIN per canali per adulti", True)
                    if tecleado is None or tecleado != config.get_setting("adult_pin"):
                        return

            # Actualiza el canal individual
            if (item.action == "mainlist" and
                    item.channel != "channelselector" and
                    config.get_setting("check_for_channel_updates") == True):
                from core import updater
                updater.update_channel(item.channel)

            # Checks if channel exists
            channel_file = os.path.join(config.get_runtime_path(),
                                        'channels', item.channel + ".py")
            logger.info("channel_file=%s" % channel_file)

            channel = None

            if item.channel in ["personal", "personal2", "personal3", "personal4", "personal5"]:
                import channels.personal as channel

            elif os.path.exists(channel_file):
                try:
                    channel = __import__('channels.%s' % item.channel, None,
                                         None, ["channels.%s" % item.channel])
                except ImportError:
                    exec "import channels." + item.channel + " as channel"

            logger.info("Running channel %s | %s" % (channel.__name__, channel.__file__))

            # Special play action
            if item.action == "play":
                logger.info("item.action=%s" % item.action.upper())
                # logger.debug("item_toPlay: " + "\n" + item.tostring('\n'))

                # First checks if channel has a "play" function
                if hasattr(channel, 'play'):
                    logger.info("Executing channel 'play' method")
                    itemlist = channel.play(item)
                    b_favourite = item.isFavourite
                    # Play should return a list of playable URLS
                    if len(itemlist) > 0 and isinstance(itemlist[0], Item):
                        item = itemlist[0]
                        if b_favourite:
                            item.isFavourite = True
                        platformtools.play_video(item)

                    # Permitir varias calidades desde play en el canal
                    elif len(itemlist) > 0 and isinstance(itemlist[0], list):
                        item.video_urls = itemlist
                        platformtools.play_video(item)

                    # If not, shows user an error message
                    else:
                        platformtools.dialog_ok("plugin", "Niente da riprodurre o riprova (de-link)")

                # If player don't have a "play" function, not uses the standard play from platformtools
                else:
                    logger.info("Executing core 'play' method")
                    platformtools.play_video(item)

            # Special action for findvideos, where the plugin looks for known urls
            elif item.action == "findvideos":

                # First checks if channel has a "findvideos" function
                if hasattr(channel, 'findvideos'):
                    itemlist = getattr(channel, item.action)(item)
                    itemlist = servertools.filter_servers(itemlist)

                # If not, uses the generic findvideos function
                else:
                    logger.info("No channel 'findvideos' method, "
                                "executing core method")
                    itemlist = servertools.find_video_items(item)

                if config.get_setting("max_links", "biblioteca") != 0:
                    itemlist = limit_itemlist(itemlist)

                from platformcode import subtitletools
                subtitletools.saveSubtitleName(item)

                platformtools.render_items(itemlist, item)

            # Special action for adding a movie to the library
            elif item.action == "add_pelicula_to_library":
                library.add_pelicula_to_library(item)

            # Special action for adding a serie to the library
            elif item.action == "add_serie_to_library":
                library.add_serie_to_library(item, channel)

            # Special action for searching, first asks for the words then call the "search" function
            elif item.action == "search":
                logger.info("item.action=%s" % item.action.upper())

                tecleado = platformtools.dialog_input('')
                if tecleado is not None:

                    # TODO revisar 'personal.py' porque no tiene función search y daría problemas
                    # DrZ3r0
                    itemlist = channel.search(item, tecleado.replace(" ", "+"))
                else:
                    return

                platformtools.render_items(itemlist, item)

            # For all other actions
            else:
                logger.info("Executing channel '%s' method" % item.action)
                itemlist = getattr(channel, item.action)(item)
                platformtools.render_items(itemlist, item)

    except urllib2.URLError, e:
        import traceback
        logger.error(traceback.format_exc())

        # Grab inner and third party errors
        if hasattr(e, 'reason'):
            logger.error("Razon del error, codigo: %s | Razon: %s" % (str(e.reason[0]), str(e.reason[1])))
            texto = config.get_localized_string(30050)  # "No se puede conectar con el sitio web"
            platformtools.dialog_ok("plugin", texto)

        # Grab server response errors
        elif hasattr(e, 'code'):
            logger.error("Codigo de error HTTP : %d" % e.code)
            # "El sitio web no funciona correctamente (error http %d)"
            platformtools.dialog_ok("plugin", config.get_localized_string(30051) % e.code)
    
    except:
        import traceback
        logger.error(traceback.format_exc())

        patron = 'File "'+os.path.join(config.get_runtime_path(), "channels", "").replace("\\", "\\\\")+'([^.]+)\.py"'
        canal = scrapertools.find_single_match(traceback.format_exc(), patron)

        try:
            import xbmc
            if config.get_platform(True)['num_version'] < 14:
                log_name = "xbmc.log"
            else:
                log_name = "kodi.log"
            log_message = "Percorso: "+xbmc.translatePath("special://logpath")+log_name
        except:
            log_message = ""

        if canal:
            platformtools.dialog_ok(
                "Errore inaspettato in " + canal,
                "Protrebbe essere un errore di connessione. Il canale web "
                "potrebbe aver modificato la sua struttura oppure si è verificato un errore in Stefano Thegroove 360.",
                "Per dettagli consulta il log.", log_message)
        else:
            platformtools.dialog_ok(
                "Si è verificato un errore su Stefano Thegroove 360",
                "Per dettagli consulta il log.",
                log_message)




def reorder_itemlist(itemlist):
    logger.info()
    # logger.debug("Inlet itemlist size: %i" % len(itemlist))

    new_list = []
    mod_list = []
    not_mod_list = []

    modified = 0
    not_modified = 0

    to_change = [['Ver en',       '[V]'],
                 ['Descargar en', '[D]']]

    for item in itemlist:
        old_title = unicode(item.title, "utf8").lower().encode("utf8")
        for before, after in to_change:
            if before in item.title:
                item.title = item.title.replace(before, after)
                break

        new_title = unicode(item.title, "utf8").lower().encode("utf8")
        if old_title != new_title:
            mod_list.append(item)
            modified += 1
        else:
            not_mod_list.append(item)
            not_modified += 1

        # logger.debug("OLD: %s | NEW: %s" % (old_title, new_title))

    new_list.extend(mod_list)
    new_list.extend(not_mod_list)

    logger.info("Titulos modificados:%i | No modificados:%i" % (modified, not_modified))

    if len(new_list) == 0:
        new_list = itemlist

    # logger.debug("Outlet itemlist size: %i" % len(new_list))
    return new_list


def limit_itemlist(itemlist):
    logger.info()
    # logger.debug("Inlet itemlist size: %i" % len(itemlist))

    try:
        opt = config.get_setting("max_links", "biblioteca")
        if opt == 0:
            new_list = itemlist
        else:
            i_max = 30 * opt
            new_list = itemlist[:i_max]

        # logger.debug("Outlet itemlist size: %i" % len(new_list))
        return new_list
    except:
        return itemlist


def play_from_library(item):
    """
        Los .strm al reproducirlos desde kodi, este espera que sea un archivo "reproducible" asi que no puede contener
        más items, como mucho se puede colocar un dialogo de seleccion.
        Esto lo solucionamos "engañando a kodi" y haciendole creer que se ha reproducido algo, asi despues mediante
        "Container.Update()" cargamos el strm como si un item desde dentro de pelisalacarta se tratara, quitando todas
        las limitaciones y permitiendo reproducir mediante la funcion general sin tener que crear nuevos métodos para
        la biblioteca.
        @type item: item
        @param item: elemento con información
    """
    logger.info()
    # logger.debug("item: \n" + item.tostring('\n'))

    import xbmcgui
    import xbmcplugin
    import xbmc
    # Intentamos reproducir una imagen (esto no hace nada y ademas no da error)
    xbmcplugin.setResolvedUrl(int(sys.argv[1]), True,
                              xbmcgui.ListItem(path=os.path.join(config.get_runtime_path(), "resources", "subtitle.mp4")))

    # Por si acaso la imagen hiciera (en futuras versiones) le damos a stop para detener la reproduccion
    xbmc.Player().stop()

    # modificamos el action (actualmente la biblioteca necesita "findvideos" ya que es donde se buscan las fuentes
    item.action = "findvideos"

    window_type = config.get_setting("window_type", "biblioteca")

    # y volvemos a lanzar kodi
    if xbmc.getCondVisibility('Window.IsMedia') and not window_type == 1:
        # Ventana convencional
        xbmc.executebuiltin("Container.Update(" + sys.argv[0] + "?" + item.tourl() + ")")

    else:
        # Ventana emergente
        from channels import biblioteca
        p_dialog = platformtools.dialog_progress_bg('Stefano', 'Caricamento in corso...')
        p_dialog.update(0, '')

        itemlist = biblioteca.findvideos(item)

        p_dialog.update(50, '')

        '''# Se filtran los enlaces segun la lista negra
        if config.get_setting('filter_servers', "servers"):
            itemlist = servertools.filter_servers(itemlist)'''

        # Se limita la cantidad de enlaces a mostrar
        if config.get_setting("max_links", "biblioteca") != 0:
            itemlist = limit_itemlist(itemlist)

        # Se "limpia" ligeramente la lista de enlaces
        if config.get_setting("replace_VD", "biblioteca") == 1:
            itemlist = reorder_itemlist(itemlist)

        p_dialog.update(100, '')
        xbmc.sleep(500)
        p_dialog.close()

        if len(itemlist) > 0:
            # El usuario elige el mirror
            opciones = []
            for item in itemlist:
                opciones.append(item.title)

            # Se abre la ventana de seleccion
            if (item.contentSerieName != "" and
                    item.contentSeason != "" and
                    item.contentEpisodeNumber != ""):
                cabecera = ("%s - %sx%s -- %s" %
                            (item.contentSerieName,
                             item.contentSeason,
                             item.contentEpisodeNumber,
                             config.get_localized_string(30163)))
            else:
                cabecera = config.get_localized_string(30163)

            seleccion = platformtools.dialog_select(cabecera, opciones)

            if seleccion == -1:
                return
            else:
                item = biblioteca.play(itemlist[seleccion])[0]
                platformtools.play_video(item)
