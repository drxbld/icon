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
    def __init__(self, title='[B]Soccer Standings[/B]'):
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
        
        rows_needed = 0
        cols_needed = 12
        h = standings.pop('Headers')
        lname = standings.pop('League Name')
        if 'Groups' in standings.keys()[0]:
            #Need 2x the columns
            cols_needed = 24
            #Need 5 * number of groups in a column for rows (4 teams + headers per group)
            rows_needed = 5 * len(standings[standings.keys()[0]])
        else:
            for x, y in standings.iteritems():
                rows_needed += len(y)
            rows_needed += 3
        self.setGeometry(1280, 720, rows_needed, cols_needed)
        
        if len(standings.keys()) == 1:
            league_name = standings.keys()[0]
            league_standings = standings[league_name]
            l = pyxbmct.Label('[B]%s[/B]' % league_name, alignment=pyxbmct.ALIGN_CENTER)
            self.placeControl(l, 0, 1, columnspan=3)
            for i, header in enumerate(h):
                tmp3 = pyxbmct.Label('[B]%s[/B]' % header, alignment=pyxbmct.ALIGN_CENTER)
                self.placeControl(tmp3, 0, 4+i)
            for number, team_dict in league_standings.iteritems():
                position = pyxbmct.Label(str(number), alignment=pyxbmct.ALIGN_CENTER)
                self.placeControl(position, int(number), 0)
                tname = pyxbmct.Label(team_dict['Name'], alignment=pyxbmct.ALIGN_CENTER)
                self.placeControl(tname, int(number), 1, columnspan=3)
                for index, head in enumerate(h):
                    tmp2 = pyxbmct.Label(team_dict[head], alignment=pyxbmct.ALIGN_CENTER)
                    self.placeControl(tmp2, int(number), 4+index)
        elif 'Conference' in standings.keys()[0]:
            #Major League Soccer
            sub_title1 = standings.keys()[0]
            sub_teams1 = len(standings[sub_title1])
            league_standings1 = standings[sub_title1]
            sub_title2 = standings.keys()[1]
            sub_teams2 = len(standings[sub_title2])
            league_standings2 = standings[sub_title2]
            #Add East Division
            stitle1 = pyxbmct.Label('[B]%s[/B]' % sub_title1, alignment=pyxbmct.ALIGN_CENTER)
            self.placeControl(stitle1, 0, 1, columnspan=3)
            for i, header in enumerate(h):
                tmp3 = pyxbmct.Label('[B]%s[/B]' % header, alignment=pyxbmct.ALIGN_CENTER)
                self.placeControl(tmp3, 0, 4+i)
            for number, team_dict in league_standings1.iteritems():
                #Add row
                position = pyxbmct.Label(str(number), alignment=pyxbmct.ALIGN_CENTER)
                self.placeControl(position, int(number), 0)
                tname = pyxbmct.Label(team_dict['Name'], alignment=pyxbmct.ALIGN_CENTER)
                self.placeControl(tname, int(number), 1, columnspan=3)
                for index, header in enumerate(h):
                    #Add each stat (column) for the row
                    tmp2 = pyxbmct.Label(team_dict[header], alignment=pyxbmct.ALIGN_CENTER)
                    self.placeControl(tmp2, int(number), 4+index)
            #Add West Division
            stitle2 = pyxbmct.Label('[B]%s[/B]' % sub_title2, alignment=pyxbmct.ALIGN_CENTER)
            self.placeControl(stitle2, sub_teams1+2, 1, columnspan=3)
            for i, header in enumerate(h):
                tmp3 = pyxbmct.Label('[B]%s[/B]' % header, alignment=pyxbmct.ALIGN_CENTER)
                self.placeControl(tmp3, sub_teams1+2, 4+i)
            for p, pos in league_standings2.iteritems():
                #Add row
                position = pyxbmct.Label(str(p), alignment=pyxbmct.ALIGN_CENTER)
                self.placeControl(position, sub_teams1+2+int(p), 0)
                tname = pyxbmct.Label(pos['Name'], alignment=pyxbmct.ALIGN_CENTER)
                self.placeControl(tname, sub_teams1+2+int(p), 1, columnspan=3)
                for num, head in enumerate(h):
                    #Add each stat (column) for the row
                    tmp2 = pyxbmct.Label(pos[head], alignment=pyxbmct.ALIGN_CENTER)
                    self.placeControl(tmp2, sub_teams1+2+int(p), 4+num)
        else:
            #Europa & Champions Leagues
            #Place headers in both columns
            for i, header in enumerate(h):
                tmp1 = pyxbmct.Label('[B]%s[/B]' % header, alignment=pyxbmct.ALIGN_CENTER)
                self.placeControl(tmp1, 0, 4+i)
                tmp2 = pyxbmct.Label('[B]%s[/B]' % header, alignment=pyxbmct.ALIGN_CENTER)
                self.placeControl(tmp2, 0, 16+i)
            ncol = 0
            for grouping_name, groups in sorted(standings.iteritems()):
                nrow = 0 
                for group, teams in sorted(groups.iteritems()):
                    gname = pyxbmct.Label('[B]%s[/B]' % group, alignment=pyxbmct.ALIGN_CENTER)
                    self.placeControl(gname, nrow, ncol, columnspan=4)
                    for i, header in enumerate(h):
                        tmp1 = pyxbmct.Label('[B]%s[/B]' % header, alignment=pyxbmct.ALIGN_CENTER)
                        self.placeControl(tmp1, nrow, 4+i)
                        tmp2 = pyxbmct.Label('[B]%s[/B]' % header, alignment=pyxbmct.ALIGN_CENTER)
                        self.placeControl(tmp2, nrow, 16+i)
                    nrow += 1
                    for position, team_data in teams.iteritems():
                        position_in_group = pyxbmct.Label('[B]%s[/B]' % str(position), alignment=pyxbmct.ALIGN_CENTER)
                        self.placeControl(position_in_group, nrow, ncol)
                        tname = pyxbmct.Label(team_data['Name'], alignment=pyxbmct.ALIGN_CENTER)
                        self.placeControl(tname, nrow, ncol+1, columnspan=3)
                        for i, header in enumerate(h):
                            tstat = pyxbmct.Label(team_data[header], alignment=pyxbmct.ALIGN_CENTER)
                            self.placeControl(tstat, nrow, ncol+4+i)
                        nrow += 1
                ncol = 12
                percentage += 50
                progress.update(percentage, ' It\'ll be worth it, I promise!')
        progress.close()