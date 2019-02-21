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




from resources.lib.modules import log_utils
from resources.lib.modules import control
from resources.lib.modules import youtube
from resources.lib.modules import youtube_menu

import os,sys,re,datetime,urlparse

thishandle = int(sys.argv[1])

# initializes as Kids Corner, functions can override based on action and subid.
class yt_index:
    def __init__(self):
        self.action = 'kidscorner'
        self.base_url = 'aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL211YWRkaWJ0dHYva2lkc25hdGlvbi9tYXN0ZXIv'.decode('base64')
        self.mainmenu = 'JXNrbm1haW4udHh0'.decode('base64') % (self.base_url)
        self.submenu  = 'JXMvJXMudHh0'.decode('base64')
        self.default_icon   = 'JXMvaWNvbnMvaWNvbi5wbmc='.decode('base64')
        self.default_fanart = 'JXMvaWNvbnMvZmFuYXJ0LmpwZw=='.decode('base64')

    def init_vars(self, action):
        try:
            if action == 'fitness':
                self.action   = 'fitness'
                self.base_url = 'aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL211YWRkaWJ0dHYvZml0bmVzc3pvbmUvbWFzdGVyLw=='.decode('base64')
                self.mainmenu = 'JXNmem1haW4udHh0'.decode('base64') % (self.base_url)
            elif action == 'legends':
                self.action   = 'legends'
                self.base_url = 'aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL211YWRkaWJ0dHYvbGVnZW5kc2FkZG9uL21hc3Rlci9tZW51Lw=='.decode('base64')
                self.mainmenu = 'JXNpaG1haW4udHh0'.decode('base64') % (self.base_url)
            elif action == 'tvReviews':
                self.action   = 'tvReviews'
                self.base_url = 'aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL211YWRkaWJ0dHYvdGhlY3JpdGljcy9tYXN0ZXIv'.decode('base64')
                self.mainmenu = 'JXN0ZWxldmlzaW9uLnR4dA=='.decode('base64') % (self.base_url)
            elif action == 'movieReviews':
                self.action   = 'movieReviews'
                self.base_url = 'aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL211YWRkaWJ0dHYvdGhlY3JpdGljcy9tYXN0ZXIv'.decode('base64')
                self.mainmenu = 'JXNtb3ZpZXMudHh0'.decode('base64') % (self.base_url)
            self.submenu = self.submenu % (self.base_url, '%s')
            self.default_icon = self.default_icon % (self.base_url)
            self.default_fanart = self.default_fanart % (self.base_url)
        except:
            pass

    def root(self, action):
        try:
            self.init_vars(action)
            menuItems = youtube_menu.youtube_menu().processMenuFile(self.mainmenu)
            for name,section,searchid,subid,playlistid,channelid,videoid,iconimage,fanart,description in menuItems:
                if not subid == 'false': # Means this item points to a submenu
                    youtube_menu.youtube_menu().addMenuItem(name, self.action, subid, iconimage, fanart, description, True)
                elif not searchid == 'false': # Means this is a search term
                    youtube_menu.youtube_menu().addSearchItem(name, searchid, iconimage, fanart)
                elif not videoid == 'false': # Means this is a video id entry
                    youtube_menu.youtube_menu().addVideoItem(name, videoid, iconimage, fanart)
                elif not channelid == 'false': # Means this is a channel id entry
                    youtube_menu.youtube_menu().addChannelItem(name, channelid, iconimage, fanart)
                elif not playlistid == 'false': # Means this is a playlist id entry
                    youtube_menu.youtube_menu().addPlaylistItem(name, playlistid, iconimage, fanart)
                elif not section == 'false': # Means this is a section placeholder/info line
                    youtube_menu.youtube_menu().addSectionItem(name, self.default_icon, self.default_fanart)
            self.endDirectory()
        except:
            pass

    def get(self, action, subid):
        try:
            self.init_vars(action)
            thisMenuFile = self.submenu % (subid)
            menuItems = youtube_menu.youtube_menu().processMenuFile(thisMenuFile)
            for name,section,searchid,subid,playlistid,channelid,videoid,iconimage,fanart,description in menuItems:
                if not subid == 'false': # Means this item points to a submenu
                    youtube_menu.youtube_menu().addMenuItem(name, self.action, subid, iconimage, fanart, description, True)
                elif not searchid == 'false': # Means this is a search term
                    youtube_menu.youtube_menu().addSearchItem(name, searchid, iconimage, fanart)
                elif not videoid == 'false': # Means this is a video id entry
                    youtube_menu.youtube_menu().addVideoItem(name, videoid, iconimage, fanart)
                elif not channelid == 'false': # Means this is a channel id entry
                    youtube_menu.youtube_menu().addChannelItem(name, channelid, iconimage, fanart)
                elif not playlistid == 'false': # Means this is a playlist id entry
                    youtube_menu.youtube_menu().addPlaylistItem(name, playlistid, iconimage, fanart)
                elif not section == 'false': # Means this is a section placeholder/info line
                    youtube_menu.youtube_menu().addSectionItem(name, self.default_icon, self.default_fanart)
            self.endDirectory()
        except:
            pass

    def endDirectory(self):
        control.directory(thishandle, cacheToDisc=True)
