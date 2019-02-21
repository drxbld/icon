# -*- coding: utf-8 -*-
# ------------------------------------------------------------
# TheGroove360 / XBMC Plugin
# Canale 
# ------------------------------------------------------------

import os

import xbmc
from core import config, filetools, scrapertools
from core.item import Item
from platformcode import logger, platformtools

try:
    # Set path to favourites.xml
    if config.is_xbmc():
        import xbmc
        FAVOURITES_PATH = xbmc.translatePath("special://profile/favourites.xml")
    else:
        FAVOURITES_PATH = os.path.join(config.get_data_path(), "favourites.xml")
except:
    import traceback
    logger.error(traceback.format_exc())


def mainlist(item):
    logger.info()
    itemlist = []

    for name, thumb, data in read_favourites():
        if "plugin://plugin.video.%s/?" % config.PLUGIN_NAME in data:
            url = scrapertools.find_single_match(data, 'plugin://plugin.video.%s/\?([^;]*)' % config.PLUGIN_NAME)\
                .replace("&quot", "")

            item = Item().fromurl(url)
            item.title = name
            item.thumbnail = thumb
            item.isFavourite = True

            if type(item.context) == str:
                item.context = item.context.split("|")
            elif type(item.context) != list:
                item.context = []

            item.context.extend([{"title": config.get_localized_string(30154),  # "Quitar de favoritos"
                                  "action": "delFavourite",
                                  "channel": "favoritos",
                                  "from_title": item.title},
                                 {"title": "Rinomina",
                                  "action": "renameFavourite",
                                  "channel": "favoritos",
                                  "from_title": item.title}
                               ])

            itemlist.append(item)

    return itemlist


def read_favourites():
    favourites_list = []
    if filetools.exists(FAVOURITES_PATH):
        data = filetools.read(FAVOURITES_PATH)

        matches = scrapertools.find_multiple_matches(data, "<favourite([^<]*)</favourite>")
        for match in matches:
            name = scrapertools.find_single_match(match, 'name="([^"]*)')
            thumb = scrapertools.find_single_match(match, 'thumb="([^"]*)')
            data = scrapertools.find_single_match(match, '[^>]*>([^<]*)')
            favourites_list.append((name, thumb, data))

    return favourites_list


def save_favourites(favourites_list):
    raw = '<favourites>' + chr(10)
    for name, thumb, data in favourites_list:
        raw += '    <favourite name="%s" thumb="%s">%s</favourite>' % (name, thumb, data) + chr(10)
    raw += '</favourites>' + chr(10)

    return filetools.write(FAVOURITES_PATH, raw)


def addFavourite(item):
    logger.info()

    # Here through the context menu, you have to recover the action and channel parameters
    if item.from_action:
        item.__dict__["action"] = item.__dict__.pop("from_action")
    if item.from_channel:
        item.__dict__["channel"] = item.__dict__.pop("from_channel")

    favourites_list = read_favourites()
    data = "ActivateWindow(10025,&quot;plugin://plugin.video.%s/?" % config.PLUGIN_NAME + item.tourl() + "&quot;,return)"
    titulo = item.title.replace('"', "'")
    favourites_list.append((titulo, item.thumbnail, data))

    if save_favourites(favourites_list):
        platformtools.dialog_ok(config.get_localized_string(30102), titulo,
                                config.get_localized_string(30108))  # 'Added to favorites'


def delFavourite(item):
    logger.info()

    if item.from_title:
        item.title = item.from_title

    favourites_list = read_favourites()
    for fav in favourites_list[:]:
        if fav[0] == item.title:
            favourites_list.remove(fav)

            if save_favourites(favourites_list):
                platformtools.dialog_ok(config.get_localized_string(30102), item.title,
                                        config.get_localized_string(30105).lower())  # 'Removed to favorites'
                platformtools.itemlist_refresh()
            break


def renameFavourite(item):
    logger.info()

    # Search for the item to rename in favourites.xml
    favourites_list = read_favourites()
    for i, fav in enumerate(favourites_list):
        if fav[0] == item.from_title:
            # open the keyb
            new_title = platformtools.dialog_input(item.from_title, item.title)
            if new_title:
                favourites_list[i] = (new_title, fav[1], fav[2])
                if save_favourites(favourites_list):
                    platformtools.dialog_ok(config.get_localized_string(30102), item.from_title,
                                            "se ha renombrado como:", new_title)  # 'Removed from favorites'
                    platformtools.itemlist_refresh()


##################################################
# Function for old favorites (.txt)
def readbookmark(filepath):
    logger.info()
    import urllib

    bookmarkfile = filetools.open_for_reading(filepath)

    lines = bookmarkfile.readlines()

    try:
        titulo = urllib.unquote_plus(lines[0].strip())
    except:
        titulo = lines[0].strip()

    try:
        url = urllib.unquote_plus(lines[1].strip())
    except:
        url = lines[1].strip()

    try:
        thumbnail = urllib.unquote_plus(lines[2].strip())
    except:
        thumbnail = lines[2].strip()

    try:
        server = urllib.unquote_plus(lines[3].strip())
    except:
        server = lines[3].strip()

    try:
        plot = urllib.unquote_plus(lines[4].strip())
    except:
        plot = lines[4].strip()

    # Added fulltitle and channel fields
    if len(lines) >= 6:
        try:
            fulltitle = urllib.unquote_plus(lines[5].strip())
        except:
            fulltitle = lines[5].strip()
    else:
        fulltitle = titulo

    if len(lines) >= 7:
        try:
            canal = urllib.unquote_plus(lines[6].strip())
        except:
            canal = lines[6].strip()
    else:
        canal = ""

    bookmarkfile.close()

    return canal, titulo, thumbnail, plot, server, url, fulltitle


def check_bookmark(readpath):
    # Create favorite list
    itemlist = []

    if readpath.startswith("special://") and config.is_xbmc():
        readpath = xbmc.translatePath(readpath)

    for fichero in sorted(filetools.listdir(readpath)):
        # Old files (".txt")
        if fichero.endswith(".txt"):
            # Wait 0.1 seconds between files, so that the file names do not overlap
            xbmc.sleep(0.1 * 1000)

            # Itemo of .txt
            canal, titulo, thumbnail, plot, server, url, fulltitle = readbookmark(filetools.join(readpath, fichero))
            if canal == "":
                canal = "favoritos"
            item = Item(channel=canal, action="play", url=url, server=server, title=fulltitle, thumbnail=thumbnail,
                        plot=plot, fanart=thumbnail, fulltitle=fulltitle, folder=False)

            filetools.rename(filetools.join(readpath, fichero), fichero[:-4] + ".old")
            itemlist.append(item)

    # Save favorites
    if itemlist:
        favourites_list = read_favourites()
        for item in itemlist:
            data = "ActivateWindow(10025,&quot;plugin://plugin.video.Stefano/?" + item.tourl() + "&quot;,return)"
            favourites_list.append((item.title, item.thumbnail, data))
        if save_favourites(favourites_list):
            logger.debug("Conversion de txt a xml correcta")


# This will only work when you migrate from previous versions, it no longer exists "bookmarkpath"
try:
    if config.get_setting("bookmarkpath") != "":
        check_bookmark(config.get_setting("bookmarkpath"))
    else:
        logger.info("No existe la ruta a los favoritos de versiones antiguas")
except:
    pass
