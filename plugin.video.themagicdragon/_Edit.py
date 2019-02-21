import xbmcaddon, base64

Decode = base64.decodestring
MainBase = (Decode('aHR0cDovL3N1cHJlbWFjeS5vcmcudWsvdG9tYnJhaWRlci9kb2dzYm9sbG9ja3MvaG9tZS50eHQ='))
addon = xbmcaddon.Addon('plugin.video.themagicdragon')