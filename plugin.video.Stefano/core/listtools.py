# -*- coding: utf-8 -*-
# ------------------------------------------------------------
# streamondemand - Community Edition
# Copyright 2015 tvalacarta@gmail.com
# http://www.mimediacenter.info/foro/viewforum.php?f=36
#
# Distributed under the terms of GNU General Public License v3 (GPLv3)
# http://www.gnu.org/licenses/gpl-3.0.html
# ------------------------------------------------------------
# This file is part of streamondemand 5.
#
# streamondemand 5 is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# streamondemand 5 is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with streamondemand 5.  If not, see <http://www.gnu.org/licenses/>.
# --------------------------------------------------------------------------------
# Server management
# -------------------------------------------------

import re

from core import httptools, scrapertools, logger
from core.item import Item
from core.tmdb import infoSod

__channel__ = ''

#####
#   build a list of titles (movie or tvshow) based on the results returned by regx
#   regx can se either the regex to be executed (findall) or the list returned by executed regex (findall)
#   itemp is a dict containing any of the following paramteres: title,url,thumbnail,content,extra,action
#   title,url,thumbnail parameters in itemp are expeted to have the format \\i ... i.e i=1 indicating the first capturing group
#   nextregx is a dict contaning regx and action
#   ignore_regx is a dict containing regx for title, url, thumbnail

plst = 'title', 'url', 'thumbnail'


def next_page(data='', regexs=None, action=''):
    next_page = scrapertools.find_single_match(data, regexs)
    if next_page != "":
        return Item(channel=__channel__,
                    action=action,
                    title="[COLOR orange]Successivo >>[/COLOR]",
                    url="%s" % next_page,
                    extra='next',
                    thumbnail="http://2.bp.blogspot.com/-fE9tzwmjaeQ/UcM2apxDtjI/AAAAAAAAeeg/WKSGM2TADLM/s1600/pager+old.png")
    else:
        return None


def list_titles(regx=None, data=None, url=None, itemp=None, nextregx=None, ignore_regx=None):
    if itemp is None:
        itemp = {}
    logger.info('[list_titles] from channel ' + __channel__)
    itemlist = []
    pt = {}

    if isinstance(regx, str):
        if not data:
            if url:
                data = httptools.downloadpage(url).data
            else:
                return []

        matches = re.compile(regx, re.DOTALL).findall(data)
    else:
        matches = regx

    for match in matches:
        for x in plst:
            if x in itemp: pt['%s' % x] = itemp['%s' % x]

        for m in range(0, len(match)):
            for pe in pt:
                pt[pe] = pt[pe].replace('\\%s' % (m + 1), match[m].replace("[", "").replace("]", ""))

        scrapedtitle = scrapertools.htmlclean(scrapertools.decodeHtmlentities(pt['title']))
        if ignore_regx is not None and 'title' in ignore_regx:
            if scrapertools.find_single_match(scrapedtitle, ignore_regx['title']): continue

        scrapedurl = pt['url']
        if ignore_regx is not None and 'url' in ignore_regx:
            if scrapertools.find_single_match(scrapedurl, ignore_regx['url']): continue

        scrapedthumbnail = ''
        if 'thumbnail' in itemp:
            scrapedthumbnail = pt['thumbnail'][:-1] if pt['thumbnail'][-1] == ' ' else pt['thumbnail']
        if ignore_regx is not None and 'thumbnail' in ignore_regx:
            if scrapertools.find_single_match(scrapedthumbnail, ignore_regx['thumbnail']): continue

        i = Item(channel=__channel__,
                 contentType=itemp['content'] if 'content' in itemp else 'movie',
                 action=itemp['action'] if 'action' in itemp else 'findvideos',
                 title=scrapedtitle,
                 fulltitle=scrapedtitle,
                 url=scrapedurl,
                 thumbnail=scrapedthumbnail)
        if 'extra' in itemp: i.extra = itemp['extra']
        if 'content' in itemp:
            if 'tvshow' in itemp['content']: i.show = scrapedtitle
        itemlist.append(i)

    if nextregx:
        i = next_page(data, nextregx['regx'], nextregx['action'])
        if i: itemlist.append(i)

    for i in itemlist:
        logger.info(i)

    return itemlist


def list_titles_info(regx=None, data=None, url=None, itemp=None, nextregx=None, tipos=None, ignore_regx=None):
    if itemp is None:
        itemp = {}
    logger.info('[list_titles_info] from channel ' + __channel__)

    if not tipos: tipos = 'movie'

    itemlist = list_titles(regx, data, url, itemp, nextregx, ignore_regx)
    for item in itemlist:
        if 'next' not in item.extra:
            item = infoSod(item, tipo=tipos)

    return itemlist


################
#   Build the list of season using sdel (regex) as token to indeitify start of seaon block.
#   If required use enddel to provide the token to identify overall end of all season html
#   epdel and enddel should not contain any capturing group .. the obejctive is get the title and use it to delimit HTML blocks
#   Return itemlist with name season in title and HMTL with episodes in the url
#   url can be passed to find_video_items() as dato or link .. based on extra HTML vs URL
#   If epdel (episode delimiter) is specified and number of seasons are <= ns then the itemlist returned 
#   will include also the list of episodes
#   extra=seasonHTML or episodesHTML if it contains also the list of episodes
#   extra=episodesURL if url contains the link and not the html

def list_seasons(item=None, data=None, sdel=None, enddel=None, action=None, epdel=None, ns=None):
    logger.info('[list_seasons] from channel ' + item.channel)
    itemlist = []
    season_titles = []
    starts = []

    if not action:
        action = 'episodios'
    if not data:
        data = httptools.downloadpage(item.url).data
    if not ns: ns = 1
    if sdel:
        patron = sdel
    else:
        patron = 'stagion[e,i].*?ITA'

    matches = re.compile(patron, re.IGNORECASE).finditer(data)
    for match in matches:
        if match.group():
            season_titles.append(scrapertools.htmlclean(match.group()))
            starts.append(match.end())

    if not enddel: enddel = '</body>'
    ep = re.finditer(enddel, data)
    for e in ep:
        epos = e.end()
    if not epos: epos = -1

    i = 1
    len_lang_titles = len(season_titles)
    while i <= len_lang_titles:
        inizio = starts[i - 1]
        fine = starts[i] if i < len_lang_titles else epos
        html = data[inizio:fine]

        # building extended list with episodes
        if epdel and len(season_titles) <= ns:
            itemlist.append(build_item(title='[COLOR orange]' + season_titles[i - 1] + '[/COLOR]'))
            episodes = list_episodes(item=item, data=html, epre=epdel)
            for e in episodes:
                itemlist.append(e)
        else:  # building simple list of seasons
            itemlist.append(build_seas_item(title=season_titles[i - 1], url=html, action=action, extra="seasonHTML"))
        i += 1

    return itemlist


##############
#   Build the list of episodes using epre as regex to collect the names.
#   regex expects at least two capturing group: the name, block with links
#   regex assumption is that there will be one episode per line
#   Return itemlist with episode name in title and HMTL with the links in the url
#   If season_titles is provided the itemlist will include also that as first item
#   epre can be a string or dict containing {'regx':,'title':,'url':,'extra':,'action':}
#   you can specify title and url using the sintax \\i to indicate the matching group to be used


def list_episodes(item=None, data=None, epre=None, action=None, season_title=None):
    logger.info('[list_episodes] from channel ' + __channel__)
    itemlist = []

    if not data: data = httptools.downloadpage(item.url).data
    if not action: action = 'findvideos'

    scrapedtitlet = '\\1'
    htmlt = '\\2'
    extra = 'episodeHTML'
    if isinstance(epre, dict):
        if 'regx' in epre: patron = epre['regx']
        if 'title' in epre: scrapedtitlet = epre['title']
        if 'url' in epre: htmlt = epre['url']
        if 'extra' in epre: extra = epre['extra']
        if 'action' in epre: action = epre['action']
    else:
        patron = epre

    if season_title:
        itemlist.append(build_item(title=season_title))

    matches = re.compile(patron).findall(data)
    for match in matches:
        scrapedtitle = scrapedtitlet
        html = htmlt
        for m in range(0, len(match)):
            html = html.replace('\\%s' % (m + 1), match[m])
            scrapedtitle = scrapedtitle.replace('\\%s' % (m + 1), match[m])
        scrapedtitle = scrapertools.htmlclean(scrapertools.decodeHtmlentities(scrapedtitle)).replace(";", "")
        if scrapedtitle[-1] == '-': scrapedtitle = scrapedtitle[:-1]
        logger.info('%s - %s' % (scrapedtitle, html))
        itemlist.append(build_ep_item(title=scrapedtitle, url=html, action=action, extra=extra))

    return itemlist


def build_mov_item(title, url=None, action=None, thumbnail=None, extra=None):
    return build_item(title, url, action, thumbnail, 'movie', extra)


def build_ep_item(title=None, url=None, action=None, thumbnail=None, extra=None):
    i = build_item(title, url, action, thumbnail, 'episode', extra)
    i.show = i.title
    return i


def build_seas_item(title, url=None, action=None, thumbnail=None, extra=None):
    i = build_item(title, url, action, thumbnail, 'season', extra)
    i.show = i.title
    return i


def build_item(title, url=None, action=None, thumbnail=None, content='', extra=''):
    logger.info('[build_item] from channel %s with content %s' % (__channel__, content))
    try:
        i = Item(channel=__channel__,
                 title=title,
                 fulltitle=title)
        if url: i.url = url
        if thumbnail: i.thumbnail = thumbnail
        if content: i.contentType = content
        if 'episod' not in extra: i.contentType = 'list'
        if action:
            i.action = action
        else:
            i.contentType = 'list'
        if extra: i.extra = extra
    except:
        logger.debug('Error in build_item')
        return None

    return i
