import xbmcaddon
import requests
import xbmcgui
import pyxbmct
import xbmc
import json
import ast
import sys
import os

_url = sys.argv[0]
_handle = int(sys.argv[1])
addon_id = 'plugin.video.sports'
addon = xbmcaddon.Addon(id=addon_id)
logo = os.path.join(addon.getAddonInfo('path').decode('utf-8'), 'logo.png')
blue = os.path.join(addon.getAddonInfo('path').decode('utf-8'), 'blue.png')
red = os.path.join(addon.getAddonInfo('path').decode('utf-8'), 'red.png')

class Plays(pyxbmct.AddonFullWindow):

    def __init__(self, title='[B]Play-By-Play[/B]'):
        super(Plays, self).__init__('[B]Play-By-Play - %s[/B]' % title)
        #Geometry(Width, Height, Rows, Columns)
        #New Addon Windows always have 1280x720 grid
        #self.setGeometry(1280, 720, 27, 4)
        self.setGeometry(1280, 720, 27, 15)
        
        teamheader = pyxbmct.Label('[B]Team[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(teamheader, 0, 0)
        timeheader = pyxbmct.Label('[B]Time[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(timeheader, 0, 1)
        scoreheader = pyxbmct.Label('   [B]Score[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(scoreheader, 0, 2)
        playheader = pyxbmct.Label('[B]Play[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(playheader, 0, 3, columnspan=12)
        
        self.listing = pyxbmct.List(_imageWidth=35, _imageHeight=35)
        self.placeControl(self.listing, 1, 0, rowspan=26, columnspan=15)
        
        # Connect a key action (Backspace) to close the window.
        self.connect(pyxbmct.ACTION_NAV_BACK, self.close)
        
        
    #row, column[, rowspan, columnspan]
    def setup(self, obj):
        progress = xbmcgui.DialogProgressBG()
        progress.create("This might take a minute")
        list_items = []
        for play in obj:
            spacing = ''
            test_time = play['Time'].replace('[B]','').replace('[/B]','')
            test_score = play['Score'].replace('[B]','').replace('[/B]','')
            
            #Setup spacing so data appears as columns
            if len(test_time) == 5:
                spacing += '     %s '
            elif len(test_time) == 4:
                spacing += '       %s '
            elif len(test_time) == 3:
                spacing += '         %s '
                
            if len(test_score) == 5:
                spacing += '       %s   '
            elif len(test_score) == 6:
                spacing += '       %s '
            elif len(test_score) == 7:
                spacing += '     %s '
            elif len(test_score) == 8:
                spacing += '     %s'
            elif len(test_score) == 9:
                spacing += '   %s'
                
            spacing += '      %s'
            
            if play['Play'].startswith('End of '):
                play['Play'] = '========== %s ==========' % play['Play']
            list_item = xbmcgui.ListItem(label=spacing % (play['Time'], play['Score'], play['Play']))
            list_item.setArt({'icon':play['Team']})
            list_items.append(list_item)
                
        self.listing.addItems(list_items)
        progress.close()
        
        
    def setAnimation(self, control):
        # Set fade animation for all add-on window controls
        control.setAnimations([('WindowOpen', 'effect=fade start=0 end=100 time=500',),
                                ('WindowClose', 'effect=fade start=100 end=0 time=500',)])