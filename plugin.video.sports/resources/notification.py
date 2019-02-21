import xbmcaddon
import requests
import xbmcgui
import pyxbmct
import xbmc
import json
import ast
import sys
import os

try:
    _url = sys.argv[0]
    _handle = int(sys.argv[1])
except:
    #Module is being accessed by service.py
    pass
    
addon_id = 'plugin.video.sports'
addon = xbmcaddon.Addon(id=addon_id)
blue = os.path.join(addon.getAddonInfo('path').decode('utf-8'), 'resources/blue.png')
red = os.path.join(addon.getAddonInfo('path').decode('utf-8'), 'resources/red.png')

class Scores(pyxbmct.AddonDialogWindow):

    def __init__(self, title='[B]Game Update[/B]', sport='nba'):
        super(Scores, self).__init__(title)
        #Geometry(Width, Height, Rows, Columns)
        #New Addon Windows always have 1280x720 grid
        self.setGeometry(300, 155, 3, 5, pos_x=980, pos_y=565)
        main_bg = pyxbmct.Image(red)
        self.placeControl(main_bg, 0, 0, rowspan=3, columnspan=5, pad_x=-3, pad_y=-3)
        bottom_bg = pyxbmct.Image(blue)
        self.placeControl(bottom_bg, 2, 0, columnspan=3, pad_x=-3, pad_y=-3)
        if '.' in sport:
            self.logo = os.path.join(addon.getAddonInfo('path').decode('utf-8'), 'resources/soccer/%s.png' % sport.replace('.',''))
        else:
            self.logo = os.path.join(addon.getAddonInfo('path').decode('utf-8'), 'resources/%s/logo.png' % sport)
        self.display_duration = int(addon.getSetting('Ntimeout')) * 1000
        
        # Connect a key action (Backspace) to close the window.
        self.connect(pyxbmct.ACTION_NAV_BACK, self.close)
    
    #row, column[, rowspan, columnspan]
    def queue(self, games):
        #j_obj = ast.literal_eval(games)
        icon = pyxbmct.Image(self.logo)
        self.placeControl(icon, 0, 3, rowspan=3, columnspan=2)
        
        team1name = pyxbmct.Label('', alignment=pyxbmct.ALIGN_LEFT)
        self.placeControl(team1name, 0, 0, columnspan=3)
        team1score = pyxbmct.Label('', alignment=pyxbmct.ALIGN_RIGHT)
        self.placeControl(team1score, 0, 2)
        team2name = pyxbmct.Label('', alignment=pyxbmct.ALIGN_LEFT)
        self.placeControl(team2name, 1, 0, columnspan=3)
        team2score = pyxbmct.Label('', alignment=pyxbmct.ALIGN_RIGHT)
        self.placeControl(team2score, 1, 2)
        gametime = pyxbmct.Label('', alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(gametime, 2, 0, columnspan=3)
        self.show()
        for game in games:
            team1name.setLabel('[B]%s[/B]' % game['Name1'])
            team1score.setLabel('[B]%s[/B]' % game['Score1'])
            team2name.setLabel('[B]%s[/B]' % game['Name2'])
            team2score.setLabel('[B]%s[/B]' % game['Score2'])
            gametime.setLabel('[B]%s[/B]' % game['Time'])
            xbmc.sleep(self.display_duration)
        self.close()
        
    def setAnimation(self, control):
        # Set fade animation for all add-on window controls
        control.setAnimations([('WindowOpen', 'effect=fade start=0 end=100 time=500',),
                                ('WindowClose', 'effect=fade start=100 end=0 time=500',)])