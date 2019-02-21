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
logo = os.path.join(addon.getAddonInfo('path').decode('utf-8'), 'resources/nhl/logo.png')
blue = os.path.join(addon.getAddonInfo('path').decode('utf-8'), 'resources/blue.png')
red = os.path.join(addon.getAddonInfo('path').decode('utf-8'), 'resources/red.png')

"""
http://romanvm.github.io/script.module.pyxbmct/skins.html
class MySkin(pyxbmct.Skin):
    @property
    def title_background_img(self):
        return red
        
    @property
    def close_button_no_focus(self):
        return logo
        
pyxbmct.addonwindow.skin = MySkin()
"""

class Score(pyxbmct.AddonDialogWindow):

    def __init__(self, title='[B]NHL[/B]'):
        super(Score, self).__init__(title)
        #Geometry(Width, Height, Rows, Columns)
        #New Addon Windows always have 1280x720 grid
        self.setGeometry(450, 175, 4, 8)
        
        main_bg = pyxbmct.Image(red)
        self.placeControl(main_bg, 0, 0, rowspan=4, columnspan=8, pad_x=-3, pad_y=-3)
        bottom_bg = pyxbmct.Image(blue)
        self.placeControl(bottom_bg, 3, 0, columnspan=5, pad_x=-3, pad_y=-3)
        
        p1header = pyxbmct.Label('[B]1[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(p1header, 0, 1)
        p2header = pyxbmct.Label('[B]2[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(p2header, 0, 2)
        p3header = pyxbmct.Label('[B]3[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(p3header, 0, 3)
        theader = pyxbmct.Label('[B]T[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(theader, 0, 4)        
        
        # Connect a key action (Backspace) to close the window.
        self.connect(pyxbmct.ACTION_NAV_BACK, self.close)
    
    #row, column[, rowspan, columnspan]
    def setup(self, obj):
        scores = obj
        #scores = ast.literal_eval(obj)
        
        team1name = pyxbmct.Label('[B]%s[/B]' % scores['Team1']['Name'], alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(team1name, 1, 0)
        team1p1 = pyxbmct.Label('[B]%s[/B]' % scores['Team1']['Score1'], alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(team1p1, 1, 1)
        team1p2 = pyxbmct.Label('[B]%s[/B]' % scores['Team1']['Score2'], alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(team1p2, 1, 2)
        team1p3 = pyxbmct.Label('[B]%s[/B]' % scores['Team1']['Score3'], alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(team1p3, 1, 3)
        team1total = pyxbmct.Label('[B]%s[/B]' % scores['Team1']['Total'], alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(team1total, 1, 4)
        
        team2name = pyxbmct.Label('[B]%s[/B]' % scores['Team2']['Name'], alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(team2name, 2, 0)
        team2p1 = pyxbmct.Label('[B]%s[/B]' % scores['Team2']['Score1'], alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(team2p1, 2, 1)
        team2p2 = pyxbmct.Label('[B]%s[/B]' % scores['Team2']['Score2'], alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(team2p2, 2, 2)
        team2p3 = pyxbmct.Label('[B]%s[/B]' % scores['Team2']['Score3'], alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(team2p3, 2, 3)
        team2total = pyxbmct.Label('[B]%s[/B]' % scores['Team2']['Total'], alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(team2total, 2, 4)

        gametime = pyxbmct.Label('[B]%s[/B]' % scores['Time'], alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(gametime, 3, 0, columnspan=5)
        
        icon = pyxbmct.Image(logo)
        self.placeControl(icon, 0, 5, rowspan=4, columnspan=3)
        
    def setAnimation(self, control):
        # Set fade animation for all add-on window controls
        control.setAnimations([('WindowOpen', 'effect=fade start=0 end=100 time=500',),
                                ('WindowClose', 'effect=fade start=100 end=0 time=500',)])