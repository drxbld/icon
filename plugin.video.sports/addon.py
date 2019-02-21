from urlparse import parse_qsl
from urllib import urlencode
from urllib import unquote
import xbmcplugin
import HTMLParser
import xbmcaddon
import importlib
import urlparse
import requests
import xbmcgui
import time
import json
import xbmc
import sys
import ast
import re

from resources.donations import donations
from resources.soccer import main as soccer
from resources.lfl import main as lfl
from resources.nba import main as nba
from resources.nhl import main as nhl
from resources.mlb import main as mlb
from resources.ufc import main as ufc
from resources.wwe import main as wwe
from resources.live import main as live
from resources.rugby import main as rugby
from resources.xgames import main as xgames
from resources.boxing import main as boxing
from resources.motorsports import main as motorsports
from resources import manager
from resources import wizard

_url = sys.argv[0]
_handle = int(sys.argv[1])
addon_id = 'plugin.video.sports'
addon = xbmcaddon.Addon(id=addon_id)
addonname = addon.getAddonInfo('name')
path = 'special://home/addons/%s/' % addon_id
icon = addon.getAddonInfo('icon')
fanart = addon.getAddonInfo('fanart')

def get_url(**kwargs):
    kwargs = {k: unicode(v).encode('ascii', 'ignore') for k,v in kwargs.iteritems()}
    return '{0}?{1}'.format(_url, urlencode(kwargs))

def router(paramstring):
    valid = eval(addon.getSetting('sgValid').title())
    params = dict(parse_qsl(sys.argv[2][1:]))
    if valid is True:
        if params:
            settings = params.get('action')
            sport = params.get('sport')
            league = params.get('league')
            if settings:
                if sport:
                    manager.load(sport, league)
                elif league == 'reset':
                    wizard.load(False)
                else:
                    donations.load()
            elif sport:
                if sport == 'nba':
                    nba.router(sys.argv[2][1:])
                elif sport == 'soccer':
                    soccer.router(sys.argv[2][1:])
                elif sport == 'nhl':
                    nhl.router(sys.argv[2][1:])
                elif sport == 'mlb':
                    mlb.router(sys.argv[2][1:])
                elif sport == 'wwe':
                    wwe.router(sys.argv[2][1:])
                elif sport == 'rugby':
                    rugby.router(sys.argv[2][1:])
                elif sport == 'lfl':
                    lfl.router(sys.argv[2][1:])
                elif sport == 'live':
                    live.router(sys.argv[2][1:])
                elif sport == 'ufc':
                    ufc.router(sys.argv[2][1:])
                elif sport == 'xgames':
                    xgames.router(sys.argv[2][1:])
                elif sport == 'boxing':
                    boxing.router(sys.argv[2][1:])
                elif sport == 'motorsports':
                    motorsports.router(sys.argv[2][1:])
            else:
                raise ValueError('Invalid paramstring: {0}!'.format(paramstring))
        else:
            welcome_home()
    else:
        dialog = xbmcgui.Dialog()
        ok = dialog.ok('Sports Guru', 'A newer version of the add-on has been released. ' + \
                                      'Until you update you will not be able to access the add-on\'s content.')
        xbmc.executebuiltin("XBMC.Container.Update(path,replace)")
        xbmc.executebuiltin("XBMC.ActivateWindow(Home)")
        
def welcome_home():
    sports = ['Soccer','NBA', 'NHL', 'MLB', 'Rugby', 'WWE', 'UFC', 'X-Games', 'Motorsports', 'Boxing',
              '[COLOR hotpink]Lingerie Football League[/COLOR]','[COLOR yellow]Live Streams[/COLOR]']
    #, '['Football-NFL', 'Golf-PGA/WPGA', 'Tennis-ATP/WTP', 'NCAA Basketball']
    for sport in sports:
        list_item = xbmcgui.ListItem(label=sport)
        list_item.setArt({'fanart': fanart, 'poster': fanart, 'thumb':  icon})
        if sport == '[COLOR hotpink]Lingerie Football League[/COLOR]':
            url = get_url(sport='lfl')
        elif sport == '[COLOR yellow]Live Streams[/COLOR]':
            url = get_url(sport='live')
            list_item.setInfo('video',{'title':'Live Streams',
                              'plot':'Live Streams of all kinds in a schedule format with localized times for your convenience. ' + \
                                     'Internet speed and server-load can influence stream reliability.\n\n' + \
                                     '[COLOR yellow]Note:[/COLOR] Pin Generation is required to use this section.'})
        else:
            url = get_url(sport=sport.replace('-','').lower())
        xbmcplugin.addDirectoryItem(_handle, url, list_item, isFolder=True)
    xbmcplugin.addSortMethod(_handle, xbmcplugin.SORT_METHOD_NONE)
    xbmcplugin.endOfDirectory(_handle)
                
if __name__ == '__main__':
    router(sys.argv[2][1:])