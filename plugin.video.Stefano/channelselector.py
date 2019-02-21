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


import glob
import os
import urlparse

from core import channeltools, logger
from core import config
from core.item import Item


def getmainlist(preferred_thumb=""):
    logger.info()
    itemlist = list()

    # Menu principale

    itemlist.append( Item(title=config.get_localized_string(30119) , channel="channelselector" , action="getchanneltypes", thumbnail = os.path.join(config.get_runtime_path() , "resources" , "images", "main_menu_category.png"),fanart = os.path.join(config.get_runtime_path() , "resources" , "images", "background.jpg"),viewmode="movie") )
    itemlist.append( Item(title=config.get_localized_string(30137) , channel="buscadorall" , action="mainlist" , thumbnail = os.path.join(config.get_runtime_path() , "resources" , "images", "main_menu_search.png"),fanart = os.path.join(config.get_runtime_path() , "resources" , "images", "background.jpg"),viewmode="movie") )
    itemlist.append( Item(title=config.get_localized_string(50002), channel="novedades" , action="mainlist", thumbnail = os.path.join(config.get_runtime_path() , "resources" , "images", "thumb_novedades.png"),fanart = os.path.join(config.get_runtime_path() , "resources" , "images", "background.jpg"),viewmode="movie") )
    itemlist.append( Item(title=config.get_localized_string(30102) , channel="favoritos" , action="mainlist" , thumbnail = os.path.join(config.get_runtime_path() , "resources" , "images", "main_menu_fav.png"),fanart = os.path.join(config.get_runtime_path() , "resources" , "images", "background.jpg"),viewmode="movie") )
    if config.get_library_support():
        itemlist.append( Item(title=config.get_localized_string(30131) , channel="biblioteca" , action="mainlist", thumbnail = os.path.join(config.get_runtime_path() , "resources" , "images", "main_menu_library.png"),fanart = os.path.join(config.get_runtime_path() , "resources" , "images", "background.jpg"),viewmode="movie") )

    if "xbmceden" in config.get_platform():
        itemlist.append( Item(title=config.get_localized_string(30100) , channel="configuracion" , action="mainlist", thumbnail = os.path.join(config.get_runtime_path() , "resources" , "images", "main_menu_conf.png"),fanart = os.path.join(config.get_runtime_path() , "resources" , "images", "background.jpg"), folder=False,viewmode="movie") )
    else:
        itemlist.append( Item(title=config.get_localized_string(30100) , channel="configuracion" , action="mainlist", thumbnail = os.path.join(config.get_runtime_path() , "resources" , "images", "main_menu_conf.png"),fanart = os.path.join(config.get_runtime_path() , "resources" , "images", "background.jpg"),viewmode="movie") )

    itemlist.append( Item(title=config.get_localized_string(30104) , channel="ayuda" , action="mainlist", thumbnail = os.path.join(config.get_runtime_path() , "resources" , "images", "main_menu_help.png"),fanart = os.path.join(config.get_runtime_path() , "resources" , "images", "background.jpg"),viewmode="movie") )
    return itemlist

def get_thumb(preferred_thumb, thumb_name):
    return urlparse.urljoin(get_thumbnail_path(preferred_thumb), thumb_name)

def getchanneltypes(preferred_thumb=""):
    logger.info()

    # Costruzione degli item
    itemlist = list()

    itemlist.append(Item(title="Top Channels", channel="channelselector", action="filterchannels",
                         category="top channels", channel_type="top channels", thumbnail= os.path.join(config.get_runtime_path() , "resources" , "images", "cat_menu_topchannels.png"), fanart = os.path.join(config.get_runtime_path() , "resources" , "images", "background.jpg"), viewmode="movie"))
    itemlist.append(Item(title=config.get_localized_string(30122), channel="channelselector", action="filterchannels",
                         category="movie", channel_type="movie", thumbnail= os.path.join(config.get_runtime_path() , "resources" , "images", "cat_menu_film.png"), fanart = os.path.join(config.get_runtime_path() , "resources" , "images", "background.jpg"), viewmode="movie"))
    itemlist.append(Item(title=config.get_localized_string(30123), channel="channelselector", action="filterchannels",
                         category="serie", channel_type="serie", thumbnail= os.path.join(config.get_runtime_path() , "resources" , "images", "cat_menu_series.png"), fanart = os.path.join(config.get_runtime_path() , "resources" , "images", "background.jpg"), viewmode="movie"))
    itemlist.append(Item(title=config.get_localized_string(30124), channel="channelselector", action="filterchannels",
                         category="anime", channel_type="anime", thumbnail= os.path.join(config.get_runtime_path() , "resources" , "images", "cat_menu_anime.png"), fanart = os.path.join(config.get_runtime_path() , "resources" , "images", "background.jpg"), viewmode="movie"))
    itemlist.append(Item(title=config.get_localized_string(30125), channel="channelselector", action="filterchannels",
                         category="documentary", channel_type="documentary", thumbnail= os.path.join(config.get_runtime_path() , "resources" , "images", "cat_menu_documentales.png"), fanart = os.path.join(config.get_runtime_path() , "resources" , "images", "background.jpg"),
                         viewmode="movie"))
    itemlist.append(Item(title="Cult", channel="channelselector", action="filterchannels",
                         category="cult", channel_type="cult", thumbnail= os.path.join(config.get_runtime_path() , "resources" , "images", "main_menu_filmontv.png"), fanart = os.path.join(config.get_runtime_path() , "resources" , "images", "background.jpg"),
                         viewmode="movie"))
    itemlist.append(Item(title=config.get_localized_string(50000), channel="saghe", action="mainlist",
                         category="saghe", channel_type="saghe", thumbnail = os.path.join(config.get_runtime_path() , "resources" , "images", "cat_menu_saghe.png"), fanart = os.path.join(config.get_runtime_path() , "resources" , "images", "background.jpg")))
    itemlist.append( Item(title=config.get_localized_string(50001) , channel="filmontv" , action="mainlist" , thumbnail = os.path.join(config.get_runtime_path() , "resources" , "images", "main_menu_filmontv.png"),fanart = os.path.join(config.get_runtime_path() , "resources" , "images", "background.jpg"), viewmode="movie") )
    itemlist.append( Item( title=config.get_localized_string(30136) , channel="channelselector" , action="filterchannels" , channel_type="vos", category="vos" , thumbnail= os.path.join(config.get_runtime_path() , "resources" , "images", "cat_menu_vos.png"), fanart = os.path.join(config.get_runtime_path() , "resources" , "images", "background.jpg"), viewmode="movie") )
    itemlist.append( Item( title="[COLOR yellow]" + config.get_localized_string(30121) + "[/COLOR]" , channel="channelselector" , action="filterchannels" , channel_type="all", category="all" , thumbnail= os.path.join(config.get_runtime_path() , "resources" , "images", "main_menu_all.png"), fanart = os.path.join(config.get_runtime_path() , "resources" , "images", "background.jpg"), viewmode="movie") )

    return itemlist


def filterchannels(category, preferred_thumb=""):
    logger.info()

    channelslist = []

    # Categoria = "allchannelstatus" attiva/disattiva canali
    appenddisabledchannels = False
    if category == "allchannelstatus":
        category = "all"
        appenddisabledchannels = True

    # Lista dei canali
    channel_path = os.path.join(config.get_runtime_path(), "channels", '*.xml')
    logger.info("channel_path=" + channel_path)

    channel_files = glob.glob(channel_path)
    logger.info("channel_files encontrados " + str(len(channel_files)))

    channel_language = config.get_setting("channel_language")
    logger.info("channel_language=" + channel_language)
    if channel_language == "":
        channel_language = "all"
        logger.info("channel_language=" + channel_language)

    for channel in channel_files:
        logger.info("channel=" + channel)

        try:
            channel_parameters = channeltools.get_channel_parameters(channel[:-4])

            # Non mostrare se il canale è incompatibile
            if not channel_parameters["compatible"]:
                continue

            # Ignora se non è un canale
            if not channel_parameters["channel"]:
                continue
            logger.info("channel_parameters=" + repr(channel_parameters))

            # Si prefiere el bannermenu y el canal lo tiene, cambia ahora de idea
            if preferred_thumb == "bannermenu" and "bannermenu" in channel_parameters:
                channel_parameters["thumbnail"] = channel_parameters["bannermenu"]

            # Se salta el canal si no está activo y no estamos activando/desactivando los canales
            channel_status = config.get_setting("enabled", channel_parameters["channel"])

            if channel_status is None:
                # si channel_status no existe es que NO HAY valor en _data.json
                channel_status = channel_parameters["active"]

            # fix temporal para solucionar que enabled aparezca como "true/false"(str) y sea true/false(bool)
            # TODO borrar este fix en la versión > 4.2.1, ya que no sería necesario
            else:
                if isinstance(channel_status, basestring):
                    if channel_status == "true":
                        channel_status = True
                    else:
                        channel_status = False
                    config.set_setting("enabled", channel_status, channel_parameters["channel"])

            if channel_status != True:
                # si obtenemos el listado de canales desde "activar/desactivar canales", y el canal está desactivado
                # lo mostramos, si estamos listando todos los canales desde el listado general y está desactivado,
                # no se muestra
                if appenddisabledchannels != True:
                    continue

            # Ignora se modalità adulto è disattivata
            if channel_parameters["adult"] == True and config.get_setting("adult_mode") == 0:
                continue

            # Il canale viene ignorato se in una lingua filtrata
            if channel_language != "all" \
                    and channel_parameters["language"] != config.get_setting("channel_language"):
                continue

            # Il canale viene ignorato se si trova in una categoria filtrata
            if category != "all" and category not in channel_parameters["categories"]:
                continue

            # Se si dispone della configurazione aggiungere un elemento nel contesto
            context = []
            if channel_parameters["has_settings"]:
                context.append({"title": "Configurar canal", "channel": "configuracion", "action": "channel_config",
                                "config": channel_parameters["channel"]})

            # Aggiungi se sei arrivato qui
            channelslist.append(Item(title=channel_parameters["title"], channel=channel_parameters["channel"],
                                     action="mainlist", thumbnail=channel_parameters["thumbnail"],
                                     fanart=channel_parameters["fanart"], category=channel_parameters["title"],
                                     language=channel_parameters["language"], viewmode="list",
                                     version=channel_parameters["version"], context=context))

        except:
            logger.error("Se ha producido un error al leer los datos del canal " + channel)
            import traceback
            logger.error(traceback.format_exc())

    channelslist.sort(key=lambda item: item.title.lower().strip())

    if category == "all":
        if config.get_setting("personalchannel5") == True:
            channelslist.insert(0, Item(title=config.get_setting("personalchannelname5"), action="mainlist",
                                        channel="personal5", thumbnail=config.get_setting("personalchannellogo5"),
                                        type="generic", viewmode="list"))
        if config.get_setting("personalchannel4") == True:
            channelslist.insert(0, Item(title=config.get_setting("personalchannelname4"), action="mainlist",
                                        channel="personal4", thumbnail=config.get_setting("personalchannellogo4"),
                                        type="generic", viewmode="list"))
        if config.get_setting("personalchannel3") == True:
            channelslist.insert(0, Item(title=config.get_setting("personalchannelname3"), action="mainlist",
                                        channel="personal3", thumbnail=config.get_setting("personalchannellogo3"),
                                        type="generic", viewmode="list"))
        if config.get_setting("personalchannel2") == True:
            channelslist.insert(0, Item(title=config.get_setting("personalchannelname2"), action="mainlist",
                                        channel="personal2", thumbnail=config.get_setting("personalchannellogo2"),
                                        type="generic", viewmode="list"))
        if config.get_setting("personalchannel") == True:
            channelslist.insert(0, Item(title=config.get_setting("personalchannelname"), action="mainlist",
                                        channel="personal", thumbnail=config.get_setting("personalchannellogo"),
                                        type="generic", viewmode="list"))

        channel_parameters = channeltools.get_channel_parameters("tengourl")
        # Se preferisci il bannermenu e il canale lo contiene, cambialo adesso
        if preferred_thumb == "bannermenu" and "bannermenu" in channel_parameters:
            channel_parameters["thumbnail"] = channel_parameters["bannermenu"]

        channelslist.insert(0, Item(title="[COLOR gray]Inserisci un URL[/COLOR]", action="mainlist", channel="tengourl",
                                    thumbnail=channel_parameters["thumbnail"], type="generic", viewmode="list"))

        channel_parameters = channeltools.get_channel_parameters("searchchannel")
        channelslist.insert(0, Item(title="[COLOR gray]Cerca canale[/COLOR]", action="search", channel="searchchannel", thumbnail=channel_parameters["thumbnail"], type="generic", viewmode="movie"))

    return channelslist


def get_thumbnail_path(preferred_thumb=""):

    web_path = ""

    if preferred_thumb == "":
        thumbnail_type = config.get_setting("thumbnail_type")
        if thumbnail_type == "":
            thumbnail_type = 2
        if thumbnail_type == 0:
            web_path = "http://media.tvalacarta.info/pelisalacarta/posters/"
        elif thumbnail_type == 1:
            web_path = "http://media.tvalacarta.info/pelisalacarta/banners/"
        elif thumbnail_type == 2:
            web_path = "http://media.tvalacarta.info/pelisalacarta/squares/"
    else:
        web_path = "http://media.tvalacarta.info/pelisalacarta/" + preferred_thumb + "/"

    return web_path
