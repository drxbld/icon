# -*- coding: utf-8 -*-

"""
    Corona Add-on
    Copyright (C) 2016 Corona

    
"""

from resources.lib.modules import control
control.execute('RunPlugin(plugin://%s)' % control.get_plugin_url({'action': 'service'}))
