# -*- coding: utf-8 -*-
# ------------------------------------------------------------
# streamondemand 5
# Copyright 2015 tvalacarta@gmail.com
# http://www.mimediacenter.info/foro/viewforum.php?f=36
#
# Distributed under the terms of GNU General Public License v3 (GPLv3)
# http://www.gnu.org/licenses/gpl-3.0.html
# ------------------------------------------------------------
# This file is part of streamondemand 5.
#
# streamondemand 5 is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# streamondemand 5 is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with streamondemand 5.  If not, see <http://www.gnu.org/licenses/>.
# --------------------------------------------------------------------------------
# Download Tools - Original based from code of VideoMonkey XBMC Plugin
# ---------------------------------------------------------------------------------

import os.path
import re
import socket
import sys
import time
import urllib
import urllib2

import config
from core import logger


def downloadfile(url, nombrefichero, headers=None, silent=False, continuar=False, resumir=True):
    logger.info("url=" + url)
    logger.info("nombrefichero=" + nombrefichero)

    if headers is None:
        headers = []

    progreso = None

    if config.is_xbmc() and nombrefichero.startswith("special://"):
        import xbmc
        nombrefichero = xbmc.translatePath(nombrefichero)

    try:
        # Si no es XBMC, siempre a "Silent"
        from platformcode import platformtools

        # antes
        # f=open(nombrefichero,"wb")
        try:
            import xbmc
            nombrefichero = xbmc.makeLegalFilename(nombrefichero)
        except:
            pass
        logger.info("nombrefichero=" + nombrefichero)

        # El fichero existe y se quiere continuar
        if os.path.exists(nombrefichero) and continuar:
            # try:
            #    import xbmcvfs
            #    f = xbmcvfs.File(nombrefichero)
            #    existSize = f.size(nombrefichero)
            # except:
            f = open(nombrefichero, 'r+b')
            if resumir:
                exist_size = os.path.getsize(nombrefichero)
                logger.info("el fichero existe, size=%d" % exist_size)
                grabado = exist_size
                f.seek(exist_size)
            else:
                exist_size = 0
                grabado = 0

        # el fichero ya existe y no se quiere continuar, se aborta
        elif os.path.exists(nombrefichero) and not continuar:
            logger.info("el fichero existe, no se descarga de nuevo")
            return -3

        # el fichero no existe
        else:
            exist_size = 0
            logger.info("el fichero no existe")

            # try:
            #    import xbmcvfs
            #    f = xbmcvfs.File(nombrefichero,"w")
            # except:
            f = open(nombrefichero, 'wb')
            grabado = 0

        # Crea el diálogo de progreso
        if not silent:
            progreso = platformtools.dialog_progress("plugin", "Download in corso...", url, nombrefichero)

        # Si la plataforma no devuelve un cuadro de diálogo válido, asume modo silencio
        if progreso is None:
            silent = True

        if "|" in url:
            additional_headers = url.split("|")[1]
            if "&" in additional_headers:
                additional_headers = additional_headers.split("&")
            else:
                additional_headers = [additional_headers]

            for additional_header in additional_headers:
                logger.info("additional_header: " + additional_header)
                name = re.findall("(.*?)=.*?", additional_header)[0]
                value = urllib.unquote_plus(re.findall(".*?=(.*?)$", additional_header)[0])
                headers.append([name, value])

            url = url.split("|")[0]
            logger.info("url=" + url)

        # Timeout del socket a 60 segundos
        socket.setdefaulttimeout(60)

        h = urllib2.HTTPHandler(debuglevel=0)
        request = urllib2.Request(url)
        for header in headers:
            logger.info("Header=" + header[0] + ": " + header[1])
            request.add_header(header[0], header[1])

        if exist_size > 0:
            request.add_header('Range', 'bytes=%d-' % (exist_size,))

        opener = urllib2.build_opener(h)
        urllib2.install_opener(opener)
        try:
            connexion = opener.open(request)
        except urllib2.HTTPError, e:
            logger.error("error %d (%s) al abrir la url %s" %
                         (e.code, e.msg, url))
            # print e.code
            # print e.msg
            # print e.hdrs
            # print e.fp
            f.close()
            if not silent:
                progreso.close()
            # El error 416 es que el rango pedido es mayor que el fichero => es que ya está completo
            if e.code == 416:
                return 0
            else:
                return -2

        try:
            totalfichero = int(connexion.headers["Content-Length"])
        except ValueError:
            totalfichero = 1

        if exist_size > 0:
            totalfichero = totalfichero + exist_size

        logger.info("Content-Length=%s" % totalfichero)

        blocksize = 100 * 1024

        bloqueleido = connexion.read(blocksize)
        logger.info("Iniciando descarga del fichero, bloqueleido=%s" % len(bloqueleido))

        maxreintentos = 10

        while len(bloqueleido) > 0:
            try:
                # Escribe el bloque leido
                f.write(bloqueleido)
                grabado += len(bloqueleido)
                percent = int(float(grabado) * 100 / float(totalfichero))
                totalmb = float(float(totalfichero) / (1024 * 1024))
                descargadosmb = float(float(grabado) / (1024 * 1024))

                # Lee el siguiente bloque, reintentando para no parar todo al primer timeout
                reintentos = 0
                while reintentos <= maxreintentos:
                    try:
                        before = time.time()
                        bloqueleido = connexion.read(blocksize)
                        after = time.time()
                        if (after - before) > 0:
                            velocidad = len(bloqueleido) / (after - before)
                            falta = totalfichero - grabado
                            if velocidad > 0:
                                tiempofalta = falta / velocidad
                            else:
                                tiempofalta = 0
                            # logger.info(sec_to_hms(tiempofalta))
                            if not silent:
                                #progreso.update( percent , "Descargando %.2fMB de %.2fMB (%d%%)" % ( descargadosmb , totalmb , percent),"Falta %s - Velocidad %.2f Kb/s" % ( sec_to_hms(tiempofalta) , velocidad/1024 ), os.path.basename(nombrefichero) )
                                progreso.update( percent , "%.2fMB/%.2fMB (%d%%) %.2f Kb/s manca %s " % ( descargadosmb , totalmb , percent , velocidad/1024 , sec_to_hms(tiempofalta)))
                        break
                    except:
                        reintentos += 1
                        logger.info("ERROR en la descarga del bloque, reintento %d" % reintentos)
                        import traceback
                        logger.error(traceback.print_exc())

                # El usuario cancelo la descarga
                try:
                    if progreso.iscanceled():
                        logger.info("Descarga del fichero cancelada")
                        f.close()
                        progreso.close()
                        return -1
                except:
                    pass

                # Ha habido un error en la descarga
                if reintentos > maxreintentos:
                    logger.info("ERROR en la descarga del fichero")
                    f.close()
                    if not silent:
                        progreso.close()

                    return -2

            except:
                import traceback
                logger.error(traceback.print_exc())

                f.close()
                if not silent:
                    progreso.close()

                # platformtools.dialog_ok('Error al descargar' , 'Se ha producido un error' , 'al descargar el archivo')

                return -2

    except:
        if url.startswith("rtmp"):
            error = downloadfileRTMP(url, nombrefichero, silent)
            if error and not silent:
                from platformcode import platformtools
                platformtools.dialog_ok("Download non consentito","Il formato RTMP non","è supportato")
        else:
            import traceback
            from pprint import pprint
            exc_type, exc_value, exc_tb = sys.exc_info()
            lines = traceback.format_exception(exc_type, exc_value, exc_tb)
            for line in lines:
                line_splits = line.split("\n")
                for line_split in line_splits:
                    logger.error(line_split)

    try:
        f.close()
    except:
        pass

    if not silent:
        try:
            progreso.close()
        except:
            pass

    logger.info("Fin descarga del fichero")


def downloadfileRTMP(url,nombrefichero,silent):
  ''' No usa librtmp ya que no siempre está disponible.
      Lanza un subproceso con rtmpdump. En Windows es necesario instalarlo.
      No usa threads así que no muestra ninguna barra de progreso ni tampoco
      se marca el final real de la descarga en el log info.
  '''
  Programfiles = os.getenv('Programfiles')
  if Programfiles:  # Windows
    rtmpdump_cmd = Programfiles + "/rtmpdump/rtmpdump.exe"
    nombrefichero = '"'+nombrefichero+'"'  # Windows necesita las comillas en el nombre
  else:
    rtmpdump_cmd = "/usr/bin/rtmpdump"

  if not os.path.isfile(rtmpdump_cmd) and not silent:
    from platformcode import platformtools
    advertencia = platformtools.dialog_ok( "Manca " + rtmpdump_cmd, "Verificare che sia installato rtmpdump")
    return True

  valid_rtmpdump_options = ["help", "url", "rtmp", "host", "port", "socks", "protocol", "playpath", "playlist", "swfUrl", "tcUrl", "pageUrl", "app", "swfhash", "swfsize", "swfVfy", "swfAge", "auth", "conn", "flashVer", "live", "subscribe", "realtime", "flv", "resume", "timeout", "start", "stop", "token", "jtv", "hashes", "buffer", "skip", "quiet", "verbose", "debug"]   # for rtmpdump 2.4

  url_args = url.split(' ')
  rtmp_url = url_args[0]
  rtmp_args = url_args[1:]

  rtmpdump_args = ["--rtmp", rtmp_url]
  for arg in rtmp_args:
    n = arg.find('=')
    if n < 0: 
      if arg not in valid_rtmpdump_options:
        continue
      rtmpdump_args += ["--"+arg]
    else:
      if arg[:n] not in valid_rtmpdump_options:
        continue
      rtmpdump_args += ["--"+arg[:n], arg[n+1:]]

  try:
    rtmpdump_args = [rtmpdump_cmd] + rtmpdump_args + ["-o", nombrefichero]
    from os import spawnv, P_NOWAIT
    logger.info("Iniciando descarga del fichero: %s" % " ".join(rtmpdump_args))
    rtmpdump_exit = spawnv(P_NOWAIT, rtmpdump_cmd, rtmpdump_args)
    if not silent:
      from platformcode import platformtools
      advertencia = platformtools.dialog_ok( "L'opzione download RTMP è sperimentale", "e il video verrà scaricato in background.", "Non verrà visualizzata alcuna barra di avanzamento.")
  except:
      return True

  return


def sec_to_hms(seconds):
    m, s = divmod(int(seconds), 60)
    h, m = divmod(m, 60)
    return "%02d:%02d:%02d" % (h, m, s)
