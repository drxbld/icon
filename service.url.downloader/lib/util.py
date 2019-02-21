# -*- coding: utf-8 -*-
import os, sys, math
import xbmc, xbmcgui, xbmcaddon

ADDON_ID = 'service.url.downloader'
ADDON = xbmcaddon.Addon()

PROFILE = xbmc.translatePath(ADDON.getAddonInfo('profile').decode('utf-8'))
if not os.path.exists(PROFILE): os.makedirs(PROFILE)

def ERROR(txt='',hide_tb=False,notify=False):
    if isinstance (txt,str): txt = txt.decode("utf-8")
    short = str(sys.exc_info()[1])
    if hide_tb:
        LOG('ERROR: {0} - {1}'.format(txt,short))
        return short
    xbmc.log("_________________________________________________________________________________",2)
    LOG('ERROR: ' + txt)
    import traceback
    tb = traceback.format_exc()
    for l in tb.splitlines(): print '    ' + l
    xbmc.log("_________________________________________________________________________________",2)
    print "`"
    if notify: notify('ERROR','ERROR: {0}'.format(short))
    return short

def LOG(message):
    message = '{0}: {1}'.format(ADDON_ID,message)
    xbmc.log(msg=message.encode("utf-8"), level=xbmc.LOGNOTICE)

def DEBUG_LOG(message):
    if DEBUG(): LOG(message)

def DEBUG():
    return xbmc.getCondVisibility('System.GetBool(debug.showloginfo)')

SIZE_NAMES = ("B","KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
def simpleSize(size):
    """
    Converts bytes to a short user friendly string
    Example: 12345 -> 12.06 KB
    """
    s = 0
    if size > 0:
        i = int(math.floor(math.log(size,1024)))
        p = math.pow(1024,i)
        s = round(size/p,1)
    if (s > 0):
        return '%.1f %s' % (s,SIZE_NAMES[i])
    else:
        return '0B'

def durationToShortText(seconds):
    """
    Converts seconds to a short user friendly string
    Example: 143 -> 2m 23s
    """
    days = int(seconds/86400)
    if days: return '%sd' % days
    left = seconds % 86400
    hours = int(left/3600)
    left = left % 3600
    mins = int(left/60)
    if hours and mins:
        return '%sh %sm' % (hours,mins)
    elif hours:
        return '%sh' % hours
    elif mins:
        return '%sm' % mins
    sec = int(left % 60)
    if sec: return '%ss' % sec
    return '0s'

def freeSpaceString(path):
    free = freeSpace(path)
    return free and '{0} free'.format(simpleSize(free)) or ''
    #return xbmc.getInfoLabel('System.FreeSpace')

def freeSpace(path):
    try:
        st = os.statvfs(path)
        if st.f_frsize:
            return (st.f_frsize * st.f_bavail)
        else:
            return (st.f_bsize * st.f_bavail)
    except:
        return 0

def notify(heading,message,icon=ADDON.getAddonInfo('icon'),time=5000,sound=True):
    try:
        xbmcgui.Dialog().notification(heading,message,icon,time,sound)
    except:
        ERROR()
        LOG('Pre-Gotham Notification: {0}: {1}'.format(repr(heading),repr(message)))
