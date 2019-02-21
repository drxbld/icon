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
_path = 'special://home/addons/%s/' % addon_id
field = xbmc.translatePath(os.path.join(_path, "resources/soccer/field.jpg"))

class Players(pyxbmct.AddonFullWindow):

    def __init__(self, title='[B]Line-Ups[/B]'):
        super(Players, self).__init__(title)
        #Geometry(Width, Height, Rows, Columns)
        #New Addon Windows always have 1280x720 grid
        self.setGeometry(1280, 720, 23, 30)
        bg_img = pyxbmct.Image(field)
        self.placeControl(bg_img, 3, 0, columnspan=30, rowspan=20, pad_x=0)
        
        self.progress = xbmcgui.DialogProgressBG()
        self.progress.create("This might take a minute")
        # Connect a key action (Backspace) to close the window.
        self.connect(pyxbmct.ACTION_NAV_BACK, self.close)
        
    #row, column[, rowspan, columnspan]
    def setup(self, lineups_obj):
        team1name   = pyxbmct.Label('[B]%s\n%s[/B]' % (lineups_obj['Team1']['Name'], 
                                                       lineups_obj['Team1']['Record']), alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(team1name, 0, 0, columnspan=10, rowspan=3)
        team1logo   = pyxbmct.Image(lineups_obj['Team1']['Logo'], aspectRatio=1)
        self.placeControl(team1logo, 0, 11, columnspan=2, rowspan=3)
        
        team1formation = pyxbmct.Label(lineups_obj['Team1']['Formation'][2:], alignment=pyxbmct.ALIGN_CENTER, textColor='0xFF000000')
        self.placeControl(team1formation, 3, 11, columnspan=2)
        
        versus      = pyxbmct.Label('[B]VS[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(versus, 0, 14, columnspan=2, rowspan=3)
        
        team2logo   = pyxbmct.Image(lineups_obj['Team2']['Logo'], aspectRatio=1)
        self.placeControl(team2logo, 0, 17, columnspan=2, rowspan=3)
        team2name   = pyxbmct.Label('[B]%s\n%s[/B]' % (lineups_obj['Team2']['Name'], 
                                                       lineups_obj['Team2']['Record']), alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(team2name, 0, 19, columnspan=10, rowspan=3)
        team2formation = pyxbmct.Label(lineups_obj['Team2']['Formation'][2:], alignment=pyxbmct.ALIGN_CENTER, textColor='0xFF000000')
        self.placeControl(team2formation, 3, 17, columnspan=2)
        
        self.progress.update(33, ' It\'ll be worth it, I promise!')
        self.setFormation(lineups_obj['Team1'])
        self.progress.update(66, ' It\'ll be worth it, I promise!')
        self.setFormation(lineups_obj['Team2'])
        self.progress.update(100, 'Done')
        self.progress.close()
        
    def setFormation(self, team):
        
        if team['Players'][6]['Position'] == 'AM' and team['Players'][7]['Position'] == 'LM':
            (team['Players'][6], team['Players'][7], team['Players'][8]) = \
                (team['Players'][7], team['Players'][8], team['Players'][6])
                
        formation = team['Formation']
        parts = formation.split('-')
        if team['Players'][1]['Position'] =='CD-L':
            p1 = team['Players'][1]
            p2 = team['Players'][2]
            p3 = team['Players'][3]
            team['Players'][1] = p3
            team['Players'][2] = p1
            team['Players'][3] = p2
        elif team['Players'][1]['Position'] =='CD':
            p1 = team['Players'][1]
            p2 = team['Players'][2]
            team['Players'][1] = p2
            team['Players'][2] = p1
        if team['Players'][4]['Position'] =='CM-L':
            p1 = team['Players'][4]
            p2 = team['Players'][5]
            p3 = team['Players'][6]
            team['Players'][4] = p3
            team['Players'][5] = p1
            team['Players'][6] = p2
        elif team['Players'][5]['Position'] =='CM-L':
            p1 = team['Players'][5]
            p2 = team['Players'][6]
            p3 = team['Players'][7]
            team['Players'][5] = p3
            team['Players'][6] = p1
            team['Players'][7] = p2
            p4 = team['Players'][8]
            team['Players'][8] = team['Players'][5]
            team['Players'][5] = p4
            
        if team['Players'][5]['Position'] == 'CM':
            team['Players'][5], team['Players'][6] = team['Players'][6], team['Players'][5]
            
        if parts[-1] == '1' and parts[-2] == '1':
            team['Players'][-1], team['Players'][-2] = team['Players'][-2], team['Players'][-1]
        
        if team['Players'][8]['Position'] == 'F' and team['Players'][9]['Position'] == 'LF':
            team['Players'][8], team['Players'][9] = team['Players'][9], team['Players'][8]
        elif team['Players'][8]['Position'] == 'F' and team['Players'][9]['Position'] == 'CF-L':
            f = team['Players'][8]
            cfl = team['Players'][9]
            cfr = team['Players'][10]
            team['Players'][8] = cfl
            team['Players'][9] = cfr
            team['Players'][10] = f
            
        
            
            
        cols_per = 15 / len(parts)
        if team['HomeAway'] == 'home':
            #left-side of the field
            col = 2
            for part in parts:
                #top row of field is 4
                #get total number of rows per player
                space_between = 20 / (int(part) + 1)
                end_space = space_between / 2
                start_row = 3 + end_space + (5-int(part))
                cols_per = 3
                for x in range(0, int(part)):
                    player_icon = pyxbmct.Image(team['Players'][0]['Headshot'], aspectRatio=1)
                    self.placeControl(player_icon, start_row, col-1, rowspan=2)
                    player_name = pyxbmct.Label(team['Players'][0]['Name'], alignment=pyxbmct.ALIGN_CENTER, textColor='0xFF000000')
                    self.placeControl(player_name, start_row+2, col-2, columnspan=3)
                    team['Players'].pop(0)
                    start_row += space_between
                col += cols_per
        else:
            #right-side of the field
            col = 29
            for part in parts:
                #top row of field is 4
                #get total number of rows per player
                space_between = 20 / (int(part) + 1)
                end_space = space_between / 2
                start_row = 20 - end_space - (5-int(part))
                cols_per = 3
                for x in range(0, int(part)):
                    player_icon = pyxbmct.Image(team['Players'][0]['Headshot'], aspectRatio=1)
                    self.placeControl(player_icon, start_row, col-1, rowspan=2)
                    player_name = pyxbmct.Label(team['Players'][0]['Name'], alignment=pyxbmct.ALIGN_CENTER, textColor='0xFF000000')
                    self.placeControl(player_name, start_row+2, col-2, columnspan=3)
                    team['Players'].pop(0)
                    start_row -= space_between
                col -= cols_per