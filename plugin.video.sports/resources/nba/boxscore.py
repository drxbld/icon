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

    def __init__(self, title='[B]Box Score[/B]'):
        super(Score, self).__init__(title)
        #Geometry(Width, Height, Rows, Columns)
        #New Addon Windows always have 1280x720 grid
        
        # Connect a key action (Backspace) to close the window.
        self.connect(pyxbmct.ACTION_NAV_BACK, self.close)
        
    #row, column[, rowspan, columnspan]
    def setup(self, boxscore_obj):
        progress = xbmcgui.DialogProgressBG()
        progress.create("This might take a minute")
        
        row_number  = 11
        row_number += len(boxscore_obj['Team1']['Stats']['Players'])
        row_number += len(boxscore_obj['Team2']['Stats']['Players'])
        self.setGeometry(1280, 720, row_number, 17)
        
        team1name   = pyxbmct.Label('[B]%s\n%s[/B]' % (boxscore_obj['Team1']['Name'], 
                                                       boxscore_obj['Team1']['Record']), alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(team1name, 0, 0, columnspan=6, rowspan=3)
        team1logo   = pyxbmct.Image(boxscore_obj['Team1']['Logo'])
        self.placeControl(team1logo, 0, 6, columnspan=1, rowspan=3)
        
        versus      = pyxbmct.Label('[B]VS[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(versus, 0, 7, columnspan=2, rowspan=3)
        
        team2logo   = pyxbmct.Image(boxscore_obj['Team2']['Logo'])
        self.placeControl(team2logo, 0, 9, columnspan=1, rowspan=3)
        team2name   = pyxbmct.Label('[B]%s\n%s[/B]' % (boxscore_obj['Team2']['Name'], 
                                                       boxscore_obj['Team2']['Record']), alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(team2name, 0, 10, columnspan=7, rowspan=3)

        
        team1header = pyxbmct.Label('[B]%s[/B]' % boxscore_obj['Team1']['Name'], alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(team1header, 3, 0, columnspan=3)
        min1header  = pyxbmct.Label('[B]MIN[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(min1header, 3, 3)
        fg1header  = pyxbmct.Label('[B]FG[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(fg1header, 3, 4)
        threept1header  = pyxbmct.Label('[B]3PT[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(threept1header, 3, 5)
        ft1header  = pyxbmct.Label('[B]FT[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(ft1header, 3, 6)
        oreb1header = pyxbmct.Label('[B]OREB[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(oreb1header, 3, 7)
        dreb1header = pyxbmct.Label('[B]DREB[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(dreb1header, 3, 8)
        reb1header = pyxbmct.Label('[B]REB[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(reb1header, 3, 9)
        ast1header = pyxbmct.Label('[B]AST[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(ast1header, 3, 10)
        stl1header = pyxbmct.Label('[B]STL[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(stl1header, 3, 11)
        blk1header = pyxbmct.Label('[B]BLK[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(blk1header, 3, 12)
        to1header = pyxbmct.Label('[B]TO[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(to1header, 3, 13)
        pf1header = pyxbmct.Label('[B]PF[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(pf1header, 3, 14)
        plusminus1header = pyxbmct.Label('[B]+/-[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(plusminus1header, 3, 15)
        pts1header = pyxbmct.Label('[B]PTS[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(pts1header, 3, 16)
        
        
        for i, player in enumerate(boxscore_obj['Team1']['Stats']['Players']):
            percentage = (4+i) * 100 / row_number
            progress.update(percentage, ' Still working on it ')
            
            playerheader = pyxbmct.Label('[B]%s[/B]' % player['Name'], alignment=pyxbmct.ALIGN_CENTER)
            self.placeControl(playerheader, 4+i, 0, columnspan=2)
            if player.get('Dnp'):
                dnp = pyxbmct.Label('[B]%s[/B]' % player['Dnp'], alignment=pyxbmct.ALIGN_CENTER)
                self.placeControl(dnp, 4+i, 3, columnspan=12)
                nextline = 5+i
                continue
            min1header  = pyxbmct.Label('[B]%s[/B]' % player['Min'], alignment=pyxbmct.ALIGN_CENTER)
            self.placeControl(min1header, 4+i, 3)
            fg1header  = pyxbmct.Label('[B]%s[/B]' % player['Fg'], alignment=pyxbmct.ALIGN_CENTER)
            self.placeControl(fg1header, 4+i, 4)
            threept1header  = pyxbmct.Label('[B]%s[/B]' % player['3Pt'], alignment=pyxbmct.ALIGN_CENTER)
            self.placeControl(threept1header, 4+i, 5)
            ft1header  = pyxbmct.Label('[B]%s[/B]' % player['Ft'], alignment=pyxbmct.ALIGN_CENTER)
            self.placeControl(ft1header, 4+i, 6)
            oreb1header = pyxbmct.Label('[B]%s[/B]' % player['Oreb'], alignment=pyxbmct.ALIGN_CENTER)
            self.placeControl(oreb1header, 4+i, 7)
            dreb1header = pyxbmct.Label('[B]%s[/B]' % player['Dreb'], alignment=pyxbmct.ALIGN_CENTER)
            self.placeControl(dreb1header, 4+i, 8)
            reb1header = pyxbmct.Label('[B]%s[/B]' % player['Reb'], alignment=pyxbmct.ALIGN_CENTER)
            self.placeControl(reb1header, 4+i, 9)
            ast1header = pyxbmct.Label('[B]%s[/B]' % player['Ast'], alignment=pyxbmct.ALIGN_CENTER)
            self.placeControl(ast1header, 4+i, 10)
            stl1header = pyxbmct.Label('[B]%s[/B]' % player['Stl'], alignment=pyxbmct.ALIGN_CENTER)
            self.placeControl(stl1header, 4+i, 11)
            blk1header = pyxbmct.Label('[B]%s[/B]' % player['Blk'], alignment=pyxbmct.ALIGN_CENTER)
            self.placeControl(blk1header, 4+i, 12)
            to1header = pyxbmct.Label('[B]%s[/B]' % player['To'], alignment=pyxbmct.ALIGN_CENTER)
            self.placeControl(to1header, 4+i, 13)
            pf1header = pyxbmct.Label('[B]%s[/B]' % player['Pf'], alignment=pyxbmct.ALIGN_CENTER)
            self.placeControl(pf1header, 4+i, 14)
            plusminus1header = pyxbmct.Label('[B]%s[/B]' % player['Plusminus'], alignment=pyxbmct.ALIGN_CENTER)
            self.placeControl(plusminus1header, 4+i, 15)
            pts1header = pyxbmct.Label('[B]%s[/B]' % player['Pts'], alignment=pyxbmct.ALIGN_CENTER)
            self.placeControl(pts1header, 4+i, 16)
            nextline = 5+i
        
        percentage = nextline * 100 / row_number
        progress.update(percentage, ' Halfway there ')
        
        teamstatlabel = pyxbmct.Label('[B]TEAM[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(teamstatlabel, nextline, 0, columnspan=3)
        teamstatfg = pyxbmct.Label('[B]%s[/B]' % boxscore_obj['Team1']['Stats']['Fg'], alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(teamstatfg, nextline, 4)
        teamstat3pt = pyxbmct.Label('[B]%s[/B]' % boxscore_obj['Team1']['Stats']['3Pt'], alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(teamstat3pt, nextline, 5)
        teamstatft = pyxbmct.Label('[B]%s[/B]' % boxscore_obj['Team1']['Stats']['Ft'], alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(teamstatft, nextline, 6)
        teamstatoreb = pyxbmct.Label('[B]%s[/B]' % boxscore_obj['Team1']['Stats']['Oreb'], alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(teamstatoreb, nextline, 7)
        teamstatdreb = pyxbmct.Label('[B]%s[/B]' % boxscore_obj['Team1']['Stats']['Dreb'], alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(teamstatdreb, nextline, 8)
        teamstatreb = pyxbmct.Label('[B]%s[/B]' % boxscore_obj['Team1']['Stats']['Reb'], alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(teamstatreb, nextline, 9)
        teamstatast = pyxbmct.Label('[B]%s[/B]' % boxscore_obj['Team1']['Stats']['Ast'], alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(teamstatast, nextline, 10)
        teamstatstl = pyxbmct.Label('[B]%s[/B]' % boxscore_obj['Team1']['Stats']['Stl'], alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(teamstatstl, nextline, 11)
        teamstatblk = pyxbmct.Label('[B]%s[/B]' % boxscore_obj['Team1']['Stats']['Blk'], alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(teamstatblk, nextline, 12)
        teamstatto = pyxbmct.Label('[B]%s[/B]' % boxscore_obj['Team1']['Stats']['To'], alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(teamstatto, nextline, 13)
        teamstatpf = pyxbmct.Label('[B]%s[/B]' % boxscore_obj['Team1']['Stats']['Pf'], alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(teamstatpf, nextline, 14)
        
        nextline += 1
        teamstatfgp = pyxbmct.Label('[B]%s[/B]' % boxscore_obj['Team1']['Stats']['Fgp'], alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(teamstatfgp, nextline, 4)
        teamstat3ptp = pyxbmct.Label('[B]%s[/B]' % boxscore_obj['Team1']['Stats']['3Ptp'], alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(teamstat3ptp, nextline, 5)
        teamstatftp = pyxbmct.Label('[B]%s[/B]' % boxscore_obj['Team1']['Stats']['Ftp'], alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(teamstatftp, nextline, 6)
        
        percentage = nextline * 100 / row_number
        progress.update(percentage, ' It\'ll be worth it, I promise ')
        
        nextline += 2
        team2header = pyxbmct.Label('[B]%s[/B]' % boxscore_obj['Team2']['Name'], alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(team2header, nextline, 0, columnspan=3)
        min2header  = pyxbmct.Label('[B]MIN[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(min2header, nextline, 3)
        fg2header  = pyxbmct.Label('[B]FG[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(fg2header, nextline, 4)
        threept2header  = pyxbmct.Label('[B]3PT[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(threept2header, nextline, 5)
        ft2header  = pyxbmct.Label('[B]FT[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(ft2header, nextline, 6)
        oreb2header = pyxbmct.Label('[B]OREB[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(oreb2header, nextline, 7)
        dreb2header = pyxbmct.Label('[B]DREB[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(dreb2header, nextline, 8)
        reb2header = pyxbmct.Label('[B]REB[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(reb2header, nextline, 9)
        ast2header = pyxbmct.Label('[B]AST[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(ast2header, nextline, 10)
        stl2header = pyxbmct.Label('[B]STL[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(stl2header, nextline, 11)
        blk2header = pyxbmct.Label('[B]BLK[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(blk2header, nextline, 12)
        to2header = pyxbmct.Label('[B]TO[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(to2header, nextline, 13)
        pf2header = pyxbmct.Label('[B]PF[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(pf2header, nextline, 14)
        plusminus2header = pyxbmct.Label('[B]+/-[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(plusminus2header, nextline, 15)
        pts2header = pyxbmct.Label('[B]PTS[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(pts2header, nextline, 16)
        nextline += 1
        
        for i, player in enumerate(boxscore_obj['Team2']['Stats']['Players']):
            percentage = (nextline+i) * 100 / row_number
            progress.update(percentage, ' Almost there ')
            
            playerheader = pyxbmct.Label('[B]%s[/B]' % player['Name'], alignment=pyxbmct.ALIGN_CENTER)
            self.placeControl(playerheader, nextline+i, 0, columnspan=2)
            if player.get('Dnp'):
                dnp = pyxbmct.Label('[B]%s[/B]' % player['Dnp'], alignment=pyxbmct.ALIGN_CENTER)
                self.placeControl(dnp, nextline+i, 3, columnspan=12)
                continue
            min1header  = pyxbmct.Label('[B]%s[/B]' % player['Min'], alignment=pyxbmct.ALIGN_CENTER)
            self.placeControl(min1header, nextline+i, 3)
            fg1header  = pyxbmct.Label('[B]%s[/B]' % player['Fg'], alignment=pyxbmct.ALIGN_CENTER)
            self.placeControl(fg1header, nextline+i, 4)
            threept1header  = pyxbmct.Label('[B]%s[/B]' % player['3Pt'], alignment=pyxbmct.ALIGN_CENTER)
            self.placeControl(threept1header, nextline+i, 5)
            ft1header  = pyxbmct.Label('[B]%s[/B]' % player['Ft'], alignment=pyxbmct.ALIGN_CENTER)
            self.placeControl(ft1header, nextline+i, 6)
            oreb1header = pyxbmct.Label('[B]%s[/B]' % player['Oreb'], alignment=pyxbmct.ALIGN_CENTER)
            self.placeControl(oreb1header, nextline+i, 7)
            dreb1header = pyxbmct.Label('[B]%s[/B]' % player['Dreb'], alignment=pyxbmct.ALIGN_CENTER)
            self.placeControl(dreb1header, nextline+i, 8)
            reb1header = pyxbmct.Label('[B]%s[/B]' % player['Reb'], alignment=pyxbmct.ALIGN_CENTER)
            self.placeControl(reb1header, nextline+i, 9)
            ast1header = pyxbmct.Label('[B]%s[/B]' % player['Ast'], alignment=pyxbmct.ALIGN_CENTER)
            self.placeControl(ast1header, nextline+i, 10)
            stl1header = pyxbmct.Label('[B]%s[/B]' % player['Stl'], alignment=pyxbmct.ALIGN_CENTER)
            self.placeControl(stl1header, nextline+i, 11)
            blk1header = pyxbmct.Label('[B]%s[/B]' % player['Blk'], alignment=pyxbmct.ALIGN_CENTER)
            self.placeControl(blk1header, nextline+i, 12)
            to1header = pyxbmct.Label('[B]%s[/B]' % player['To'], alignment=pyxbmct.ALIGN_CENTER)
            self.placeControl(to1header, nextline+i, 13)
            pf1header = pyxbmct.Label('[B]%s[/B]' % player['Pf'], alignment=pyxbmct.ALIGN_CENTER)
            self.placeControl(pf1header, nextline+i, 14)
            plusminus1header = pyxbmct.Label('[B]%s[/B]' % player['Plusminus'], alignment=pyxbmct.ALIGN_CENTER)
            self.placeControl(plusminus1header, nextline+i, 15)
            pts1header = pyxbmct.Label('[B]%s[/B]' % player['Pts'], alignment=pyxbmct.ALIGN_CENTER)
            self.placeControl(pts1header, nextline+i, 16)
            totalline = i + 1
            
        nextline += totalline + 1
        
        percentage = nextline * 100 / row_number
        progress.update(percentage, ' Finishing Touches ')
        
        teamstatlabel = pyxbmct.Label('[B]TEAM[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(teamstatlabel, nextline, 0, columnspan=3)
        teamstatfg = pyxbmct.Label('[B]%s[/B]' % boxscore_obj['Team2']['Stats']['Fg'], alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(teamstatfg, nextline, 4)
        teamstat3pt = pyxbmct.Label('[B]%s[/B]' % boxscore_obj['Team2']['Stats']['3Pt'], alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(teamstat3pt, nextline, 5)
        teamstatft = pyxbmct.Label('[B]%s[/B]' % boxscore_obj['Team2']['Stats']['Ft'], alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(teamstatft, nextline, 6)
        teamstatoreb = pyxbmct.Label('[B]%s[/B]' % boxscore_obj['Team2']['Stats']['Oreb'], alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(teamstatoreb, nextline, 7)
        teamstatdreb = pyxbmct.Label('[B]%s[/B]' % boxscore_obj['Team2']['Stats']['Dreb'], alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(teamstatdreb, nextline, 8)
        teamstatreb = pyxbmct.Label('[B]%s[/B]' % boxscore_obj['Team2']['Stats']['Reb'], alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(teamstatreb, nextline, 9)
        teamstatast = pyxbmct.Label('[B]%s[/B]' % boxscore_obj['Team2']['Stats']['Ast'], alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(teamstatast, nextline, 10)
        teamstatstl = pyxbmct.Label('[B]%s[/B]' % boxscore_obj['Team2']['Stats']['Stl'], alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(teamstatstl, nextline, 11)
        teamstatblk = pyxbmct.Label('[B]%s[/B]' % boxscore_obj['Team2']['Stats']['Blk'], alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(teamstatblk, nextline, 12)
        teamstatto = pyxbmct.Label('[B]%s[/B]' % boxscore_obj['Team2']['Stats']['To'], alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(teamstatto, nextline, 13)
        teamstatpf = pyxbmct.Label('[B]%s[/B]' % boxscore_obj['Team2']['Stats']['Pf'], alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(teamstatpf, nextline, 14)
        
        nextline += 1
        teamstatfgp = pyxbmct.Label('[B]%s[/B]' % boxscore_obj['Team2']['Stats']['Fgp'], alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(teamstatfgp, nextline, 4)
        teamstat3ptp = pyxbmct.Label('[B]%s[/B]' % boxscore_obj['Team2']['Stats']['3Ptp'], alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(teamstat3ptp, nextline, 5)
        teamstatftp = pyxbmct.Label('[B]%s[/B]' % boxscore_obj['Team2']['Stats']['Ftp'], alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(teamstatftp, nextline, 6)
        
        progress.close()