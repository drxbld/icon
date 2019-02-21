# -*- coding: iso-8859-1 -*-
# ------------------------------------------------------------
# streamondemand - XBMC Plugin
# Conector para streamango
# http://www.mimediacenter.info/foro/viewforum.php?f=36
# by DrZ3r0
# ------------------------------------------------------------

import re
import urllib

from core import logger
from core import scrapertools


def get_video_url(page_url, premium=False, user="", password="", video_password=""):
    logger.info("url=" + page_url)
    video_urls = []

    headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 7_0_2 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11A501 Safari/9537.53'}

    data = scrapertools.cache_page(page_url, headers=headers)

    headers['Referer'] = page_url
    headers = urllib.urlencode(headers)

    matches = scrapertools.find_multiple_matches(data, r'{type:"video/mp4",src:"([^"]+)",height:([^,]+),')
    for media_url, vtype in matches:
        if media_url.startswith("//"):
            media_url = "http:%s" % media_url
        video_urls.append([vtype + " [streamango]", media_url + '|' + headers])

    return video_urls


# Encuentra videos de este servidor en el texto pasado
def find_videos(text):
    encontrados = set()
    devuelve = []

    patronvideos = '(?://|\.)streamango\.com/(?:f/|embed/)?([0-9a-zA-Z]+)'
    logger.info("find_videos #" + patronvideos + "#")
    matches = re.compile(patronvideos, re.DOTALL).findall(text)

    for match in matches:
        titulo = "[streamango]"
        url = "http://streamango.com/embed/%s" % match
        if url not in encontrados:
            logger.info("url=" + url)
            devuelve.append([titulo, url, 'streamango'])
            encontrados.add(url)
        else:
            logger.info("url duplicada=" + url)

    return devuelve
