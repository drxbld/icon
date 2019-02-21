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

class Score(pyxbmct.AddonFullWindow):

    def __init__(self, title='[B]Box Score[/B]'):
        super(Score, self).__init__(title)
        #Geometry(Width, Height, Rows, Columns)
        #New Addon Windows always have 1280x720 grid
        #self.setGeometry(1280, 720, 27, 17)
        
        self.team1 = []
        self.team2 = []
        
        # Connect a key action (Backspace) to close the window.
        self.connect(pyxbmct.ACTION_NAV_BACK, self.close)
        
    #row, column[, rowspan, columnspan]
    def setup(self, boxscore_obj):
        self.row_number = 3 + 4
        #Add the number of players from whatever team has the most players
        if len(boxscore_obj['Team1']['Stats']['Players']) > len(boxscore_obj['Team2']['Stats']['Players']):
            self.row_number += len(boxscore_obj['Team1']['Stats']['Players'])
        else:
            self.row_number += len(boxscore_obj['Team2']['Stats']['Players'])
        if len(boxscore_obj['Team1']['Stats']['Scratches']) > len(boxscore_obj['Team2']['Stats']['Scratches']):
            self.row_number += len(boxscore_obj['Team1']['Stats']['Scratches'])
        else:
            self.row_number += len(boxscore_obj['Team2']['Stats']['Scratches'])
        self.setGeometry(1280, 720, self.row_number, 20)
        #3 rows for top head-to-head banner
        #4 rows for team stats - team1, team1 percentages, team2, team2 percentages
        #Now add 1 row for each player on each team
        
        self.boxscore_obj = boxscore_obj
        
        team1name   = pyxbmct.Button('[B]%s\n%s[/B]' % (boxscore_obj['Team1']['Name'], 
                                                        boxscore_obj['Team1']['Record']), alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(team1name, 0, 0, columnspan=5, rowspan=3)
        team1logo   = pyxbmct.Image(boxscore_obj['Team1']['Logo'])
        self.placeControl(team1logo, 0, 5, rowspan=3)
        self.connect(team1name, lambda: self.switch_teams('Team1'))
        
        versus      = pyxbmct.Label('[B]VS[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(versus, 0, 6, rowspan=3)
        
        team2logo   = pyxbmct.Image(boxscore_obj['Team2']['Logo'])
        self.placeControl(team2logo, 0, 7, rowspan=3)
        team2name   = pyxbmct.Button('[B]%s\n%s[/B]' % (boxscore_obj['Team2']['Name'], 
                                                        boxscore_obj['Team2']['Record']), alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(team2name, 0, 8, columnspan=5, rowspan=3)
        self.connect(team2name, lambda: self.switch_teams('Team2'))
        
        team1name.controlLeft(team2name)
        team1name.controlRight(team2name)
        
        team2name.controlLeft(team1name)
        team2name.controlRight(team1name)
        self.setFocus(team1name)
        
        
        toiheader = pyxbmct.Label('[B]Time On Ice[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(toiheader, 2, 13, columnspan=4)
        foheader  = pyxbmct.Label('[B]Faceoffs[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(foheader, 2, 17, columnspan=3)
        
        
        g1header         = pyxbmct.Label('[B]G[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(g1header, 3, 3)
        a1header         = pyxbmct.Label('[B]A[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(a1header, 3, 4)
        plusminus1header = pyxbmct.Label('[B]+/-[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(plusminus1header, 3, 5)
        sog1header       = pyxbmct.Label('[B]SOG[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(sog1header, 3, 6)
        bs1header        = pyxbmct.Label('[B]BS[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(bs1header, 3, 7)
        pim1header       = pyxbmct.Label('[B]PIM[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(pim1header, 3, 8)
        ht1header        = pyxbmct.Label('[B]HT[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(ht1header, 3, 9)
        tk1header        = pyxbmct.Label('[B]TK[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(tk1header, 3, 10)
        gv1header        = pyxbmct.Label('[B]GV[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(gv1header, 3, 11)
        shf1header       = pyxbmct.Label('[B]SHF[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(shf1header, 3, 12)
        tot1header       = pyxbmct.Label('[B] TOT [/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(tot1header, 3, 13)
        pp1header        = pyxbmct.Label('[B]  PP  [/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(pp1header, 3, 14)
        sh1header        = pyxbmct.Label('[B]  SH  [/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(sh1header, 3, 15)
        ev1header        = pyxbmct.Label('[B]  EV  [/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(ev1header, 3, 16)
        fw1header        = pyxbmct.Label('[B]FW[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(fw1header, 3, 17)
        fl1header        = pyxbmct.Label('[B]FL[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(fl1header, 3, 18)
        fop1header       = pyxbmct.Label('[B]FO % [/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(fop1header, 3, 19)
        self.init_stats()
        
    def init_stats(self):
        #create image to cover window to hide one team's stats
        #and show other team's stats over top of the image
        #background image = pyxbmct.Skin().background_img
        
        #Team2 data is created first 
        #so we can place the coverup background img over it
        progress = xbmcgui.DialogProgressBG()
        progress.create("This might take a minute")
        self.team2header = pyxbmct.Label('[B]%s[/B]' % self.boxscore_obj['Team2']['Name'], alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(self.team2header, 3, 0, columnspan=3)
        self.team2header.setVisible(False)
        self.team2.append(self.team2header)
        
        for i, player in enumerate(self.boxscore_obj['Team2']['Stats']['Players']):
            playerheader = pyxbmct.Label('[B]%s[/B]' % player['Name'], alignment=pyxbmct.ALIGN_CENTER)
            self.team2.append(playerheader)
            self.placeControl(playerheader, 4+i, 0, columnspan=3)
            g2           = pyxbmct.Label('[B]%s[/B]' % player['G'], alignment=pyxbmct.ALIGN_CENTER)
            self.team2.append(g2)
            self.placeControl(g2, 4+i, 3)
            a2           = pyxbmct.Label('[B]%s[/B]' % player['A'], alignment=pyxbmct.ALIGN_CENTER)
            self.team2.append(a2)
            self.placeControl(a2, 4+i, 4)
            plusminus2   = pyxbmct.Label('[B]%s[/B]' % player['+/-'], alignment=pyxbmct.ALIGN_CENTER)
            self.team2.append(plusminus2)
            self.placeControl(plusminus2, 4+i, 5)
            sog2         = pyxbmct.Label('[B]  %s  [/B]' % player['Sog'], alignment=pyxbmct.ALIGN_CENTER)
            self.team2.append(sog2)
            self.placeControl(sog2, 4+i, 6)
            bs2          = pyxbmct.Label('[B]%s[/B]' % player['Bs'], alignment=pyxbmct.ALIGN_CENTER)
            self.team2.append(bs2)
            self.placeControl(bs2, 4+i, 7)
            pim2         = pyxbmct.Label('[B]%s[/B]' % player['Pim'], alignment=pyxbmct.ALIGN_CENTER)
            self.team2.append(pim2)
            self.placeControl(pim2, 4+i, 8)
            ht2          = pyxbmct.Label('[B]%s[/B]' % player['Ht'], alignment=pyxbmct.ALIGN_CENTER)
            self.team2.append(ht2)
            self.placeControl(ht2, 4+i, 9)
            tk2          = pyxbmct.Label('[B]%s[/B]' % player['Tk'], alignment=pyxbmct.ALIGN_CENTER)
            self.team2.append(tk2)
            self.placeControl(tk2, 4+i, 10)
            gv2          = pyxbmct.Label('[B]%s[/B]' % player['Gv'], alignment=pyxbmct.ALIGN_CENTER)
            self.team2.append(gv2)
            self.placeControl(gv2, 4+i, 11)
            shf2         = pyxbmct.Label('[B]%s[/B]' % player['Shf'], alignment=pyxbmct.ALIGN_CENTER)
            self.team2.append(shf2)
            self.placeControl(shf2, 4+i, 12)
            toi2         = pyxbmct.Label('[B]%s[/B]' % player['Tot'], alignment=pyxbmct.ALIGN_CENTER)
            self.team2.append(toi2)
            self.placeControl(toi2, 4+i, 13)
            pp2          = pyxbmct.Label('[B]%s[/B]' % player['Pp'], alignment=pyxbmct.ALIGN_CENTER)
            self.team2.append(pp2)
            self.placeControl(pp2, 4+i, 14)
            sh2          = pyxbmct.Label('[B]%s[/B]' % player['Sh'], alignment=pyxbmct.ALIGN_CENTER)
            self.team2.append(sh2)
            self.placeControl(sh2, 4+i, 15)
            ev2          = pyxbmct.Label('[B]%s[/B]' % player['Ev'], alignment=pyxbmct.ALIGN_CENTER)
            self.team2.append(ev2)
            self.placeControl(ev2, 4+i, 16)
            fw2          = pyxbmct.Label('[B]%s[/B]' % player['Fw'], alignment=pyxbmct.ALIGN_CENTER)
            self.team2.append(fw2)
            self.placeControl(fw2, 4+i, 17)
            fl2          = pyxbmct.Label('[B]%s[/B]' % player['Fl'], alignment=pyxbmct.ALIGN_CENTER)
            self.team2.append(fl2)
            self.placeControl(fl2, 4+i, 18)
            percent2     = pyxbmct.Label('[B]%s[/B]' % player['%'], alignment=pyxbmct.ALIGN_CENTER)
            self.team2.append(percent2)
            self.placeControl(percent2, 4+i, 19)
            nextline     = 5+i
            
        
        #EXPERIMENTAL
        #Hide first row of values since
        #coverup leaves top of characters exposed
        for i in range(0,19):
            self.team2[i].setVisible(False)
        
        team2totalsheader = pyxbmct.Label('[B]Team[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.team2.append(team2totalsheader)
        self.placeControl(team2totalsheader, nextline, 0, columnspan=3)
        team2sog          = pyxbmct.Label('[B]%s[/B]' % self.boxscore_obj['Team2']['Stats']['Sog'], alignment=pyxbmct.ALIGN_CENTER)
        self.team2.append(team2sog)
        self.placeControl(team2sog, nextline, 6)
        team2pim          = pyxbmct.Label('[B]%s[/B]' % self.boxscore_obj['Team2']['Stats']['Pim'], alignment=pyxbmct.ALIGN_CENTER)
        self.team2.append(team2pim)
        self.placeControl(team2pim, nextline, 8)
        team2ht           = pyxbmct.Label('[B]%s[/B]' % self.boxscore_obj['Team2']['Stats']['Ht'], alignment=pyxbmct.ALIGN_CENTER)
        self.team2.append(team2ht)
        self.placeControl(team2ht, nextline, 9)
        team2tk           = pyxbmct.Label('[B]%s[/B]' % self.boxscore_obj['Team2']['Stats']['Tk'], alignment=pyxbmct.ALIGN_CENTER)
        self.team2.append(team2tk)
        self.placeControl(team2tk, nextline, 10)
        team2gv           = pyxbmct.Label('[B]%s[/B]' % self.boxscore_obj['Team2']['Stats']['Gv'], alignment=pyxbmct.ALIGN_CENTER)
        self.team2.append(team2gv)
        self.placeControl(team2gv, nextline, 11)
        team2fw           = pyxbmct.Label('[B]%s[/B]' % self.boxscore_obj['Team2']['Stats']['Fw'], alignment=pyxbmct.ALIGN_CENTER)
        self.team2.append(team2fw)
        self.placeControl(team2fw, nextline, 17)
        
        nextline += 2
        team2scratchesheader = pyxbmct.Label('[B]Scratches[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.team2.append(team2scratchesheader)
        self.placeControl(team2scratchesheader, nextline, 0, columnspan=3)
        nextline += 1
        for s, scratch in enumerate(self.boxscore_obj['Team2']['Stats']['Scratches']):
            team2scratchedplayer = pyxbmct.Label('[B]%s[/B]' % scratch, alignment=pyxbmct.ALIGN_CENTER)
            self.team2.append(team2scratchedplayer)
            self.placeControl(team2scratchedplayer, nextline+s, 0, columnspan=3)
            
        nextline -= 1
        team2goaltending                  = pyxbmct.Label('[B]Goaltending[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.team2.append(team2goaltending)
        self.placeControl(team2goaltending, nextline, 4, columnspan=3)
        team2goaltendingsaheader          = pyxbmct.Label('[B]SA[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.team2.append(team2goaltendingsaheader)
        self.placeControl(team2goaltendingsaheader, nextline, 7)
        team2goaltendinggaheader          = pyxbmct.Label('[B]GA[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.team2.append(team2goaltendinggaheader)
        self.placeControl(team2goaltendinggaheader, nextline, 8)
        team2goaltendingsavesheader       = pyxbmct.Label('[B]Saves[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.team2.append(team2goaltendingsavesheader)
        self.placeControl(team2goaltendingsavesheader, nextline, 9)
        team2goaltendingsavepercentheader = pyxbmct.Label('[B]SV%[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.team2.append(team2goaltendingsavepercentheader)
        self.placeControl(team2goaltendingsavepercentheader, nextline, 10)
        team2goaltendingtoiheader         = pyxbmct.Label('[B]TOI[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.team2.append(team2goaltendingtoiheader)
        self.placeControl(team2goaltendingtoiheader, nextline, 11)
        
        team2ppsummary = pyxbmct.Label('[B]Power Play\nSummary[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.team2.append(team2ppsummary)
        self.placeControl(team2ppsummary, nextline, 13, columnspan=2, rowspan=2)
        team2ppheader = pyxbmct.Label('[B]PPG / PPO[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.team2.append(team2ppheader)
        self.placeControl(team2ppheader, nextline, 15, columnspan=2)
        tempval = '[B]%s of %s[/B]' % (self.boxscore_obj['Team2']['Stats']['Powerplay']['Ppg'], 
                                       self.boxscore_obj['Team2']['Stats']['Powerplay']['Ppo'])
        team2ppstats = pyxbmct.Label(tempval, alignment=pyxbmct.ALIGN_CENTER)
        self.team2.append(team2ppstats)
        self.placeControl(team2ppstats, nextline+1, 15, columnspan=2)
        
        nextline += 1
        for s, goalie in enumerate(self.boxscore_obj['Team2']['Stats']['Goaltending']):
            team2goaltending                  = pyxbmct.Label('[B]%s[/B]' % goalie['Name'], alignment=pyxbmct.ALIGN_CENTER)
            self.team2.append(team2goaltending)
            self.placeControl(team2goaltending, nextline+s, 4, columnspan=3)
            team2goaltendingsaheader          = pyxbmct.Label('[B]%s[/B]' % goalie['Sa'], alignment=pyxbmct.ALIGN_CENTER)
            self.team2.append(team2goaltendingsaheader)
            self.placeControl(team2goaltendingsaheader, nextline+s, 7)
            team2goaltendinggaheader          = pyxbmct.Label('[B]%s[/B]' % goalie['Ga'], alignment=pyxbmct.ALIGN_CENTER)
            self.team2.append(team2goaltendinggaheader)
            self.placeControl(team2goaltendinggaheader, nextline+s, 8)
            team2goaltendingsavesheader       = pyxbmct.Label('[B]%s[/B]' % goalie['Sv'], alignment=pyxbmct.ALIGN_CENTER)
            self.team2.append(team2goaltendingsavesheader)
            self.placeControl(team2goaltendingsavesheader, nextline+s, 9)
            team2goaltendingsavepercentheader = pyxbmct.Label('[B]%s[/B]' % goalie['Sv%'], alignment=pyxbmct.ALIGN_CENTER)
            self.team2.append(team2goaltendingsavepercentheader)
            self.placeControl(team2goaltendingsavepercentheader, nextline+s, 10)
            team2goaltendingtoiheader         = pyxbmct.Label('[B]%s[/B]' % goalie['Tot'], alignment=pyxbmct.ALIGN_CENTER)
            self.team2.append(team2goaltendingtoiheader)
            self.placeControl(team2goaltendingtoiheader, nextline+s, 11)
        #EXPERIMENTAL
            
        #Create a psuedo background image 
        #using the default skin's background image
        self.coverup = pyxbmct.Image(pyxbmct.Skin().background_img)
        self.placeControl(self.coverup, 4, 0, rowspan=self.row_number+1, columnspan=20)
        
        #Now that we've covered up team2 stats
        #We can set up & show team1 stats
        
        progress.update(50, "Half-way there!")
        
        team1header = pyxbmct.Label('[B]%s[/B]' % self.boxscore_obj['Team1']['Name'], alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(team1header, 3, 0, columnspan=3)
        self.team1.append(team1header)
        
        for i, player in enumerate(self.boxscore_obj['Team1']['Stats']['Players']):
            playerheader = pyxbmct.Label('[B]%s[/B]' % player['Name'], alignment=pyxbmct.ALIGN_CENTER)
            self.team1.append(playerheader)
            self.placeControl(playerheader, 4+i, 0, columnspan=3)
            g1           = pyxbmct.Label('[B]%s[/B]' % player['G'], alignment=pyxbmct.ALIGN_CENTER)
            self.team1.append(g1)
            self.placeControl(g1, 4+i, 3)
            a1           = pyxbmct.Label('[B]%s[/B]' % player['A'], alignment=pyxbmct.ALIGN_CENTER)
            self.team1.append(a1)
            self.placeControl(a1, 4+i, 4)
            plusminus1   = pyxbmct.Label('[B]%s[/B]' % player['+/-'], alignment=pyxbmct.ALIGN_CENTER)
            self.team1.append(plusminus1)
            self.placeControl(plusminus1, 4+i, 5)
            sog1         = pyxbmct.Label('[B]  %s  [/B]' % player['Sog'], alignment=pyxbmct.ALIGN_CENTER)
            self.team1.append(sog1)
            self.placeControl(sog1, 4+i, 6)
            bs1          = pyxbmct.Label('[B]%s[/B]' % player['Bs'], alignment=pyxbmct.ALIGN_CENTER)
            self.team1.append(bs1)
            self.placeControl(bs1, 4+i, 7)
            pim1         = pyxbmct.Label('[B]%s[/B]' % player['Pim'], alignment=pyxbmct.ALIGN_CENTER)
            self.team1.append(pim1)
            self.placeControl(pim1, 4+i, 8)
            ht1          = pyxbmct.Label('[B]%s[/B]' % player['Ht'], alignment=pyxbmct.ALIGN_CENTER)
            self.team1.append(ht1)
            self.placeControl(ht1, 4+i, 9)
            tk1          = pyxbmct.Label('[B]%s[/B]' % player['Tk'], alignment=pyxbmct.ALIGN_CENTER)
            self.team1.append(tk1)
            self.placeControl(tk1, 4+i, 10)
            gv1          = pyxbmct.Label('[B]%s[/B]' % player['Gv'], alignment=pyxbmct.ALIGN_CENTER)
            self.team1.append(gv1)
            self.placeControl(gv1, 4+i, 11)
            shf1         = pyxbmct.Label('[B]%s[/B]' % player['Shf'], alignment=pyxbmct.ALIGN_CENTER)
            self.team1.append(shf1)
            self.placeControl(shf1, 4+i, 12)
            tot1         = pyxbmct.Label('[B]%s[/B]' % player['Tot'], alignment=pyxbmct.ALIGN_CENTER)
            self.team1.append(tot1)
            self.placeControl(tot1, 4+i, 13)
            pp1          = pyxbmct.Label('[B]%s[/B]' % player['Pp'], alignment=pyxbmct.ALIGN_CENTER)
            self.team1.append(pp1)
            self.placeControl(pp1, 4+i, 14)
            sh1          = pyxbmct.Label('[B]%s[/B]' % player['Sh'], alignment=pyxbmct.ALIGN_CENTER)
            self.team1.append(sh1)
            self.placeControl(sh1, 4+i, 15)
            ev1          = pyxbmct.Label('[B]%s[/B]' % player['Ev'], alignment=pyxbmct.ALIGN_CENTER)
            self.team1.append(ev1)
            self.placeControl(ev1, 4+i, 16)
            fw1          = pyxbmct.Label('[B]%s[/B]' % player['Fw'], alignment=pyxbmct.ALIGN_CENTER)
            self.team1.append(fw1)
            self.placeControl(fw1, 4+i, 17)
            fl1          = pyxbmct.Label('[B]%s[/B]' % player['Fl'], alignment=pyxbmct.ALIGN_CENTER)
            self.team1.append(fl1)
            self.placeControl(fl1, 4+i, 18)
            percent1     = pyxbmct.Label('[B]%s[/B]' % player['%'], alignment=pyxbmct.ALIGN_CENTER)
            self.team1.append(percent1)
            self.placeControl(percent1, 4+i, 19)
            nextline     = 5+i
            
        #EXPERIMENTAL
        team1totalsheader = pyxbmct.Label('[B]Team[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.team1.append(team1totalsheader)
        self.placeControl(team1totalsheader, nextline, 0, columnspan=3)
        team1sog          = pyxbmct.Label('[B]%s[/B]' % self.boxscore_obj['Team1']['Stats']['Sog'], alignment=pyxbmct.ALIGN_CENTER)
        self.team1.append(team1sog)
        self.placeControl(team1sog, nextline, 6)
        team1pim          = pyxbmct.Label('[B]%s[/B]' % self.boxscore_obj['Team1']['Stats']['Pim'], alignment=pyxbmct.ALIGN_CENTER)
        self.team1.append(team1pim)
        self.placeControl(team1pim, nextline, 8)
        team1ht           = pyxbmct.Label('[B]%s[/B]' % self.boxscore_obj['Team1']['Stats']['Ht'], alignment=pyxbmct.ALIGN_CENTER)
        self.team1.append(team1ht)
        self.placeControl(team1ht, nextline, 9)
        team1tk           = pyxbmct.Label('[B]%s[/B]' % self.boxscore_obj['Team1']['Stats']['Tk'], alignment=pyxbmct.ALIGN_CENTER)
        self.team1.append(team1tk)
        self.placeControl(team1tk, nextline, 10)
        team1gv           = pyxbmct.Label('[B]%s[/B]' % self.boxscore_obj['Team1']['Stats']['Gv'], alignment=pyxbmct.ALIGN_CENTER)
        self.team1.append(team1gv)
        self.placeControl(team1gv, nextline, 11)
        team1fw           = pyxbmct.Label('[B]%s[/B]' % self.boxscore_obj['Team1']['Stats']['Fw'], alignment=pyxbmct.ALIGN_CENTER)
        self.team1.append(team1fw)
        self.placeControl(team1fw, nextline, 17)
        
        nextline += 2
        team1scratchesheader = pyxbmct.Label('[B]Scratches[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.team1.append(team1scratchesheader)
        self.placeControl(team1scratchesheader, nextline, 0, columnspan=3)
        
        nextline += 1
        for s, scratch in enumerate(self.boxscore_obj['Team1']['Stats']['Scratches']):
            team1scratchedplayer = pyxbmct.Label('[B]%s[/B]' % scratch, alignment=pyxbmct.ALIGN_CENTER)
            self.team1.append(team1scratchedplayer)
            self.placeControl(team1scratchedplayer, nextline+s, 0, columnspan=3)
            
        nextline -= 1
        team1goaltending                  = pyxbmct.Label('[B]Goaltending[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.team1.append(team1goaltending)
        self.placeControl(team1goaltending, nextline, 4, columnspan=3)
        team1goaltendingsaheader          = pyxbmct.Label('[B]SA[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.team1.append(team1goaltendingsaheader)
        self.placeControl(team1goaltendingsaheader, nextline, 7)
        team1goaltendinggaheader          = pyxbmct.Label('[B]GA[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.team1.append(team1goaltendinggaheader)
        self.placeControl(team1goaltendinggaheader, nextline, 8)
        team1goaltendingsavesheader       = pyxbmct.Label('[B]Saves[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.team1.append(team1goaltendingsavesheader)
        self.placeControl(team1goaltendingsavesheader, nextline, 9)
        team1goaltendingsavepercentheader = pyxbmct.Label('[B]SV%[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.team1.append(team1goaltendingsavepercentheader)
        self.placeControl(team1goaltendingsavepercentheader, nextline, 10)
        team1goaltendingtoiheader         = pyxbmct.Label('[B]TOI[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.team1.append(team1goaltendingtoiheader)
        self.placeControl(team1goaltendingtoiheader, nextline, 11)
        
        team1ppsummary = pyxbmct.Label('[B]Power Play\nSummary[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.team1.append(team1ppsummary)
        self.placeControl(team1ppsummary, nextline, 13, columnspan=2, rowspan=2)
        team1ppheader  = pyxbmct.Label('[B]PPG / PPO[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.team1.append(team1ppheader)
        self.placeControl(team1ppheader, nextline, 15, columnspan=2)
        tempval        = '%s of %s' % (self.boxscore_obj['Team1']['Stats']['Powerplay']['Ppg'], 
                                       self.boxscore_obj['Team1']['Stats']['Powerplay']['Ppo'])
        team1ppstats   = pyxbmct.Label('[B]%s[/B]' % tempval, alignment=pyxbmct.ALIGN_CENTER)
        self.team1.append(team1ppstats)
        self.placeControl(team1ppstats, nextline+1, 15, columnspan=2)
        
        nextline += 1
        for s, goalie in enumerate(self.boxscore_obj['Team1']['Stats']['Goaltending']):
            team1goaltending                  = pyxbmct.Label('[B]%s[/B]' % goalie['Name'], alignment=pyxbmct.ALIGN_CENTER)
            self.team1.append(team1goaltending)
            self.placeControl(team1goaltending, nextline+s, 4, columnspan=3)
            team1goaltendingsaheader          = pyxbmct.Label('[B]%s[/B]' % goalie['Sa'], alignment=pyxbmct.ALIGN_CENTER)
            self.team1.append(team1goaltendingsaheader)
            self.placeControl(team1goaltendingsaheader, nextline+s, 7)
            team1goaltendinggaheader          = pyxbmct.Label('[B]%s[/B]' % goalie['Ga'], alignment=pyxbmct.ALIGN_CENTER)
            self.team1.append(team1goaltendinggaheader)
            self.placeControl(team1goaltendinggaheader, nextline+s, 8)
            team1goaltendingsavesheader       = pyxbmct.Label('[B]%s[/B]' % goalie['Sv'], alignment=pyxbmct.ALIGN_CENTER)
            self.team1.append(team1goaltendingsavesheader)
            self.placeControl(team1goaltendingsavesheader, nextline+s, 9)
            team1goaltendingsavepercentheader = pyxbmct.Label('[B]%s[/B]' % goalie['Sv%'], alignment=pyxbmct.ALIGN_CENTER)
            self.team1.append(team1goaltendingsavepercentheader)
            self.placeControl(team1goaltendingsavepercentheader, nextline+s, 10)
            team1goaltendingtoiheader         = pyxbmct.Label('[B]%s[/B]' % goalie['Tot'], alignment=pyxbmct.ALIGN_CENTER)
            self.team1.append(team1goaltendingtoiheader)
            self.placeControl(team1goaltendingtoiheader, nextline+s, 11)
        #EXPERIMENTAL
        progress.update(100, "Done")
        progress.close()
            
    def switch_teams(self, team):
        if team == 'Team2':
            for element in self.team1:
                element.setVisible(False)
            for i in range(0,19):
                self.team2[i].setVisible(True)
            self.coverup.setVisible(False)
            self.team2header.setVisible(True)
        elif team == 'Team1':
            self.team2header.setVisible(False)
            self.coverup.setVisible(True)
            for element in self.team1:
                element.setVisible(True)
            for i in range(0,19):
                self.team2[i].setVisible(False)