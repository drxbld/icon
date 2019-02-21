import pyxbmct.addonwindow as pyxbmct
import xbmcaddon
import requests
import xbmcgui
import xbmcvfs
import xbmc
import json
import os

addon_id = 'plugin.video.sports'
_addon = xbmcaddon.Addon(id=addon_id)
_path = 'special://home/addons/%s/' % addon_id
_teams = xbmc.translatePath(os.path.join(_path, "resources/teams.json"))

leagues = {
            "eng.1":"English Premier League",
            "eng.2":"English League Championship",
            "eng.3":"English League One",
            "eng.4":"English League Two",
            "uefa.europa":"UEFA Europa League",
            "uefa.champions":"UEFA Champions League",
            "ita.1":"Italian Serie A",
            "esp.1":"Spain La Liga",
            "sco.1":"Scottish Premier League",
            "fra.1":"French Ligue 1",
            "ger.1":"German Bundesliga",
            "usa.1":"Major League Soccer",
            "fifa.friendly":"International Friendlies",
            "fifa.world":"World Cup"
          }

class MultiChoiceDialog(pyxbmct.AddonDialogWindow):
    def __init__(self, title="", check_icon=None, items=None, presets=None):
        super(MultiChoiceDialog, self).__init__(title)
        self.setGeometry(450, 550, 9, 4)
        self.selected = []
        self.set_controls()
        self.connect_controls()
        self.listing.addItems(items or [])
        self.check_icon = check_icon
        print presets
        #http://romanvm.github.io/Kodistubs/_autosummary/xbmcgui.html#xbmcgui.ControlList
        for preset in presets:
            list_item = self.listing.getListItem(preset)
            list_item.setIconImage(self.check_icon)
            list_item.setLabel2("checked")
        self.set_navigation()

    def set_controls(self):
        self.listing = pyxbmct.List(_imageWidth=35, _imageHeight=35)
        self.placeControl(self.listing, 0, 0, rowspan=8, columnspan=4)
        self.ok_button = pyxbmct.Button("OK")
        self.placeControl(self.ok_button, 8, 1)
        self.cancel_button = pyxbmct.Button("Cancel")
        self.placeControl(self.cancel_button, 8, 2)

    def connect_controls(self):
        self.connect(self.listing, self.check_uncheck)
        self.connect(self.ok_button, self.ok)
        self.connect(self.cancel_button, self.close)

    def set_navigation(self):
        self.listing.controlUp(self.ok_button)
        self.listing.controlDown(self.ok_button)
        self.ok_button.setNavigation(self.listing, self.listing, self.cancel_button, self.cancel_button)
        self.cancel_button.setNavigation(self.listing, self.listing, self.ok_button, self.ok_button)
        if self.listing.size():
            self.setFocus(self.listing)
        else:
            self.setFocus(self.cancel_button)

    def check_uncheck(self):
        list_item = self.listing.getSelectedItem()
        if list_item.getLabel2() == "checked":
            list_item.setIconImage("")
            list_item.setLabel2("unchecked")
        else:
            list_item.setIconImage(self.check_icon)
            list_item.setLabel2("checked")

    def ok(self):
        self.selected = [index for index in xrange(self.listing.size())
                                if self.listing.getListItem(index).getLabel2() == "checked"]
        super(MultiChoiceDialog, self).close()

    def close(self):
        self.selected = []
        super(MultiChoiceDialog, self).close()
        
def load(sport, league=None):
    with open(_teams, "rb") as f: 
        teams_obj = json.load(f)
        
    check_icon = xbmc.translatePath(os.path.join(_path, "resources/%s/select.png" % sport))
    if league is None:
        all = teams_obj[sport]['all']
        selected = teams_obj[sport]['selected']
        title = sport.upper()
    elif league == 'fifa.friendly':
        all = teams_obj[league]['all']
        selected = teams_obj[league]['selected']
        title = leagues[league]
    else:
        #we need to fetch teams dynamically
        teams_endpoint = 'http://cdn.espn.com/soccer/standings/_/league/%s&xhr=1'
        data = requests.get(teams_endpoint % league)
        j_obj = json.loads(data.text)
        all = []
        for group in j_obj['content']['standings']['groups']:
            for team in group['standings']['entries']:
                all.append(team['team']['displayName'])
        selected = teams_obj[league]['selected']
        title = leagues[league]
        
    presets = [all.index(s) for s in selected]
    dialog = MultiChoiceDialog("%s - Select teams" % title, check_icon, all, presets)  
    dialog.doModal()
    
    if len(dialog.selected) > 0:
        if league is None:
            teams_obj[sport]['selected'] = [team for i, team in enumerate(all) if i in dialog.selected]
        else:
            teams_obj[league]['selected'] = [team for i, team in enumerate(all) if i in dialog.selected]
    
    with open(_teams, "wb") as f: 
        f.write(json.dumps(teams_obj, indent=4, sort_keys=True))
    
    del dialog