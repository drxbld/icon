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

class Score(pyxbmct.AddonFullWindow):
    def __init__(self, title='[B]NHL Standings[/B]'):
        super(Score, self).__init__(title)
        #Geometry(Width, Height, Rows, Columns)
        #New Addon Windows always have 1280x720 grid        
        
        # Connect a key action (Backspace) to close the window.
        self.connect(pyxbmct.ACTION_NAV_BACK, self.close)
        
    #row, column[, rowspan, columnspan]
    def setup(self, standings):
        progress = xbmcgui.DialogProgressBG()
        progress.create("This might take a minute")
        percentage = 0
        h = standings.pop('Headers')
        lname = standings.pop('League Name')
        
        rows_needed = len(standings.keys()[0]) + len(standings.keys()[1])
        self.setGeometry(1280, 720, rows_needed, 21)
        startingrow = 0
        for key, conf in standings.iteritems():
            confname = pyxbmct.Label('[B]%s[/B]' % key, alignment=pyxbmct.ALIGN_CENTER)
            self.placeControl(confname, startingrow, 0, columnspan=4)
            offset = 0
            for i, header in enumerate(h):
                tmpheader = pyxbmct.Label('[B]%s[/B]' % header, alignment=pyxbmct.ALIGN_CENTER)
                if header in ['HOME','ROAD']:
                    self.placeControl(tmpheader, startingrow, 4+i+offset, columnspan=2)
                    offset += 1
                else:
                    self.placeControl(tmpheader, startingrow, 4+i+offset)
            startingrow += 1
            for t, team in enumerate(conf):
                tname = pyxbmct.Label(team['Name'], alignment=pyxbmct.ALIGN_CENTER)
                self.placeControl(tname, startingrow+t, 0, columnspan=4)
                offset = 0
                for i, header in enumerate(h):
                    tval = pyxbmct.Label(team[header].strip(), alignment=pyxbmct.ALIGN_CENTER)
                    if header in ['HOME','ROAD']:
                        self.placeControl(tval, startingrow+t, 4+i+offset, columnspan=2)
                        offset += 1
                    else:
                        self.placeControl(tval, startingrow+t, 4+i+offset)
            startingrow += t+1
            percentage += 50
            progress.update(percentage, 'Half-way there!')
        progress.update(100, 'Done')
        progress.close()