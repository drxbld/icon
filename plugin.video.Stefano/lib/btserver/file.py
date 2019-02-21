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
from cursor import Cursor

class File(object):
    def __init__(self, path, base, index, size, fmap, piece_size, client):
        self._client = client
        self.path=path
        self.base=base
        self.index=index
        self.size=size

        self.piece_size=piece_size

        self.full_path= os.path.join(base,path)
        self.first_piece=fmap.piece
        self.offset=fmap.start
        self.last_piece=self.first_piece + max((size-1+fmap.start),0) // piece_size

        self.cursor = None

    def create_cursor(self, offset=None):
        self.cursor = Cursor(self)
        if offset:
            self.cursor.seek(offset)
        return self.cursor

    def map_piece(self, ofs):
        return self.first_piece+ (ofs+self.offset) // self.piece_size , (ofs+self.offset) % self.piece_size

    def update_piece(self, n, data):
        if self.cursor:
            self.cursor.update_piece(n,data)

    def __str__(self):
        return self.path