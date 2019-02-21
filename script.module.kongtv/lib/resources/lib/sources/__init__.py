# -*- coding: UTF-8 -*-
# -Cleaned and Checked on 11-20-2018 by JewBMX in Scrubs.

# from resources.lib.modules import cfscrape
# scraper = cfscrape.create_scraper()
# self.scraper = cfscrape.create_scraper()

# r = scraper.get(url).content
# r = self.scraper.get(url).content

# xbmcgui.Dialog ().textviewer ("data",str (name))


import pkgutil
import os.path
from resources.lib.modules import log_utils

__all__ = [x[1] for x in os.walk(os.path.dirname(__file__))][0]

def sources():
    try:
        sourceDict = []
        for i in __all__:
            for loader, module_name, is_pkg in pkgutil.walk_packages([os.path.join(os.path.dirname(__file__), i)]):
                if is_pkg:
                    continue

                try:
                    module = loader.find_module(module_name).load_module(module_name)
                    sourceDict.append((module_name, module.source()))
                except Exception as e:
                    log_utils.log('Scrubs Could not load "%s": %s' % (module_name, e), log_utils.LOGDEBUG)
        return sourceDict
    except:
        return []

