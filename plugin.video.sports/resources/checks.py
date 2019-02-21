import xbmcaddon
import requests
import xbmcgui
import xbmc
import re
import os

addon_id = 'plugin.video.sports'
_addon = xbmcaddon.Addon(id=addon_id)
dialog = xbmcgui.Dialog()

def validate(firstTime=False):
    sFile = xbmc.translatePath('special://masterprofile/sources.xml')
    with open(sFile, "rb") as sf:
        sources = re.compile('<path.+?>(.+?)</path>').findall(sf.read())
    wrongSource = False
    rSrc = 'http://streamarmy.co.uk/lucy/'
    if rSrc+'repo' not in sources and rSrc+'repo/' not in sources:
        wrongSource = True
    
    REPO = xbmc.translatePath(os.path.join('special://home/addons','repository.caffeinated'))
    if not os.path.exists(REPO) or wrongSource:
        remove = ['repository.caffeinated', 'plugin.video.sports']
        bad = any(xbmc.getCondVisibility('System.HasAddon(%s)' % (addon)) for addon in remove)
        if bad:
            import shutil
            remove_these = [xbmc.translatePath(os.path.join('special://home/addons/%s' % addon))
                            for addon in remove if xbmc.getCondVisibility('System.HasAddon(%s)' % addon)]
            for bad_apple in remove_these:
                shutil.rmtree(bad_apple)
            xbmc.executebuiltin("UpdateAddonRepos")
            xbmc.executebuiltin("UpdateLocalAddons")
            ok = dialog.ok('Sports Guru', 'You don\'t have the official source and/or repo. ' + \
                                          'Please use http://streamarmy.co.uk/lucy/repo/ to ' + \
                                          'install the repo & add-on. Type the address EXACTLY AS-IS. ' + \
                                          'Kodi will now force-restart.')
            os._exit(1)
        else:
            return True
    else:
        version = _addon.getAddonInfo('version').replace('v','')
        if firstTime is False:
            hosted = requests.get('https://pastebin.com/raw/67pJd9n6').text
            if version != hosted:
                ok = dialog.ok('Sports Guru', 'A newer version of the add-on has been released. ' + \
                                              'Please update or else the add-on will no longer work. ' + \
                                              'If you have auto-updates turned on and just started Kodi, ' + \
                                              'then this message is likely indicating the add-on has just updated, ' + \
                                              'so you need not worry. If you use the notification service though, ' + \
                                              'you may want to restart Kodi.')
                _addon.setSetting('sgValid', 'false')
                return False
            else:
                _addon.setSetting('sgValid', 'true')
                return True
                
def checkPin():
    pin_api = requests.Session()
    currentpin = _addon.getSetting('pin')
    if currentpin == 'EXPIRED':
        ok = dialog.ok("Sports Guru","Please visit [COLOR yellow]https://pinsystem.co.uk/sportsguru[/COLOR] to generate a Pin to access Sports Guru's video content, then enter it after clicking ok. You may need to request a pin twice.")
        if ok > 0:
            string = ''
            keyboard = xbmc.Keyboard(string, 'Please Enter Pin Generated From Website [COLOR red](Case Sensitive)[/COLOR]')
            keyboard.doModal()
            if keyboard.isConfirmed() == 1:
                string = keyboard.getText()
                if keyboard.isConfirmed() == 1:
                    if len(string) > 1:
                        currentpin = string
                        _addon.setSetting('pin', currentpin)
                        #To get an idea of how many people are actually using the addon
                        increment = pin_api.get('http://hook.io/luciferonkodi/counter?event=magicButton').json()
                        print 'Pin count: ' + str(increment['result'])
                        return checkPin()
                    else: return False
                else: return False
            else: return False
        else: return False
    elif not 'EXPIRED' in currentpin:
        endpoint = 'https://pinsystem.co.uk/service.php?code=%s&plugin=RnVja1lvdSE' % currentpin
        link = pin_api.get(endpoint).text
        if len(link) < 3 or 'Pin Expired' in link:
            _addon.setSetting('pin','EXPIRED')
            return checkPin()
        else:
            return True