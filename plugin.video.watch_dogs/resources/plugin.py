import xbmc, xbmcaddon, xbmcgui, xbmcplugin
import os
import time

def installOPENaddon(IDdoADDON):    
    pathTOaddon = os.path.join(xbmc.translatePath('special://home/addons'), IDdoADDON)

    if not os.path.exists(pathTOaddon)==True:
        xbmc.executebuiltin('InstallAddon(%s)' % (IDdoADDON))
        xbmc.executebuiltin('SendClick(11)'), time.sleep(2), xbmcgui.Dialog().ok("Add-on Install", "The addon was not present. Please wait for installation to finish.")
    else:
        pass
    if os.path.exists(pathTOaddon)==True:
        xbmc.executebuiltin('RunAddon(%s)' % (IDdoADDON))
    else:
        xbmcgui.Dialog().ok("Add-on Error", "Could not install or open add-on. Please try again...")

installOPENaddon("plugin.video.WildWest")


def installOPENaddon2(IDdoADDON2):    
    pathTOaddon = os.path.join(xbmc.translatePath('special://home/addons'), IDdoADDON2)

    if not os.path.exists(pathTOaddon)==True:
        xbmc.executebuiltin('InstallAddon(%s)' % (IDdoADDON2))
        xbmc.executebuiltin('SendClick(11)'), time.sleep(2), xbmcgui.Dialog().ok("Add-on Install", "The addon was not present. Please wait for installation to finish.")
    else:
        pass
    if os.path.exists(pathTOaddon)==True:
        xbmc.executebuiltin('RunAddon(%s)' % (IDdoADDON2))
    else:
        xbmcgui.Dialog().ok("Add-on Error", "Could not install or open add-on. Please try again...")

installOPENaddon2("plugin.video.tooontown")