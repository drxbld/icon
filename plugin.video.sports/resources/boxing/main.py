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
fanart = xbmc.translatePath(os.path.join(path, "resources/boxing/background.jpg"))

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
        
        #Plays selected highlight clip
        if endpoint:
            if endpoint == 'replays':
                if link:
                    replays.show_qualities(link, title)
                elif page is None:
                    from .. import checks
                    okayd = checks.checkPin()
                    if okayd is False:
                        ok = xbmcgui.Dialog().ok('Sports Guru', 'You need a valid pin in order to use this section of the add-on.')
                        quit()
                    replays.get_games()
                else:
                    replays.get_games(page)
            else:
                raise ValueError('Invalid paramstring: {0}!'.format(paramstring))
        else:
            raise ValueError('Invalid paramstring: {0}!'.format(paramstring))
    else:
        list_item = xbmcgui.ListItem(label='Full-Fight Replays')
        list_item.setArt({'fanart':fanart,'thumb':icon,'poster':icon})
        list_item.setInfo('video',{'plot':'Full-Fight Replays section for Boxing.\n\n[COLOR yellow]Note:[/COLOR] Pin Generation is required to use this section.','title':'Full-Race Replays'})
        url = get_url(sport='boxing', endpoint='replays')
        xbmcplugin.addDirectoryItem(_handle, url, list_item, isFolder=True)
        
        xbmcplugin.addSortMethod(_handle, xbmcplugin.SORT_METHOD_NONE)
        xbmcplugin.endOfDirectory(_handle)
        
if __name__ == '__main__':
    router(sys.argv[2][1:])