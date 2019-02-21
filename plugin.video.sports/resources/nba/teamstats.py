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

class Stats(pyxbmct.AddonDialogWindow):

    def __init__(self, title='[B]Team Stats[/B]'):
        super(Stats, self).__init__(title)
        #Geometry(Width, Height, Rows, Columns)
        #New Addon Windows always have 1280x720 grid
        self.setGeometry(576, 496, 22, 16)
        # Connect a key action (Backspace) to close the window.
        self.connect(pyxbmct.ACTION_NAV_BACK, self.close)
        
    #row, column[, rowspan, columnspan]
    def setup(self, stats_obj):
        progress = xbmcgui.DialogProgressBG()
        progress.create("This might take a minute")
        c1title = pyxbmct.Label('[B]Matchup[/B]')
        self.placeControl(c1title, 0, 0, columnspan=10, rowspan=2)
        team1name   = pyxbmct.Label('[B]%s[/B]' % (stats_obj['Team1']['Name']), alignment=pyxbmct.ALIGN_RIGHT)
        self.placeControl(team1name, 0, 10, columnspan=3, rowspan=2)

        team2name   = pyxbmct.Label('[B]%s[/B]' % (stats_obj['Team2']['Name']), alignment=pyxbmct.ALIGN_RIGHT)
        self.placeControl(team2name, 0, 13, columnspan=3, rowspan=2)

        teamstatslist = ['FG Made-Attempted','Field Goal %','3PT Made-Attempted','Three Point %','FT Made-Attempted',
                         'Free Throw %','Total Rebounds','Offensive Rebounds','Defensive Rebounds','Assists','Steals',
                         'Blocks','Total Turnovers','Points Off Turnovers','Fast Break Points','Points in Paint',
                         'Personal Fouls','Technical Fouls','Flagrant Fouls']
        over = ['Offensive Rebounds','Defensive Rebounds','Points Off Turnovers','Technical Fouls','Flagrant Fouls']
        for i, ts in enumerate(teamstatslist):
            if ts in over:
                statName = pyxbmct.Label(ts)
                self.placeControl(statName, 2+i, 1, columnspan=9)
            else:
                statName = pyxbmct.Label('[B]%s[/B]' % ts)
                self.placeControl(statName, 2+i, 0, columnspan=10)
                
            t1val = pyxbmct.Label(stats_obj['Team1']['Stats'][ts], alignment=pyxbmct.ALIGN_RIGHT)
            t2val = pyxbmct.Label(stats_obj['Team2']['Stats'][ts], alignment=pyxbmct.ALIGN_RIGHT)
            self.placeControl(t1val, 2+i, 10, columnspan=3)
            self.placeControl(t2val, 2+i, 13, columnspan=3)
        progress.close()