# -*- coding: utf-8 -*-
import os, sys, binascii, math
import xbmc, xbmcgui, xbmcaddon

ADDON_ID = 'script.module.url.downloader'
ADDON = xbmcaddon.Addon()
T = ADDON.getLocalizedString

PATH = xbmc.translatePath(ADDON.getAddonInfo('path').decode('utf-8'))
PROFILE = xbmc.translatePath(ADDON.getAddonInfo('profile').decode('utf-8'))
if not os.path.exists(PROFILE): os.makedirs(PROFILE)

def ERROR(txt='',hide_tb=False,notify=False):
    if isinstance (txt,str): txt = txt.decode("utf-8")
    short = str(sys.exc_info()[1])
    if hide_tb:
        LOG('ERROR: {0} - {1}'.format(txt,short))
        return short
    print "_________________________________________________________________________________"
    LOG('ERROR: ' + txt)
    import traceback
    tb = traceback.format_exc()
    for l in tb.splitlines(): print '    ' + l
    print "_________________________________________________________________________________"
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

def getSetting(key,default=None):
    setting = ADDON.getSetting(key)
    return _processSetting(setting,default)

def _processSetting(setting,default):
    if not setting: return default
    if isinstance(default,bool):
        return setting.lower() == 'true'
    elif isinstance(default,float):
        return float(setting)
    elif isinstance(default,int):
        return int(float(setting or 0))
    elif isinstance(default,list):
        if setting: return binascii.unhexlify(setting).split('\0')
        else: return default

    return setting

def setSetting(key,value):
    value = _processSettingForWrite(value)
    ADDON.setSetting(key,value)

def _processSettingForWrite(value):
    if isinstance(value,list):
        value = binascii.hexlify('\0'.join(value))
    elif isinstance(value,bool):
        value = value and 'true' or 'false'
    return str(value)


def busyDialog(func):
    def inner(*args,**kwargs):
        try:
            xbmc.executebuiltin("ActivateWindow(10138)")
            func(*args,**kwargs)
        finally:
            xbmc.executebuiltin("Dialog.Close(10138)")
    return inner

def cleanFilename(filename):
    import string
    import unidecode
    try:
        filename = unidecode.unidecode(filename).decode('utf8')
    except:
        ERROR('Failed to convert chars in filename',hide_tb=True)
    filename = filename.replace(': ',' - ').strip()
    valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
    return ''.join(c if c in valid_chars else '_' for c in filename)

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
        s = round(size/p,2)
    if (s > 0):
        return '%s %s' % (s,SIZE_NAMES[i])
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
    if hours: return '%sh' % hours
    left = left % 3600
    mins = int(left/60)
    if mins: return '%sm' % mins
    sec = int(left % 60)
    if sec: return '%ss' % sec
    return '0s'

def notify(heading,message,icon=ADDON.getAddonInfo('icon'),time=5000,sound=True):
    try:
        xbmcgui.Dialog().notification(heading,message,icon,time,sound)
    except:
        ERROR()
        LOG('Pre-Gotham Notification: {0}: {1}'.format(repr(heading),repr(message)))

