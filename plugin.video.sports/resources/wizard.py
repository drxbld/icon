import xbmcaddon
import xbmcgui
import xbmc
import os

dialog = xbmcgui.Dialog()
addon_id = 'plugin.video.sports'
_addon = xbmcaddon.Addon(id=addon_id)
iLengths = ['1','2','3','4','5','10','15','30','60']
nLengths = ['5','6','7','8','9','10','15','30']
dTypes = ['Individual Game Notifications','Ticker Notifications']
nTypes = {'Basketball':{'Upcoming Game':'nba_upcominggame','Game Started':'nba_startofgame','Lead Change':'nba_leadchange',
                        'Period Change':'nba_periodchange','Game Ended':'nba_endofgame'},
          'Ice Hockey':{'Upcoming Game':'nhl_upcominggame','Game Started':'nhl_startofgame','Score Change':'nhl_scorechange',
                        'Period Change':'nhl_periodchange','Game Ended':'nhl_endofgame'},
          'Baseball':  {'Upcoming Game':'mlb_upcominggame','Game Started':'mlb_startofgame','Score Change':'mlb_scorechange',
                        'Inning Change':'mlb_inningchange','Game Ended':'mlb_endofgame'},
          'Soccer':    {'Upcoming Game':'soccer_upcominggame','Game Started':'soccer_startofgame','Score Change':'soccer_scorechange',
                        'Halftime':'soccer_halftime','Game Ended':'soccer_endofgame'}}
sports = {'Basketball':'nba_enable','Ice Hockey':'nhl_enable','Baseball':'mlb_enable','Soccer':'soccer_enable'}
leagues = {
            "English Premier League":     "eng.1",
            "English League Championship":"eng.2",
            "English League One":         "eng.3",
            "English League Two":         "eng.4",
            "UEFA Europa League":         "uefa.europa",
            "UEFA Champions League":      "uefa.champions",
            "Italian Serie A":            "ita.1",
            "Spain La Liga":              "esp.1",
            "Scottish Premier League":    "sco.1",
            "French Ligue 1":             "fra.1",
            "German Bundesliga":          "ger.1",
            "Major League Soccer":        "usa.1",
            "International Friendlies":   "fifa.friendly",
            "World Cup":                  "fifa.world"
          }

def load(first_time):
    if not first_time:
        resetConfirmed = dialog.yesno('Sports Guru', 'Continuing with the set-up will wipe out your existing preferences. [B]Are you sure?[/B]')
        if resetConfirmed:
            try:
                import shutil
                current_settings = xbmc.translatePath('special://userdata/addon_data/plugin.video.sports')
                shutil.rmtree(current_settings)
                xbmc.executebuiltin('Container.Update')
            except:
                pass
        else:
            return
    else:
        _addon.setSetting('firstrun', 'false')
    
    ok = dialog.ok('Sports Guru', 'Welcome to the Sports Guru set-up wizard! Click Ok to begin.')
    if ok:
        wantnotifications = dialog.yesno('Sports Guru', 'Do you want to use the notifications service the add-on offers?')
        if wantnotifications:
            _addon.setSetting('allow', 'true')
            
            ok = dialog.ok('Sports Guru', 'Great! First things first, please select Update Interval.\n' + \
                           '[B]Note:[/B] It\'s best to stick with the default 1 minute. ' + \
                           'However, shorter intervals may have an adverse effect on low-spec devices (causing lag).')
            howoften = dialog.select('Sports Guru', iLengths)
            if howoften > -1:
                _addon.setSetting('interval', iLengths[howoften])
                ok = dialog.ok('Sports Guru', 'Second, please select the notification format you prefer.')
                whatkind = dialog.select('Sports Guru', dTypes)
                if whatkind > -1:
                    ok = dialog.ok('Sports Guru', 'Next please select the notification timeout length.')
                    nLength = dialog.select('Sports Guru - Notification Timeout (seconds)', nLengths)
                    if whatkind == 0:
                        _addon.setSetting('multi', 'false')
                        _addon.setSetting('Ntimeout', nLengths[nLength])
                    elif whatkind == 1:
                        _addon.setSetting('multi', 'true')
                        _addon.setSetting('Ttimeout', nLengths[nLength])
                    else:
                        _addon.setSetting('allow', 'false')
                        return
                    ok = dialog.ok('Sports Guru', 'Alright, I\'ve set your update interval to %s minute(s) ' % str(iLengths[howoften]) + \
                                   'and notification preference to %s. Now let\'s move onto the sports/leagues you want notifications for.' % dTypes[whatkind])
                    whichsports = dialog.multiselect('Choose your Sports', sports.keys())
                    if whichsports is not None:
                        for sIndex, key in enumerate(sports.keys()):
                            s = sports.keys()[sIndex]
                            sportId = sports[s]
                            if sIndex in whichsports:
                                _addon.setSetting(sportId, 'true')
                                #Ask what types of notification they want for this sport
                                ok = dialog.ok('Sports Guru', 'Please select the notification types you want for %s.' % s)
                                whichnotifications = dialog.multiselect('Choose Notification Types', nTypes[s].keys())
                                if whichnotifications is not None:
                                    for nIndex, key in enumerate(nTypes[s].keys()):
                                        n = nTypes[s].keys()[nIndex]
                                        settingId = nTypes[s][n]
                                        if nIndex in whichnotifications:
                                            _addon.setSetting(settingId, 'true')
                                        else:
                                            _addon.setSetting(settingId, 'false')
                                else:
                                    _addon.setSetting('allow', 'false')
                                    return
                                
                                if 'Soccer' in s:
                                    ok = dialog.ok('Sports Guru', 'I noticed you selected Soccer. ' + \
                                                   'Since that sport has multiple leagues click Ok to select the leagues you want.')
                                    whichleagues = dialog.multiselect('Choose your Soccer Leagues', leagues.keys())
                                    if whichleagues is not None:
                                        for lIndex, key in enumerate(leagues.keys()):
                                            l = leagues.keys()[lIndex]
                                            leagueId = leagues[l]
                                            if lIndex in whichleagues:
                                                _addon.setSetting(leagueId, 'true')
                                                ok = dialog.ok('Sports Guru', 'Click Ok to select the teams you want notifications for in the %s' % l)
                                                from resources import manager
                                                manager.load('soccer', leagueId)
                                            else:
                                                _addon.setSetting(leagueId, 'false')
                                    else:
                                        _addon.setSetting('allow', 'false')
                                        return
                                else:
                                    ok = dialog.ok('Sports Guru', 'Click Ok to select the teams you want notifications for in the [B]%s[/B] League' % sportId.split('_')[0].upper())
                                    from resources import manager
                                    manager.load(sportId.split('_')[0])
                            else:
                                _addon.setSetting(sportId, 'false')
                        restart = dialog.ok('Sports Guru', 'Set-up is now complete. For your settings to take effect please restart Kodi.')
                    else:
                        _addon.setSetting('allow', 'false')
                else:
                    _addon.setSetting('allow', 'false')
            else:
                _addon.setSetting('allow', 'false')
        else:
            _addon.setSetting('allow', 'false')
    else:
        _addon.setSetting('allow', 'false')