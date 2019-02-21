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
import zipfile

from core import logger
import config


class ziptools:

    def extract(self, file, dir, folder_to_extract="", overwrite_question=False, backup=False):
        logger.info("file=%s" % file)
        logger.info("dir=%s" % dir)
        
        if not dir.endswith(':') and not os.path.exists(dir):
            os.mkdir(dir)

        zf = zipfile.ZipFile(file)
        if not folder_to_extract:
            self._createstructure(file, dir)
        num_files = len(zf.namelist())

        for name in zf.namelist():
            logger.info("name=%s" % name)
            if not name.endswith('/'):
                content = zf.read(name)
                name = name.replace('-master', '')
                logger.info("no es un directorio")
                try:
                    (path, filename) = os.path.split(os.path.join(dir, name))
                    logger.info("path=%s" % path)
                    logger.info("name=%s" % name)
                    if folder_to_extract:
                        if path != os.path.join(dir, folder_to_extract):
                            break
                    else:
                        os.makedirs(path)
                except:
                    pass

                if folder_to_extract:
                    outfilename = os.path.join(dir, filename)
                else:
                    outfilename = os.path.join(dir, name)

                logger.info("outfilename=%s" % outfilename)
                try:
                    if os.path.exists(outfilename) and overwrite_question:
                        from platformcode import platformtools
                        dyesno = platformtools.dialog_yesno("Il file esiste già",
                                                            "Il file %s esiste già" \
                                                            ", vuoi sovrascrivere?" \
                                                            % os.path.basename(outfilename))
                        if not dyesno:
                            break
                        if backup:
                            import time
                            import shutil
                            hora_folder = "Copia seguridad [%s]" % time.strftime("%d-%m_%H-%M", time.localtime())
                            backup = os.path.join(config.get_data_path(), 'backups', hora_folder, folder_to_extract)
                            if not os.path.exists(backup):
                                os.makedirs(backup)
                            shutil.copy2(outfilename, os.path.join(backup, os.path.basename(outfilename)))
                        
                    outfile = open(outfilename, 'wb')
                    outfile.write(content)
                except:
                    logger.info("Error en fichero " + name)

    def _createstructure(self, file, dir):
        self._makedirs(self._listdirs(file), dir)

    def create_necessary_paths(filename):
        try:
            (path,name) = os.path.split(filename)
            os.makedirs( path)
        except:
            pass

    def _makedirs(self, directories, basedir):
        for dir in directories:
            curdir = os.path.join(basedir, dir)
            if not os.path.exists(curdir):
                os.mkdir(curdir)

    def _listdirs(self, file):
        zf = zipfile.ZipFile(file)
        dirs = []
        for name in zf.namelist():
            if name.endswith('/'):
                dirs.append(name.replace('-master', ''))

        dirs.sort()
        return dirs
