import xbmcaddon
import requests
import xbmcgui
import pyxbmct
import xbmc
import json
import sys
import os

try:
    _url = sys.argv[0]
    _handle = int(sys.argv[1])
except:
    #Module is being accessed by service.py
    pass
    
addon_id = 'plugin.video.sports'
addon = xbmcaddon.Addon(id=addon_id)
blue = os.path.join(addon.getAddonInfo('path').decode('utf-8'), 'resources/blue.png')

#Create custom skin design for ticker notification
#http://romanvm.github.io/script.module.pyxbmct/skins.html
class MySkin(pyxbmct.Skin):
    @property
    def close_button_focus(self):
        return ''#blue

    @property
    def close_button_no_focus(self):
        return ''#blue
    
    @property
    def header_height(self):
        #Set title bar height to 0 so it isn't visible.
        return 0
        
    #Set close_btn width and height to 0 so it isn't visible.
    @property
    def close_btn_width(self):
        return 0

    @property
    def close_btn_height(self):
        return 0
        
    

#Set pyxbmct addonwindow skin to our custom skin
pyxbmct.addonwindow.skin = MySkin()
#Now windows we create will display with the custom style we've provided
class Scores(pyxbmct.AddonDialogWindow):

    def __init__(self, title=''):
        super(Scores, self).__init__(title)
        #Geometry(Width, Height, Rows, Columns)
        #New Addon Windows always have 1280x720 grid
        self.setGeometry(1280, 30, 3, 50, pos_x=1, pos_y=690)
        main_bg = pyxbmct.Image(blue)
        self.placeControl(main_bg, 0, 0, rowspan=4, columnspan=49, pad_x=-5, pad_y=-5)
        
        btn_bg = pyxbmct.Image(blue)
        self.placeControl(btn_bg, 0, 49, columnspan=2, rowspan=4, pad_x=-5, pad_y=-5)
        self.display_duration = int(addon.getSetting('Ttimeout')) * 1000
        
        # Connect a key action (Backspace) to close the window.
        self.connect(pyxbmct.ACTION_NAV_BACK, self.close)
    
    #row, column[, rowspan, columnspan]
    def queue(self, sports):
        rssStr = ''.join(['[B]%s[/B]%s' % (sport.upper(),
                 ''.join([' %s %s %s %s  %s  | ' % (game['Name1'],
                 game['Score1'], game['Name2'], game['Score2'],
                 game['Time']) for game in games])) for (sport,
                 games) in sports.iteritems()])
        rssStr = rssStr + rssStr
        rssLabel = pyxbmct.FadeLabel()
        #self.placeControl(rssLabel, 0, 0, columnspan=49, pad_y=-5)
        self.placeControl(rssLabel, 0, 0, columnspan=49, rowspan=4, pad_y=-1)
        rssLabel.addLabel(rssStr)
        
        self.close_button = pyxbmct.Button('X  ')
        self.placeControl(self.close_button, 0, 49, columnspan=3, rowspan=4, pad_y=-5, pad_x=5)
        self.connect(self.close_button, self.close)
        extra_iterations = 0
        for key, gs in sports.iteritems():
            if len(gs) > 3:
                extra_iterations += len(gs) - 3 / 3
        total_iterations = len(sports.keys()) + extra_iterations
        self.display_duration = self.display_duration * total_iterations
        self.show()
        xbmc.sleep(self.display_duration)
        self.close()
        
        #rssLabel.setAnimations([('conditional', 'condition=true effect=slide start=1280,0 end=-1280,0 time=10000 loop=true',)])
        
    def setAnimation(self, control):
        # Set fade animation for all add-on window controls
        control.setAnimations([('WindowOpen', 'effect=fade start=0 end=100 time=500',),
                                ('WindowClose', 'effect=fade start=100 end=0 time=500',)])