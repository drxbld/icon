from urlparse import parse_qsl
from urllib import urlencode
import xbmcplugin
import xbmcaddon
import xbmcgui
import xbmc
import time
import sys
import ast
import os

import replays

_url = sys.argv[0]
_handle = int(sys.argv[1])
addon_id = 'plugin.video.sports'
addon = xbmcaddon.Addon(id=addon_id)
addonname = addon.getAddonInfo('name')
icon = addon.getAddonInfo('icon')
path = 'special://home/addons/%s/' % addon_id
fanart = xbmc.translatePath(os.path.join(path, "resources/lfl/background.jpg"))

def get_url(**kwargs):
    kwargs = {k: unicode(v).encode('ascii', 'ignore') for k,v in kwargs.iteritems()}
    return '{0}?{1}'.format(_url, urlencode(kwargs))

def router(paramstring):
    params = dict(parse_qsl(sys.argv[2][1:]))
    params.pop('sport')
    if params:
        title           = params.get('title')
        link            = params.get('link')
        endpoint        = params.get('endpoint')
        page            = params.get('page')
        age             = params.get('age')
        searchfor       = params.get('searchfor')
        season          = params.get('season')
        week            = params.get('week')
        teams           = params.get('teams')
        
        #Plays selected highlight clip
        if endpoint:
            if endpoint == 'replays':
                if searchfor is not None:
                    replays.find_quarters(age, title, searchfor, season, week, teams)
                elif page is None:
                    from .. import checks
                    okayd = checks.checkPin()
                    if okayd is False:
                        ok = xbmcgui.Dialog().ok('Sports Guru', 'You need a valid pin in order to use this section of the add-on.')
                        quit()
                    replays.get_games(age)
                else:
                    replays.get_games(age, page)
            else:
                raise ValueError('Invalid paramstring: {0}!'.format(paramstring))
        else:
            raise ValueError('Invalid paramstring: {0}!'.format(paramstring))
    else:
        list_item = xbmcgui.ListItem(label='Most Recent Full-Game Replays')
        list_item.setArt({'fanart':fanart,'thumb':icon,'poster':icon})
        list_item.setInfo('video',{'plot':'','title':'Most Recent Full-Game Replays'})
        url = get_url(sport='lfl', endpoint='replays', age='mostrecent')
        xbmcplugin.addDirectoryItem(_handle, url, list_item, isFolder=True)
        
        list_item = xbmcgui.ListItem(label='Older/Past Seasons Full-Game Replays')
        list_item.setArt({'fanart':fanart,'thumb':icon,'poster':icon})
        list_item.setInfo('video',{'plot':'','title':'Most Recent Full-Game Replays'})
        url = get_url(sport='lfl', endpoint='replays', age='older')
        xbmcplugin.addDirectoryItem(_handle, url, list_item, isFolder=True)
        
        xbmcplugin.addSortMethod(_handle, xbmcplugin.SORT_METHOD_NONE)
        xbmcplugin.endOfDirectory(_handle)
        
if __name__ == '__main__':
    router(sys.argv[2][1:])