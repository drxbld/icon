from urlparse import parse_qsl
from urllib import urlencode
from urllib import unquote
import xbmcplugin
import xbmcaddon
import requests
import xbmcgui
import xbmc
import time
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
fanart = xbmc.translatePath(os.path.join(path, "resources/soccer/background.jpg"))
_tempdata = xbmc.translatePath(os.path.join(path, "temp.json"))
placeholder = xbmc.translatePath(os.path.join(path, "resources/soccer/player.png"))
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
standings_url  = 'http://cdn.espn.com/soccer/standings/_/league/{league}&xhr=1'
games_url      = 'http://www.espn.com/soccer/scoreboard/_/league/{league}/date/{YYYYMMDD}&xhr=1'
game_url       = 'http://cdn.espn.com/core/soccer/match?gameId={gameId}&xhr=1'
lineups_url    = 'http://www.espn.com/soccer/lineups?gameId={gameId}&xhr=1'
matchstats_url = 'http://www.espn.com/soccer/matchstats?gameId={gameId}&xhr=1'
playbyplay_url = 'http://www.espn.com/soccer/commentary?gameId={gameId}&xhr=1'

def get_url(**kwargs):
    kwargs = {k: unicode(v).encode('ascii', 'ignore') for k,v in kwargs.iteritems()}
    return '{0}?{1}'.format(_url, urlencode(kwargs))
    
def display_leagues():
    #today = time.strftime("%Y%m%d") #YYYYMMDD
    #for testing
    #today = '20180512'
    for league, code in leagues.iteritems():
        """
        #Get Game Count for League
        data  = requests.get(games_url.format(league=code, YYYYMMDD=today), 
                             headers={'Cache-Control':'no-cache'})
        j_obj = json.loads(data.text)
        games = j_obj['content']['sbData']['events']
        oleague = league
        if len(games) > 0:
            league += ' (%d)' % len(games)
        #End Get Game Count for League
        """
        list_item = xbmcgui.ListItem(label=league)
        list_item.setArt({'fanart':fanart,'thumb':icon,'poster':icon})
        list_item.setInfo('video',{'title':league})
        
        """
        standings = get_url(sport='soccer', league=code, endpoint='standings')
        replays   = get_url(sport='soccer', league=oleague, endpoint='replays')
        commands  = []
        commands.append(( 'Standings',        'XBMC.RunPlugin(%s)'        % standings, ))
        commands.append(( 'Full-Game Replays','XBMC.Container.Update(%s)' % replays, ))
        list_item.addContextMenuItems( commands )
        """
        url = get_url(sport='soccer', league=league)
        
        xbmcplugin.addDirectoryItem(_handle, url, list_item, isFolder=True)
    xbmcplugin.addSortMethod(_handle, xbmcplugin.SORT_METHOD_TITLE)
    xbmcplugin.endOfDirectory(_handle)
    
def display_mainmenu(league):
    list_item = xbmcgui.ListItem(label='Full-Game Replays')
    list_item.setArt({'fanart':fanart,'thumb':icon,'poster':icon})
    list_item.setInfo('video',{'plot':'Full-Game Replays section for all past games.\n\n[COLOR yellow]Note:[/COLOR] Pin Generation is required to use this section.','title':'Full-Game Replays'})
    replays = get_url(sport='soccer', league=league, endpoint='replays')
    xbmcplugin.addDirectoryItem(_handle, replays, list_item, isFolder=True)
    
    list_item = xbmcgui.ListItem(label='Today\'s Games')
    list_item.setArt({'fanart':fanart,'thumb':icon,'poster':icon})
    list_item.setInfo('video',{'plot':'List of all scheduled games in this league today.','title':'Today\'s Games'})
    todaysgames = get_url(sport='soccer', league=leagues[league], endpoint='today')
    xbmcplugin.addDirectoryItem(_handle, todaysgames, list_item, isFolder=True)
    
    if league != 'International Friendlies':
        list_item = xbmcgui.ListItem(label='League Standings')
        list_item.setArt({'fanart':fanart,'thumb':icon,'poster':icon})
        list_item.setInfo('video',{'plot':'League standings divided into groups where applicable','title':'League Standings'})
        standings = get_url(sport='soccer', league=leagues[league], endpoint='standings')
        xbmcplugin.addDirectoryItem(_handle, standings, list_item, isFolder=False)
    
    xbmcplugin.addSortMethod(_handle, xbmcplugin.SORT_METHOD_NONE)
    xbmcplugin.endOfDirectory(_handle)
    
    
def display_gameoptions(game_obj):
    game = ast.literal_eval(game_obj)
    
    list_item = xbmcgui.ListItem(label='Forms & Head-to-Head Stats')
    list_item.setArt({'fanart':fanart,'thumb':icon,'poster':icon})
    list_item.setInfo('video',{'plot':'Previous game records in all competitions/leagues','title':'Forms & Head-to-Head Stats'})
    formsh2h = get_url(sport='soccer', league=game['League'], gameId=game['GameId'], endpoint='h2hforms', game_obj=game)
    xbmcplugin.addDirectoryItem(_handle, formsh2h, list_item, isFolder=False)
    
    list_item = xbmcgui.ListItem(label='Starting Line-ups')
    list_item.setArt({'fanart':fanart,'thumb':icon,'poster':icon})
    list_item.setInfo('video',{'plot':'Visual starting line-ups. Usually this data becomes available close to game-time, so check here 30 minutes to an hour prior to kickoff.','title':'Starting Line-ups'})
    lineups = get_url(sport='soccer', league=game['League'], gameId=game['GameId'], endpoint='lineups', game_obj=game)
    xbmcplugin.addDirectoryItem(_handle, lineups, list_item, isFolder=False)
    
    list_item = xbmcgui.ListItem(label='Play-by-Play')
    list_item.setArt({'fanart':fanart,'thumb':icon,'poster':icon})
    list_item.setInfo('video',{'plot':'Entire play-by-play for the game','title':'Play-by-Play'})
    commentary = get_url(sport='soccer', league=game['League'], gameId=game['GameId'], endpoint='commentary', game_obj=game)
    xbmcplugin.addDirectoryItem(_handle, commentary, list_item, isFolder=False)
    
    list_item = xbmcgui.ListItem(label='Match Stats')
    list_item.setArt({'fanart':fanart,'thumb':icon,'poster':icon})
    list_item.setInfo('video',{'plot':'Team game stats side-by-side for comparison','title':'Match Stats'})
    matchstats = get_url(sport='soccer', league=game['League'], gameId=game['GameId'], endpoint='matchstats', game_obj=game)
    xbmcplugin.addDirectoryItem(_handle, matchstats, list_item, isFolder=False)
    
    list_item = xbmcgui.ListItem(label='Highlights')
    list_item.setArt({'fanart':fanart,'thumb':icon,'poster':icon})
    list_item.setInfo('video',{'plot':'[COLOR green]HD[/COLOR] Highlight clips of the game','title':'Game Highlights'})
    highlights = get_url(sport='soccer', league=game['League'], gameId=game['GameId'], endpoint='highlights', game_obj=game)
    xbmcplugin.addDirectoryItem(_handle, highlights, list_item, isFolder=True)
    
    xbmcplugin.addSortMethod(_handle, xbmcplugin.SORT_METHOD_NONE)
    xbmcplugin.endOfDirectory(_handle)
    
#Returns json-friendly list object [{},{},{}]
def get_games(league):
    today = time.strftime("%Y%m%d") #YYYYMMDD
    #for testing
    #today = '20180512'
    #today = '20180411'
    data  = requests.get(games_url.format(league=league, YYYYMMDD=today), 
                         headers={'Cache-Control':'no-cache'})
    j_obj = json.loads(data.text)
    games = j_obj['content']['sbData']['events']
    game_list = []
    for game in games:
        #temp_date       = time.strptime(game['gameDate'], '%Y-%m-%dT%H:%M:%SZ')
        #game_date       = time.strftime("%b %e, %Y", temp_date)
        details         = game['competitions'][0]
        gameId          = game['id']
        if game['status']['type']['completed']:
            current_time = 'FT'
        elif game['status']['type']['shortDetail'] == 'HT':
            current_time = 'HT'
        elif game['status']['type']['state'] == 'pre' or \
             game['status']['type']['description'] == 'Scheduled':
            current_time = game['status']['type']['detail'].split(' at ')[1]
        else:
            current_time = game['status']['displayClock']
        team_one        = details['competitors'][0]['team']['displayName']
        team_two        = details['competitors'][1]['team']['displayName']
        abbrev_one      = details['competitors'][0]['team']['shortDisplayName']
        abbrev_two      = details['competitors'][1]['team']['shortDisplayName']
        score_one       = details['competitors'][0]['score']
        score_two       = details['competitors'][1]['score']
        title           = '%s vs %s (%s)' % (team_one, team_two, current_time)
        game_list.append({'Title':   title,       'GameId':  gameId,
                          'Name1':   team_one,    'Name2':   team_two,
                          'Abbrev1': abbrev_one,  'Abbrev2': abbrev_two,
                          'Score1':  score_one,   'Score2':  score_two,
                          'Time':    current_time,'League':  league})
    return game_list

def check_for_updates(league, teams):
    with open(_tempdata, "rb") as f:
        tempdata = json.load(f)
        
    types = [type 
             for type in ['soccer_upcominggame','soccer_startofgame','soccer_scorechange','soccer_halftime','soccer_endofgame'] 
             if eval(addon.getSetting(type).title()) is True]
    updated_games = get_games(league)
    games_to_keep = [updated_game 
                     for updated_game in updated_games 
                     if updated_game['Name1'] in str(teams) or updated_game['Name2'] in str(teams)]
    updates = []
    td = tempdata[league]
    #Now look at game data to see if any notifications need to be presented
    for game in games_to_keep:
        gametitle = game['Title']
        try:
            gametitle = gametitle.replace(re.compile('(\s\(.+?\))').findall(gametitle)[0],'')
        except:
            pass
        if 'soccer_upcominggame' in types and gametitle not in td.keys():
            #We haven't announced this upcoming game yet, so do so
            updates.append(game)
        elif 'soccer_startofgame' in types and any(['PM' in td[gametitle]['Time'],
             'AM' in td[gametitle]['Time']]) and all(['PM' not in game['Time'
             ], 'AM' not in game['Time'], 'FT' not in game['Time']]):
            updates.append(game)
        elif 'soccer_scorechange' in types and any([int(game['Score1']) > int(td[gametitle]['Score1']),
                                                    int(game['Score2']) > int(td[gametitle]['Score2'])]):
            updates.append(game)
        elif 'soccer_halftime' in types and any([all(['\'' in td[gametitle]['Time'], 'HT' in game['Time']])]):
            updates.append(game)
        elif 'soccer_endofgame' in types and any([all(['FT' not in td[gametitle]['Time'], 'FT' in game['Time']])]):
            updates.append(game)
        #Save/Overwrite tempdata as we go to save time
        tempdata[league][gametitle] = game
    with open(_tempdata, "wb") as f: 
        f.write(json.dumps(tempdata, indent=4, sort_keys=True))
    return updates
    
def display_games(games):
    if len(games) > 0:
        for game in games:
            details = '%s vs %s\n%s [B]-[/B] %s\n%s' % (game['Name1'],  game['Name2'], 
                                                        game['Score1'], game['Score2'],
                                                        game['Time'])
            list_item = xbmcgui.ListItem(label=game['Title'])
            list_item.setArt({'fanart':fanart,'thumb':icon,'poster':icon})
            list_item.setInfo('video',{'plot':details,'title':game['Title']})
            innermenu = get_url(sport='soccer', league=game['League'], endpoint='details', game_obj=game)
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
#        of playbyplay for specific game
def get_playbyplay(gameId):
    data       = requests.get(playbyplay_url.format(gameId=gameId))
    j_obj      = json.loads(data.text)
    if j_obj['gamepackageJSON'].get('commentary'):
        teams      = j_obj['gamepackageJSON']['boxscore']['teams']
        teamlogo   = {teams[0]['team']['displayName']: teams[0]['team']['logo'],
                      teams[1]['team']['displayName']: teams[1]['team']['logo']}
        playbyplay = []
        for play in j_obj['gamepackageJSON']['commentary']:
            if play.get('play', {}).get('team', None):
                team = teamlogo[play['play']['team']['displayName']]
            else:
                team = ''
            if play['text'].startswith('Goal!'):
                playbyplay.append({'Time': '[B]%s[/B]' % play['time']['displayValue'], 
                                   'Team': team,
                                   'Play': '[B]%s[/B]' % play['text']})
            else:
                playbyplay.append({'Time': play['time']['displayValue'], 
                                   'Team': team,
                                   'Play': play['text']})
        return playbyplay
    else:
        return []
        
def get_highlights(gameId):
    data            = requests.get(game_url.format(gameId=gameId))
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
        url = get_url(sport='soccer', play_me=highlight['Clip'])
        xbmcplugin.addDirectoryItem(_handle, url, list_item, False)
    xbmcplugin.addSortMethod(_handle, xbmcplugin.SORT_METHOD_NONE)
    xbmcplugin.endOfDirectory(_handle)
    
def get_standings(league):
    data  = requests.get(standings_url.format(league=league), headers={'Cache-Control':'no-cache'})
    j_obj = json.loads(data.text)
    s = j_obj['content']['standings']['groups']
    c = j_obj['content']['config']['categories'][1:]
    headers = [cat['abbreviation'] for cat in c]
    standings = {'Headers':headers, 'League Name':j_obj['content']['standings']['name']}
    if league == 'uefa.europa':
        #We need to split the display into sensible portions (A-F, G-L)
        group_of_groups1, group_of_groups2 = s[:6], s[6:]
        groups_to_process = [group_of_groups1, group_of_groups2]
        groupnames = ['Groups A-F', 'Groups G-L']
    elif league == 'uefa.champions' or league == 'fifa.world':
        #We need to split the display into sensisble portions (A-D, E-H)
        group_of_groups1, group_of_groups2 = s[:4], s[4:]
        groups_to_process = [group_of_groups1, group_of_groups2]
        groupnames = ['Groups A-D', 'Groups E-H']
    elif league == 'usa.1':
        #Split East & West Conferences
        group_of_groups1, group_of_groups2 = s[0], s[1]
        groups_to_process = [group_of_groups1, group_of_groups2]
        groupnames = ['Eastern Conference', 'Western Conference']
    else:
        #No need to split, only one group
        groups_to_process = [s[0]]
        lname = j_obj['content']['standings']['name']
        groupnames = [lname]
    for g, group in enumerate(groups_to_process):
        tmp_standings = {}
        tmp_group = {}
        if isinstance(group, dict):
            for t, team in enumerate(group['standings']['entries']):
                tmp_team = {'Name':team['team']['displayName']}
                [(tmp_team.update({s['abbreviation']: '[COLOR red]%s[/COLOR]'
                 % s['displayValue']}) if s['displayValue'].startswith('-'
                 ) else (tmp_team.update({s['abbreviation']: '[COLOR green]%s[/COLOR]'
                 % s['displayValue']}) if s['displayValue'].startswith('+'
                 ) else tmp_team.update({s['abbreviation']: s['displayValue']})))
                 for s in (team['stats'])[1:]]
                tmp_group[t+1] = tmp_team
            if len(groups_to_process) > 1:
                standings[group['name']] = tmp_group
            else:
                standings[groupnames[g]] = tmp_group
        else:
            #Europa & Champions Leagues
            #These have sub-groups since there are so many letter groups
            #Example: Champions league's group[0] would be Groups A-D
            #         & group[1] will be Groups E-H
            for ig, inner_group in enumerate(group):
                grouped_letters = {}
                for t, team in enumerate(inner_group['standings']['entries']):
                    tmp_team = {'Name':team['team']['displayName']}
                    [(tmp_team.update({s['abbreviation']: '[COLOR red]%s[/COLOR]'
                     % s['displayValue']}) if s['displayValue'].startswith('-'
                     ) else (tmp_team.update({s['abbreviation']: '[COLOR green]%s[/COLOR]'
                     % s['displayValue']}) if s['displayValue'].startswith('+'
                     ) else tmp_team.update({s['abbreviation']: s['displayValue']})))
                     for s in (team['stats'])[1:]]
                    grouped_letters[t+1] = tmp_team
                tmp_group[inner_group['name']] = grouped_letters
            standings[groupnames[g]] = tmp_group
    return standings
    
def get_lineups(gameId):
    data  = requests.get(lineups_url.format(gameId=gameId))
    j_obj = json.loads(data.text)
    rosters = j_obj['gamepackageJSON']['rosters']
    if rosters[0].get('roster'):
        lineups = {}
        team1 = {}
        team2 = {}
        starters1 = []
        starters2 = []
        formation_one = rosters[0]['formation']
        formation_two = rosters[1]['formation']
        
        temp_form = '1-%s' % formation_one
        cols = temp_form.split('-')
        num_of_starters = sum(int(i) for i in cols)
        for player in rosters[0]['roster'][:num_of_starters]:
            name = player['athlete']['displayName']
            #Save last name only
            name = name[name.find(' ')+1:]
            if player['athlete'].get('headshot'):
                headshot = player['athlete']['headshot']['href']
            else:
                headshot = placeholder
            jersey = player['jersey']
            position = player['position']['abbreviation']
            starters1.append({'Name':name,
                              'Headshot':headshot,
                              'Jersey':jersey,
                              'Position':position})
            
        homeAway = '%sTeam' % rosters[0]['homeAway']
        record1 = ''#j_obj['__gamepackage__'][homeAway]['record'][0]['displayValue']
        team1 = {
            'HomeAway': rosters[0]['homeAway'],
            'Name':     rosters[0]['team']['displayName'],
            'Logo':     rosters[0]['team']['logos'][0]['href'],
            'Record':   record1,
            'Formation':'1-%s' % formation_one,
            'Players':  starters1
        }
        
        temp_form = '1-%s' % formation_two
        cols = temp_form.split('-')
        num_of_starters = sum(int(i) for i in cols)
        for player in rosters[1]['roster'][:num_of_starters]:
            name = player['athlete']['displayName']
            #Save last name only
            name = name[name.find(' ')+1:]
            if player['athlete'].get('headshot'):
                headshot = player['athlete']['headshot']['href']
            else:
                headshot = placeholder
            jersey = player['jersey']
            position = player['position']['abbreviation']
            starters2.append({'Name':name,
                              'Headshot':headshot,
                              'Jersey':jersey,
                              'Position':position})
        
        homeAway = '%sTeam' % rosters[1]['homeAway']
        record2 = ''#j_obj['__gamepackage__'][homeAway]['record'][0]['displayValue']
        team2 = {
            'HomeAway': rosters[1]['homeAway'],
            'Name':     rosters[1]['team']['displayName'],
            'Logo':     rosters[1]['team']['logos'][0]['href'],
            'Record':   record2,
            'Formation':'1-%s' % formation_two,
            'Players':  starters2
        }
        lineups = {'Team1':team1, 'Team2':team2}
        return lineups
    else:
        return {}
        
def get_h2hforms(gameId):
    h2hforms      = {'H2H':[],'Form1':{},'Form2':{}}
    data          = requests.get(matchstats_url.format(gameId=gameId))
    j_obj         = json.loads(data.text)
    h2h_data      = j_obj['gamepackageJSON']['headToHeadGames'][0]
    form_data     = j_obj['gamepackageJSON']['boxscore']['form']
    
    #Get H2H game data
    base_team = {'Name': h2h_data['team']['displayName'],
                 'Logo': h2h_data['team']['logo']}
    for h2h in h2h_data['events']:
        #https://www.tutorialspoint.com/python/time_strftime.htm
        temp_date       = time.strptime(h2h['gameDate'], '%Y-%m-%dT%H:%MZ')
        game_date       = time.strftime("%b %d, %Y", temp_date)
        final_score     = '%s-%s' % (h2h['homeTeamScore'], h2h['awayTeamScore'])
        if h2h['atVs'] == '@':
            team1 = h2h['opponent']['displayName']
            logo1 = h2h['opponent']['logo']
            team2 = base_team['Name']
            logo2 = base_team['Logo']
        else:
            team1 = base_team['Name']
            logo1 = base_team['Logo']
            team2 = h2h['opponent']['displayName']
            logo2 = h2h['opponent']['logo']
        temph = {'Score': final_score, 'Date':  game_date,
                 'Team1': team1,       'Team2': team2,
                 'Logo1': logo1,       'Logo2': logo2,
                 'Competition': h2h['leagueName']}
        h2hforms['H2H'].append(temph)
        
    #Get form data for Team 1
    form1 = {'Name':  form_data[0]['team']['displayName'],
             'Logo':  form_data[0]['team']['logo'],
             'Games': []}
    for event in form_data[0]['events']:
        temp_date         = time.strptime(event['gameDate'], '%Y-%m-%dT%H:%MZ')
        game_date         = time.strftime("%b %d, %Y", temp_date)
        final_score       = '%s-%s' % (event['homeTeamScore'], event['awayTeamScore'])
        result            = event['gameResult']
        if result == 'W':
            result = '[COLOR green]%s[/COLOR]' % result
        elif result == 'L':
            result = '[COLOR red]%s[/COLOR]' % result
        if event['atVs'] == '@':
            team1 = event['opponent']['displayName']
            logo1 = event['opponent']['logo']
            team2 = form1['Name']
            logo2 = form1['Logo']
        else:
            team1 = form1['Name']
            logo1 = form1['Logo']
            team2 = event['opponent']['displayName']
            logo2 = event['opponent']['logo']
        tempe = {'Result': result,
                 'Score':  final_score, 'Date':  game_date,
                 'Team1':  team1,       'Team2': team2,
                 'Logo1':  logo1,       'Logo2': logo2,
                 'Competition': event['leagueName']}
        form1['Games'].append(tempe)
    h2hforms['Form1'] = form1
    
    #Now get form data for Team 2
    form2 = {'Name':  form_data[1]['team']['displayName'],
             'Logo':  form_data[1]['team']['logo'],
             'Games': []}
    for event in form_data[1]['events']:
        temp_date         = time.strptime(event['gameDate'], '%Y-%m-%dT%H:%MZ')
        game_date         = time.strftime("%b %d, %Y", temp_date)
        final_score       = '%s-%s' % (event['homeTeamScore'], event['awayTeamScore'])
        result            = event['gameResult']
        if result == 'W':
            result = '[COLOR green]%s[/COLOR]' % result
        elif result == 'L':
            result = '[COLOR red]%s[/COLOR]' % result
        if event['atVs'] == '@':
            team1 = event['opponent']['displayName']
            logo1 = event['opponent']['logo']
            team2 = form2['Name']
            logo2 = form2['Logo']
        else:
            team1 = form2['Name']
            logo1 = form2['Logo']
            team2 = event['opponent']['displayName']
            logo2 = event['opponent']['logo']
        tempe = {'Result': result,
                 'Score':  final_score, 'Date':  game_date,
                 'Team1':  team1,       'Team2': team2,
                 'Logo1':  logo1,       'Logo2': logo2,
                 'Competition': event['leagueName']}
        form2['Games'].append(tempe)
    h2hforms['Form2'] = form2
    
    return h2hforms
    
def get_matchstats(gameId):
    data              = requests.get(matchstats_url.format(gameId=gameId))
    j_obj             = json.loads(data.text)
    team1             = {'Stats':{'Players':[]}}
    team2             = {'Stats':{'Players':[]}}
    rtestname         = j_obj['gamepackageJSON']['rosters'][0]['team']['displayName']
    btestname         = j_obj['gamepackageJSON']['boxscore']['teams'][0]['team']['displayName']
    if rtestname == btestname:
        for stat in j_obj['gamepackageJSON']['boxscore']['teams'][0]['statistics']:
            team1['Stats'][stat['label'].title()] = stat['displayValue']
        for stat in j_obj['gamepackageJSON']['boxscore']['teams'][1]['statistics']:
            team2['Stats'][stat['label'].title()] = stat['displayValue']
    else:
        for stat in j_obj['gamepackageJSON']['boxscore']['teams'][1]['statistics']:
            team1['Stats'][stat['label'].title()] = stat['displayValue']
        for stat in j_obj['gamepackageJSON']['boxscore']['teams'][0]['statistics']:
            team2['Stats'][stat['label'].title()] = stat['displayValue']
    #Save team status since we're making multiple api calls and
    #want to make sure we grab the right data for each team
    team1['HomeAway'] = j_obj['gamepackageJSON']['rosters'][0]['homeAway']
    team2['HomeAway'] = j_obj['gamepackageJSON']['rosters'][1]['homeAway']
    data              = requests.get(lineups_url.format(gameId=gameId))
    j_obj             = json.loads(data.text)
    if j_obj['gamepackageJSON']['rosters'][0]['homeAway'] == team1['HomeAway']:
        roster1 = j_obj['gamepackageJSON']['rosters'][0]
        roster2 = j_obj['gamepackageJSON']['rosters'][1]
    else:
        roster1 = j_obj['gamepackageJSON']['rosters'][1]
        roster2 = j_obj['gamepackageJSON']['rosters'][0]
    team1['Name'] = roster1['team']['displayName']
    team1['Logo'] = roster1['team']['logos'][0]['href']
    team2['Name'] = roster2['team']['displayName']
    team2['Logo'] = roster2['team']['logos'][0]['href']
    team1['Score'] = j_obj['__gamepackage__']['%sTeam' % team1['HomeAway']]['score']
    team2['Score'] = j_obj['__gamepackage__']['%sTeam' % team2['HomeAway']]['score']
    for athlete in roster1['roster']:
        player = {}
        player['Name'] = athlete['athlete']['displayName']
        for s in athlete['stats']:
            player[s['abbreviation']] = s['displayValue']
        team1['Stats']['Players'].append(player)
    for athlete in roster2['roster']:
        player = {}
        player['Name'] = athlete['athlete']['displayName']
        for s in athlete['stats']:
            player[s['abbreviation']] = s['displayValue']
        team2['Stats']['Players'].append(player)
    matchstats = {'Team1': team1, 'Team2': team2}
    return matchstats