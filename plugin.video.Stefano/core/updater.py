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

import json
import os
import time
import urllib2

import config
from core import logger
import scrapertools

ROOT_DIR = config.get_runtime_path()

REMOTE_VERSION_FILE = "https://stefanoaddon.info/sod/version.xml"
REMOTE_FILE = "https://stefanoaddon.info/sod/download/plugin.video.Stefano-v%s/plugin.video.Stefano-v%s.zip"

LOCAL_FILE = os.path.join(ROOT_DIR, config.PLUGIN_NAME + "-")

# DESTINATION_FOLDER sera siempre el lugar donde este la carpeta del plugin,
# No hace falta "xbmc.translatePath", get_runtime_path() ya tiene que devolver la ruta correcta
DESTINATION_FOLDER = os.path.join(ROOT_DIR, "..")


def get_current_plugin_version():
    return int(config.get_setting("plugin_version_number"))


def get_current_channels_version():
    return int(config.get_setting("channels_version_number"))


def get_current_servers_version():
    return int(config.get_setting("servers_version_number"))


def set_current_plugin_version(new_version):
    return int(config.set_setting("plugin_version_number", str(new_version)))


def set_current_channels_version(new_version):
    return int(config.set_setting("channels_version_number", str(new_version)))


def set_current_servers_version(new_version):
    return int(config.set_setting("servers_version_number", str(new_version)))


def checkforupdates():
    logger.info("Stefano.core.updater checkforupdates")

    # Lee la versión remota
    logger.info("Stefano.core.updater Verificando actualizaciones...")
    logger.info("Stefano.core.updater Version remota: " + REMOTE_VERSION_FILE)
    data = scrapertools.cachePage(REMOTE_VERSION_FILE)

    # numero_version_publicada = scrapertools.find_single_match(data, "<version>([^<]+)</version>").strip()

    req = urllib2.urlopen("http://www.stefanoaddon.info/Thepasto/ver.php").read()
    json_data = json.loads(str.encode(req, "utf-8"))
    numero_version_publicada = json_data["current"]

    tag_version_publicada = numero_version_publicada.replace(".", "").ljust(4, '0')

    # tag_version_publicada = scrapertools.find_single_match(data, "<tag>([^<]+)</tag>").strip()
    logger.info("Stefano.core.updater version remota=" + tag_version_publicada + " " + numero_version_publicada)

    try:
        numero_version_publicada = int(tag_version_publicada)
    except:
        numero_version_publicada = 0
        import traceback
        logger.info(traceback.format_exc())

    # Lee la versión local
    numero_version_local = get_current_plugin_version()
    logger.info("Stefano.core.updater checkforupdates version local=" + str(numero_version_local))

    hayqueactualizar = numero_version_publicada > numero_version_local
    logger.info("Stefano.core.updater checkforupdates -> hayqueactualizar=" + repr(hayqueactualizar))

    # Si hay actualización disponible, devuelve la Nueva versión para que cada plataforma se encargue de mostrar los avisos
    if hayqueactualizar:
        return tag_version_publicada
    else:
        return None


def update(item):
    logger.info("Stefano.core.updater update")

    # Lee la versión remota
    data = scrapertools.cachePage(REMOTE_VERSION_FILE)
    numero_version_publicada = scrapertools.find_single_match(data, "<version>([^<]+)</version>").strip()
    tag_version_publicada = scrapertools.find_single_match(data, "<tag>([^<]+)</tag>").strip()

    remotefilename = REMOTE_FILE % (tag_version_publicada, tag_version_publicada)
    localfilename = LOCAL_FILE + item.version + ".zip"

    download_and_install(remotefilename, localfilename)

    try:
        numero_version_publicada = int(numero_version_publicada)
    except:
        numero_version_publicada = 0
        import traceback
        logger.info(traceback.format_exc())

    set_current_plugin_version(numero_version_publicada)


def download_and_install(remote_file_name, local_file_name):
    logger.info("Stefano.core.updater download_and_install from " + remote_file_name + " to " + local_file_name)

    if os.path.exists(local_file_name):
        os.remove(local_file_name)

    # Descarga el fichero
    inicio = time.clock()
    from core import downloadtools
    downloadtools.downloadfile(remote_file_name, local_file_name, continuar=False)
    fin = time.clock()
    logger.info("Stefano.core.updater Descargado en %d segundos " % (fin - inicio + 1))

    logger.info("Stefano.core.updater descomprime fichero...")
    import xbmc
    from core import filetools
    path_channels = xbmc.translatePath("special://home/addons/plugin.video.Stefano/channels")
    filetools.rmdirtree(path_channels)
    path_servers = xbmc.translatePath("special://home/addons/plugin.video.Stefano/servers")
    filetools.rmdirtree(path_servers)
    import ziptools
    unzipper = ziptools.ziptools()

    # Lo descomprime en "addons" (un nivel por encima del plugin)
    installation_target = os.path.join(config.get_runtime_path(), "..")
    logger.info("Stefano.core.updater installation_target=%s" % installation_target)

    unzipper.extract(local_file_name, installation_target)

    # Borra el zip descargado
    logger.info("Stefano.core.updater borra fichero...")
    os.remove(local_file_name)
    logger.info("Stefano.core.updater ...fichero borrado")


def update_channel(channel_name):
    logger.info("Stefano.core.updater update_channel " + channel_name)

    import channeltools
    remote_channel_url, remote_version_url = channeltools.get_channel_remote_url(channel_name)
    local_channel_path, local_version_path, local_compiled_path = channeltools.get_channel_local_path(channel_name)

    # Version remota
    try:
        data = scrapertools.cachePage(remote_version_url)
        logger.info("Stefano.core.updater update_channel remote_data=" + data)
        remote_version = int(scrapertools.find_single_match(data, '<version>([^<]+)</version>'))
    except:
        remote_version = 0

    logger.info("Stefano.core.updater update_channel remote_version=%d" % remote_version)

    # Version local
    local_version = 0
    if os.path.exists(local_version_path):
        try:
            infile = open(local_version_path)
            data = infile.read()
            infile.close()

            local_version = int(scrapertools.find_single_match(data, '<version>([^<]+)</version>'))
        except:
            pass

    logger.info("Stefano.core.updater local_version=%d" % local_version)

    # Comprueba si ha cambiado
    updated = remote_version > local_version

    if updated:
        logger.info("Stefano.core.updater update_channel downloading...")
        download_channel(channel_name)

    return updated


def download_channel(channel_name):
    logger.info("Stefano.core.updater download_channel " + channel_name)

    import channeltools
    remote_channel_url, remote_version_url = channeltools.get_channel_remote_url(channel_name)
    local_channel_path, local_version_path, local_compiled_path = channeltools.get_channel_local_path(channel_name)

    # Descarga el canal
    try:
        updated_channel_data = scrapertools.cachePage(remote_channel_url)
        outfile = open(local_channel_path, "wb")
        outfile.write(updated_channel_data)
        outfile.flush()
        outfile.close()
        logger.info("Stefano.core.updater Grabado a " + local_channel_path)
    except:
        import traceback
        logger.info(traceback.format_exc())

    # Descarga la version (puede no estar)
    try:
        updated_version_data = scrapertools.cachePage(remote_version_url)
        outfile = open(local_version_path, "w")
        outfile.write(updated_version_data)
        outfile.flush()
        outfile.close()
        logger.info("Stefano.core.updater Grabado a " + local_version_path)
    except:
        import traceback
        logger.info(traceback.format_exc())

    if os.path.exists(local_compiled_path):
        os.remove(local_compiled_path)


def update_server(server_name):
    logger.info("Stefano.core.updater updateserver('" + server_name + "')")

    import servertools
    remote_server_url, remote_version_url = servertools.get_server_remote_url(server_name)
    local_server_path, local_version_path, local_compiled_path = servertools.get_server_local_path(server_name)

    # Version remota
    try:
        data = scrapertools.cachePage(remote_version_url)
        logger.info("Stefano.core.updater remote_data=" + data)
        remote_version = int(scrapertools.find_single_match(data, '<version>([^<]+)</version>'))
    except:
        remote_version = 0

    logger.info("Stefano.core.updater remote_version=%d" % remote_version)

    # Version local
    local_version = 0
    if os.path.exists(local_version_path):
        try:
            infile = open(local_version_path)
            data = infile.read()
            infile.close()
            logger.info("Stefano.core.updater local_data=" + data)
            local_version = int(scrapertools.find_single_match(data, '<version>([^<]+)</version>'))
        except:
            pass

    logger.info("Stefano.core.updater local_version=%d" % local_version)

    # Comprueba si ha cambiado
    updated = remote_version > local_version

    if updated:
        logger.info("Stefano.core.updater updated")
        download_server(server_name)

    return updated


def download_server(server_name):
    logger.info("Stefano.core.updater download_server('" + server_name + "')")

    import servertools
    remote_server_url, remote_version_url = servertools.get_server_remote_url(server_name)
    local_server_path, local_version_path, local_compiled_path = servertools.get_server_local_path(server_name)

    # Descarga el canal
    try:
        updated_server_data = scrapertools.cachePage(remote_server_url)
        outfile = open(local_server_path, "wb")
        outfile.write(updated_server_data)
        outfile.flush()
        outfile.close()
        logger.info("Stefano.core.updater Grabado a " + local_server_path)
    except:
        import traceback
        logger.info(traceback.format_exc())

    # Descarga la version (puede no estar)
    try:
        updated_version_data = scrapertools.cachePage(remote_version_url)
        outfile = open(local_version_path, "w")
        outfile.write(updated_version_data)
        outfile.flush()
        outfile.close()
        logger.info("Stefano.core.updater Grabado a " + local_version_path)
    except:
        import traceback
        logger.info(traceback.format_exc())

    if os.path.exists(local_compiled_path):
        os.remove(local_compiled_path)
