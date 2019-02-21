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

class Forms(pyxbmct.AddonFullWindow):

    def __init__(self, title='[B]Forms[/B]'):
        super(Forms, self).__init__(title)
        #Geometry(Width, Height, Rows, Columns)
        #New Addon Windows always have 1280x720 grid
        
        self.setGeometry(1280, 720, 24, 9)
        
        # Connect a key action (Backspace) to close the window.
        self.connect(pyxbmct.ACTION_NAV_BACK, self.close)
        
    #row, column[, rowspan, columnspan]
    def setup(self, forms_obj):
        progress = xbmcgui.DialogProgressBG()
        progress.create("This might take a minute")
        #Form1
        form1logo   = pyxbmct.Image(forms_obj['Form1']['Logo'], aspectRatio=2)
        self.placeControl(form1logo, 0, 0, rowspan=2)
        form1name   = pyxbmct.Label('[B]%s[/B]' % forms_obj['Form1']['Name'], alignment=pyxbmct.ALIGN_CENTER_Y)
        self.placeControl(form1name, 0, 1, columnspan=6, rowspan=2)
        #Next row
        form1last5  = pyxbmct.Label('[B]LAST FIVE GAMES[/B]')
        form1date   = pyxbmct.Label('[B]DATE[/B]')
        form1comp   = pyxbmct.Label('[B]COMPETITION[/B]')
        self.placeControl(form1last5, 2, 0, columnspan=6)
        self.placeControl(form1date, 2, 6)
        self.placeControl(form1comp, 2, 7, columnspan=2)
        #Now print each game
        for g, game in enumerate(forms_obj['Form1']['Games']):
            gResult = pyxbmct.Label('[B]%s[/B]' % game['Result'])
            self.placeControl(gResult, 3+g, 0)
            t1name = pyxbmct.Label(game['Team1'], alignment=pyxbmct.ALIGN_RIGHT)
            t1logo = pyxbmct.Image(game['Logo1'], aspectRatio=2)
            self.placeControl(t1name, 3+g, 0, columnspan=2)
            self.placeControl(t1logo, 3+g, 2)
            
            score = pyxbmct.Label(game['Score'], alignment=pyxbmct.ALIGN_CENTER_X)
            self.placeControl(score, 3+g, 2, columnspan=2)
            
            t2logo = pyxbmct.Image(game['Logo2'], aspectRatio=2)
            t2name = pyxbmct.Label(game['Team2'], alignment=pyxbmct.ALIGN_LEFT)
            self.placeControl(t2logo, 3+g, 3)
            self.placeControl(t2name, 3+g, 4, columnspan=2)
            
            d = pyxbmct.Label(game['Date'])
            self.placeControl(d, 3+g, 6)
            comp = pyxbmct.Label(game['Competition'])
            self.placeControl(comp, 3+g, 7, columnspan=2)
            
        progress.update(33, ' It\'ll be worth it, I promise!')
        #Form2
        form2logo   = pyxbmct.Image(forms_obj['Form2']['Logo'], aspectRatio=2)
        self.placeControl(form2logo, 8, 0, rowspan=2)
        form2name   = pyxbmct.Label('[B]%s[/B]' % forms_obj['Form2']['Name'], alignment=pyxbmct.ALIGN_CENTER_Y)
        self.placeControl(form2name, 8, 1, columnspan=6, rowspan=2)
        #Next row
        form2last5  = pyxbmct.Label('[B]LAST FIVE GAMES[/B]')
        form2date   = pyxbmct.Label('[B]DATE[/B]')
        form2comp   = pyxbmct.Label('[B]COMPETITION[/B]')
        self.placeControl(form2last5, 10, 0, columnspan=6)
        self.placeControl(form2date, 10, 6)
        self.placeControl(form2comp, 10, 7, columnspan=2)
        #Now print each game
        for g, game in enumerate(forms_obj['Form2']['Games']):
            gResult = pyxbmct.Label('[B]%s[/B]' % game['Result'])
            self.placeControl(gResult, 11+g, 0)
            t1name = pyxbmct.Label(game['Team1'], alignment=pyxbmct.ALIGN_RIGHT)
            t1logo = pyxbmct.Image(game['Logo1'], aspectRatio=2)
            self.placeControl(t1name, 11+g, 0, columnspan=2)
            self.placeControl(t1logo, 11+g, 2)
            
            score = pyxbmct.Label(game['Score'], alignment=pyxbmct.ALIGN_CENTER_X)
            self.placeControl(score, 11+g, 2, columnspan=2)
            
            t2logo = pyxbmct.Image(game['Logo2'], aspectRatio=2)
            t2name = pyxbmct.Label(game['Team2'], alignment=pyxbmct.ALIGN_LEFT)
            self.placeControl(t2logo, 11+g, 3)
            self.placeControl(t2name, 11+g, 4, columnspan=2)
            
            d = pyxbmct.Label(game['Date'])
            self.placeControl(d, 11+g, 6)
            comp = pyxbmct.Label(game['Competition'])
            self.placeControl(comp, 11+g, 7, columnspan=2)
            
        progress.update(66, ' It\'ll be worth it, I promise!')
        h2hrecord = pyxbmct.Label('[B]Head To Head Record[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(h2hrecord, 16, 0, columnspan=2, rowspan=2)
        #Next row
        h2hlast5  = pyxbmct.Label('[B]LAST FIVE GAMES[/B]')
        h2hdate   = pyxbmct.Label('[B]DATE[/B]')
        h2hcomp   = pyxbmct.Label('[B]COMPETITION[/B]')
        self.placeControl(h2hlast5, 18, 0, columnspan=6)
        self.placeControl(h2hdate, 18, 6)
        self.placeControl(h2hcomp, 18, 7, columnspan=2)
        #Head-to-Head
        for g, game in enumerate(forms_obj['H2H']):
            t1name = pyxbmct.Label(game['Team1'], alignment=pyxbmct.ALIGN_RIGHT)
            t1logo = pyxbmct.Image(game['Logo1'], aspectRatio=2)
            self.placeControl(t1name, 19+g, 0, columnspan=2)
            self.placeControl(t1logo, 19+g, 2)
            
            score = pyxbmct.Label(game['Score'], alignment=pyxbmct.ALIGN_CENTER_X)
            self.placeControl(score, 19+g, 2, columnspan=2)
            
            t2logo = pyxbmct.Image(game['Logo2'], aspectRatio=2)
            t2name = pyxbmct.Label(game['Team2'], alignment=pyxbmct.ALIGN_LEFT)
            self.placeControl(t2logo, 19+g, 3)
            self.placeControl(t2name, 19+g, 4, columnspan=2)
            
            d = pyxbmct.Label(game['Date'])
            self.placeControl(d, 19+g, 6)
            comp = pyxbmct.Label(game['Competition'])
            self.placeControl(comp, 19+g, 7, columnspan=2)
        progress.update(100, 'Done')
        progress.close()