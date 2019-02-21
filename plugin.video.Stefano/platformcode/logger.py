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

import inspect
import os

import xbmc
from core import config

loggeractive = (config.get_setting("debug") is True)


def log_enable(active):
    global loggeractive
    loggeractive = active


def encode_log(message=""):
    # Unicode to utf8
    if type(message) == unicode:
        message = message.encode("utf8")

    # All encodings to utf8
    elif type(message) == str:
        message = unicode(message, "utf8", errors="replace").encode("utf8")

    # Objects to string
    else:
        message = str(message)

    return message


def get_caller(message=None):
    module = inspect.getmodule(inspect.currentframe().f_back.f_back)

    # En boxee en ocasiones no detecta el modulo, de este modo lo hacemos manual
    if module is None:
        module = ".".join(
            os.path.splitext(inspect.currentframe().f_back.f_back.f_code.co_filename.split("Stefano")[1])[0].split(
                os.path.sep))[1:]
    else:
        module = module.__name__

    function = inspect.currentframe().f_back.f_back.f_code.co_name

    if module == "__main__":
        module = "Stefano"
    else:
        module = "Stefano." + module
    if message:
        if module not in message:
            if function == "<module>":
                return module + " " + message
            else:
                return module + " [" + function + "] " + message
        else:
            return message
    else:
        if function == "<module>":
            return module
        else:
            return module + "." + function


def info(texto=""):
    if loggeractive:
        xbmc.log(get_caller(encode_log(texto)), xbmc.LOGNOTICE)


def debug(texto=""):
    if loggeractive:
        texto = "    [" + get_caller() + "] " + encode_log(texto)

        xbmc.log("######## DEBUG #########", xbmc.LOGNOTICE)
        xbmc.log(texto, xbmc.LOGNOTICE)


def error(texto=""):
    texto = "    [" + get_caller() + "] " + encode_log(texto)

    xbmc.log("######## ERROR #########", xbmc.LOGERROR)
    xbmc.log(texto, xbmc.LOGERROR)
