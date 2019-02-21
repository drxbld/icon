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
logo = os.path.join(addon.getAddonInfo('path').decode('utf-8'), 'logo.png')
blue = os.path.join(addon.getAddonInfo('path').decode('utf-8'), 'blue.png')
red = os.path.join(addon.getAddonInfo('path').decode('utf-8'), 'red.png')

class Score(pyxbmct.AddonFullWindow):
    def __init__(self, title='[B]Box Score[/B]'):
        super(Score, self).__init__(title)
        #Geometry(Width, Height, Rows, Columns)
        #New Addon Windows always have 1280x720 grid
        #self.setGeometry(1280, 720, 27, 17)
        
        self.hitting = []
        self.pitching = []
        
        # Connect a key action (Backspace) to close the window.
        self.connect(pyxbmct.ACTION_NAV_BACK, self.close)
        
    #row, column[, rowspan, columnspan]
    def setup(self, boxscore_obj):
        self.row_number = 3 + 4
        # + 2 for the header & team total rows
        team1total =  len(boxscore_obj['Team1']['Stats']['Hitting']['Players']) + 2
        team1total += len(boxscore_obj['Team1']['Stats']['Hitting']['Extras'].keys())
        # + 1 for the header row
        team1total += len(boxscore_obj['Team1']['Stats']['Fielding'].keys()) + 1
        
        # + 2 for the header & team total rows
        team2total =  len(boxscore_obj['Team2']['Stats']['Hitting']['Players']) + 2
        team2total += len(boxscore_obj['Team2']['Stats']['Hitting']['Extras'].keys())
        # + 1 for the header row
        team2total += len(boxscore_obj['Team2']['Stats']['Fielding'].keys()) + 1
        
        if team1total > team2total:
            self.row_number += team1total
        else:
            self.row_number += team2total
        
        self.setGeometry(1280, 720, self.row_number, 24)
        #3 rows for top head-to-head banner
        #4 rows for team stats - team1, team1 percentages, team2, team2 percentages
        #Now add 1 row for each player on each team
        
        self.boxscore_obj = boxscore_obj
        
        hittingbtn  = pyxbmct.Button('[B]Hitting[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(hittingbtn, 0, 0, columnspan=3, rowspan=3)
        self.connect(hittingbtn, lambda: self.switch_stats('Hitting'))
        pitchingbtn  = pyxbmct.Button('[B]Pitching[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(pitchingbtn, 3, 0, columnspan=3, rowspan=3)
        self.connect(pitchingbtn, lambda: self.switch_stats('Pitching'))
        
        pitchingbtn.controlUp(hittingbtn)
        pitchingbtn.controlDown(hittingbtn)
        hittingbtn.controlUp(pitchingbtn)
        hittingbtn.controlDown(pitchingbtn)
        self.setFocus(hittingbtn)
        
        team1name   = pyxbmct.Label('[B]%s\n%s[/B]' % (boxscore_obj['Team1']['Name'], 
                                                       boxscore_obj['Team1']['Record']), alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(team1name, 0, 3, columnspan=6, rowspan=6)
        team1logo   = pyxbmct.Image(boxscore_obj['Team1']['Logo'])
        self.placeControl(team1logo, 0, 9, columnspan=2, rowspan=6)
        
        versus      = pyxbmct.Label('[B]VS[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(versus, 0, 11, columnspan=3, rowspan=6)
        
        team2logo   = pyxbmct.Image(boxscore_obj['Team2']['Logo'])
        self.placeControl(team2logo, 0, 14, columnspan=2, rowspan=6)
        team2name   = pyxbmct.Label('[B]%s\n%s[/B]' % (boxscore_obj['Team2']['Name'], 
                                                       boxscore_obj['Team2']['Record']), alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(team2name, 0, 16, columnspan=5, rowspan=6)
        self.init_stats()
        
    def init_stats(self):
        progress = xbmcgui.DialogProgressBG()
        progress.create("This might take a minute")
        team1pitchers = pyxbmct.Label('[B]Pitchers[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.pitching.append(team1pitchers)
        self.placeControl(team1pitchers, 6, 0, columnspan=2)
        ip1header = pyxbmct.Label('[B]IP[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.pitching.append(ip1header)
        self.placeControl(ip1header, 6, 2)
        ph1header  = pyxbmct.Label('[B]H[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.pitching.append(ph1header)
        self.placeControl(ph1header, 6, 3)
        pr1header  = pyxbmct.Label('[B]R[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.pitching.append(pr1header)
        self.placeControl(pr1header, 6, 4)
        er1header  = pyxbmct.Label('[B]ER[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.pitching.append(er1header)
        self.placeControl(er1header, 6, 5)
        pbb1header  = pyxbmct.Label('[B]BB[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.pitching.append(pbb1header)
        self.placeControl(pbb1header, 6, 6)
        pk1header  = pyxbmct.Label('[B]K[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.pitching.append(pk1header)
        self.placeControl(pk1header, 6, 7)
        hr1header  = pyxbmct.Label('[B]HR[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.pitching.append(hr1header)
        self.placeControl(hr1header, 6, 8)
        pcst1header  = pyxbmct.Label('[B]PC-ST[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.pitching.append(pcst1header)
        self.placeControl(pcst1header, 6, 9, columnspan=2)
        era1header  = pyxbmct.Label('[B]ERA[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.pitching.append(era1header)
        self.placeControl(era1header, 6, 11)
        
        nextline = 0
        t1pitches = 0
        t1strikes = 0
        t1ks = 0
        for p, player in enumerate(self.boxscore_obj['Team1']['Stats']['Pitching']['Players']):
            player1name =  pyxbmct.Label('[B]%s[/B]' % player['Name'], alignment=pyxbmct.ALIGN_CENTER)
            self.pitching.append(player1name)
            self.placeControl(player1name, 7+p, 0, columnspan=2)
            player1ip =  pyxbmct.Label('[B]%s[/B]' % player['IP'], alignment=pyxbmct.ALIGN_CENTER)
            self.pitching.append(player1ip)
            self.placeControl(player1ip, 7+p, 2)
            player1h =  pyxbmct.Label('[B]%s[/B]' % player['H'], alignment=pyxbmct.ALIGN_CENTER)
            self.pitching.append(player1h)
            self.placeControl(player1h, 7+p, 3)
            player1r =  pyxbmct.Label('[B]%s[/B]' % player['R'], alignment=pyxbmct.ALIGN_CENTER)
            self.pitching.append(player1r)
            self.placeControl(player1r, 7+p, 4)
            player1er =  pyxbmct.Label('[B]%s[/B]' % player['ER'], alignment=pyxbmct.ALIGN_CENTER)
            self.pitching.append(player1er)
            self.placeControl(player1er, 7+p, 5)
            player1bb =  pyxbmct.Label('[B]%s[/B]' % player['BB'], alignment=pyxbmct.ALIGN_CENTER)
            self.pitching.append(player1bb)
            self.placeControl(player1bb, 7+p, 6)
            player1k =  pyxbmct.Label('[B]%s[/B]' % player['K'], alignment=pyxbmct.ALIGN_CENTER)
            t1ks += int(player['K'])
            self.pitching.append(player1k)
            self.placeControl(player1k, 7+p, 7)
            player1hr =  pyxbmct.Label('[B]%s[/B]' % player['HR'], alignment=pyxbmct.ALIGN_CENTER)
            self.pitching.append(player1hr)
            self.placeControl(player1hr, 7+p, 8)
            player1pcst =  pyxbmct.Label('[B]%s[/B]' % player['PC-ST'], alignment=pyxbmct.ALIGN_CENTER)
            t1pitches += int(player['PC-ST'].split('-')[0])
            t1strikes += int(player['PC-ST'].split('-')[1])
            self.pitching.append(player1pcst)
            self.placeControl(player1pcst, 7+p, 9, columnspan=2)
            era = player['ERA']
            if len(era) > 4:
                era = era[:-1]
            player1era =  pyxbmct.Label('[B]%s[/B]' % era, alignment=pyxbmct.ALIGN_CENTER)
            self.pitching.append(player1era)
            self.placeControl(player1era, 7+p, 11)
            nextline = 7+p+1
            
        teamstats = self.boxscore_obj['Team1']['Stats']['Pitching']
        pteam1lbl =  pyxbmct.Label('[B]Team[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.pitching.append(pteam1lbl)
        self.placeControl(pteam1lbl, nextline, 0, columnspan=2)
        #pteam1ip =  pyxbmct.Label('[B]%s[/B]' % teamstats['IP'], alignment=pyxbmct.ALIGN_CENTER)
        #self.pitching.append(pteam1ip)
        #self.placeControl(pteam1ip, nextline, 2)
        pteam1h =  pyxbmct.Label('[B]%s[/B]' % teamstats['H'], alignment=pyxbmct.ALIGN_CENTER)
        self.pitching.append(pteam1h)
        self.placeControl(pteam1h, nextline, 3)
        pteam1r =  pyxbmct.Label('[B]%s[/B]' % teamstats['R'], alignment=pyxbmct.ALIGN_CENTER)
        self.pitching.append(pteam1r)
        self.placeControl(pteam1r, nextline, 4)
        pteam1er =  pyxbmct.Label('[B]%s[/B]' % teamstats['ER'], alignment=pyxbmct.ALIGN_CENTER)
        self.pitching.append(pteam1er)
        self.placeControl(pteam1er, nextline, 5)
        pteam1bb =  pyxbmct.Label('[B]%s[/B]' % teamstats['BB'], alignment=pyxbmct.ALIGN_CENTER)
        self.pitching.append(pteam1bb)
        self.placeControl(pteam1bb, nextline, 6)
        pteam1k =  pyxbmct.Label('[B]%s[/B]' % str(t1ks), alignment=pyxbmct.ALIGN_CENTER)
        self.pitching.append(pteam1k)
        self.placeControl(pteam1k, nextline, 7)
        pteam1hr =  pyxbmct.Label('[B]%s[/B]' % teamstats['HR'], alignment=pyxbmct.ALIGN_CENTER)
        self.pitching.append(pteam1hr)
        self.placeControl(pteam1hr, nextline, 8)
        pteam1pcst =  pyxbmct.Label('[B]%s-%s[/B]' % (str(t1pitches), str(t1strikes)), alignment=pyxbmct.ALIGN_CENTER)
        self.pitching.append(pteam1pcst)
        self.placeControl(pteam1pcst, nextline, 9, columnspan=2)
        
        nextline += 2
        result = '[B]Pitching[/B]\n'
        pitchingextras = self.boxscore_obj['Team1']['Stats']['Pitching']['Extras']
        for stat in pitchingextras.keys():
            result += '[B]%s[/B]: \n  %s\n' % (stat, pitchingextras[stat].replace('; ','\n  '))
            
        pextratextbox1 = pyxbmct.TextBox()
        whatsleft = self.row_number - nextline + 2
        self.pitching.append(pextratextbox1)
        self.placeControl(pextratextbox1, nextline, 0, rowspan=whatsleft, columnspan=11)
        pextratextbox1.setText(result)
        pextratextbox1.autoScroll(3000, 2000, 2000)
        
        #Team 2 Pitching
        
        team2pitchers = pyxbmct.Label('[B]Pitchers[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.pitching.append(team2pitchers)
        self.placeControl(team2pitchers, 6, 12, columnspan=2)
        ip2header = pyxbmct.Label('[B]IP[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.pitching.append(ip2header)
        self.placeControl(ip2header, 6, 14)
        ph2header  = pyxbmct.Label('[B]H[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.pitching.append(ph2header)
        self.placeControl(ph2header, 6, 15)
        pr2header  = pyxbmct.Label('[B]R[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.pitching.append(pr2header)
        self.placeControl(pr2header, 6, 16)
        er2header  = pyxbmct.Label('[B]ER[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.pitching.append(er2header)
        self.placeControl(er2header, 6, 17)
        pbb2header  = pyxbmct.Label('[B]BB[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.pitching.append(pbb2header)
        self.placeControl(pbb2header, 6, 18)
        pk2header  = pyxbmct.Label('[B]K[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.pitching.append(pk2header)
        self.placeControl(pk2header, 6, 19)
        hr2header  = pyxbmct.Label('[B]HR[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.pitching.append(hr2header)
        self.placeControl(hr2header, 6, 20)
        pcst2header  = pyxbmct.Label('[B]PC-ST[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.pitching.append(pcst2header)
        self.placeControl(pcst2header, 6, 21, columnspan=2)
        era2header  = pyxbmct.Label('[B]ERA[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.pitching.append(era2header)
        self.placeControl(era2header, 6, 23)
        
        nextline = 0
        t2pitches = 0
        t2strikes = 0
        t2ks = 0
        for p, player in enumerate(self.boxscore_obj['Team2']['Stats']['Pitching']['Players']):
            player2name =  pyxbmct.Label('[B]%s[/B]' % player['Name'], alignment=pyxbmct.ALIGN_CENTER)
            self.pitching.append(player2name)
            self.placeControl(player2name, 7+p, 12, columnspan=2)
            player2ip =  pyxbmct.Label('[B]%s[/B]' % player['IP'], alignment=pyxbmct.ALIGN_CENTER)
            self.pitching.append(player2ip)
            self.placeControl(player2ip, 7+p, 14)
            player2h =  pyxbmct.Label('[B]%s[/B]' % player['H'], alignment=pyxbmct.ALIGN_CENTER)
            self.pitching.append(player2h)
            self.placeControl(player2h, 7+p, 15)
            player2r =  pyxbmct.Label('[B]%s[/B]' % player['R'], alignment=pyxbmct.ALIGN_CENTER)
            self.pitching.append(player2r)
            self.placeControl(player2r, 7+p, 16)
            player2er =  pyxbmct.Label('[B]%s[/B]' % player['ER'], alignment=pyxbmct.ALIGN_CENTER)
            self.pitching.append(player2er)
            self.placeControl(player2er, 7+p, 17)
            player2bb =  pyxbmct.Label('[B]%s[/B]' % player['BB'], alignment=pyxbmct.ALIGN_CENTER)
            self.pitching.append(player2bb)
            self.placeControl(player2bb, 7+p, 18)
            player2k =  pyxbmct.Label('[B]%s[/B]' % player['K'], alignment=pyxbmct.ALIGN_CENTER)
            t2ks += int(player['K'])
            self.pitching.append(player2k)
            self.placeControl(player2k, 7+p, 19)
            player2hr =  pyxbmct.Label('[B]%s[/B]' % player['HR'], alignment=pyxbmct.ALIGN_CENTER)
            self.pitching.append(player2hr)
            self.placeControl(player2hr, 7+p, 20)
            player2pcst =  pyxbmct.Label('[B]%s[/B]' % player['PC-ST'], alignment=pyxbmct.ALIGN_CENTER)
            t2pitches += int(player['PC-ST'].split('-')[0])
            t2strikes += int(player['PC-ST'].split('-')[1])
            self.pitching.append(player2pcst)
            self.placeControl(player2pcst, 7+p, 21, columnspan=2)
            era = player['ERA']
            if len(era) > 4:
                era = era[:-1]
            player2era =  pyxbmct.Label('[B]%s[/B]' % era, alignment=pyxbmct.ALIGN_CENTER)
            self.pitching.append(player2era)
            self.placeControl(player2era, 7+p, 23)
            nextline = 7+p+1
            
        teamstats = self.boxscore_obj['Team2']['Stats']['Pitching']
        pteam2lbl =  pyxbmct.Label('[B]Team[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.pitching.append(pteam2lbl)
        self.placeControl(pteam2lbl, nextline, 12, columnspan=2)
        pteam2h =  pyxbmct.Label('[B]%s[/B]' % teamstats['H'], alignment=pyxbmct.ALIGN_CENTER)
        self.pitching.append(pteam2h)
        self.placeControl(pteam2h, nextline, 15)
        pteam2r =  pyxbmct.Label('[B]%s[/B]' % teamstats['R'], alignment=pyxbmct.ALIGN_CENTER)
        self.pitching.append(pteam2r)
        self.placeControl(pteam2r, nextline, 16)
        pteam2er =  pyxbmct.Label('[B]%s[/B]' % teamstats['ER'], alignment=pyxbmct.ALIGN_CENTER)
        self.pitching.append(pteam2er)
        self.placeControl(pteam2er, nextline, 17)
        pteam2bb =  pyxbmct.Label('[B]%s[/B]' % teamstats['BB'], alignment=pyxbmct.ALIGN_CENTER)
        self.pitching.append(pteam2bb)
        self.placeControl(pteam2bb, nextline, 18)
        pteam2k =  pyxbmct.Label('[B]%s[/B]' % str(t2ks), alignment=pyxbmct.ALIGN_CENTER)
        self.pitching.append(pteam2k)
        self.placeControl(pteam2k, nextline, 19)
        pteam2hr =  pyxbmct.Label('[B]%s[/B]' % teamstats['HR'], alignment=pyxbmct.ALIGN_CENTER)
        self.pitching.append(pteam2hr)
        self.placeControl(pteam2hr, nextline, 20)
        pteam2pcst =  pyxbmct.Label('[B]%s-%s[/B]' % (str(t2pitches), str(t2strikes)), alignment=pyxbmct.ALIGN_CENTER)
        self.pitching.append(pteam2pcst)
        self.placeControl(pteam2pcst, nextline, 21, columnspan=2)
        
        nextline += 2
        result = '[B]Pitching[/B]\n'
        pitchingextras = self.boxscore_obj['Team2']['Stats']['Pitching']['Extras']
        for stat in pitchingextras.keys():
            result += '[B]%s[/B]: \n  %s\n' % (stat, pitchingextras[stat].replace('; ','\n  '))
            
        pextratextbox2 = pyxbmct.TextBox()
        whatsleft = self.row_number - nextline + 2
        self.pitching.append(pextratextbox2)
        self.placeControl(pextratextbox2, nextline, 12, rowspan=whatsleft, columnspan=11)
        pextratextbox2.setText(result)
        pextratextbox2.autoScroll(3000, 2000, 2000)
        
        
        
        
        
        
        
        #Create a psuedo background image 
        #using the default skin's background image
        self.coverup = pyxbmct.Image(pyxbmct.Skin().background_img)
        self.placeControl(self.coverup, 5, 0, rowspan=self.row_number+1, columnspan=24)
        #Now that we've covered up pitching stats
        #We can set up & show hitting stats
        
        progress.update(50, "Half-way there!")
        
        team1hitters = pyxbmct.Label('[B]Hitters[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.hitting.append(team1hitters)
        self.placeControl(team1hitters, 6, 0, columnspan=3)
        ab1header  = pyxbmct.Label('[B]AB[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.hitting.append(ab1header)
        self.placeControl(ab1header, 6, 3)
        r1header  = pyxbmct.Label('[B]R[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.hitting.append(r1header)
        self.placeControl(r1header, 6, 4)
        h1header  = pyxbmct.Label('[B]H[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.hitting.append(h1header)
        self.placeControl(h1header, 6, 5)
        rbi1header  = pyxbmct.Label('[B]RBI[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.hitting.append(rbi1header)
        self.placeControl(rbi1header, 6, 6)
        bb1header = pyxbmct.Label('[B]BB[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.hitting.append(bb1header)
        self.placeControl(bb1header, 6, 7)
        k1header = pyxbmct.Label('[B]K[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.hitting.append(k1header)
        self.placeControl(k1header, 6, 8)
        avg1header = pyxbmct.Label('[B]AVG[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.hitting.append(avg1header)
        self.placeControl(avg1header, 6, 9)
        obp1header = pyxbmct.Label('[B]OBP[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.hitting.append(obp1header)
        self.placeControl(obp1header, 6, 10)
        slg1header = pyxbmct.Label('[B]SLG[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.hitting.append(slg1header)
        self.placeControl(slg1header, 6, 11)
        
        nextline = 0
        for p, player in enumerate(self.boxscore_obj['Team1']['Stats']['Hitting']['Players']):
            player1name =  pyxbmct.Label('[B]%s[/B]' % player['Name'], alignment=pyxbmct.ALIGN_CENTER)
            self.hitting.append(player1name)
            self.placeControl(player1name, 7+p, 0, columnspan=3)
            player1ab =  pyxbmct.Label('[B]%s[/B]' % player['AB'], alignment=pyxbmct.ALIGN_CENTER)
            self.hitting.append(player1ab)
            self.placeControl(player1ab, 7+p, 3)
            player1r =  pyxbmct.Label('[B]%s[/B]' % player['R'], alignment=pyxbmct.ALIGN_CENTER)
            self.hitting.append(player1r)
            self.placeControl(player1r, 7+p, 4)
            player1h =  pyxbmct.Label('[B]%s[/B]' % player['H'], alignment=pyxbmct.ALIGN_CENTER)
            self.hitting.append(player1h)
            self.placeControl(player1h, 7+p, 5)
            player1rbi =  pyxbmct.Label('[B]%s[/B]' % player['RBI'], alignment=pyxbmct.ALIGN_CENTER)
            self.hitting.append(player1rbi)
            self.placeControl(player1rbi, 7+p, 6)
            player1bb =  pyxbmct.Label('[B]%s[/B]' % player['BB'], alignment=pyxbmct.ALIGN_CENTER)
            self.hitting.append(player1bb)
            self.placeControl(player1bb, 7+p, 7)
            player1k =  pyxbmct.Label('[B]%s[/B]' % player['K'], alignment=pyxbmct.ALIGN_CENTER)
            self.hitting.append(player1k)
            self.placeControl(player1k, 7+p, 8)
            player1avg =  pyxbmct.Label('[B]%s[/B]' % player['AVG'], alignment=pyxbmct.ALIGN_CENTER)
            self.hitting.append(player1avg)
            self.placeControl(player1avg, 7+p, 9)
            player1obp =  pyxbmct.Label('[B]%s[/B]' % player['OBP'], alignment=pyxbmct.ALIGN_CENTER)
            self.hitting.append(player1obp)
            self.placeControl(player1obp, 7+p, 10)
            slg = player['SLG']
            if len(slg) > 4:
                slg = slg[:-1]
            player1slg =  pyxbmct.Label('[B]%s[/B]' % slg, alignment=pyxbmct.ALIGN_CENTER)
            self.hitting.append(player1slg)
            self.placeControl(player1slg, 7+p, 11)
            nextline = 7+p+1
            
        teamstats = self.boxscore_obj['Team1']['Stats']['Hitting']
        team1lbl =  pyxbmct.Label('[B]Team[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.hitting.append(team1lbl)
        self.placeControl(team1lbl, nextline, 0, columnspan=3)
        team1ab =  pyxbmct.Label('[B]%s[/B]' % teamstats['AB'], alignment=pyxbmct.ALIGN_CENTER)
        self.hitting.append(team1ab)
        self.placeControl(team1ab, nextline, 3)
        team1r =  pyxbmct.Label('[B]%s[/B]' % teamstats['R'], alignment=pyxbmct.ALIGN_CENTER)
        self.hitting.append(team1r)
        self.placeControl(team1r, nextline, 4)
        team1h =  pyxbmct.Label('[B]%s[/B]' % teamstats['H'], alignment=pyxbmct.ALIGN_CENTER)
        self.hitting.append(team1h)
        self.placeControl(team1h, nextline, 5)
        team1rbi =  pyxbmct.Label('[B]%s[/B]' % teamstats['RBI'], alignment=pyxbmct.ALIGN_CENTER)
        self.hitting.append(team1rbi)
        self.placeControl(team1rbi, nextline, 6)
        team1bb =  pyxbmct.Label('[B]%s[/B]' % teamstats['BB'], alignment=pyxbmct.ALIGN_CENTER)
        self.hitting.append(team1bb)
        self.placeControl(team1bb, nextline, 7)
        team1k =  pyxbmct.Label('[B]%s[/B]' % teamstats['K'], alignment=pyxbmct.ALIGN_CENTER)
        self.hitting.append(team1k)
        self.placeControl(team1k, nextline, 8)
        team1avg =  pyxbmct.Label('[B]%s[/B]' % teamstats['AVG'], alignment=pyxbmct.ALIGN_CENTER)
        self.hitting.append(team1avg)
        self.placeControl(team1avg, nextline, 9)
        
        nextline += 2
        result = '[B]Batting[/B]\n'
        battingextras = self.boxscore_obj['Team1']['Stats']['Hitting']['Extras']
        for stat in battingextras.keys():
            result += '[B]%s[/B]: %s\n' % (stat, battingextras[stat])
        result += '\n[B]Fielding[/B]\n'
        fieldingextras = self.boxscore_obj['Team1']['Stats']['Fielding']
        for stat in fieldingextras.keys():
            result += '[B]%s[/B]: %s\n' % (stat, fieldingextras[stat])
            
        extratextbox1 = pyxbmct.TextBox()
        whatsleft = self.row_number - nextline + 2
        self.hitting.append(extratextbox1)
        self.placeControl(extratextbox1, nextline, 0, rowspan=whatsleft, columnspan=11)
        extratextbox1.setText(result)
        extratextbox1.autoScroll(3000, 2000, 2000)
        
        #Start Team2
        
        team2hitters = pyxbmct.Label('[B]Hitters[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.hitting.append(team2hitters)
        self.placeControl(team2hitters, 6, 12, columnspan=3)
        ab2header  = pyxbmct.Label('[B]AB[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.hitting.append(ab2header)
        self.placeControl(ab2header, 6, 15)
        r2header  = pyxbmct.Label('[B]R[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.hitting.append(r2header)
        self.placeControl(r2header, 6, 16)
        h2header  = pyxbmct.Label('[B]H[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.hitting.append(h2header)
        self.placeControl(h2header, 6, 17)
        rbi2header  = pyxbmct.Label('[B]RBI[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.hitting.append(rbi2header)
        self.placeControl(rbi2header, 6, 18)
        bb2header = pyxbmct.Label('[B]BB[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.hitting.append(bb2header)
        self.placeControl(bb2header, 6, 19)
        k2header = pyxbmct.Label('[B]K[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.hitting.append(k2header)
        self.placeControl(k2header, 6, 20)
        avg2header = pyxbmct.Label('[B]AVG[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.hitting.append(avg2header)
        self.placeControl(avg2header, 6, 21)
        obp2header = pyxbmct.Label('[B]OBP[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.hitting.append(obp2header)
        self.placeControl(obp2header, 6, 22)
        slg2header = pyxbmct.Label('[B]SLG[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.hitting.append(slg2header)
        self.placeControl(slg2header, 6, 23)
        
        nextline = 0
        for p, player in enumerate(self.boxscore_obj['Team2']['Stats']['Hitting']['Players']):
            player2name =  pyxbmct.Label('[B]%s[/B]' % player['Name'], alignment=pyxbmct.ALIGN_CENTER)
            self.hitting.append(player2name)
            self.placeControl(player2name, 7+p, 12, columnspan=3)
            player2ab =  pyxbmct.Label('[B]%s[/B]' % player['AB'], alignment=pyxbmct.ALIGN_CENTER)
            self.hitting.append(player2ab)
            self.placeControl(player2ab, 7+p, 15)
            player2r =  pyxbmct.Label('[B]%s[/B]' % player['R'], alignment=pyxbmct.ALIGN_CENTER)
            self.hitting.append(player2r)
            self.placeControl(player2r, 7+p, 16)
            player2h =  pyxbmct.Label('[B]%s[/B]' % player['H'], alignment=pyxbmct.ALIGN_CENTER)
            self.hitting.append(player2h)
            self.placeControl(player2h, 7+p, 17)
            player2rbi =  pyxbmct.Label('[B]%s[/B]' % player['RBI'], alignment=pyxbmct.ALIGN_CENTER)
            self.hitting.append(player2rbi)
            self.placeControl(player2rbi, 7+p, 18)
            player2bb =  pyxbmct.Label('[B]%s[/B]' % player['BB'], alignment=pyxbmct.ALIGN_CENTER)
            self.hitting.append(player2bb)
            self.placeControl(player2bb, 7+p, 19)
            player2k =  pyxbmct.Label('[B]%s[/B]' % player['K'], alignment=pyxbmct.ALIGN_CENTER)
            self.hitting.append(player2k)
            self.placeControl(player2k, 7+p, 20)
            player2avg =  pyxbmct.Label('[B]%s[/B]' % player['AVG'], alignment=pyxbmct.ALIGN_CENTER)
            self.hitting.append(player2avg)
            self.placeControl(player2avg, 7+p, 21)
            player2obp =  pyxbmct.Label('[B]%s[/B]' % player['OBP'], alignment=pyxbmct.ALIGN_CENTER)
            self.hitting.append(player2obp)
            self.placeControl(player2obp, 7+p, 22)
            slg = player['SLG']
            if len(slg) > 4:
                slg = slg[:-1]
            player2slg =  pyxbmct.Label('[B]%s[/B]' % slg, alignment=pyxbmct.ALIGN_CENTER)
            self.hitting.append(player2slg)
            self.placeControl(player2slg, 7+p, 23)
            nextline = 7+p+1
            
        teamstats = self.boxscore_obj['Team2']['Stats']['Hitting']
        team2lbl =  pyxbmct.Label('[B]Team[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.hitting.append(team2lbl)
        self.placeControl(team2lbl, nextline, 12, columnspan=3)
        team2ab =  pyxbmct.Label('[B]%s[/B]' % teamstats['AB'], alignment=pyxbmct.ALIGN_CENTER)
        self.hitting.append(team2ab)
        self.placeControl(team2ab, nextline, 15)
        team2r =  pyxbmct.Label('[B]%s[/B]' % teamstats['R'], alignment=pyxbmct.ALIGN_CENTER)
        self.hitting.append(team2r)
        self.placeControl(team2r, nextline, 16)
        team2h =  pyxbmct.Label('[B]%s[/B]' % teamstats['H'], alignment=pyxbmct.ALIGN_CENTER)
        self.hitting.append(team2h)
        self.placeControl(team2h, nextline, 17)
        team2rbi =  pyxbmct.Label('[B]%s[/B]' % teamstats['RBI'], alignment=pyxbmct.ALIGN_CENTER)
        self.hitting.append(team2rbi)
        self.placeControl(team2rbi, nextline, 18)
        team2bb =  pyxbmct.Label('[B]%s[/B]' % teamstats['BB'], alignment=pyxbmct.ALIGN_CENTER)
        self.hitting.append(team2bb)
        self.placeControl(team2bb, nextline, 19)
        team2k =  pyxbmct.Label('[B]%s[/B]' % teamstats['K'], alignment=pyxbmct.ALIGN_CENTER)
        self.hitting.append(team2k)
        self.placeControl(team2k, nextline, 20)
        team2avg =  pyxbmct.Label('[B]%s[/B]' % teamstats['AVG'], alignment=pyxbmct.ALIGN_CENTER)
        self.hitting.append(team2avg)
        self.placeControl(team2avg, nextline, 21)
        
        nextline += 2
        result = '[B]Batting[/B]\n'
        battingextras = self.boxscore_obj['Team2']['Stats']['Hitting']['Extras']
        for stat in battingextras.keys():
            result += '[B]%s[/B]: %s\n' % (stat, battingextras[stat])
        result += '\n[B]Fielding[/B]\n'
        fieldingextras = self.boxscore_obj['Team2']['Stats']['Fielding']
        for stat in fieldingextras.keys():
            result += '[B]%s[/B]: %s\n' % (stat, fieldingextras[stat])
            
        extratextbox2 = pyxbmct.TextBox()
        whatsleft = self.row_number - nextline + 2
        self.hitting.append(extratextbox2)
        self.placeControl(extratextbox2, nextline, 12, rowspan=whatsleft, columnspan=11)
        extratextbox2.setText(result)
        extratextbox2.autoScroll(3000, 2000, 2000)
        
        progress.update(100, "Done")
        progress.close()
        
    def switch_stats(self, stats):
        if stats == 'Pitching':
            for element in self.hitting:
                element.setVisible(False)
            self.coverup.setVisible(False)
        elif stats == 'Hitting':
            self.coverup.setVisible(True)
            for element in self.hitting:
                element.setVisible(True)