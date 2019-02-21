# -*- coding: iso-8859-1 -*-
# ------------------------------------------------------------
# streamondemand - XBMC Plugin
# Conector para streamango
# http://www.mimediacenter.info/foro/viewforum.php?f=36
# by DrZ3r0
# ------------------------------------------------------------

import re
import urllib


from core import httptools, logger, scrapertools


def test_video_exists(page_url):
    logger.info("(page_url='%s')" % page_url)

    data = httptools.downloadpage(page_url).data
    if "We are unable to find the video" in data:
        return False, "[streamango] Il file non esiste o è stato cancellato"

    return True, ""


def get_video_url(page_url,
                  premium=False,
                  user="",
                  password="",
                  video_password=""):
    logger.info("(page_url='%s')" % page_url)

    data = httptools.downloadpage(page_url).data

    video_urls = []

    matches = scrapertools.find_multiple_matches(
        data,
        "type:\"video/([^\"]+)\",src:d\('([^']+)',(.*?)\).+?height:(\d+)")

    for ext, encoded, code, quality in matches:

        media_url = decode(encoded, int(code))

        while media_url[-1] == '@':
            media_url = media_url[:-1]

        if not media_url.startswith("http"):
            media_url = "http:" + media_url
        video_urls.append([".%s %sp [streamango]" % (ext, quality), media_url])

    video_urls.reverse()
    for video_url in video_urls:
        logger.info("%s - %s" % (video_url[0], video_url[1]))

    return video_urls


def decode(encoded, code):
    logger.info("encoded '%s', code '%s'" % (encoded, code))

    _0x59b81a = ""
    k = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/='
    k = k[::-1]

    count = 0
    while count < len(encoded):
        _0x4a2f3a = k.index(encoded[count])
        count += 1
        _0x29d5bf = k.index(encoded[count])
        count += 1
        _0x3b6833 = k.index(encoded[count])
        count += 1
        _0x426d70 = k.index(encoded[count])
        count += 1

        _0x2e4782 = ((_0x4a2f3a << 2) | (_0x29d5bf >> 4))
        _0x2c0540 = (((_0x29d5bf & 15) << 4) | (_0x3b6833 >> 2))
        _0x5a46ef = ((_0x3b6833 & 3) << 6) | _0x426d70
        _0x2e4782 = _0x2e4782 ^ code

        _0x59b81a = str(_0x59b81a) + chr(_0x2e4782)

        if _0x3b6833 != 64:
            _0x59b81a = str(_0x59b81a) + chr(_0x2c0540)
        if _0x3b6833 != 64:
            _0x59b81a = str(_0x59b81a) + chr(_0x5a46ef)

    return _0x59b81a



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
