# -*- coding: UTF-8 -*-
# -Cleaned and Checked on 01-03-2019 by JewBMX in Scrubs.

# from resources.lib.modules import cfscrape

# scraper = cfscrape.create_scraper()
# self.scraper = cfscrape.create_scraper()

# r = scraper.get(url).content
# r = self.scraper.get(url).content

# xbmcgui.Dialog ().textviewer ("data",str (name))
# if test.status() is False: raise Exception()

import os.path

files = os.listdir(os.path.dirname(__file__))
__all__ = [filename[:-3] for filename in files if not filename.startswith('__') and filename.endswith('.py')]

