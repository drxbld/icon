# -*- coding: utf-8 -*-

from lib import unshortenit


def expand_url(url):

    long_url, _ = unshortenit.unshorten_only(url)

    return long_url if long_url != url else ""
