"""

    Copyright (C) 2018 MuadDib

    ----------------------------------------------------------------------------
    "THE BEER-WARE LICENSE" (Revision 42):
    @tantrumdev wrote this file.  As long as you retain this notice you
    can do whatever you want with this stuff. If we meet some day, and you think
    this stuff is worth it, you can buy him a beer in return. - Muad'Dib
    ----------------------------------------------------------------------------


"""

import re,requests,os,traceback,urlparse
import koding
import __builtin__
import xbmc,xbmcaddon,xbmcgui
from koding import route
from resources.lib.plugin import Plugin
from resources.lib.player import JenPlayer
from resources.lib.util import dom_parser
from resources.lib.util.context import get_context_items
from resources.lib.util.xml import JenItem, JenList, display_list
from unidecode import unidecode

addon_id = xbmcaddon.Addon().getAddonInfo('id')
addon_fanart = xbmcaddon.Addon().getAddonInfo('fanart')
addon_icon   = xbmcaddon.Addon().getAddonInfo('icon')
next_icon = os.path.join(xbmc.translatePath(xbmcaddon.Addon().getAddonInfo('path')), 'resources', 'media', 'next.png')

User_Agent     = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'
base_main_link = 'https://www.b98.tv/'

class B98TV(Plugin):
    name = "b98tv"
    priority = 200

    def process_item(self, item_xml):
        if "<B98>" in item_xml:
            item = JenItem(item_xml)
            if "serieslist" in item.get("B98", ""):
                result_item = {
                    'label': item["title"],
                    'icon': item.get("thumbnail", addon_icon),
                    'fanart': item.get("fanart", addon_fanart),
                    'mode': "B98Series",
                    'url': item.get("B98", ""),
                    'folder': True,
                    'imdb': "0",
                    'content': "files",
                    'season': "0",
                    'episode': "0",
                    'info': {},
                    'year': "0",
                    'context': get_context_items(item),
                    "summary": item.get("summary", None)
                }
            elif "playtoon/" in item.get("B98", ""):
                result_item = {
                    'label': item["title"],
                    'icon': item.get("thumbnail", addon_icon),
                    'fanart': item.get("fanart", addon_fanart),
                    'mode': "B98Play",
                    'url': item.get("B98", ""),
                    'folder': False,
                    'imdb': "0",
                    'content': "files",
                    'season': "0",
                    'episode': "0",
                    'info': {},
                    'year': "0",
                    'context': get_context_items(item),
                    "summary": item.get("summary", None)
                }
            result_item['fanart_small'] = result_item["fanart"]
            return result_item

@route(mode='B98Series', args=["url"])
def get_B98Main_Processor(url):
    xml = ""
    url = url.replace('serieslist/', '')
    try:
        url = urlparse.urljoin(base_main_link, url)
        html = requests.get(url).content
        item_list = dom_parser.parseDOM(html, 'div', attrs={'class': 'item col-lg-3 col-md-3 col-sm-12 '})
        for content in item_list:
            link = re.compile('href="(.+?)"',re.DOTALL).findall(content)[0]
            icon, title = re.compile('img src="(.+?) alt="(.+?)"',re.DOTALL).findall(content)[0]
            try:
                link = link.replace(base_main_link,'')
                title = replaceHTMLCodes(title)
                if 'videos_categories' in link:
                    if 'Darkwing Duck' not in title: # Why Dandy? Why?
                        xml += "<dir>"\
                               "    <title>%s</title>"\
                               "    <meta>"\
                               "        <summary>%s</summary>"\
                               "    </meta>"\
                               "    <B98>serieslist/%s</B98>"\
                               "    <thumbnail>%s</thumbnail>"\
                               "</dir>" % (title,title,link,icon)
                else:
                    xml += "<item>"\
                           "    <title>%s</title>"\
                           "    <meta>"\
                           "        <summary>%s</summary>"\
                           "    </meta>"\
                           "    <B98>playtoon/%s</B98>"\
                           "    <thumbnail>%s</thumbnail>"\
                           "</item>" % (title,title,link,icon)
            except:
                continue

        try:
            navi_link = re.compile('a class="next page-numbers" href="(.+?)"',re.DOTALL).findall(html)[0]
            xml += "<dir>"\
                   "    <title>Next Page >></title>"\
                   "    <meta>"\
                   "        <summary>Click here to see the next page of awesome content!</summary>"\
                   "    </meta>"\
                   "    <B98>serieslist/%s</B98>"\
                   "    <thumbnail>%s</thumbnail>"\
                   "</dir>" % (navi_link,next_icon)
        except:
            pass
    except:
        pass

    jenlist = JenList(xml)
    display_list(jenlist.get_list(), jenlist.get_content_type())


@route(mode='B98Play', args=["url"])
def get_B98Play(url):
    url = url.replace('playtoon/', '')
    try:
        url = urlparse.urljoin(base_main_link, url)
        html = requests.get(url).content
        vid_url  = re.compile('file: "(.*?)"',re.DOTALL).findall(html)[0]
        if 'http:' in vid_url:
            vid_url = vid_url.replace('http:', 'https:')
        ep_title = re.compile('title>(.*?)\|',re.DOTALL).findall(html)[0]
        ep_icon  = re.compile('og:image" content="(.*?)"',re.DOTALL).findall(html)[0]
        vid_url = vid_url + '|User-Agent=' + User_Agent
        xbmc.executebuiltin("PlayMedia(%s)" % (vid_url))
        quit()
        return
    except:
        pass


def replaceHTMLCodes(txt):
    txt = re.sub("(&#[0-9]+)([^;^0-9]+)", "\\1;\\2", txt)
    txt = txt.replace("&quot;", "\"").replace("&amp;", "&")
    txt = txt.replace('&#8216;','\'').replace('&#8217;','\'').replace('&#038;','&').replace('&#8230;','....')
    txt = txt.strip()
    return txt


def replaceEscapeCodes(txt):
    try:
        import html.parser as html_parser
    except:
        import HTMLParser as html_parser
    txt = html_parser.HTMLParser().unescape(txt)
    return txt


def remove_non_ascii(text):
    try:
        text = text.decode('utf-8').replace(u'\xc2', u'A').replace(u'\xc3', u'A').replace(u'\xc4', u'A').replace(u'\xe2', u'a')
    except:
        pass
    return unidecode(text)
