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

class Match(pyxbmct.AddonFullWindow):

    def __init__(self, title='[B]Match Stats[/B]'):
        super(Match, self).__init__(title)
        #Geometry(Width, Height, Rows, Columns)
        #New Addon Windows always have 1280x720 grid
        
        # Connect a key action (Backspace) to close the window.
        self.connect(pyxbmct.ACTION_NAV_BACK, self.close)
        
    #row, column[, rowspan, columnspan]
    def setup(self, boxscore_obj):
        progress = xbmcgui.DialogProgressBG()
        progress.create("This might take a minute")
        percentage = 0
        row_number = 5
        row_number += len(boxscore_obj['Team1']['Stats'])
        if len(boxscore_obj['Team1']['Stats']['Players']) > len(boxscore_obj['Team2']['Stats']['Players']):
            row_number += len(boxscore_obj['Team1']['Stats']['Players'])
        else:
            row_number += len(boxscore_obj['Team2']['Stats']['Players'])
        self.setGeometry(1280, 720, row_number, 24)
        
        team1logo   = pyxbmct.Image(boxscore_obj['Team1']['Logo'])
        self.placeControl(team1logo, 0, 0, columnspan=4, rowspan=5)
        team1name   = pyxbmct.Label('[B]%s[/B]' % boxscore_obj['Team1']['Name'], alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(team1name, 0, 3, columnspan=6, rowspan=3)
        
        team1score  = pyxbmct.Label('[B]%s[/B]' % boxscore_obj['Team1']['Score'], alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(team1score, 0, 9, columnspan=2, rowspan=3)
        
        versus      = pyxbmct.Label('[B]VS[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(versus, 0, 11, columnspan=2, rowspan=3)
        
        team2score  = pyxbmct.Label('[B]%s[/B]' % boxscore_obj['Team2']['Score'], alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(team2score, 0, 13, columnspan=2, rowspan=3)
        
        
        team2name   = pyxbmct.Label('[B]%s[/B]' % boxscore_obj['Team2']['Name'], alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(team2name, 0, 14, columnspan=6, rowspan=3)
        team2logo   = pyxbmct.Image(boxscore_obj['Team2']['Logo'])
        self.placeControl(team2logo, 0, 20, columnspan=4, rowspan=5)
        
        teamstatlist = ['Fouls','Yellow Cards','Red Cards','Offsides','Corner Kicks','Saves','Possesion','Shots','On Goal']
        
        for ts, stat in enumerate(teamstatlist):
            if stat == 'Possesion':
                t1val = pyxbmct.Label('{}%'.format(boxscore_obj['Team1']['Stats'][stat]), alignment=pyxbmct.ALIGN_CENTER)
                sName = pyxbmct.Label(stat.replace('ssesion','ssession'), alignment=pyxbmct.ALIGN_CENTER)
                t2val = pyxbmct.Label('{}%'.format(boxscore_obj['Team2']['Stats'][stat]), alignment=pyxbmct.ALIGN_CENTER)
            else:
                t1val = pyxbmct.Label(boxscore_obj['Team1']['Stats'][stat], alignment=pyxbmct.ALIGN_CENTER)
                sName = pyxbmct.Label(stat, alignment=pyxbmct.ALIGN_CENTER)
                t2val = pyxbmct.Label(boxscore_obj['Team2']['Stats'][stat], alignment=pyxbmct.ALIGN_CENTER)
            self.placeControl(t1val, 3+ts, 7)
            self.placeControl(sName, 3+ts, 10, columnspan=4)
            self.placeControl(t2val, 3+ts, 16)
            nextline = 5+ts
        
        fouls = pyxbmct.Label('[B]Fouls[/B]', alignment=pyxbmct.ALIGN_CENTER)
        discipline = pyxbmct.Label('[B]Discipline[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(fouls, nextline, 8, columnspan=2)
        self.placeControl(discipline, nextline, 10, columnspan=2)
        fouls2 = pyxbmct.Label('[B]Fouls[/B]', alignment=pyxbmct.ALIGN_CENTER)
        discipline2 = pyxbmct.Label('[B]Discipline[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(fouls2, nextline, 20, columnspan=2)
        self.placeControl(discipline2, nextline, 22, columnspan=2)
        nextline += 1
        
        team1header = pyxbmct.Label('[B]%s[/B]' % boxscore_obj['Team1']['Name'], alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(team1header, nextline, 0, columnspan=3)
        pf1header = pyxbmct.Label('[B]SH[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(pf1header, nextline, 3)
        blk1header = pyxbmct.Label('[B]SOT[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(blk1header, nextline, 4)
        to1header = pyxbmct.Label('[B]G[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(to1header, nextline, 5)
        ast1header = pyxbmct.Label('[B]A[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(ast1header, nextline, 6)
        stl1header = pyxbmct.Label('[B]OF[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(stl1header, nextline, 7)
        fg1header  = pyxbmct.Label('[B]FC[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(fg1header, nextline, 8)
        threept1header  = pyxbmct.Label('[B]FA[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(threept1header, nextline, 9)
        ft1header  = pyxbmct.Label('[B][COLOR yellow]YC[/COLOR][/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(ft1header, nextline, 10)
        oreb1header = pyxbmct.Label('[B][COLOR red]RC[/COLOR][/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(oreb1header, nextline, 11)
        
        team2header = pyxbmct.Label('[B]%s[/B]' % boxscore_obj['Team2']['Name'], alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(team2header, nextline, 12, columnspan=3)
        pf2header = pyxbmct.Label('[B]SH[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(pf2header, nextline, 15)
        blk2header = pyxbmct.Label('[B]SOT[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(blk2header, nextline, 16)
        to2header = pyxbmct.Label('[B]G[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(to2header, nextline, 17)
        ast2header = pyxbmct.Label('[B]A[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(ast2header, nextline, 18)
        stl2header = pyxbmct.Label('[B]OF[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(stl2header, nextline, 19)
        fg2header  = pyxbmct.Label('[B]FC[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(fg2header, nextline, 20)
        threept2header  = pyxbmct.Label('[B]FA[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(threept2header, nextline, 21)
        ft2header  = pyxbmct.Label('[B][COLOR yellow]YC[/COLOR][/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(ft2header, nextline, 22)
        oreb2header = pyxbmct.Label('[B][COLOR red]RC[/COLOR][/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(oreb2header, nextline, 23)
        
        percentage += 30
        progress.update(percentage, ' It\'ll be worth it, I promise!')
        
        nextline += 1
        orig_nextline = nextline
        goalies = []
        for i, player in enumerate(boxscore_obj['Team1']['Stats']['Players']):
            try:
                stl1header = pyxbmct.Label('[B]%s[/B]' % player['OF'], alignment=pyxbmct.ALIGN_CENTER)
                self.placeControl(stl1header, nextline+i, 7)
            except:
                if player.get('S'):
                    goalies.append(player)
                nextline -= 1
                continue
            playerheader = pyxbmct.Label('[B]%s[/B]' % player['Name'], alignment=pyxbmct.ALIGN_CENTER)
            self.placeControl(playerheader, nextline+i, 0, columnspan=3)
            pf1header = pyxbmct.Label('[B]%s[/B]' % player['SH'], alignment=pyxbmct.ALIGN_CENTER)
            self.placeControl(pf1header, nextline+i, 3)
            blk1header = pyxbmct.Label('[B]%s[/B]' % player['ST'], alignment=pyxbmct.ALIGN_CENTER)
            self.placeControl(blk1header, nextline+i, 4)
            to1header = pyxbmct.Label('[B]%s[/B]' % player['G'], alignment=pyxbmct.ALIGN_CENTER)
            self.placeControl(to1header, nextline+i, 5)
            ast1header = pyxbmct.Label('[B]%s[/B]' % player['A'], alignment=pyxbmct.ALIGN_CENTER)
            self.placeControl(ast1header, nextline+i, 6)
            fg1header  = pyxbmct.Label('[B]%s[/B]' % player['FC'], alignment=pyxbmct.ALIGN_CENTER)
            self.placeControl(fg1header, nextline+i, 8)
            threept1header  = pyxbmct.Label('[B]%s[/B]' % player['FA'], alignment=pyxbmct.ALIGN_CENTER)
            self.placeControl(threept1header, nextline+i, 9)
            reb1header = pyxbmct.Label('[B]%s[/B]' % player['YC'], alignment=pyxbmct.ALIGN_CENTER)
            self.placeControl(reb1header, nextline+i, 10)
            oreb1header = pyxbmct.Label('[B]%s[/B]' % player['RC'], alignment=pyxbmct.ALIGN_CENTER)
            self.placeControl(oreb1header, nextline+i, 11)
            goalie_line = nextline+i+1
        for g, goalie in enumerate(goalies):
            goalieheader = pyxbmct.Label('[B]%s[/B]' % goalie['Name'], alignment=pyxbmct.ALIGN_CENTER)
            self.placeControl(goalieheader, goalie_line+g, 0, columnspan=3)
            gpf1header = pyxbmct.Label('[B]  %s  Saves[/B]' % goalie['S'], alignment=pyxbmct.ALIGN_CENTER)
            self.placeControl(gpf1header, goalie_line+g, 3, columnspan=5)
            
            gfg1header  = pyxbmct.Label('[B]%s[/B]' % goalie['FC'], alignment=pyxbmct.ALIGN_CENTER)
            self.placeControl(gfg1header, goalie_line+g, 8)
            gthreept1header  = pyxbmct.Label('[B]%s[/B]' % goalie['FA'], alignment=pyxbmct.ALIGN_CENTER)
            self.placeControl(gthreept1header, goalie_line+g, 9)
            greb1header = pyxbmct.Label('[B]%s[/B]' % goalie['YC'], alignment=pyxbmct.ALIGN_CENTER)
            self.placeControl(greb1header, goalie_line+g, 10)
            goreb1header = pyxbmct.Label('[B]%s[/B]' % goalie['RC'], alignment=pyxbmct.ALIGN_CENTER)
            self.placeControl(goreb1header, goalie_line+g, 11)
        
        percentage += 30
        progress.update(percentage, ' It\'ll be worth it, I promise!')
            
        nextline = orig_nextline
        goalies = []
        for i, player in enumerate(boxscore_obj['Team2']['Stats']['Players']):
            try:
                stl1header = pyxbmct.Label('[B]%s[/B]' % player['OF'], alignment=pyxbmct.ALIGN_CENTER)
                self.placeControl(stl1header, nextline+i, 19)
            except:
                if player.get('S'):
                    goalies.append(player)
                nextline -= 1
                continue
            playerheader = pyxbmct.Label('[B]%s[/B]' % player['Name'], alignment=pyxbmct.ALIGN_CENTER)
            self.placeControl(playerheader, nextline+i, 12, columnspan=3)
            pf1header = pyxbmct.Label('[B]%s[/B]' % player['SH'], alignment=pyxbmct.ALIGN_CENTER)
            self.placeControl(pf1header, nextline+i, 15)
            blk1header = pyxbmct.Label('[B]%s[/B]' % player['ST'], alignment=pyxbmct.ALIGN_CENTER)
            self.placeControl(blk1header, nextline+i, 16)
            to1header = pyxbmct.Label('[B]%s[/B]' % player['G'], alignment=pyxbmct.ALIGN_CENTER)
            self.placeControl(to1header, nextline+i, 17)
            ast1header = pyxbmct.Label('[B]%s[/B]' % player['A'], alignment=pyxbmct.ALIGN_CENTER)
            self.placeControl(ast1header, nextline+i, 18)
            fg1header  = pyxbmct.Label('[B]%s[/B]' % player['FC'], alignment=pyxbmct.ALIGN_CENTER)
            self.placeControl(fg1header, nextline+i, 20)
            threept1header  = pyxbmct.Label('[B]%s[/B]' % player['FA'], alignment=pyxbmct.ALIGN_CENTER)
            self.placeControl(threept1header, nextline+i, 21)
            reb1header = pyxbmct.Label('[B]%s[/B]' % player['YC'], alignment=pyxbmct.ALIGN_CENTER)
            self.placeControl(reb1header, nextline+i, 22)
            oreb1header = pyxbmct.Label('[B]%s[/B]' % player['RC'], alignment=pyxbmct.ALIGN_CENTER)
            self.placeControl(oreb1header, nextline+i, 23)
            goalie_line = nextline+i+1
        for g, goalie in enumerate(goalies):
            goalie2header = pyxbmct.Label('[B]%s[/B]' % goalie['Name'], alignment=pyxbmct.ALIGN_CENTER)
            self.placeControl(goalie2header, goalie_line+g, 12, columnspan=3)
            gpf2header = pyxbmct.Label('[B]  %s  Saves[/B]' % goalie['S'], alignment=pyxbmct.ALIGN_CENTER)
            self.placeControl(gpf2header, goalie_line+g, 15, columnspan=5)
            
            gfg2header  = pyxbmct.Label('[B]%s[/B]' % goalie['FC'], alignment=pyxbmct.ALIGN_CENTER)
            self.placeControl(gfg2header, goalie_line+g, 20)
            gthreept2header  = pyxbmct.Label('[B]%s[/B]' % goalie['FA'], alignment=pyxbmct.ALIGN_CENTER)
            self.placeControl(gthreept2header, goalie_line+g, 21)
            greb2header = pyxbmct.Label('[B]%s[/B]' % goalie['YC'], alignment=pyxbmct.ALIGN_CENTER)
            self.placeControl(greb2header, goalie_line+g, 22)
            goreb2header = pyxbmct.Label('[B]%s[/B]' % goalie['RC'], alignment=pyxbmct.ALIGN_CENTER)
            self.placeControl(goreb2header, goalie_line+g, 23)
            
        progress.update(100, 'Done')
        progress.close()