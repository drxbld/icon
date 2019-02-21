"""
    air_table movie list template
    Copyright (C) 2018, Team OTB
    Version 1.0.0

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

    -------------------------------------------------------------

    -------- These are the xml examples you place in your xml to call the plugin
          Make the tag relevant to your plugin. <temp_movie> is the example below-----

    Returns the Template Movie list-

    <dir>
    <title>Template Movie List</title>
    <Movies>all</Movies>
    </dir>


    ---------------------

    Possible Genre's are:
    Action
    Adventure
    Comedy
    Concert
    Documentary
    Drama
    Family
    Kids
    Romance
    SciFi
    Standup Comedy
    Thriller
    War
    Western

    -----------------------

    Genre tag examples

    <dir>
    <title>Template Action Movies</title>
    <temp_movie>genre/Action</temp_movie>
    </dir>

    <dir>
    <title>Template Comedy Movies</title>
    <temp_movie>genre/Comedy</temp_movie>
    </dir>    

    --------------------------------------------------------------

"""



from __future__ import absolute_import
import requests
import re
import os
import xbmc
import xbmcaddon
import json
from koding import route
from ..plugin import Plugin
from resources.lib.external.airtable.airtable import Airtable
from resources.lib.util.context import get_context_items
from resources.lib.util.xml import JenItem, JenList, display_list
from requests.exceptions import HTTPError
import time
from unidecode import unidecode


"""
----------------------------------------------------------
"""
table_id = "appwxTRdrEcQQOVl8"
table_name = "Movies"
workspace_api_key = "keyBJeHJoJq6Rq9Zl"
"""
----------------------------------------------------------
"""


CACHE_TIME = 3600  # change to wanted cache time in seconds

addon_fanart = xbmcaddon.Addon().getAddonInfo('fanart')
addon_icon = xbmcaddon.Addon().getAddonInfo('icon')
AddonName = xbmc.getInfoLabel('Container.PluginName')
AddonName = xbmcaddon.Addon(AddonName).getAddonInfo('id')



class Template_Movie_List(Plugin):

    name = "template_movie_list"


    def process_item(self, item_xml):
        if "<Movies>" in item_xml:
            item = JenItem(item_xml)
            if "all" in item.get("Movies", ""):
                result_item = {
                    'label': item["title"],
                    'icon': item.get("thumbnail", addon_icon),
                    'fanart': item.get("fanart", addon_fanart),
                    'mode': "open_Movies_movies",
                    'url': "",
                    'folder': True,
                    'imdb': "0",
                    'season': "0",
                    'episode': "0",
                    'info': {},
                    'year': "0",
                    'context': get_context_items(item),
                    "summary": item.get("summary", None)
                }
                result_item["properties"] = {
                    'fanart_image': result_item["fanart"]
                }
                result_item['fanart_small'] = result_item["fanart"]
                return result_item

            elif "genre" in item.get("Movies", ""):    
                result_item = {
                    'label': item["title"],
                    'icon': item.get("thumbnail", addon_icon),
                    'fanart': item.get("fanart", addon_fanart),
                    'mode': "open_Movies_genre_movies",
                    'url': item.get("Movies", ""),
                    'folder': True,
                    'imdb': "0",
                    'season': "0",
                    'episode': "0",
                    'info': {},
                    'year': "0",
                    'context': get_context_items(item),
                    "summary": item.get("summary", None)
                }
                result_item["properties"] = {
                    'fanart_image': result_item["fanart"]
                }
                result_item['fanart_small'] = result_item["fanart"]
                return result_item 


@route(mode='open_Movies_movies')
def open_movies():
    xml = ""
    at = Airtable(table_id, table_name, api_key=workspace_api_key)
    match = at.get_all(maxRecords=700, sort=['name'])  
    for field in match:
        try:
            res = field['fields']   
            name = res['name']
            name = remove_non_ascii(name)
            summary = res['summary']
            summary = remove_non_ascii(summary)
            fanart = res['fanart']
            thumbnail = res['thumbnail']
            link1 = res['link1']
            link2 = res['link2']
            link3 = res['link3']
            xml += "<item>"\
                   "<title>%s</title>"\
                   "<meta>"\
                   "<content>movie</content>"\
                   "<imdb></imdb>"\
                   "<title></title>"\
                   "<year></year>"\
                   "<thumbnail>%s</thumbnail>"\
                   "<fanart>%s</fanart>"\
                   "<summary>%s</summary>"\
                   "</meta>"\
                   "<link>"\
                   "<sublink>%s</sublink>"\
                   "<sublink>%s</sublink>"\
                   "<sublink>%s</sublink>"\
                   "<sublink>(Trailer)</sublink>"\
                   "</link>"\
                   "</item>" % (name,thumbnail,fanart,summary,link1,link2,link3)                    
        except:
            pass                                                                     
    jenlist = JenList(xml)
    display_list(jenlist.get_list(), jenlist.get_content_type())

@route(mode='open_Movies_genre_movies',args=["url"])
def open_genre_movies(url):
    xml = ""
    genre = url.split("/")[-1]
    at = Airtable(table_id, table_name, api_key=workspace_api_key)
    try:
        match = at.search('type', genre)
        for field in match:
            res = field['fields']   
            name = res['name']
            name = remove_non_ascii(name)
            summary = res['summary']
            summary = remove_non_ascii(summary)
            fanart = res['fanart']
            thumbnail = res['thumbnail']
            link1 = res['link1']
            link2 = res['link2']
            link3 = res['link3']
            xml += "<item>"\
                   "<title>%s</title>"\
                   "<meta>"\
                   "<content>movie</content>"\
                   "<imdb></imdb>"\
                   "<title></title>"\
                   "<year></year>"\
                   "<thumbnail>%s</thumbnail>"\
                   "<fanart>%s</fanart>"\
                   "<summary>%s</summary>"\
                   "</meta>"\
                   "<link>"\
                   "<sublink>%s(Link 1)</sublink>"\
                   "<sublink>%s(Link 2)</sublink>"\
                   "<sublink>%s(Link 3)</sublink>"\
                   "<sublink>(Trailer)</sublink>"\
                   "</link>"\
                   "</item>" % (name,thumbnail,fanart,summary,link1,link2,link3)                   
    except:
        pass                  
    jenlist = JenList(xml)
    display_list(jenlist.get_list(), jenlist.get_content_type())


def remove_non_ascii(text):
    return unidecode(text)
   