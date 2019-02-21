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
logo = os.path.join(addon.getAddonInfo('path').decode('utf-8'), 'resources/nba/logo.png')
blue = os.path.join(addon.getAddonInfo('path').decode('utf-8'), 'resources/blue.png')
red = os.path.join(addon.getAddonInfo('path').decode('utf-8'), 'resources/red.png')

class Score(pyxbmct.AddonDialogWindow):

    def __init__(self, title='[B]NBA[/B]'):
        super(Score, self).__init__(title)
        #Geometry(Width, Height, Rows, Columns)
        #New Addon Windows always have 1280x720 grid
        self.setGeometry(500, 175, 4, 9)
        
        main_bg = pyxbmct.Image(red)
        self.placeControl(main_bg, 0, 0, rowspan=4, columnspan=9, pad_x=-3, pad_y=-3)
        bottom_bg = pyxbmct.Image(blue)
        self.placeControl(bottom_bg, 3, 0, columnspan=6, pad_x=-3, pad_y=-3)
        
        q1header = pyxbmct.Label('[B]1[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(q1header, 0, 1)
        q2header = pyxbmct.Label('[B]2[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(q2header, 0, 2)
        q3header = pyxbmct.Label('[B]3[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(q3header, 0, 3)
        q4header = pyxbmct.Label('[B]4[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(q4header, 0, 4)
        theader = pyxbmct.Label('[B]T[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(theader, 0, 5)        
        
        # Connect a key action (Backspace) to close the window.
        self.connect(pyxbmct.ACTION_NAV_BACK, self.close)
    
    #row, column[, rowspan, columnspan]
    def setup(self, obj):
        print obj
        scores = obj
        #scores = ast.literal_eval(obj)
        
        team1name = pyxbmct.Label('[B]%s[/B]' % scores['Team1']['Name'], alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(team1name, 1, 0)
        team1q1 = pyxbmct.Label('[B]%s[/B]' % scores['Team1']['Score1'], alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(team1q1, 1, 1)
        team1q2 = pyxbmct.Label('[B]%s[/B]' % scores['Team1']['Score2'], alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(team1q2, 1, 2)
        team1q3 = pyxbmct.Label('[B]%s[/B]' % scores['Team1']['Score3'], alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(team1q3, 1, 3)
        team1q4 = pyxbmct.Label('[B]%s[/B]' % scores['Team1']['Score4'], alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(team1q4, 1, 4)
        team1total = pyxbmct.Label('[B]%s[/B]' % scores['Team1']['Total'], alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(team1total, 1, 5)
        
        team2name = pyxbmct.Label('[B]%s[/B]' % scores['Team2']['Name'], alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(team2name, 2, 0)
        team2q1 = pyxbmct.Label('[B]%s[/B]' % scores['Team2']['Score1'], alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(team2q1, 2, 1)
        team2q2 = pyxbmct.Label('[B]%s[/B]' % scores['Team2']['Score2'], alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(team2q2, 2, 2)
        team2q3 = pyxbmct.Label('[B]%s[/B]' % scores['Team2']['Score3'], alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(team2q3, 2, 3)
        team2q4 = pyxbmct.Label('[B]%s[/B]' % scores['Team2']['Score4'], alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(team2q4, 2, 4)
        team2total = pyxbmct.Label('[B]%s[/B]' % scores['Team2']['Total'], alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(team2total, 2, 5)

        gametime = pyxbmct.Label('[B]%s[/B]' % scores['Time'], alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(gametime, 3, 0, columnspan=6)
        
        icon = pyxbmct.Image(logo)
        self.placeControl(icon, 0, 6, rowspan=4, columnspan=3)
        
    def setAnimation(self, control):
        # Set fade animation for all add-on window controls
        control.setAnimations([('WindowOpen', 'effect=fade start=0 end=100 time=500',),
                                ('WindowClose', 'effect=fade start=100 end=0 time=500',)])