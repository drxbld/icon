from urlparse import parse_qsl
import xbmcplugin
import xbmcaddon
import xbmcgui
import time
import sys
import ast

import api as soccer_api
import playbyplay
import matchstats
import standings
import replays
import lineup
import forms

_handle = int(sys.argv[1])
addon_id = 'plugin.video.sports'
addon = xbmcaddon.Addon(id=addon_id)
addonname = addon.getAddonInfo('name')

def router(paramstring):
    params = dict(parse_qsl(sys.argv[2][1:]))
    params.pop('sport')
    if params:
        play_me          = params.get('play_me')
        league           = params.get('league')
        gameId           = params.get('gameId')
        endpoint         = params.get('endpoint')
        game_obj         = params.get('game_obj')
        title            = params.get('title')
        link             = params.get('link')
        data             = params.get('data')
        page             = params.get('page')
        #live             = params.get('checkForStream')
        
        #Plays selected highlight clip
        if play_me:
            play_item = xbmcgui.ListItem(path=play_me)
            xbmcplugin.setResolvedUrl(_handle, True, listitem=play_item)
        elif endpoint:
            if endpoint == 'replays':
                if link:
                    replays.resolve(link, data, title)
                elif page is None:
                    from .. import checks
                    okayd = checks.checkPin()
                    if okayd is False:
                        ok = xbmcgui.Dialog().ok('Sports Guru', 'You need a valid pin in order to use this section of the add-on.')
                        quit()
                    replays.get_matches(league)
                else:
                    replays.get_matches(league, page)
            elif endpoint == 'today':
                game_list = soccer_api.get_games(league)
                soccer_api.display_games(game_list)
            elif endpoint == 'details':
                soccer_api.display_gameoptions(game_obj)
            elif endpoint == 'commentary':
                #gameId = '509296' #for testing
                pbp_list = soccer_api.get_playbyplay(gameId)
                if len(pbp_list) > 0:
                    game = ast.literal_eval(game_obj)
                    playbyplay_window = playbyplay.Plays(game['Title'])
                    playbyplay_window.setup(pbp_list)
                    playbyplay_window.doModal()
                    del playbyplay_window
                else:
                    nodata(game_obj)
            elif endpoint == 'h2hforms':
                #gameId = '509296' #for testing
                forms_data = soccer_api.get_h2hforms(gameId)
                forms_window = forms.Forms()
                forms_window.setup(forms_data)
                forms_window.doModal()
                del forms_window
            elif endpoint == 'lineups':
                #gameId = '491358' #for testing
                lineups = soccer_api.get_lineups(gameId)
                if len(lineups) > 0:
                    lineup_window = lineup.Players()
                    lineup_window.setup(lineups)
                    lineup_window.doModal()
                    del lineup_window
                else:
                    game = ast.literal_eval(game_obj)
                    line1 =  'The lineups for the [B]%s vs %s[/B] match aren\'t available yet. ' \
                             % (game['Abbrev1'], game['Abbrev2'])
                    line1 += 'Please check back shortly before the game begins. '
                    line1 += 'Start time is [B]%s[/B]' % game['Time']
                    xbmcgui.Dialog().ok(addonname, line1)
            elif endpoint == 'matchstats':
                stats = soccer_api.get_matchstats(gameId)
                if len(stats) > 0:
                    matchstats_window = matchstats.Match()
                    matchstats_window.setup(stats)
                    matchstats_window.doModal()
                    del matchstats_window
                else:
                    nodata(game_obj)
            elif endpoint == 'highlights':
                #gameId = '480579' #for testing
                highlights = soccer_api.get_highlights(gameId)
                if len(highlights) > 0:
                    soccer_api.display_highlights(highlights)
                else:
                    nodata(game_obj)
            elif endpoint == 'standings':
                standings_list = soccer_api.get_standings(league)
                standings_window = standings.Score()
                standings_window.setup(standings_list)
                standings_window.doModal()
                del standings_window
        elif league:
            #game_list = soccer_api.get_games(league)
            #soccer_api.display_games(game_list)
            soccer_api.display_mainmenu(league)
        else:
            raise ValueError('Invalid paramstring: {0}!'.format(paramstring))
    else:
        soccer_api.display_leagues()

def nodata(obj):
    game = ast.literal_eval(obj)
    cleaned_title = game['Title'][:game['Title'].find(' (')]
    if '(FT)' in game['Title']:
        line1 = 'There are no recap videos for the %s match. ' % cleaned_title
        line1 += 'You can check the Full-Game Replay section at '
        line1 += 'a later time to view the entire game.'
        xbmcgui.Dialog().ok(addonname, line1)
    else:
        line1 = 'The [B]%s[/B] game has not ended yet, ' % cleaned_title
        line1 += 'so there are no recap videos to show. '
        line1 += 'Please check back after the game ends. '
        if 'AM' in game['Time'] or 'PM' in game['Time']:
            line1 += 'Start time is [B]%s[/B]' % game['Time']
        elif 'HT' in game['Time']:
            line1 += 'Game is currently at [B]HT[/B]'
        else:
            line1 += 'Game is currently in the [B]%s[/B] minute' % game['Time']
        xbmcgui.Dialog().ok(addonname, line1)
                
if __name__ == '__main__':
    router(sys.argv[2][1:])