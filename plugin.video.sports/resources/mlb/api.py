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
fanart = xbmc.translatePath(os.path.join(path, "resources/mlb/background.jpg"))
_tempdata = xbmc.translatePath(os.path.join(path, "temp.json"))

mlb_stats = 'http://sports.espn.go.com/mlb/bottomline/scores'
xhr_url = 'http://cdn.espn.com/core/mlb/boxscore?gameId=%s&xhr=1'
division_standings = 'http://cdn.espn.com/mlb/standings/_/group/league&xhr=1'
base_legend = ['%A2','%A3','%A5','%A7','%AC','%AB','%B1','%BB']

def get_url(**kwargs):
    kwargs = {k: unicode(v).encode('ascii', 'ignore') for k,v in kwargs.iteritems()}
    return '{0}?{1}'.format(_url, urlencode(kwargs))

#Starting endpoint
#Returns json-friendly list object [{},{},{}]
def get_games():
    resp = requests.get(mlb_stats, headers={'Cache-Control':'no-cache'}).text
    #for testing
    #resp = requests.get('https://pastebin.com/raw/jy33VQdx').text
    """
    %A2     - bases empty
    %A3     - man on first
    %A5     - man on second
    %A7     - man on third
    %AC     - man on first & second
    %AB     - man on first & third
    %B1     - man on second & third (Possibly mixed up with %BB)
    %BB     - bases loaded (Possibly mixed up with %B1)
    """
    for base in base_legend:
        resp = resp.replace(base, '')
    decoded_resp = unquote(resp)
    game_list = []
    game = 0
    for line in decoded_resp.split('&'):
        if line.startswith('mlb_s_left'):
            #first datapoint of game
            if ' at ' in line:
                #game hasn't started yet
                teams = line.split('=')[1].split(' at ')
            else:
                teams = line.split('=')[1].split('   ')
                
            try:
                current_time = re.compile('\((.+?)\)').findall(teams[1])[0]
            except:
                current_time = 'SUSPENDED'
            teams[1] = teams[1].replace(' (%s)' % current_time, '').replace('()','')
            
            if 'PM' not in current_time and 'AM' not in current_time:
                team_one  = teams[0].rsplit(' ', 1)[0].replace('^','')
                team_two  = teams[1].rsplit(' ', 1)[0].replace('^','')
                if not current_time == 'POSTPONED':
                    score_one = teams[0].rsplit(' ', 1)[1]
                    score_two = teams[1].rsplit(' ', 1)[1]
                else:
                    score_one = '0'
                    score_two = '0'
            else:
                team_one  = teams[0]
                team_two  = teams[1]
                score_one = '0'
                score_two = '0'
            
            game_list.append({'Title':'%s vs %s' % (team_one, team_two),
                              'Name1':team_one,    'Name2':team_two,
                              'Score1':score_one,  'Score2':score_two,
                              'Time':current_time, 'PlayerHighlights':[]})
        if line.startswith('mlb_s_right') and not 'count' in line:
            #Top Player Stats
            #w: phelps l: parker s: someone
            players = line.split('=')[1]
            if 'W:' in players:
                players = players.replace(' W: ',',W:')
                players = players.replace(' L: ',',L:')
                players = players.replace(' S: ',',S:')
                for player in players.split(','):
                    p_stat = player.split(':')
                    player_name  = p_stat[1].strip().rstrip()
                    player_stats = p_stat[0]
                    game_list[game]['PlayerHighlights'].append({'PlayerName': player_name,
                                                                'PlayerStats':player_stats})
            else:
                game_list[game]['PlayerHighlights'].append({'PlayerName': players,
                                                            'PlayerStats':''})
        if line.startswith('mlb_s_url'):
            #last datapoint of game
            game_list[game]['FullStats'] = line.split('=', 1)[1]
            game += 1
    return game_list

def check_for_updates(teams):
    with open(_tempdata, "rb") as f:
        tempdata = json.load(f)
        
    types = [type 
             for type in ['mlb_upcominggame','mlb_startofgame','mlb_scorechange','mlb_inningchange','mlb_endofgame'] 
             if eval(addon.getSetting(type).title()) is True]
    updated_games = get_games()
    games_to_keep = [updated_game for updated_game in updated_games
                     if updated_game['Name1'].replace('New York ', 'NY ')
                     in str(teams).replace('New York ', 'NY ')
                     or updated_game['Name2'].replace('New York ', 'NY ')
                     in str(teams).replace('New York ', 'NY ')]
    updates = []
    td = tempdata['mlb']
    #Now look at game data to see if any notifications need to be presented
    for game in games_to_keep:
        gametitle = game['Title']
        if 'mlb_upcominggame' in types and gametitle not in td.keys():
            #We haven't announced this upcoming game yet, so do so
            updates.append(game)
        elif 'mlb_startofgame' in types and any(['PM' in td[gametitle]['Time'],
             'AM' in td[gametitle]['Time']]) and all(['PM' not in game['Time'
             ], 'AM' not in game['Time'], 'FINAL' not in game['Time']]):
            updates.append(game)
        elif 'mlb_scorechange' in types and any([int(game['Score1']) > int(td[gametitle]['Score1']),
                                                 int(game['Score2']) > int(td[gametitle]['Score2'])]):
            updates.append(game)
        elif 'mlb_inningchange' in types and any([all(['BOTTOM' in td[gametitle]['Time'], 'TOP' in game['Time']]),
                                                  all(['SUSPENDED' in game['Time'], 'SUSPENDED' not in td[gametitle]['Time']]),
                                                  all(['POSTPONED' in game['Time'], 'POSTPONED' not in td[gametitle]['Time']])]):
            updates.append(game)
        elif 'mlb_endofgame' in types and all(['FINAL' not in td[gametitle]['Time'], 'FINAL' in game['Time']]):
            updates.append(game)
        #Save/Overwrite tempdata as we go to save time
        tempdata['mlb'][gametitle] = game
    with open(_tempdata, "wb") as f: 
        f.write(json.dumps(tempdata, indent=4, sort_keys=True))
    return updates
    
def display_mainmenu():
    list_item = xbmcgui.ListItem(label='Full-Game Replays')
    list_item.setArt({'fanart':fanart,'thumb':icon,'poster':icon})
    list_item.setInfo('video',{'plot':'Full-Game Replays section for all past games.\n\n[COLOR yellow]Note:[/COLOR] Pin Generation is required to use this section.','title':'Full-Game Replays'})
    replays = get_url(sport='mlb', endpoint='replays')
    xbmcplugin.addDirectoryItem(_handle, replays, list_item, isFolder=True)
    
    list_item = xbmcgui.ListItem(label='Today\'s Games')
    list_item.setArt({'fanart':fanart,'thumb':icon,'poster':icon})
    list_item.setInfo('video',{'plot':'Games from previous night will be shown until noon the following day. After noon you will see games for today/the upcoming night','title':'Today\'s Games'})
    todaysgames = get_url(sport='mlb', endpoint='today')
    xbmcplugin.addDirectoryItem(_handle, todaysgames, list_item, isFolder=True)
    
    list_item = xbmcgui.ListItem(label='League Standings')
    list_item.setArt({'fanart':fanart,'thumb':icon,'poster':icon})
    list_item.setInfo('video',{'plot':'League standings divided into American & National Leagues','title':'League Standings'})
    standings = get_url(sport='mlb', endpoint='standings')
    xbmcplugin.addDirectoryItem(_handle, standings, list_item, isFolder=False)
    
    xbmcplugin.addSortMethod(_handle, xbmcplugin.SORT_METHOD_NONE)
    xbmcplugin.endOfDirectory(_handle)
       
def display_gameoptions(game_obj):
    game = ast.literal_eval(game_obj)
    list_item = xbmcgui.ListItem(label='Highlights')
    list_item.setArt({'fanart':fanart,'thumb':icon,'poster':icon})
    list_item.setInfo('video',{'plot':'[COLOR green]HD[/COLOR] Highlight clips of the game','title':'Game Highlights'})
    hItem = get_url(sport='mlb', highlights=game['FullStats'].replace('boxscore','video'), game_obj=game)
    xbmcplugin.addDirectoryItem(_handle, hItem, list_item, isFolder=True)
    
    list_item = xbmcgui.ListItem(label='Boxscores')
    list_item.setArt({'fanart':fanart,'thumb':icon,'poster':icon})
    list_item.setInfo('video',{'plot':'In-depth boxscore data for both teams','title':'Boxscores'})
    bItem = get_url(sport='mlb', boxscores=game['FullStats'], game_obj=game)
    xbmcplugin.addDirectoryItem(_handle, bItem, list_item, isFolder=False)
    
    list_item = xbmcgui.ListItem(label='Play-by-Play')
    list_item.setArt({'fanart':fanart,'thumb':icon,'poster':icon})
    list_item.setInfo('video',{'plot':'Entire play-by-play for the game','title':'Play-by-Play'})
    playbyplay = get_url(sport='mlb', playbyplay=game['FullStats'].replace('boxscore','playbyplay'), game_obj=game)
    xbmcplugin.addDirectoryItem(_handle, playbyplay, list_item, isFolder=False)
    
    xbmcplugin.addSortMethod(_handle, xbmcplugin.SORT_METHOD_NONE)
    xbmcplugin.endOfDirectory(_handle)
    
#Input:  json-friendly list object [{},{},{}]
#Output: games directory
def display_games(games):
    if len(games) > 0:
        for game in games:
            title = '%s (%s)' % (game['Title'], game['Time'])
            details = '%s\n%s\n%s - %s\n\n[B]Highlights:[/B]\n' % (game['Title'], game['Time'], game['Score1'], game['Score2'])
            
            list_item = xbmcgui.ListItem(label=title)
            list_item.setArt({'fanart':fanart,'thumb':icon,'poster':icon})
                
            details += '\n'.join(['%s %s' % (highlight['PlayerName'], highlight['PlayerStats']) for highlight in game['PlayerHighlights']])
            list_item.setInfo('video',{'plot':details,'title':title})
            """
            boxscores = get_url(sport='mlb', boxscores=game['FullStats'], game_obj=game)
            playbyplay = get_url(sport='mlb', playbyplay=game['FullStats'].replace('boxscore','playbyplay'), game_obj=game)
            list_item.addContextMenuItems([('Box Scores',   'XBMC.RunPlugin(%s)' % boxscores),
                                           ('Play-By-Play', 'XBMC.RunPlugin(%s)' % playbyplay)])
                                           
            url = get_url(sport='mlb', highlights=game['FullStats'].replace('boxscore','video'), game_obj=game)
            """
            innermenu = get_url(sport='mlb', endpoint='details', game_obj=game)
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
        data            = requests.get(game_link + '&xhr=1')
        j_obj           = json.loads(data.text)
        videos          = j_obj['gamepackageJSON'].get('videos',{})
        videos2         = j_obj['gamepackageJSON'].get('article',{}).get('video',{})
        if len(videos) > 0 or len(videos2) > 0:
            highlights_list = []
            for video in videos:
                image       = video['thumbnail']
                title       = video['headline']
                description = video['description']
                clip        = video['links']['source']['mezzanine']['href']
                highlights_list.append({'Image':       image,
                                        'Title':       title,
                                        'Description': description,
                                        'Clip':        clip})
            for video in videos2:
                image       = video['thumbnail']
                title       = video['title']
                description = video['description']
                clip        = video['links']['source']['mezzanine']['href']
                highlights_list.append({'Image':       image,
                                        'Title':       title,
                                        'Description': description,
                                        'Clip':        clip})
            
            #Attempt to remove duplicates
            return [dict(t) for t in set([tuple(d.items()) for d in highlights_list])]
        else:
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
        url = get_url(sport='mlb', play_me=highlight['Clip'])
        xbmcplugin.addDirectoryItem(_handle, url, list_item, False)
    xbmcplugin.addSortMethod(_handle, xbmcplugin.SORT_METHOD_NONE)
    xbmcplugin.endOfDirectory(_handle)

def get_standings():
    data    = requests.get(division_standings, headers={'Cache-Control':'no-cache'})
    j_obj   = json.loads(data.text)
    c       = j_obj['content']['config']['categories']
    headers = [cat['abbreviation'] for cat in c]
    league1 = j_obj['content']['standings']['groups'][0]
    league2 = j_obj['content']['standings']['groups'][1]
    name1   = league1['name']
    name2   = league2['name']
    standings = {'Headers':headers, 'League Name':j_obj['content']['standings']['name'],
                 name1:[], name2:[]}
    for entry in league1['standings']['entries']:
        tmp_team = {'Name':entry['team']['displayName']}
        [(tmp_team.update({s['abbreviation']: '[COLOR red]%s[/COLOR]'
         % s['displayValue']}) if s['displayValue'].startswith('-'
         ) else (tmp_team.update({s['abbreviation'
         ]: '[COLOR green]%s[/COLOR]' % s['displayValue'
         ]}) if s['displayValue'].startswith('+'
         ) else (tmp_team.update({s['abbreviation']: s['displayValue'
         ]}) if not s['abbreviation']
         in ['ROAD','LAST TEN'] else tmp_team.update({s['shortDisplayName']: s['displayValue'
         ]})))) for s in entry['stats']]
        if tmp_team['STRK'].startswith('W'):
            tmp_team['STRK'] = '[COLOR green]%s[/COLOR]' % tmp_team['STRK']
        else:
            tmp_team['STRK'] = '[COLOR red]%s[/COLOR]' % tmp_team['STRK']
        standings[name1].append(tmp_team)
    for entry in league2['standings']['entries']:
        tmp_team = {'Name':entry['team']['displayName']}
        [(tmp_team.update({s['abbreviation']: '[COLOR red]%s[/COLOR]'
         % s['displayValue']}) if s['displayValue'].startswith('-'
         ) else (tmp_team.update({s['abbreviation'
         ]: '[COLOR green]%s[/COLOR]' % s['displayValue'
         ]}) if s['displayValue'].startswith('+'
         ) else (tmp_team.update({s['abbreviation']: s['displayValue'
         ]}) if not s['abbreviation']
         in ['ROAD','LAST TEN'] else tmp_team.update({s['shortDisplayName']: s['displayValue'
         ]})))) for s in entry['stats']]
        if tmp_team['STRK'].startswith('W'):
            tmp_team['STRK'] = '[COLOR green]%s[/COLOR]' % tmp_team['STRK']
        else:
            tmp_team['STRK'] = '[COLOR red]%s[/COLOR]' % tmp_team['STRK']
        standings[name2].append(tmp_team)
    return standings
    
#Input:  url with gameId
#Output: json-friendly list object [{},{},{}] 
#        of playbyplay for specific game
def get_playbyplay(game_link):
    if 'playbyplay' in game_link:
        data       = requests.get(game_link + '&xhr=1')
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
                
            try:
                p = play['text']
                if p.startswith('Pitch '):
                    p += ' (%s - %s)' % (str(play['resultCount']['balls']), str(play['resultCount']['strikes']))
                elif play['type']['text'] == 'End Inning' and play['period']['number'] > 8 and p.startswith('Middle'):
                    p = 'Final Score - End of Game'
            except:
                if play['type']['text'] == 'end batter/pitcher':
                    continue
                p = play['type']['text']
            if play['scoringPlay']:
                playbyplay.append({'Inning': '[B]%s%s[/B]' % (play['period']['type'], str(play['period']['number'])), 
                                   'Team': team,
                                   'Play': '[B]%s[/B]' % p,
                                   'Score':'[B]%s - %s[/B]' % (play['awayScore'], play['homeScore'])})
            else:
                playbyplay.append({'Inning': '%s%s' % (play['period']['type'], str(play['period']['number'])), 
                                   'Team': team,
                                   'Play': p,
                                   'Score':'%s - %s' % (play['awayScore'], play['homeScore'])})
        return playbyplay
    else:
        return []
        
#Input:  url with gameId
#Output: json-friendly object {}
#        of box scores for specific game
def get_boxscores(game_link):
    if 'boxscore' in game_link:
        gameId          = game_link.split('=')[1]
        data            = requests.get(xhr_url % gameId)
        j_obj           = json.loads(data.text)
        gamepackage     = j_obj['__gamepackage__']
        boxscores       = {}
        
        team1record = '%s, %s Road' % (gamepackage['awayTeam']['record'][0]['displayValue'],
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
        team1hitting        = team1['statistics'][0]
        team1hittingextras  = team1['details'][0]
        team1fielding       = team1['details'][2]
        team1pitching       = team1['statistics'][1]
        team1pitchingextras = team1['details'][1]
        team2hitting        = team2['statistics'][0]
        team2hittingextras  = team2['details'][0]
        team2fielding       = team2['details'][2]
        team2pitching       = team2['statistics'][1]
        team2pitchingextras = team2['details'][1]
        
        hitting = ['AB', 'R', 'H', 'RBI', 'BB', 'SO', 'BA', 'OBP', 'SLG', 'P']
        pitching = ['IP', 'H', 'R', 'ER',  'BB', 'K', 'HR',  'ERA']
        
        stats = {}
        for stat in team1hitting['stats']:
            abb = stat['abbreviation']
            if abb in hitting:
                if abb == 'SO':
                    stats['K']  = stat['displayValue']
                elif abb == 'P':
                    stats['AVG'] = stat['displayValue']
                else:
                    stats[abb]  = stat['displayValue']
        boxscores['Team1']['Stats']['Hitting'] = stats
        
        extras = {}
        for stat in team1hittingextras['stats']:
            if len(stat['displayName']) > 10:
                extras[stat['abbreviation']] = stat['displayValue']
            else:
                extras[stat['displayName']] = stat['displayValue']
        boxscores['Team1']['Stats']['Hitting']['Extras'] = extras
        
        stats = {}
        for stat in team1fielding['stats']:
            if len(stat['displayName']) > 10:
                stats[stat['abbreviation']] = stat['displayValue']
            else:
                stats[stat['displayName']] = stat['displayValue']
        boxscores['Team1']['Stats']['Fielding'] = stats
        
        stats = {}
        for stat in team1pitching['stats']:
            abb = stat['abbreviation']
            if abb in pitching:
                stats[abb]  = stat['displayValue']
        boxscores['Team1']['Stats']['Pitching'] = stats
        
        extras = {}
        for stat in team1pitchingextras['stats']:
            if stat.get('displayValue'):
                extras[stat['displayName']] = stat['displayValue']
        boxscores['Team1']['Stats']['Pitching']['Extras'] = extras
        
        stats = {}
        for stat in team2hitting['stats']:
            abb = stat['abbreviation']
            if abb in hitting:
                if abb == 'SO':
                    stats['K']  = stat['displayValue']
                elif abb == 'P':
                    stats['AVG'] = stat['displayValue']
                else:
                    stats[abb]  = stat['displayValue']
        boxscores['Team2']['Stats']['Hitting'] = stats
        
        extras = {}
        for stat in team2hittingextras['stats']:
            if len(stat['displayName']) > 10:
                extras[stat['abbreviation']] = stat['displayValue']
            else:
                extras[stat['displayName']] = stat['displayValue']
        boxscores['Team2']['Stats']['Hitting']['Extras'] = extras
        
        stats = {}
        for stat in team2fielding['stats']:
            if len(stat['displayName']) > 10:
                stats[stat['abbreviation']] = stat['displayValue']
            else:
                stats[stat['displayName']] = stat['displayValue']
        boxscores['Team2']['Stats']['Fielding'] = stats
        
        
        stats = {}
        for stat in team2pitching['stats']:
            abb = stat['abbreviation']
            if abb in pitching:
                stats[abb]  = stat['displayValue']
        boxscores['Team2']['Stats']['Pitching'] = stats
        
        extras = {}
        for stat in team2pitchingextras['stats']:
            if stat.get('displayValue'):
                extras[stat['displayName']] = stat['displayValue']
        boxscores['Team2']['Stats']['Pitching']['Extras'] = extras
        
        
        #Now for the player stats
        boxscores['Team1']['Stats']['Hitting']['Players']  = []
        boxscores['Team1']['Stats']['Pitching']['Players'] = []
        boxscores['Team2']['Stats']['Hitting']['Players']  = []
        boxscores['Team2']['Stats']['Pitching']['Players'] = []
        
        ignore_hitting    = ['H-AB',  '#P']
        ignore_pitching   = ['PC']#['PC-ST', 'PC']
        players1hitting   = j_boxscore['players'][0]['statistics'][0]
        players1pitching  = j_boxscore['players'][0]['statistics'][1]
        players2hitting   = j_boxscore['players'][1]['statistics'][0]
        players2pitching  = j_boxscore['players'][1]['statistics'][1]     
        
        hitting_lbs = players1hitting['labels']
        for player in players1hitting['athletes']:
            player_dict = {}
            player_dict['Name'] = player['athlete']['shortName']
            player_dict['Position'] = player['athlete']['position']['abbreviation']
            for s, stat in enumerate(hitting_lbs):
                if stat in ignore_hitting:
                    continue
                player_dict[stat] = player['stats'][s]
            boxscores['Team1']['Stats']['Hitting']['Players'].append(player_dict)
            
        pitching_lbs = players1pitching['labels']
        for player in players1pitching['athletes']:
            player_dict = {}
            player_dict['Name'] = player['athlete']['shortName']
            player_dict['Position'] = player['athlete']['position']['abbreviation']
            for s, stat in enumerate(pitching_lbs):
                if stat in ignore_pitching:
                    continue
                player_dict[stat] = player['stats'][s]
            boxscores['Team1']['Stats']['Pitching']['Players'].append(player_dict)
            
        hitting_lbs = players2hitting['labels']
        for player in players2hitting['athletes']:
            player_dict = {}
            player_dict['Name'] = player['athlete']['shortName']
            player_dict['Position'] = player['athlete']['position']['abbreviation']
            for s, stat in enumerate(hitting_lbs):
                if stat in ignore_hitting:
                    continue
                player_dict[stat] = player['stats'][s]
            boxscores['Team2']['Stats']['Hitting']['Players'].append(player_dict)
            
        pitching_lbs = players2pitching['labels']
        for player in players2pitching['athletes']:
            player_dict = {}
            player_dict['Name'] = player['athlete']['shortName']
            player_dict['Position'] = player['athlete']['position']['abbreviation']
            for s, stat in enumerate(pitching_lbs):
                if stat in ignore_pitching:
                    continue
                player_dict[stat] = player['stats'][s]
            boxscores['Team2']['Stats']['Pitching']['Players'].append(player_dict)
            
        #print json.dumps(boxscores)
        return boxscores
    else:
        return {}