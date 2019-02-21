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
                 

import os

import config
import jsontools
from core import logger
import scrapertools

DEFAULT_UPDATE_URL = "https://raw.githubusercontent.com/stesev1/channels/master/channels/"


def str_to_bool(s):
    if s == 'true':
        return True
    elif s == 'false' or s == '':
        return False
    else:
        raise ValueError("Cannot covert '%s' to a bool" % s)


def is_adult(channel_name):
    logger.info("channel_name=" + channel_name)

    channel_parameters = get_channel_parameters(channel_name)

    return channel_parameters["adult"]


def get_channel_parameters(channel_name):
    # logger.info("streamondemand.core.channeltools get_channel_parameters channel_name="+channel_name)
    channel_xml = os.path.join(config.get_runtime_path(), 'channels', channel_name+".xml")

    if os.path.exists(channel_xml):
        # logger.info("channel_name+".xml found")

        infile = open(channel_xml, "rb")
        data = infile.read()
        infile.close()

        channel_parameters = dict()
        channel_parameters["title"] = scrapertools.find_single_match(data, "<name>([^<]*)</name>")
        channel_parameters["channel"] = scrapertools.find_single_match(data, "<id>([^<]*)</id>")
        channel_parameters["active"] = str_to_bool(scrapertools.find_single_match(data, "<active>([^<]*)</active>"))
        channel_parameters["adult"] = str_to_bool(scrapertools.find_single_match(data, "<adult>([^<]*)</adult>"))
        channel_parameters["language"] = scrapertools.find_single_match(data, "<language>([^<]*)</language>")
        channel_parameters["version"] = scrapertools.find_single_match(data, "<version>([^<]*)</version>")

        # Imagenes: se admiten url y archivos locales dentro de "resources/images"
        channel_parameters["thumbnail"] = scrapertools.find_single_match(data, "<thumbnail>([^<]*)</thumbnail>")
        channel_parameters["bannermenu"] = scrapertools.find_single_match(data, "<bannermenu>([^<]*)</bannermenu>")
        channel_parameters["fanart"] = scrapertools.find_single_match(data, "<fanart>([^<]*)</fanart>")

        if channel_parameters["thumbnail"] and "://" not in channel_parameters["thumbnail"]:
            channel_parameters["thumbnail"] = os.path.join(config.get_runtime_path(), "resources", "images", "squares",
                                                           channel_parameters["thumbnail"])
        if channel_parameters["bannermenu"] and "://" not in channel_parameters["bannermenu"]:
            channel_parameters["bannermenu"] = os.path.join(config.get_runtime_path(), "resources", "images",
                                                            "bannermenu", channel_parameters["bannermenu"])
        if channel_parameters["fanart"] and "://" not in channel_parameters["fanart"]:
            channel_parameters["fanart"] = os.path.join(config.get_runtime_path(), "resources", "images", "fanart",
                                                        channel_parameters["fanart"])

        channel_parameters["update_url"] = scrapertools.find_single_match(data, "<update_url>([^<]*)</update_url>")
        if channel_parameters["update_url"] == "":
            channel_parameters["update_url"] = DEFAULT_UPDATE_URL

        include_in_global_search = scrapertools.find_single_match(
            data, "<include_in_global_search>([^<]*)</include_in_global_search>")

        if include_in_global_search in ["", "true"]:
            channel_parameters["include_in_global_search"] = True
        else:
            channel_parameters["include_in_global_search"] = False

        category_list = []
        matches = scrapertools.find_multiple_matches(data, "<category>([^<]*)</category>")
        for match in matches:
            category_list.append(match)

        channel_parameters["categories"] = category_list

        # Obtenemos si el canal tiene opciones de configuración
        channel_parameters["has_settings"] = False
        # esta regex devuelve 2 valores por elemento <settings>, el contenido del propio nodo y un \t, por lo que hay
        # posteriormente coger solo el valor del indice 0.
        matches = scrapertools.find_multiple_matches(data, "<settings>((.|\n)*?)<\/settings>")
        for match in matches:
            _id = scrapertools.find_single_match(match[0], "<id>([^<]*)</id>")
            if _id and "include_in_" not in _id:
                channel_parameters["has_settings"] = True
                break

        # Inicio - condiciones para mostrar canal compatible
        python_condition = scrapertools.find_single_match(data, "<python>([^<]*)</python>")
        if python_condition:
            import sys

            def versiontuple(v):
                return tuple(map(int, (v.split("."))))

            if sys.version_info < versiontuple(python_condition):
                python_compatible = False
            else:
                python_compatible = True
        else:
            python_compatible = True

        addon_version_condition = scrapertools.find_single_match(data, "<addon_version>([^<]*)</addon_version>")
        if addon_version_condition:
            import versiontools
            addon_version = int(addon_version_condition.replace(".", "").ljust(len(str(
                versiontools.get_current_plugin_version())), '0'))
            if versiontools.get_current_plugin_version() < addon_version:
                addon_version_compatible = False
            else:
                addon_version_compatible = True
        else:
            addon_version_compatible = True

        channel_parameters["compatible"] = True

        if not python_compatible or not addon_version_compatible:
            channel_parameters["compatible"] = False
        # Fin - condiciones para mostrar canal compatible

        logger.info(channel_name + " -> " + repr(channel_parameters))

    else:
        logger.info(channel_name + ".xml NOT found")

        channel_parameters = dict()
        channel_parameters["adult"] = False
        channel_parameters["update_url"] = DEFAULT_UPDATE_URL

    return channel_parameters



def get_channel_json(channel_name):
    # logger.info("channel_name="+channel_name)
    channel_xml = os.path.join(config.get_runtime_path(), 'channels', channel_name + ".xml")
    channel_json = jsontools.xmlTojson(channel_xml)
    return channel_json['channel']


def get_channel_controls_settings(channel_name):
    # logger.info("channel_name="+channel_name)
    dict_settings = {}
    list_controls = []

    settings = get_channel_json(channel_name)['settings']
    if type(settings) == list:
        list_controls = settings
    else:
        list_controls.append(settings)

    # Conversion de str a bool, etc...
    for c in list_controls:
        if 'id' not in c or 'type' not in c or 'default' not in c:
            # Si algun control de la lista  no tiene id, type o default lo ignoramos
            continue

        if 'enabled' not in c or c['enabled'] is None:
            c['enabled'] = True
        else:
            if c['enabled'].lower() == "true":
                c['enabled'] = True
            elif c['enabled'].lower() == "false":
                c['enabled'] = False

        if 'visible' not in c or c['visible'] is None:
            c['visible'] = True

        else:
            if c['visible'].lower() == "true":
                c['visible'] = True
            elif c['visible'].lower() == "false":
                c['visible'] = False

        if c['type'] == 'bool':
            c['default'] = (c['default'].lower() == "true")

        if unicode(c['default']).isnumeric():
            c['default'] = int(c['default'])

        dict_settings[c['id']] = c['default']

    return list_controls, dict_settings


def get_channel_setting(name, channel):
    """
    Retorna el valor de configuracion del parametro solicitado.

    Devuelve el valor del parametro 'name' en la configuracion propia del canal 'channel'.

    Si se especifica el nombre del canal busca en la ruta \addon_data\plugin.video.pelisalacarta\settings_channels el
    archivo channel_data.json y lee el valor del parametro 'name'. Si el archivo channel_data.json no existe busca en la
    carpeta channels el archivo channel.xml y crea un archivo channel_data.json antes de retornar el valor solicitado.


    @param name: nombre del parametro
    @type name: str
    @param channel: nombre del canal
    @type channel: str

    @return: El valor del parametro 'name'
    @rtype: str

    """
    # Creamos la carpeta si no existe
    if not os.path.exists(os.path.join(config.get_data_path(), "settings_channels")):
        os.mkdir(os.path.join(config.get_data_path(), "settings_channels"))

    file_settings = os.path.join(config.get_data_path(), "settings_channels", channel+"_data.json")
    dict_settings = {}
    dict_file = {}
    if os.path.exists(file_settings):
        # Obtenemos configuracion guardada de ../settings/channel_data.json
        try:
            dict_file = jsontools.load_json(open(file_settings, "rb").read())
            if isinstance(dict_file, dict) and 'settings' in dict_file:
                dict_settings = dict_file['settings']
        except EnvironmentError:
            logger.error("ERROR al leer el archivo: %s" % file_settings)
    
    if not dict_settings or name not in dict_settings:
        # Obtenemos controles del archivo ../channels/channel.xml
        try:
            list_controls, default_settings = get_channel_controls_settings(channel)
        except:
            default_settings = {}

        if name in default_settings:  # Si el parametro existe en el channel.xml creamos el channel_data.json
            default_settings.update(dict_settings)
            dict_settings = default_settings
            dict_file['settings'] = dict_settings
            # Creamos el archivo ../settings/channel_data.json
            json_data = jsontools.dump_json(dict_file)
            try:
                open(file_settings, "wb").write(json_data)
            except EnvironmentError:
                logger.error("ERROR al salvar el archivo: %s" % file_settings)

    # Devolvemos el valor del parametro local 'name' si existe, si no se devuelve None
    return dict_settings.get(name, None)


def set_channel_setting(name, value, channel):
    """
    Fija el valor de configuracion del parametro indicado.

    Establece 'value' como el valor del parametro 'name' en la configuracion propia del canal 'channel'.
    Devuelve el valor cambiado o None si la asignacion no se ha podido completar.

    Si se especifica el nombre del canal busca en la ruta \addon_data\plugin.video.streamondemand\settings_channels el archivo channel_data.json
    y establece el parametro 'name' al valor indicado por 'value'. 
    Si el parametro 'name' no existe lo añade, con su valor, al archivo correspondiente.

    @param name: nombre del parametro
    @type name: str
    @param value: valor del parametro
    @type value: str
    @param channel: nombre del canal
    @type channel: str

    @return: 'value' en caso de que se haya podido fijar el valor y None en caso contrario
    @rtype: str, None

    """
    # Creamos la carpeta si no existe
    if not os.path.exists(os.path.join(config.get_data_path(), "settings_channels")):
        os.mkdir(os.path.join(config.get_data_path(), "settings_channels"))

    file_settings = os.path.join(config.get_data_path(), "settings_channels", channel+"_data.json")
    dict_settings = {}

    dict_file = None

    if os.path.exists(file_settings):
        # Obtenemos configuracion guardada de ../settings/channel_data.json
        try:
            dict_file = jsontools.load_json(open(file_settings, "r").read())
            dict_settings = dict_file.get('settings', {})
        except EnvironmentError:
            logger.error("ERROR al leer el archivo: %s" % file_settings)

    dict_settings[name] = value

    # comprobamos si existe dict_file y es un diccionario, sino lo creamos
    if dict_file is None or not dict_file:
        dict_file = {}

    dict_file['settings'] = dict_settings

    # Creamos el archivo ../settings/channel_data.json
    try:
        json_data = jsontools.dump_json(dict_file)
        open(file_settings, "w").write(json_data)
    except EnvironmentError:
        logger.error("ERROR al salvar el archivo: %s" % file_settings)
        return None

    return value


def get_channel_module(channel_name, package="channels"):
    # Sustituye al que hay en servertools.py ...
    # ...pero añade la posibilidad de incluir un paquete diferente de "channels"
    if not "." in channel_name:
      channel_module = __import__('%s.%s' % (package,channel_name), None, None, ['%s.%s' % (package,channel_name)])
    else:
      channel_module = __import__(channel_name, None, None, [channel_name])
    return channel_module


def get_channel_remote_url(channel_name):

    channel_parameters = get_channel_parameters(channel_name)
    remote_channel_url = channel_parameters["update_url"]+channel_name+".py"
    remote_version_url = channel_parameters["update_url"]+channel_name+".xml" 

    logger.info("remote_channel_url=" + remote_channel_url)
    logger.info("remote_version_url=" + remote_version_url)
    
    return remote_channel_url, remote_version_url


def get_channel_local_path(channel_name):

    if channel_name != "channelselector":
        local_channel_path = os.path.join(config.get_runtime_path(), 'channels', channel_name + ".py")
        local_version_path = os.path.join(config.get_runtime_path(), 'channels', channel_name + ".xml")
        local_compiled_path = os.path.join(config.get_runtime_path(), 'channels', channel_name + ".pyo")
    else:
        local_channel_path = os.path.join(config.get_runtime_path(), channel_name + ".py")
        local_version_path = os.path.join(config.get_runtime_path(), channel_name + ".xml")
        local_compiled_path = os.path.join(config.get_runtime_path(), channel_name + ".pyo")

    logger.info("local_channel_path=" + local_channel_path)
    logger.info("local_version_path=" + local_version_path)
    logger.info("local_compiled_path=" + local_compiled_path)

    return local_channel_path, local_version_path, local_compiled_path
