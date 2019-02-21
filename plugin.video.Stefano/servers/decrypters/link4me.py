# -*- coding: utf-8 -*-
# StreamOnDemand Community Edition - Kodi Addon

import urllib

from core import httptools, scrapertools, logger


def get_long_url(short_url, referer):
    logger.info("short_url = '%s'" % short_url)

    _headers = dict()
    _headers['Referer'] = referer

    html = httptools.downloadpage(short_url, headers=_headers, cookies=False).data

    _csrfToken = scrapertools.find_single_match(html, 'name="_csrfToken" value="([^"]+)"')
    alias = scrapertools.find_single_match(html, 'name="alias" value="([^"]+)"')
    ci = scrapertools.find_single_match(html, 'name="ci" value="([^"]+)"')
    cui = scrapertools.find_single_match(html, 'name="cui" value="([^"]+)"')
    cii = scrapertools.find_single_match(html, 'name="cii" value="([^"]+)"')
    country = scrapertools.find_single_match(html, 'name="country" value="([^"]+)"')
    ct = scrapertools.find_single_match(html, 'name="ct" value="([^"]+)"')
    dh = scrapertools.find_single_match(html, 'name="dh" value="([^"]+)"')
    _Tokenfields = scrapertools.find_single_match(html, 'name="_Token\[fields\]" value="([^"]+)"')
    _Tokenunlocked = scrapertools.find_single_match(html, 'name="_Token\[unlocked\]" value="([^"]+)"')

    post_data = dict()
    post_data['_method'] = 'POST'
    post_data['_csrfToken'] = _csrfToken
    post_data['alias'] = alias
    post_data['ci'] = ci
    post_data['cui'] = cui
    post_data['cii'] = cii
    post_data['ref'] = referer
    post_data['country'] = country
    post_data['ct'] = ct
    post_data['dh'] = dh
    post_data['adsnetwork1'] = 'popads'
    post_data['adsnetwork2'] = scrapertools.find_single_match(html, r"parse:function\(e\){\s*var url = '([^']+)';")
    post_data['_Token[fields]'] = _Tokenfields
    post_data['_Token[unlocked]'] = _Tokenunlocked
    post_data = urllib.urlencode(post_data)

    _headers['Referer'] = short_url
    _headers['X-Requested-With'] = 'XMLHttpRequest'
    _headers['Accept'] = 'application/json, text/javascript, */*; q=0.01'
    _headers['Cookie'] = 'csrfToken=%s' % _csrfToken

    data = httptools.downloadpage(
        'http://link4.me/links/go',
        post=post_data,
        headers=_headers,
        cookies=False).data

    return scrapertools.find_single_match(data, '"url":"([^"]+?)"').replace('\/', '/')
