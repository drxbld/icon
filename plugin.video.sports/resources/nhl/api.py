from urlparse import parse_qsl
from urllib import urlencode
from urllib import unquote
import xbmcplugin
import xbmcaddon
import requests
import datetime
import xbmcgui
import xbmc
import json
import sys
import ast
import re
import os

try:
    _url = sys.argv[0]
    _handle = int(sys.argv[1])
except:
    #Module is being accessed by service.py
    pass
    
addon_id = 'plugin.video.sports'
addon = xbmcaddon.Addon(id=addon_id)
addonname = addon.getAddonInfo('name')
path = 'special://home/addons/%s/' % addon_id
icon = addon.getAddonInfo('icon')
fanart = xbmc.translatePath(os.path.join(path, "resources/nhl/background.jpg"))
_tempdata = xbmc.translatePath(os.path.join(path, "temp.json"))
nhl_stats = 'http://www.espn.com/nhl/bottomline/scores'
espn_xhr_url = 'http://cdn.espn.com/core/nhl/recap?gameId=%s&xhr=1'
nhl_xhr_url = 'https://statsapi.web.nhl.com/api/v1/schedule?startDate=%s&endDate=%s'
conference_standings = 'http://api.espn.com/v1/sports/hockey/nhl/standings?apikey=iay88gnrz4un1jiaclo88df33'

def get_url(**kwargs):
    kwargs = {k: unicode(v).encode('ascii', 'ignore') for k,v in kwargs.iteritems()}
    return '{0}?{1}'.format(_url, urlencode(kwargs))

#Starting endpoint
#Returns json-friendly list object [{},{},{}]
def get_games():
    resp = requests.get(nhl_stats)
    #for testing
    #resp = requests.get('https://pastebin.com/raw/nkxaiy84')
    decoded_resp = unquote(resp.text)

    game_list = []
    game = 0
    for line in decoded_resp.split('&'):
        if line.startswith('nhl_s_left'):
            #first datapoint of game
            if ' at ' in line:
                #game hasn't started yet
                teams = line.split('=')[1].split(' at ')
            else:
                teams = line.split('=')[1].split('   ')
                        
            current_time = re.compile('\((.+?)\)').findall(teams[1])[0]
            teams[1] = teams[1].replace(' (%s)' % current_time, '')
                    
            if current_time == '0:00 IN OT' or current_time == 'END OF 3RD':
                current_time = 'FINAL'
                    
            if 'PM' not in current_time and 'AM' not in current_time:
                team_one  = teams[0].rsplit(' ', 1)[0].replace('^','')
                team_two  = teams[1].rsplit(' ', 1)[0].replace('^','')
                score_one = teams[0].rsplit(' ', 1)[1]
                score_two = teams[1].rsplit(' ', 1)[1]
            else:
                team_one  = teams[0]
                team_two  = teams[1]
                score_one = '0'
                score_two = '0'
                    
            game_list.append({'Title':'%s vs %s' % (team_one, team_two),
                              'Name1':team_one,    'Name2':team_two,
                              'Score1':score_one,  'Score2':score_two,
                              'Time':current_time, 'PlayerHighlights':[]})
        if line.startswith('nhl_s_right') and not 'count' in line:
            #Top Player Stats
            nhl_s_right  = line.split('=')[1]
            player_name  = " ".join(nhl_s_right.split(' ', 2)[:2])
            player_stats = " ".join(nhl_s_right.split(' ', 2)[2:])
            game_list[game]['PlayerHighlights'].append({'PlayerName':player_name,
                                                        'PlayerStats':player_stats})
        if line.startswith('nhl_s_url'):
            #last datapoint of game
            game_list[game]['FullStats'] = line.split('=', 1)[1]
            game += 1
    return game_list

def check_for_updates(teams):
    with open(_tempdata, "rb") as f:
        tempdata = json.load(f)
        
    types = [type 
             for type in ['nhl_upcominggame','nhl_startofgame','nhl_scorechange','nhl_periodchange','nhl_endofgame'] 
             if eval(addon.getSetting(type).title()) is True]
    updated_games = get_games()
    games_to_keep = [updated_game for updated_game in updated_games
                     if updated_game['Name1'].replace('New York ', 'NY '
                     ).replace('New Jersey ', 'NJ ')
                     in str(teams).replace('New York ', 'NY '
                     ).replace('New Jersey ', 'NJ ') or updated_game['Name2'
                     ].replace('New York ', 'NY ').replace('New Jersey ',
                     'NJ ') in str(teams).replace('New York ', 'NY '
                     ).replace('New Jersey ', 'NJ ')]
    updates = []
    td = tempdata['nhl']
    #Now look at game data to see if any notifications need to be presented
    for game in games_to_keep:
        gametitle = game['Title']
        if 'nhl_upcominggame' in types and gametitle not in td.keys():
            #We haven't announced this upcoming game yet, so do so
            updates.append(game)
        elif 'nhl_startofgame' in types and any(['PM' in td[gametitle]['Time'],
             'AM' in td[gametitle]['Time']]) and all(['PM' not in game['Time'
             ], 'AM' not in game['Time'], 'FINAL' not in game['Time']]):
            updates.append(game)
        elif 'nhl_scorechange' in types and any([int(game['Score1']) > int(td[gametitle]['Score1']),
                                                 int(game['Score2']) > int(td[gametitle]['Score2'])]):
            updates.append(game)
        elif 'nhl_periodchange' in types and any([all(['1ST' in td[gametitle]['Time'], '2ND' in game['Time']]),
                                                  all(['2ND' in td[gametitle]['Time'], '3RD' in game['Time']]),
                                                  all(['3RD' in td[gametitle]['Time'], 'OT' in game['Time']]),
                                                  all(['OT' in td[gametitle]['Time'], 'SO' in game['Time']])]):
            updates.append(game)
        elif 'nhl_endofgame' in types and any([all(['4TH' in td[gametitle]['Time'], 'FINAL' in game['Time']]),
                                               all(['OT' in td[gametitle]['Time'], 'FINAL' in game['Time']]),
                                               all(['SO' in td[gametitle]['Time'], 'FINAL' in game['Time']])]):
            updates.append(game)
        #Save/Overwrite tempdata as we go to save time
        tempdata['nhl'][gametitle] = game
    with open(_tempdata, "wb") as f: 
        f.write(json.dumps(tempdata, indent=4, sort_keys=True))
    return updates

def display_mainmenu():
    list_item = xbmcgui.ListItem(label='Full-Game Replays')
    list_item.setArt({'fanart':fanart,'thumb':icon,'poster':icon})
    list_item.setInfo('video',{'plot':'Full-Game Replays section for all past games.\n\n[COLOR yellow]Note:[/COLOR] Pin Generation is required to use this section.','title':'Full-Game Replays'})
    replays = get_url(sport='nhl', endpoint='replays')
    xbmcplugin.addDirectoryItem(_handle, replays, list_item, isFolder=True)
    
    list_item = xbmcgui.ListItem(label='Today\'s Games')
    list_item.setArt({'fanart':fanart,'thumb':icon,'poster':icon})
    list_item.setInfo('video',{'plot':'Games from previous night will be shown until noon the following day. After noon you will see games for today/the upcoming night','title':'Today\'s Games'})
    todaysgames = get_url(sport='nhl', endpoint='today')
    xbmcplugin.addDirectoryItem(_handle, todaysgames, list_item, isFolder=True)
    
    list_item = xbmcgui.ListItem(label='League Standings')
    list_item.setArt({'fanart':fanart,'thumb':icon,'poster':icon})
    list_item.setInfo('video',{'plot':'League standings divided into Eastern & Western Conferences','title':'League Standings'})
    standings = get_url(sport='nhl', endpoint='standings')
    xbmcplugin.addDirectoryItem(_handle, standings, list_item, isFolder=False)
    
    xbmcplugin.addSortMethod(_handle, xbmcplugin.SORT_METHOD_NONE)
    xbmcplugin.endOfDirectory(_handle)
       
def display_gameoptions(game_obj):
    game = ast.literal_eval(game_obj)
    list_item = xbmcgui.ListItem(label='Highlights')
    list_item.setArt({'fanart':fanart,'thumb':icon,'poster':icon})
    list_item.setInfo('video',{'plot':'[COLOR green]HD[/COLOR] Highlight clips of the game','title':'Game Highlights'})
    hItem = get_url(sport='nhl', highlights=game['FullStats'].replace('boxscore','video'), game_obj=game)
    xbmcplugin.addDirectoryItem(_handle, hItem, list_item, isFolder=True)
    
    list_item = xbmcgui.ListItem(label='Boxscores')
    list_item.setArt({'fanart':fanart,'thumb':icon,'poster':icon})
    list_item.setInfo('video',{'plot':'In-depth boxscore data for both teams','title':'Boxscores'})
    bItem = get_url(sport='nhl', boxscores=game['FullStats'], game_obj=game)
    xbmcplugin.addDirectoryItem(_handle, bItem, list_item, isFolder=False)
    
    list_item = xbmcgui.ListItem(label='Play-by-Play')
    list_item.setArt({'fanart':fanart,'thumb':icon,'poster':icon})
    list_item.setInfo('video',{'plot':'Entire play-by-play for the game','title':'Play-by-Play'})
    playbyplay = get_url(sport='nhl', playbyplay=game['FullStats'].replace('boxscore','playbyplay'), game_obj=game)
    xbmcplugin.addDirectoryItem(_handle, playbyplay, list_item, isFolder=False)
    
    xbmcplugin.addSortMethod(_handle, xbmcplugin.SORT_METHOD_NONE)
    xbmcplugin.endOfDirectory(_handle)
    
#Input:  json-friendly list object [{},{},{}]
#Output: games directory
def display_games(games):
    if len(games) > 0:
        for game in games:
            team1 = game['Title'].split(' vs ')[0]
            team2 = game['Title'].split(' vs ')[1]
            title = '%s (%s)' % (game['Title'], game['Time'])
            if len(game['PlayerHighlights']) > 0:
                details = '%s\n%s\n\n[B]Highlights:[/B]\n' % (game['Title'], game['Time'])
                details += '\n'.join(['%s %s' % (highlight['PlayerName'], highlight['PlayerStats']) 
                                      for highlight in game['PlayerHighlights']])
            else:
                details = '%s\n%s' % (game['Title'], game['Time'])
                details += '\n%s - %s' % (game['Score1'], game['Score2'])
            
            list_item = xbmcgui.ListItem(label=title)
            list_item.setArt({'fanart':fanart,'thumb':icon,'poster':icon})
            list_item.setInfo('video',{'plot':details,'title':title})
            
            innermenu = get_url(sport='nhl', endpoint='details', game_obj=game)
            xbmcplugin.addDirectoryItem(_handle, innermenu, list_item, isFolder=True)
        xbmcplugin.addSortMethod(_handle, xbmcplugin.SORT_METHOD_NONE)
        xbmcplugin.endOfDirectory(_handle)
    else:
        line1 = 'There are no games scheduled for this league today'
        line2 = 'However, you can watch Full Game Replays.'
        line3 = '[B]Note[/B]: Not all games may be available to replay.'
        xbmcgui.Dialog().ok(addonname, line1, line2, line3)

#Input:  url with gameId
#Output: json-friendly list object [{},{},{}] 
#        of highlights for specific game
def get_highlights(game_link):
    if 'video' in game_link:
        try:
            gameId            = game_link.split('=')[1]
            data              = requests.get(espn_xhr_url % gameId)
            j_obj             = json.loads(data.text)
            game              = j_obj['game']['sports'][0]['leagues'][0]['events'][0]['competitions'][0]
            teams             = game['competitors']
            t1name            = teams[0]['team']['name']
            t2name            = teams[1]['team']['name']
            gdate             = game['date'][:10]
            
            #Try date from api first
            nhl_games_on_date = nhl_xhr_url % (gdate, gdate)
            nhl_resp          = requests.get(nhl_games_on_date)
            nhl_obj           = json.loads(nhl_resp.text)['dates'][0]
            
            nhl_game_url      = ''
            for g in nhl_obj['games']:
                test1 = g['teams']['away']['team']['name']
                test2 = g['teams']['home']['team']['name']
                if (t1name in test1 and t2name in test2) or (t1name in test2 and t2name in test1):
                    nhl_game_url = 'https://statsapi.web.nhl.com%s' % g['content']['link']
                    break
            #if nhl_game_url is empty then we need to try checking yesterday's date.
            if nhl_game_url == '':
                #YYYY-MM-DD
                split_date        = gdate.split('-')
                date              = datetime.datetime(int(split_date[0]), int(split_date[1]), int(split_date[2]))
                date             -= datetime.timedelta(days=1)
                sdate             = date.strftime('%Y-%m-%d')
                
                nhl_games_on_date = nhl_xhr_url % (sdate, sdate)
                nhl_resp          = requests.get(nhl_games_on_date)
                nhl_obj           = json.loads(nhl_resp.text)['dates'][0]
                
                for g in nhl_obj['games']:
                    test1 = g['teams']['away']['team']['name']
                    test2 = g['teams']['home']['team']['name']
                    if (t1name in test1 and t2name in test2) or (t1name in test2 and t2name in test1):
                        nhl_game_url = 'https://statsapi.web.nhl.com%s' % g['content']['link']
                        break
            
            nhl_site_resp   = requests.get(nhl_game_url)
            nhl_site_clips  = json.loads(nhl_site_resp.text)
            
            videos          = nhl_site_clips['highlights']['scoreboard']['items']
            highlights_list = []
            for video in videos:
                if video['type'] == 'video':
                    image       = video['image']['cuts']['1136x640']['src']
                    title       = video['title']
                    description = video['description']
                    clip        = video['playbacks'][-1]['url']
                    highlights_list.append({'Image': image,
                                            'Title': title,
                                            'Description': description,
                                            'Clip': clip})
            return highlights_list
        except:
            return []
    else:
        return []
        
#Input:  json-friendly list object [{},{},{}]
#Output: highlight clips directory
def display_highlights(highlights):
    for highlight in highlights:
        list_item = xbmcgui.ListItem(path=highlight['Clip'], label=highlight['Title'])
        list_item.setArt({'fanart': highlight['Image'],
                          'thumb':  highlight['Image'],
                          'poster': highlight['Image']})
        list_item.setInfo('video', {'plot':  highlight['Description'],
                                    'title': highlight['Title']})
        list_item.setProperty('IsPlayable','true')
        url = get_url(sport='nhl', play_me=highlight['Clip'])
        xbmcplugin.addDirectoryItem(_handle, url, list_item, False)
    xbmcplugin.addSortMethod(_handle, xbmcplugin.SORT_METHOD_NONE)
    xbmcplugin.endOfDirectory(_handle)

def get_standings():
    data    = requests.get(conference_standings, headers={'Cache-Control':'no-cache'})
    j_obj   = json.loads(data.text)
    headers = ['GP','W','L','OTL','PTS','ROW','SOW','SOL','HOME','ROAD','GF','GA','DIFF','L10','STRK']
    conf1   = j_obj['sports'][0]['leagues'][0]['groups'][0]
    conf2   = j_obj['sports'][0]['leagues'][0]['groups'][1]
    name1   = conf1['name']
    name2   = conf2['name']
    standings = {'Headers':headers, 'League Name':j_obj['sports'][0]['leagues'][0]['name'],
                 name1:[], name2:[]}
    for group in conf1['groups']:
        for competitor in group['competitors']:
            temp_dict = {'Name':'%s %s' % (competitor['location'], competitor['name']),
                         'GP':   str(competitor['stats']['gamesPlayed']),
                         'W':    str(competitor['record']['wins']),
                         'L':    str(competitor['record']['losses']),
                         'OTL':  str(competitor['record']['overtimeLosses']),
                         'PTS':  str(competitor['stats']['standingsPoints']),
                         'ROW':  str(competitor['record']['regulationOvertimeWins']),
                         'SOW':  str(competitor['record']['shootoutWins']),
                         'SOL':  str(competitor['record']['shootoutLosses']),
                         'HOME': competitor['record']['home']['summary'],
                         'ROAD': competitor['record']['away']['summary'],
                         'GF':   str(competitor['stats']['pointsForTotal']),
                         'GA':   str(competitor['stats']['pointsAgainstTotal']),
                         'DIFF': str(competitor['stats']['pointsForTotal'] - competitor['stats']['pointsAgainstTotal']),
                         'L10':  competitor['record']['lastTen']['summary'],
                         'STRK': str(competitor['stats']['streak'])}
            if int(temp_dict['DIFF']) > 0:
                temp_dict['DIFF'] = '[COLOR green]+%s[/COLOR]' % temp_dict['DIFF']
            elif int(temp_dict['DIFF']) < 0:
                temp_dict['DIFF'] = '[COLOR red]%s[/COLOR]' % temp_dict['DIFF']
            if int(temp_dict['STRK']) > 0:
                temp_dict['STRK'] = '[COLOR green]W%s[/COLOR]' % temp_dict['STRK']
            elif int(temp_dict['STRK']) < 0:
                temp_dict['STRK'] = '[COLOR red]L%s[/COLOR]' % temp_dict['STRK'].replace('-','')
            standings[name1].append(temp_dict)
    new1 = sorted(standings[name1], key=lambda k: int(k['PTS']), reverse=True)
    standings[name1] = new1
    for group in conf2['groups']:
        for competitor in group['competitors']:
            temp_dict = {'Name':'%s %s' % (competitor['location'], competitor['name']),
                         'GP':   str(competitor['stats']['gamesPlayed']),
                         'W':    str(competitor['record']['wins']),
                         'L':    str(competitor['record']['losses']),
                         'OTL':  str(competitor['record']['overtimeLosses']),
                         'PTS':  str(competitor['stats']['standingsPoints']),
                         'ROW':  str(competitor['record']['regulationOvertimeWins']),
                         'SOW':  str(competitor['record']['shootoutWins']),
                         'SOL':  str(competitor['record']['shootoutLosses']),
                         'HOME': competitor['record']['home']['summary'],
                         'ROAD': competitor['record']['away']['summary'],
                         'GF':   str(competitor['stats']['pointsForTotal']),
                         'GA':   str(competitor['stats']['pointsAgainstTotal']),
                         'DIFF': str(competitor['stats']['pointsForTotal'] - competitor['stats']['pointsAgainstTotal']),
                         'L10':  competitor['record']['lastTen']['summary'],
                         'STRK': str(competitor['stats']['streak'])}
            if int(temp_dict['DIFF']) > 0:
                temp_dict['DIFF'] = '[COLOR green]+%s[/COLOR]' % temp_dict['DIFF']
            elif int(temp_dict['DIFF']) < 0:
                temp_dict['DIFF'] = '[COLOR red]%s[/COLOR]' % temp_dict['DIFF']
            if int(temp_dict['STRK']) > 0:
                temp_dict['STRK'] = '[COLOR green]W%s[/COLOR]' % temp_dict['STRK']
            elif int(temp_dict['STRK']) < 0:
                temp_dict['STRK'] = '[COLOR red]L%s[/COLOR]' % temp_dict['STRK'].replace('-','')
            standings[name2].append(temp_dict)
    new2 = sorted(standings[name2], key=lambda k: int(k['PTS']), reverse=True)
    standings[name2] = new2
    return standings
    
def get_playbyplay(game_link):
    if all(['preview' not in game_link, 'scoreboard' not in game_link,
            'gamecast' not in game_link, 'playbyplay' in game_link]):
        gameId            = game_link.split('=')[1]
        data              = requests.get(espn_xhr_url % gameId)
        j_obj             = json.loads(data.text)
        game              = j_obj['game']['sports'][0]['leagues'][0]['events'][0]['competitions'][0]
        teams             = game['competitors']
        t1name            = teams[0]['team']['name']
        t2name            = teams[1]['team']['name']
        teamlogo          = {teams[0]['team']['abbreviation']: teams[0]['team']['logos']['large']['href'],
                             teams[1]['team']['abbreviation']: teams[1]['team']['logos']['large']['href']}
        gdate             = game['date'][:10]
        
        #Try date from api first
        nhl_games_on_date = nhl_xhr_url % (gdate, gdate)
        nhl_resp          = requests.get(nhl_games_on_date)
        nhl_obj           = json.loads(nhl_resp.text)['dates'][0]
        
        nhl_game_url      = ''
        for g in nhl_obj['games']:
            test1 = g['teams']['away']['team']['name']
            test2 = g['teams']['home']['team']['name']
            if (t1name in test1 and t2name in test2) or (t1name in test2 and t2name in test1):
                nhl_game_url = 'https://statsapi.web.nhl.com%s' % g['link']
                break
        #if nhl_game_url is empty then we need to try checking yesterday's date.
        if nhl_game_url == '':
            #YYYY-MM-DD
            split_date        = gdate.split('-')
            date              = datetime.datetime(int(split_date[0]), int(split_date[1]), int(split_date[2]))
            date             -= datetime.timedelta(days=1)
            sdate             = date.strftime('%Y-%m-%d')
            
            nhl_games_on_date = nhl_xhr_url % (sdate, sdate)
            nhl_resp          = requests.get(nhl_games_on_date)
            nhl_obj           = json.loads(nhl_resp.text)['dates'][0]
            
            for g in nhl_obj['games']:
                test1 = g['teams']['away']['team']['name']
                test2 = g['teams']['home']['team']['name']
                if (t1name in test1 and t2name in test2) or (t1name in test2 and t2name in test1):
                    nhl_game_url = 'https://statsapi.web.nhl.com%s' % g['link']
                    break
        
        nhl_site_resp  = requests.get(nhl_game_url)
        nhl_site_stats = json.loads(nhl_site_resp.text)
        
        ignore_play_types   = ['PERIOD_OFFICIAL','PERIOD_READY','GAME_SCHEDULED']
        donot_double_events = ['Giveaway','Takeaway','Period End','Game End','Shootout Complete']
        playbyplay          = []
        linescores          = nhl_site_stats['liveData']['linescore']
        so_score            = {linescores['teams']['away']['team']['triCode']:0,
                               linescores['teams']['home']['team']['triCode']:0}
        
        for play in nhl_site_stats['liveData']['plays']['allPlays']:
            if not play['result']['eventTypeId'] in ignore_play_types:
                #Get team logo
                if play.get('team'):
                    try:
                        team = teamlogo[play['team']['triCode']]
                    except:
                        team = teamlogo[play['team']['triCode'][:-1]]
                else:
                    team = ''
                
                #Get time on clock
                if play['about']['ordinalNum'] == 'SO':
                    t = '00:00'
                else:
                    t = play['about']['periodTimeRemaining']
                    
                #Get play details
                if play['result'].get('gameWinningGoal') and play['result']['gameWinningGoal']:
                    p = 'Game-Winning Goal: %s' % play['result']['description']
                elif play['result']['event'] in donot_double_events:
                    p = play['result']['description']
                elif play['result']['event'] == 'Period Start':
                    p = '%s %s' % (play['about']['ordinalNum'], play['result']['description'])
                else:
                    p = '%s: %s' % (play['result']['event'], play['result']['description'])
                    
                #Get score
                if play['about']['ordinalNum'] == 'SO':
                    if play['result']['event'] == 'Goal':
                        so_score[play['team']['triCode']] += 1
                    away = linescores['teams']['away']['team']['triCode']
                    home = linescores['teams']['home']['team']['triCode']
                    if play['result']['description'] == 'End of Shootout':
                        if int(so_score[away]) > int(so_score[home]):
                            away_score = str(int(play['about']['goals']['away'])+1)
                            home_score = play['about']['goals']['home']
                        else:
                            away_score = play['about']['goals']['away']
                            home_score = str(int(play['about']['goals']['home'])+1)
                        s = '%s - %s' % (away_score, 
                                         home_score)
                        so_score[away] = away_score
                        so_score[home] = home_score
                    else:
                        s = '%s - %s' % (so_score[away], 
                                         so_score[home])
                else:
                    s = '%s - %s' % (play['about']['goals']['away'], 
                                     play['about']['goals']['home'])
                                 
                #Bold play if scoring occurred
                if play['result']['event'] == 'Goal':
                    playbyplay.append({'Time': '[B]%s[/B]' % t, 
                                       'Team': team,
                                       'Play': '[B]%s[/B]' % p,
                                       'Score':'[B]%s[/B]' % s})
                else:
                    playbyplay.append({'Time': t, 
                                       'Team': team,
                                       'Play': p,
                                       'Score':s})
        return playbyplay
    else:
        return []
    
#Input:  url with gameId
#Output: json-friendly object {}
#        of periodic scores for specific game
def get_scoreboard(game_link):
    if not 'preview' in game_link:
        gameId     = game_link.split('=')[1]
        data       = requests.get(espn_xhr_url % gameId)
        j_obj      = json.loads(data.text)
        game       = j_obj['game']['sports'][0]['leagues'][0]['events'][0]['competitions'][0]
        #game_time = '%s %s' % (game['clock'], game['period'])
        game_time  = game['status']['description']
        team1      = game['competitors'][0]
        team2      = game['competitors'][1]
        
        scoreboard = {}
        team1name  = team1['team']['abbreviation']
        total1     = team1['score']
        scores1    = []
        team2name  = team2['team']['abbreviation']
        total2     = team2['score']
        scores2    = []
        
        for p in range(0, 3):
            try:
                scores1.append(team1['linescores'][p]['score'])
                scores2.append(team2['linescores'][p]['score'])
            except IndexError:
                scores1.append('')
                scores2.append('')

        scoreboard['Team1'] = {'Name'  : team1name,
                               'Score1': scores1[0],
                               'Score2': scores1[1],
                               'Score3': scores1[2],
                               'Total' : total1}
        scoreboard['Team2'] = {'Name'  : team2name,
                               'Score1': scores2[0],
                               'Score2': scores2[1],
                               'Score3': scores2[2],
                               'Total' : total2}
        scoreboard['Time'] = game_time
        return scoreboard
    else:
        return {}

#Input:  url with gameId
#Output: json-friendly object {}
#        of box scores for specific game
def get_boxscores(game_link):
    if not 'preview' in game_link:
        gameId        = game_link.split('=')[1]
        data          = requests.get(espn_xhr_url % gameId)
        j_obj         = json.loads(data.text)
        game          = j_obj['game']['sports'][0]['leagues'][0]['events'][0]['competitions'][0]
        team1         = game['competitors'][0]
        team2         = game['competitors'][1]
        team1location = team1['homeAway']
        team2location = team2['homeAway']
        players1      = team1['team']['athletes']
        players2      = team2['team']['athletes']
        boxscores     = {}
        
        boxscores['Team1'] = {'Name':   team1['team']['name'],
                              'Logo':   team1['team']['logos']['large']['href'],
                              'Record': team1['team']['record']['summary'],
                              'Stats':  {}}
        boxscores['Team2'] = {'Name':   team2['team']['name'],
                              'Logo':   team2['team']['logos']['large']['href'],
                              'Record': team2['team']['record']['summary'],
                              'Stats':  {}}
                              
        boxscores['Team1']['Stats']['Players']     = []
        boxscores['Team2']['Stats']['Players']     = []
        boxscores['Team1']['Stats']['Scratches']   = []
        boxscores['Team2']['Stats']['Scratches']   = []
        boxscores['Team1']['Stats']['Goaltending'] = []
        boxscores['Team2']['Stats']['Goaltending'] = []
        boxscores['Team1']['Stats']['Powerplay']   = {}
        boxscores['Team2']['Stats']['Powerplay']   = {}
        
        powerplay     = ['PPG','PPO']
        team_change   = {'GA':'GV','TA':'TK','HITS':'HT'}
        player_ignore = ['P','PPG','PPA','SHG','SHA','GWG','GTG','PROD','%']
        player_change = {'FOW':'FW','FOL':'FL','TOI':'TOT'}
        
        #Now let's get team stats
        for stat in team1['team']['statistics'][0]['statCategories'][0]['stats']:
            if stat['abbreviation'] in powerplay:
                boxscores['Team1']['Stats']['Powerplay'][stat['abbreviation'].title()] = stat['displayValue']
            elif stat['abbreviation'] in team_change.keys():
                stat['abbreviation'] = team_change[stat['abbreviation']]
                boxscores['Team1']['Stats'][stat['abbreviation'].title()] = stat['displayValue']
            else:
                boxscores['Team1']['Stats'][stat['abbreviation'].title()] = stat['displayValue']
        
        for stat in team2['team']['statistics'][0]['statCategories'][0]['stats']:
            if stat['abbreviation'] in powerplay:
                boxscores['Team2']['Stats']['Powerplay'][stat['abbreviation'].title()] = stat['displayValue']
            elif stat['abbreviation'] in team_change.keys():
                stat['abbreviation'] = team_change[stat['abbreviation']]
                boxscores['Team2']['Stats'][stat['abbreviation'].title()] = stat['displayValue']
            else:
                boxscores['Team2']['Stats'][stat['abbreviation'].title()] = stat['displayValue']
        
        #Get date in format YYYY-MM-DD
        gdate             = game['date'][:10]        
        nhl_games_on_date = nhl_xhr_url % (gdate, gdate)
        t1name            = team1['team']['name']
        t2name            = team2['team']['name']
        nhl_resp          = requests.get(nhl_games_on_date)
        nhl_obj           = json.loads(nhl_resp.text)['dates'][0]
        
        nhl_game_url      = ''
        for g in nhl_obj['games']:
            test1 = g['teams']['away']['team']['name']
            test2 = g['teams']['home']['team']['name']
            if (t1name in test1 and t2name in test2) or (t1name in test2 and t2name in test1):
                nhl_game_url = 'https://statsapi.web.nhl.com%s' % g['link']
                break
        #if nhl_game_url is empty then we need to try checking yesterday's date.
        if nhl_game_url == '':
            #YYYY-MM-DD
            split_date        = gdate.split('-')
            date              = datetime.datetime(int(split_date[0]), int(split_date[1]), int(split_date[2]))
            date             -= datetime.timedelta(days=1)
            sdate             = date.strftime('%Y-%m-%d')
            
            nhl_games_on_date = nhl_xhr_url % (sdate, sdate)
            nhl_resp          = requests.get(nhl_games_on_date)
            nhl_obj           = json.loads(nhl_resp.text)['dates'][0]
            
            for g in nhl_obj['games']:
                test1 = g['teams']['away']['team']['name']
                test2 = g['teams']['home']['team']['name']
                if (t1name in test1 and t2name in test2) or (t1name in test2 and t2name in test1):
                    nhl_game_url = 'https://statsapi.web.nhl.com%s' % g['link']
                    break
                    
        nhl_site_resp  = requests.get(nhl_game_url)
        nhl_site_stats = json.loads(nhl_site_resp.text)
        
        #Now let's get team scratches
        t              = nhl_site_stats['liveData']['boxscore']['teams'][team1location]
        team_scratches = t['scratches']
        for scratch in team_scratches:
            fullid           = 'ID%s' % scratch
            scratched_player = t['players'][fullid]['person']['fullName']
            player_position  = t['players'][fullid]['position']['abbreviation']
            boxscores['Team1']['Stats']['Scratches'].append(scratched_player)
            
        t              = nhl_site_stats['liveData']['boxscore']['teams'][team2location]
        team_scratches = t['scratches']
        for scratch in team_scratches:
            fullid           = 'ID%s' % scratch
            scratched_player = t['players'][fullid]['person']['fullName']
            player_position  = t['players'][fullid]['position']['abbreviation']
            boxscores['Team2']['Stats']['Scratches'].append(scratched_player)
        
        #Now let's get player stats
        for player in players1:
            p_obj             = {}
            p_obj['Name']     = player['shortName']
            p_obj['Position'] = player['positions'][0]['abbreviation']
            for stat in player['statistics'][0]['statCategories'][0]['stats']:
                if stat['abbreviation'] in player_ignore:
                    continue
                elif stat['abbreviation'] in player_change.keys():
                    stat['abbreviation'] = player_change[stat['abbreviation']]
                p_obj[stat['abbreviation'].title()] = stat['displayValue']
            
            last_name = p_obj['Name'][3:].lower()
            
            if p_obj['Position'] == 'G':
                boxscores['Team1']['Stats']['Goaltending'].append(p_obj)
            else:
                team_players = nhl_site_stats['liveData']['boxscore']['teams'][team1location]['players']
                for nhl_player in team_players:
                    np = team_players[nhl_player]
                    print np['person']['fullName']
                    print last_name
                    if np['person']['fullName'].lower().endswith(last_name):
                        p_obj['Ev'] = np['stats']['skaterStats']['evenTimeOnIce']
                        p_obj['Pp'] = np['stats']['skaterStats']['powerPlayTimeOnIce']
                        p_obj['Sh'] = np['stats']['skaterStats']['shortHandedTimeOnIce']
                        p_obj['Tk'] = np['stats']['skaterStats']['takeaways']
                        if np['stats']['skaterStats'].get('faceOffPct'):
                            p_obj['%'] = np['stats']['skaterStats']['faceOffPct']
                        else:
                            p_obj['%'] = '0'
                        break
                boxscores['Team1']['Stats']['Players'].append(p_obj)
            
        for player in players2:
            p_obj             = {}
            p_obj['Name']     = player['shortName']
            p_obj['Position'] = player['positions'][0]['abbreviation']
            for stat in player['statistics'][0]['statCategories'][0]['stats']:
                if stat['abbreviation'] in player_ignore:
                    continue
                elif stat['abbreviation'] in player_change.keys():
                    stat['abbreviation'] = player_change[stat['abbreviation']]
                p_obj[stat['abbreviation'].title()] = stat['displayValue']
            
            last_name = p_obj['Name'][3:].lower()
            
            if p_obj['Position'] == 'G':
                boxscores['Team2']['Stats']['Goaltending'].append(p_obj)
            else:
                team_players = nhl_site_stats['liveData']['boxscore']['teams'][team2location]['players']
                for nhl_player in team_players:
                    np = team_players[nhl_player]
                    if np['person']['fullName'].lower().endswith(last_name):
                        p_obj['Ev'] = np['stats']['skaterStats']['evenTimeOnIce']
                        p_obj['Pp'] = np['stats']['skaterStats']['powerPlayTimeOnIce']
                        p_obj['Sh'] = np['stats']['skaterStats']['shortHandedTimeOnIce']
                        p_obj['Tk'] = np['stats']['skaterStats']['takeaways']
                        if np['stats']['skaterStats'].get('faceOffPct'):
                            p_obj['%'] = np['stats']['skaterStats']['faceOffPct']
                        else:
                            p_obj['%'] = '0'
                        break
                boxscores['Team2']['Stats']['Players'].append(p_obj)
        return boxscores
    else:
        return {}