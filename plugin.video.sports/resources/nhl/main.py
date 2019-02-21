from urlparse import parse_qsl
import xbmcplugin
import xbmcaddon
import xbmcgui
import time
import sys
import ast

import api as nhl_api
import scoreboard
import playbyplay
import standings
import boxscore
import replays

_handle = int(sys.argv[1])
addon_id = 'plugin.video.sports'
addon = xbmcaddon.Addon(id=addon_id)
addonname = addon.getAddonInfo('name')

def router(paramstring):
    params = dict(parse_qsl(sys.argv[2][1:]))
    params.pop('sport')
    if params:
        play_me         = params.get('play_me')
        scoreboard_link = params.get('scoreboard')
        boxscores_link  = params.get('boxscores')
        teamstats_link  = params.get('teamstats')
        highlights_link = params.get('highlights')
        playbyplay_link = params.get('playbyplay')
        game_obj        = params.get('game_obj')
        title           = params.get('title')
        link            = params.get('link')
        endpoint        = params.get('endpoint')
        page            = params.get('page')
        
        #Plays selected highlight clip
        if play_me:
            play_item = xbmcgui.ListItem(path=play_me)
            xbmcplugin.setResolvedUrl(_handle, True, listitem=play_item)
            
        elif endpoint:
            if endpoint == 'replays':
                if link:
                    replays.show_qualities(link, title)
                elif page is None:
                    from .. import checks
                    okayd = checks.checkPin()
                    if okayd is False:
                        ok = xbmcgui.Dialog().ok('Sports Guru', 'You need a valid pin in order to use this section of the add-on.')
                        quit()
                    replays.get_games()
                else:
                    replays.get_games(page)
            elif endpoint == 'today':
                game_list = nhl_api.get_games()
                nhl_api.display_games(game_list)
            elif endpoint == 'details':
                nhl_api.display_gameoptions(game_obj)
            elif endpoint == 'standings':
                standings_list = nhl_api.get_standings()
                standings_window = standings.Score()
                standings_window.setup(standings_list)
                standings_window.doModal()
                del standings_window
            
        elif teamstats_link:
            line1 = 'You forget to complete this section'
            line2 = 'Make sure you do so before releasing'
            xbmcgui.Dialog().ok(addonname, line1, line2)
            
        #Highlight Clips
        #Displays highlight clips of specific game
        elif highlights_link:
            #highlights_link = 'http://www.espn.com/nhl/boxscore?gameId=400962711'
            h_list = nhl_api.get_highlights(highlights_link)
            if len(h_list) > 0:
                nhl_api.display_highlights(h_list)
            else:
                nodata(game_obj)
                
        #Play-By-Play Window
        elif playbyplay_link:
            #############The following link is for testing only####################
            #Regular 3-period game
            #playbyplay_link = 'http://www.espn.com/nhl/boxscore?gameId=400962648'
            #OT game
            #playbyplay_link = 'http://www.espn.com/nhl/boxscore?gameId=400962485'
            #SO game
            #playbyplay_link = 'http://www.espn.com/nhl/boxscore?gameId=400962444'
            ################Remove after testing is complete#######################
            
            pbp_list = nhl_api.get_playbyplay(playbyplay_link)
            if len(pbp_list) > 0:
                game = ast.literal_eval(game_obj)
                playbyplay_window = playbyplay.Plays(game['Title'])
                playbyplay_window.setup(pbp_list)
                playbyplay_window.doModal()
                del playbyplay_window
            else:
                nodata(game_obj)
                
        #Scoreboard Window
        #Activates when selecting specific game
        elif scoreboard_link:
            #############The following link is for testing only####################
            #scoreboard_link = 'http://www.espn.com/nhl/boxscore?gameId=400962632'
            ################Remove after testing is complete#######################
            
            score_obj = nhl_api.get_scoreboard(scoreboard_link)
            if len(score_obj) > 0:
                scoreboard_window = scoreboard.Score()
                scoreboard_window.setup(score_obj)
                scoreboard_window.doModal()
                del scoreboard_window
            else:
                nodata(game_obj)
            
        elif boxscores_link:
            #############The following link is for testing only####################
            #boxscores_link = 'http://www.espn.com/nhl/boxscore?gameId=400962675'
            #boxscores_link = 'http://www.espn.com/nhl/boxscore?gameId=400962444'
            ################Remove after testing is complete#######################
            
            boxscore_obj = nhl_api.get_boxscores(boxscores_link)
            if len(boxscore_obj) > 0:
                boxscore_window = boxscore.Score()
                boxscore_window.setup(boxscore_obj)
                boxscore_window.doModal()
                del boxscore_window
            else:
                nodata(game_obj)
        else:
            raise ValueError('Invalid paramstring: {0}!'.format(paramstring))
    else:
        #game_list = nhl_api.get_games()
        #nhl_api.display_games(game_list)
        nhl_api.display_mainmenu()

def nodata(obj):
    game = ast.literal_eval(obj)
    line1 = 'The %s game has not started yet.' % game['Title']
    line2 = 'Please check back after the game begins'
    line3 = 'Start time is %s' % game['Time']
    xbmcgui.Dialog().ok(addonname, line1, line2, line3)
                
if __name__ == '__main__':
    router(sys.argv[2][1:])