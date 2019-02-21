import importlib
import xbmcaddon
import xbmcgui
import xbmc
import json
import time
import re
import os

addon_id = 'plugin.video.sports'
_addon = xbmcaddon.Addon(id=addon_id)
_path = 'special://home/addons/%s/' % addon_id
_teams = xbmc.translatePath(os.path.join(_path, "resources/teams.json"))
_tempdata = xbmc.translatePath(os.path.join(_path, "temp.json"))
_changelog = xbmc.translatePath(os.path.join(_path, "changelog.txt"))

#wipe out existing tempdata
with open(_tempdata, "wb") as f: 
    f.write('{"nba":{},"nhl":{},"mlb":{},"eng.1":{},"eng.2":{},"eng.3":{},' + \
            '"eng.4":{},"uefa.champions":{},"uefa.europa":{},"usa.1":{},' + \
            '"ita.1":{},"esp.1":{},"sco.1":{},"fra.1":{},"ger.1":{},' + \
            '"fifa.friendly":{},"fifa.world":{}}')

first_time = eval(_addon.getSetting('firstrun').title())
should_i_start = eval(_addon.getSetting('allow').title())
time_between_checks = int(_addon.getSetting('interval')) * 60
we_should_show_multi = eval(_addon.getSetting('multi').title())
version = _addon.getSetting('sgVersion')

xbmc.log("Sports Guru: Welcome to Sports Guru!", level=xbmc.LOGNOTICE)
from resources import checks
valid = checks.validate(first_time)

if first_time is True:
    xbmc.log("Sports Guru: Running First-Time Wizard", level=xbmc.LOGNOTICE)
    from resources import wizard
    wizard.load(first_time)
    _addon.setSetting('firstrun', 'false')
else:
    with open(_changelog, "rb") as cl:
        sChangelog = cl.read()
    v = sChangelog.split(' ')[0]
    if v.replace('v','') != version:
        sChangelog = sChangelog.split('===')[0]
        ok = xbmcgui.Dialog().textviewer('Sports Guru - %s Release Notes' % v, sChangelog)
        _addon.setSetting('sgVersion', v.replace('v',''))
    else:
        try:
            last_donation_prompt = time.strftime('%m%Y', time.strptime(_addon.getSetting('lastmonth'), '%m%Y'))
            thismonth = time.strftime("%m%Y")
            if thismonth > last_donation_prompt:
                xbmc.log("Sports Guru: It's time to show the donation prompt again", level=xbmc.LOGNOTICE)
                dialog = xbmcgui.Dialog()
                line1 = 'As you may or may not know, a lot of time and effort has gone into the Sports Guru add-on. ' + \
                        'It is by far the largest project I\'ve taken on in my leisure time, having taken 3+ months to ' + \
                        'reach a version I was comfortable releasing publicly. ' + \
                        'So, if you regularly enjoy it please consider donating what you can. ' + \
                        'Donations help me pay for necessities such as pet supplies, food, and medical bills. ' + \
                        'The misses is on permanent disability due to multiple chronic illnesses, so we\'re a one-income household. ' + \
                        'Therefore, every little bit helps. Donations also allow me to spend more time adding to & improving the add-on ' + \
                        'instead of doing freelance gigs to make an extra buck.\n\n' + \
                        'For those that have money to spare you can donate directly via Paypal. ' + \
                        'To donate anonymously you can send any amount of btc, bch, eth or ltc. ' + \
                        'If you aren\'t able to spare anything that\'s completely understandable. ' + \
                        'However, if you\'d like you can still "donate" if you have an android phone by downloading & playing free crypto games.\n' + \
                        '[B]Note: This is a monthly automated prompt.[/B]'
                ok = dialog.textviewer('Sports Guru - Please take a minute to read', line1)
                from resources.donations import donations
                donations.load()
                _addon.setSetting('lastmonth', str(thismonth))
        except:
            pass

    #get team list
    with open(_teams, "rb") as f: 
        teams_obj = json.load(f)
        
    all_sports = ['nba','mlb','soccer','nhl']
    all_leagues = ['eng.1','eng.2','eng.3','eng.4','uefa.champions','uefa.europa',
                   'usa.1','ita.1','esp.1','sco.1','fra.1','ger.1','fifa.friendly','fifa.world']
    enabled_sports = [sport for sport in all_sports if eval(_addon.getSetting('%s_enable' % sport).title()) is True]
    if 'soccer' in enabled_sports:
        enabled_soccer_leagues = [league for league in all_leagues if eval(_addon.getSetting(league).title()) is True]

    if __name__ == '__main__':
        if should_i_start is True and valid is True:
            monitor = xbmc.Monitor()
            xbmc.log("Sports Guru: Service Started", level=xbmc.LOGNOTICE)
            
            while not monitor.abortRequested():
                #Sleep/wait for abort
                xbmc.log("Sports Guru: Waiting %s seconds before checking for score updates" % str(time_between_checks),
                         level=xbmc.LOGNOTICE)
                
                if monitor.waitForAbort(time_between_checks):
                    # Abort was requested while waiting. We should exit
                    break
                
                update_dict = {}
                #Now get current data for each enabled sport
                for sport in enabled_sports:
                    api = importlib.import_module('resources.%s.api' % sport)
                    xbmc.log("Sports Guru: Checking for %s updates" % sport, 
                             level=xbmc.LOGNOTICE)
                    if sport == 'soccer':
                        for league in enabled_soccer_leagues:
                            teams = teams_obj[league]['selected']
                            updates = api.check_for_updates(league, teams)
                            
                            if len(updates) > 0:
                                xbmc.log("Sports Guru: We have %s updates for %s soccer league" % (str(len(updates)), league), 
                                         level=xbmc.LOGNOTICE)
                                if we_should_show_multi is True:
                                    update_dict[league] = updates
                                else:
                                    from resources import notification
                                    popup = notification.Scores(sport=league)
                                    popup.queue(updates)
                            else: 
                                xbmc.log("Sports Guru: No updates found for %s soccer league" % league, 
                                         level=xbmc.LOGNOTICE)
                    else:
                        teams = teams_obj[sport]['selected']
                        updates = api.check_for_updates(teams)
                        if len(updates) > 0:
                            xbmc.log("Sports Guru: We have %s updates for %s" % (str(len(updates)), sport), 
                                     level=xbmc.LOGNOTICE)
                            if we_should_show_multi is True:
                                update_dict[sport] = updates
                            else:
                                from resources import notification
                                popup = notification.Scores(sport=sport)
                                popup.queue(updates)
                        else: 
                            xbmc.log("Sports Guru: No updates found for %s" % sport, 
                                     level=xbmc.LOGNOTICE)
                if we_should_show_multi is True and len(update_dict) > 0:
                    from resources import ticker
                    popup = ticker.Scores()
                    popup.queue(update_dict)