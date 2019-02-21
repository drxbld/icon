from urlparse import parse_qsl
from urllib import urlencode
from urllib import unquote
import xbmcplugin
import xbmcaddon
import requests
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
fanart = xbmc.translatePath(os.path.join(path, "resources/nba/background.jpg"))
_tempdata = xbmc.translatePath(os.path.join(path, "temp.json"))

nba_stats = 'http://sports.espn.go.com/nba/bottomline/scores'
xhr_url = 'http://cdn.espn.com/core/nba/boxscore?gameId=%s&xhr=1'
league_standings = 'http://cdn.espn.com/nba/standings/_/group/league&xhr=1'
conference_standings = 'http://cdn.espn.com/nba/standings/_/group/conference&xhr=1'

def get_url(**kwargs):
    kwargs = {k: unicode(v).encode('ascii', 'ignore') for k,v in kwargs.iteritems()}
    return '{0}?{1}'.format(_url, urlencode(kwargs))

#Starting endpoint
#Returns json-friendly list object [{},{},{}]
def get_games():
    resp = requests.get(nba_stats)
    #for testing
    #resp = requests.get('https://pastebin.com/raw/SVwe34YC')
    decoded_resp = unquote(resp.text)
    game_list = []
    game = 0
    for line in decoded_resp.split('&'):
        if line.startswith('nba_s_left'):
            #first datapoint of game
            if ' at ' in line:
                #game hasn't started yet
                teams = line.split('=')[1].split(' at ')
            else:
                teams = line.split('=')[1].split('   ')
                
            current_time = re.compile('\((.+?)\)').findall(teams[1])[0]
            teams[1] = teams[1].replace(' (%s)' % current_time, '')
            
            if current_time == '0:00 IN OT' or current_time == 'END OF 4TH':
                current_time = 'FINAL'
            
            if 'PM' not in current_time and 'AM' not in current_time:
                #game has already started or may have already ended
                team_one  = teams[0].rsplit(' ', 1)[0].replace('^','')
                team_two  = teams[1].rsplit(' ', 1)[0].replace('^','')
                score_one = teams[0].rsplit(' ', 1)[1]
                score_two = teams[1].rsplit(' ', 1)[1]
            else:
                #game hasn't started yet
                team_one  = teams[0]
                team_two  = teams[1]
                score_one = '0'
                score_two = '0'
            
            game_list.append({'Title':'%s vs %s' % (team_one, team_two),
                              'Name1':team_one,    'Name2':team_two,
                              'Score1':score_one,  'Score2':score_two,
                              'Time':current_time, 'PlayerHighlights':[]})
        if line.startswith('nba_s_right') and not 'count' in line:
            #Top Player Stats
            nba_s_right  = line.split('=')[1]
            player_name  = " ".join(nba_s_right.split(' ', 2)[:2])
            player_stats = " ".join(nba_s_right.split(' ', 2)[2:])
            game_list[game]['PlayerHighlights'].append({'PlayerName':player_name,
                                                        'PlayerStats':player_stats})
        if line.startswith('nba_s_url'):
            #last datapoint of game
            game_list[game]['FullStats'] = line.split('=', 1)[1]
            game += 1
    return game_list
    
def check_for_updates(teams):
    with open(_tempdata, "rb") as f:
        tempdata = json.load(f)
        
    types = [type 
             for type in ['nba_upcominggame','nba_startofgame','nba_leadchange','nba_periodchange','nba_endofgame'] 
             if eval(addon.getSetting(type).title()) is True]
    updated_games = get_games()
    games_to_keep = [updated_game 
                     for updated_game in updated_games 
                     if updated_game['Name1'] in str(teams) or updated_game['Name2'] in str(teams)]
    updates = []
    td = tempdata['nba']
    #Now look at game data to see if any notifications need to be presented
    for game in games_to_keep:
        gametitle = game['Title']
        if 'nba_upcominggame' in types and gametitle not in td.keys():
            #We haven't announced this upcoming game yet, so do so
            updates.append(game)
        elif 'nba_startofgame' in types and any(['PM' in td[gametitle]['Time'],
             'AM' in td[gametitle]['Time']]) and all(['PM' not in game['Time'
             ], 'AM' not in game['Time'], 'FINAL' not in game['Time']]):
            updates.append(game)
        elif 'nba_leadchange' in types and any([all([int(td[gametitle]['Score1']) > int(td[gametitle]['Score2']),
                                                int(game['Score1']) < int(game['Score2'])]),
                                                all([int(td[gametitle]['Score2']) > int(td[gametitle]['Score1']),
                                                int(game['Score2']) < int(game['Score1'])])]):
            updates.append(game)
        elif 'nba_periodchange' in types and any([all(['1ST' in td[gametitle]['Time'], '2ND' in game['Time']]),
                                                  all(['2ND' in td[gametitle]['Time'], '3RD' in game['Time']]),
                                                  all(['3RD' in td[gametitle]['Time'], '4TH' in game['Time']]),
                                                  all(['4TH' in td[gametitle]['Time'], 'OT' in game['Time']])]):
            updates.append(game)
        elif 'nba_endofgame' in types and any([all(['4TH' in td[gametitle]['Time'], 'FINAL' in game['Time']]),
                                               all(['OT' in td[gametitle]['Time'], 'FINAL' in game['Time']])]):
            updates.append(game)
        #Save/Overwrite tempdata as we go to save time
        tempdata['nba'][gametitle] = game
    with open(_tempdata, "wb") as f: 
        f.write(json.dumps(tempdata, indent=4, sort_keys=True))
    return updates

def display_mainmenu():
    list_item = xbmcgui.ListItem(label='Full-Game Replays')
    list_item.setArt({'fanart':fanart,'thumb':icon,'poster':icon})
    list_item.setInfo('video',{'plot':'Full-Game Replays section for all past games.\n\n[COLOR yellow]Note:[/COLOR] Pin Generation is required to use this section.','title':'Full-Game Replays'})
    replays = get_url(sport='nba', endpoint='replays')
    xbmcplugin.addDirectoryItem(_handle, replays, list_item, isFolder=True)
    
    list_item = xbmcgui.ListItem(label='Today\'s Games')
    list_item.setArt({'fanart':fanart,'thumb':icon,'poster':icon})
    list_item.setInfo('video',{'plot':'Games from previous night will be shown until noon the following day. After noon you will see games for today/the upcoming night','title':'Today\'s Games'})
    todaysgames = get_url(sport='nba', endpoint='today')
    xbmcplugin.addDirectoryItem(_handle, todaysgames, list_item, isFolder=True)
    
    list_item = xbmcgui.ListItem(label='League Standings')
    list_item.setArt({'fanart':fanart,'thumb':icon,'poster':icon})
    list_item.setInfo('video',{'plot':'League standings divided into Eastern & Western Conferences','title':'League Standings'})
    standings = get_url(sport='nba', endpoint='standings')
    xbmcplugin.addDirectoryItem(_handle, standings, list_item, isFolder=False)
    
    xbmcplugin.addSortMethod(_handle, xbmcplugin.SORT_METHOD_NONE)
    xbmcplugin.endOfDirectory(_handle)
    
    
def display_gameoptions(game_obj):
    game = ast.literal_eval(game_obj)
    list_item = xbmcgui.ListItem(label='Highlights')
    list_item.setArt({'fanart':fanart,'thumb':icon,'poster':icon})
    list_item.setInfo('video',{'plot':'[COLOR green]HD[/COLOR] Highlight clips of the game','title':'Game Highlights'})
    hItem = get_url(sport='nba', highlights=game['FullStats'].replace('boxscore','video'), game_obj=game)
    xbmcplugin.addDirectoryItem(_handle, hItem, list_item, isFolder=True)
    
    list_item = xbmcgui.ListItem(label='Boxscores')
    list_item.setArt({'fanart':fanart,'thumb':icon,'poster':icon})
    list_item.setInfo('video',{'plot':'In-depth boxscore data for both teams','title':'Boxscores'})
    bItem = get_url(sport='nba', boxscores=game['FullStats'], game_obj=game)
    xbmcplugin.addDirectoryItem(_handle, bItem, list_item, isFolder=False)
    
    list_item = xbmcgui.ListItem(label='Play-by-Play')
    list_item.setArt({'fanart':fanart,'thumb':icon,'poster':icon})
    list_item.setInfo('video',{'plot':'Entire play-by-play for the game','title':'Play-by-Play'})
    playbyplay = get_url(sport='nba', playbyplay=game['FullStats'].replace('boxscore','playbyplay'), game_obj=game)
    xbmcplugin.addDirectoryItem(_handle, playbyplay, list_item, isFolder=False)
    
    list_item = xbmcgui.ListItem(label='Team Stats')
    list_item.setArt({'fanart':fanart,'thumb':icon,'poster':icon})
    list_item.setInfo('video',{'plot':'Team Stats side-by-side for comparison','title':'Team Stats'})
    teamstats = get_url(sport='nba', teamstats=game['FullStats'].replace('boxscore','matchup'), game_obj=game)
    xbmcplugin.addDirectoryItem(_handle, teamstats, list_item, isFolder=False)
    
    xbmcplugin.addSortMethod(_handle, xbmcplugin.SORT_METHOD_NONE)
    xbmcplugin.endOfDirectory(_handle)

#Input:  json-friendly list object [{},{},{}]
#Output: games directory
def display_games(games):
    if len(games) > 0:
        for game in games:
            title = '%s (%s)' % (game['Title'], game['Time'])
            details = '%s\n%s\n\n[B]Highlights:[/B]\n' % (game['Title'], game['Time'])
            
            details += '\n'.join(['%s %s' % (highlight['PlayerName'], highlight['PlayerStats']) for highlight in game['PlayerHighlights']])
            
            list_item = xbmcgui.ListItem(label=title)
            list_item.setArt({'fanart':fanart,'thumb':icon,'poster':icon})
            list_item.setInfo('video',{'plot':details,'title':title})
            """
            boxscores  = get_url(sport='nba', boxscores=game['FullStats'], game_obj=game)
            playbyplay = get_url(sport='nba', playbyplay=game['FullStats'].replace('boxscore','playbyplay'), game_obj=game)
            teamstats  = get_url(sport='nba', teamstats=game['FullStats'].replace('boxscore','matchup'), game_obj=game)
            commands   = []
            commands.append(( 'Box Scores',   'XBMC.RunPlugin(%s)' % boxscores, ))
            commands.append(( 'Play-By-Play', 'XBMC.RunPlugin(%s)' % playbyplay, ))
            commands.append(( 'Team Stats',   'XBMC.RunPlugin(%s)' % teamstats, ))
            list_item.addContextMenuItems( commands )                          
            
            highlights = get_url(sport='nba', highlights=game['FullStats'].replace('boxscore','video'), game_obj=game)
            """
            innermenu = get_url(sport='nba', endpoint='details', game_obj=game)
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
        gameId          = game_link.split('=')[1]
        data            = requests.get(xhr_url % gameId)
        j_obj           = json.loads(data.text)
        videos          = j_obj['gamepackageJSON']['videos']
        highlights_list = []
        for video in videos:
            image       = video['thumbnail']
            title       = video['headline']
            description = video['description']
            clip        = video['links']['source']['mezzanine']['href']
            highlights_list.append({'Image': image,
                                    'Title': title,
                                    'Description': description,
                                    'Clip': clip})
        return highlights_list
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
        url = get_url(sport='nba', play_me=highlight['Clip'])
        xbmcplugin.addDirectoryItem(_handle, url, list_item, False)
    xbmcplugin.addSortMethod(_handle, xbmcplugin.SORT_METHOD_NONE)
    xbmcplugin.endOfDirectory(_handle)
    
def get_standings():
    data    = requests.get(conference_standings, headers={'Cache-Control':'no-cache'})
    j_obj   = json.loads(data.text)
    c       = j_obj['content']['config']['categories']
    headers = [cat['abbreviation'] for cat in c]
    conf1   = j_obj['content']['standings']['groups'][0]
    conf2   = j_obj['content']['standings']['groups'][1]
    name1   = conf1['name']
    name2   = conf2['name']
    standings = {'Headers':headers, 'League Name':j_obj['content']['standings']['name'],
                 name1:[], name2:[]}
    for entry in conf1['standings']['entries']:
        tmp_team = {'Name':entry['team']['displayName']}
        [(tmp_team.update({s['abbreviation']: '[COLOR red]%s[/COLOR]'
         % s['displayValue']}) if s['displayValue'].startswith('-'
         ) else (tmp_team.update({s['abbreviation'
         ]: '[COLOR green]%s[/COLOR]' % s['displayValue'
         ]}) if s['displayValue'].startswith('+'
         ) else (tmp_team.update({s['abbreviation']: s['displayValue'
         ]}) if len(s['abbreviation'])
         > 0 else tmp_team.update({s['shortDisplayName']: s['displayValue'
         ]})))) for s in entry['stats']]
        standings[name1].append(tmp_team)
    for entry in conf2['standings']['entries']:
        tmp_team = {'Name':entry['team']['displayName']}
        [(tmp_team.update({s['abbreviation']: '[COLOR red]%s[/COLOR]'
         % s['displayValue']}) if s['displayValue'].startswith('-'
         ) else (tmp_team.update({s['abbreviation'
         ]: '[COLOR green]%s[/COLOR]' % s['displayValue'
         ]}) if s['displayValue'].startswith('+'
         ) else (tmp_team.update({s['abbreviation']: s['displayValue'
         ]}) if len(s['abbreviation'])
         > 0 else tmp_team.update({s['shortDisplayName']: s['displayValue'
         ]})))) for s in entry['stats']]
        standings[name2].append(tmp_team)
    return standings
    
    
    
#Input:  url with gameId
#Output: json-friendly list object [{},{},{}] 
#        of playbyplay for specific game
def get_playbyplay(game_link):
    #if not 'preview' in game_link:
    if 'playbyplay' in game_link:
        gameId     = game_link.split('=')[1]
        data       = requests.get(xhr_url % gameId)
        j_obj      = json.loads(data.text)
        teams      = j_obj['gamepackageJSON']['boxscore']['teams']
        teamlogo   = {teams[0]['team']['id']: teams[0]['team']['logo'],
                      teams[1]['team']['id']: teams[1]['team']['logo']}
        playbyplay = []
        for play in j_obj['gamepackageJSON']['plays']:
            if play.get('team'):
                team = teamlogo[play['team']['id']]
            else:
                team = ''
            if play['scoringPlay']:
                playbyplay.append({'Time': '[B]%s[/B]' % play['clock']['displayValue'], 
                                   'Team': team,
                                   'Play': '[B]%s[/B]' % play['text'],
                                   'Score':'[B]%s - %s[/B]' % (play['awayScore'], play['homeScore'])})
            else:
                playbyplay.append({'Time': play['clock']['displayValue'], 
                                   'Team': team,
                                   'Play': play['text'],
                                   'Score':'%s - %s' % (play['awayScore'], play['homeScore'])})
        return playbyplay
    else:
        return []
        
#Input:  url with gameId
#Output: json-friendly object {}
#        of quarterly scores for specific game
def get_scoreboard(game_link):
    if not 'preview' in game_link:
        gameId     = game_link.split('=')[1]
        data       = requests.get(xhr_url % gameId)
        j_obj      = json.loads(data.text)
        scoreboard = {}
        game_time  = j_obj['gamepackageJSON']['header']['competitions'][0]['status']['type']['description']
        team1      = j_obj['gamepackageJSON']['header']['competitions'][0]['competitors'][1]
        team2      = j_obj['gamepackageJSON']['header']['competitions'][0]['competitors'][0]
        
        team1name  = team1['team']['abbreviation']
        total1     = team1['score']
        scores1    = []
        team2name  = team2['team']['abbreviation']
        total2     = team2['score']
        scores2    = []
        
        for p in range(0, 4):
            try:
                scores1.append(team1['linescores'][p]['displayValue'])
                scores2.append(team2['linescores'][p]['displayValue'])
            except IndexError:
                scores1.append('')
                scores2.append('')

        scoreboard['Team1'] = {'Name'  : team1name,
                               'Score1': scores1[0],
                               'Score2': scores1[1],
                               'Score3': scores1[2],
                               'Score4': scores1[3],
                               'Total' : total1}
        scoreboard['Team2'] = {'Name'  : team2name,
                               'Score1': scores2[0],
                               'Score2': scores2[1],
                               'Score3': scores2[2],
                               'Score4': scores2[3],
                               'Total' : total2}
        scoreboard['Time'] = game_time
        
        return scoreboard
    else:
        return {}

def get_teamstats(game_link):
    if not 'preview' in game_link:
        data            = requests.get(game_link+'&xhr=1')
        j_obj           = json.loads(data.text)
        gamepackage     = j_obj['__gamepackage__']
        teamstats       = {}
        
        team1record = '%s, %s Away' % (gamepackage['awayTeam']['record'][0]['displayValue'],
                                       gamepackage['awayTeam']['record'][1]['displayValue'])
        team2record = '%s, %s Home' % (gamepackage['homeTeam']['record'][0]['displayValue'],
                                       gamepackage['homeTeam']['record'][1]['displayValue'])
        teamstats['Team1'] = {'Name':   gamepackage['awayTeam']['team']['name'],
                              'Logo':   gamepackage['awayTeam']['team']['logos'][0]['href'],
                              'Record': team1record,
                              'Stats':  {}}
        teamstats['Team2'] = {'Name':   gamepackage['homeTeam']['team']['name'],
                              'Logo':   gamepackage['homeTeam']['team']['logos'][0]['href'],
                              'Record': team2record,
                              'Stats':  {}}
        
        j_boxscore = j_obj['gamepackageJSON']['boxscore']
        team1 = j_boxscore['teams'][0]
        team2 = j_boxscore['teams'][1]
        teamstatslist = ['FG Made-Attempted','Field Goal %','3PT Made-Attempted','Three Point %','FT Made-Attempted',
                         'Free Throw %','Total Rebounds','Offensive Rebounds','Defensive Rebounds','Assists','Steals',
                         'Blocks','Total Turnovers','Points Off Turnovers','Fast Break Points','Points in Paint',
                         'Personal Fouls','Technical Fouls','Flagrant Fouls']
        for stat in team1['statistics']:
            if stat['label'] in teamstatslist:
                if stat['label'].endswith('%'):
                    teamstats['Team1']['Stats'][stat['label']] = '{}%'.format(stat['displayValue'])
                else:
                    teamstats['Team1']['Stats'][stat['label']] = stat['displayValue']
        for stat in team2['statistics']:
            if stat['label'] in teamstatslist:
                if stat['label'].endswith('%'):
                    teamstats['Team2']['Stats'][stat['label']] = '{}%'.format(stat['displayValue'])
                else:
                    teamstats['Team2']['Stats'][stat['label']] = stat['displayValue']
        
        return teamstats
    else:
        return {}
        
#Input:  url with gameId
#Output: json-friendly object {}
#        of box scores for specific game
def get_boxscores(game_link):
    if not 'preview' in game_link:
        gameId          = game_link.split('=')[1]
        data            = requests.get(xhr_url % gameId)
        j_obj           = json.loads(data.text)
        gamepackage     = j_obj['__gamepackage__']
        boxscores       = {}
        
        team1record = '%s, %s Away' % (gamepackage['awayTeam']['record'][0]['displayValue'],
                                       gamepackage['awayTeam']['record'][1]['displayValue'])
        team2record = '%s, %s Home' % (gamepackage['homeTeam']['record'][0]['displayValue'],
                                       gamepackage['homeTeam']['record'][1]['displayValue'])
        boxscores['Team1'] = {'Name':   gamepackage['awayTeam']['team']['name'],
                              'Logo':   gamepackage['awayTeam']['team']['logos'][0]['href'],
                              'Record': team1record,
                              'Stats':  {}}
        boxscores['Team2'] = {'Name':   gamepackage['homeTeam']['team']['name'],
                              'Logo':   gamepackage['homeTeam']['team']['logos'][0]['href'],
                              'Record': team2record,
                              'Stats':  {}}
        
        j_boxscore = j_obj['gamepackageJSON']['boxscore']
        team1 = j_boxscore['teams'][0]
        team2 = j_boxscore['teams'][1]
        teamstats = ['Fg','Fgp','3Pt','3Ptp','Ft','Ftp','Reb','Oreb','Dreb','Ast','Stl','Blk','To']
        for s, stat in enumerate(teamstats):
            if stat.endswith('p'):
                boxscores['Team1']['Stats'][stat] = '{}%'.format(team1['statistics'][s]['displayValue'])
                boxscores['Team2']['Stats'][stat] = '{}%'.format(team2['statistics'][s]['displayValue'])
            else:
                boxscores['Team1']['Stats'][stat] = team1['statistics'][s]['displayValue']
                boxscores['Team2']['Stats'][stat] = team2['statistics'][s]['displayValue']
        #Skipping all other team stats as we have nowhere to put them
        #Plus they aren't directly displayed on the webpage anyway
        boxscores['Team1']['Stats']['Pf'] = team1['statistics'][21]['displayValue']
        boxscores['Team2']['Stats']['Pf'] = team2['statistics'][21]['displayValue']
        
        #Now for the player stats
        boxscores['Team1']['Stats']['Players'] = []
        boxscores['Team2']['Stats']['Players'] = []
        players1 = j_boxscore['players'][0]['statistics'][0]['athletes']
        players2 = j_boxscore['players'][1]['statistics'][0]['athletes']
        
        statlbls = j_boxscore['players'][0]['statistics'][0]['labels']
        for player in players1:
            player_dict = {}
            player_dict['Name']          = player['athlete']['shortName']
            player_dict['Position']      = player['athlete']['position']['abbreviation']
            if player['didNotPlay']:
                player_dict['Dnp']       = 'DNP: %s' % player['reason']
            else:
                for l, lbl in enumerate(statlbls):
                    if lbl == '+/-':
                        lbl = 'plusminus'
                    player_dict[lbl.title()] = player['stats'][l]
            boxscores['Team1']['Stats']['Players'].append(player_dict)
            
        for player in players2:
            player_dict = {}
            player_dict['Name']          = player['athlete']['shortName']
            player_dict['Position']      = player['athlete']['position']['abbreviation']
            if player['didNotPlay']:
                player_dict['Dnp']       = 'DNP: %s' % player['reason']
            else:
                for l, lbl in enumerate(statlbls):
                    if lbl == '+/-':
                        lbl = 'plusminus'
                    player_dict[lbl.title()] = player['stats'][l]
            boxscores['Team2']['Stats']['Players'].append(player_dict)
        
        return boxscores
    else:
        return {}