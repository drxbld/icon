# -*- coding: utf-8 -*-

"""
    focus Add-on
    Copyright (C) 2016 focus

    
"""

from resources.lib.modules import control
control.execute('RunPlugin(plugin://%s)' % control.get_plugin_url({'action': 'service'}))
