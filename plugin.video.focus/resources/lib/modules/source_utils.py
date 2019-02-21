# -*- coding: utf-8 -*-

"""
    focus Add-on
    Copyright (C) 2016 focus

    
"""

import base64
import urlparse
import urllib
import hashlib
import re

from resources.lib.modules import client
from resources.lib.modules import trakt
from resources.lib.modules import pyaes


def is_anime(content, type, type_id):
    try:
        r = trakt.getGenre(content, type, type_id)
        return 'anime' in r or 'animation' in r
    except:
        return False


def get_release_quality(release_name):
    if release_name is None: return
    try: release_name = release_name.encode('utf-8')
    except: pass

    try:
        release_name = release_name.upper()

        fmt = re.sub('(.+)(\.|\(|\[|\s)(\d{4}|S\d*E\d*|S\d*)(\.|\)|\]|\s)', '', release_name)
        fmt = re.split('\.|\(|\)|\[|\]|\s|-', fmt)
        fmt = [i.lower() for i in fmt]

        if '1080p' in fmt: quality = '1080p'
        elif '720p' in fmt: quality = 'HD'
        else: quality = 'SD'
        if any(i in ['dvdscr', 'r5', 'r6'] for i in fmt): quality = 'SCR'
        elif any(i in ['camrip', 'tsrip', 'hdcam', 'hdts', 'dvdcam', 'dvdts', 'cam', 'telesync', 'ts'] for i in fmt): quality = 'CAM'

        info = []
        if '3d' in fmt or '.3D.' in release_name: info.append('3D')
        if any(i in ['hevc', 'h265', 'x265'] for i in fmt): info.append('HEVC')

        return quality, info
    except:
        return 'SD', []

def getFileType(url):

    try: url = url.lower()
    except: url = str(url)
    type = ''
    
    if 'bluray' in url: type += ' BLURAY /'
    if '.web-dl' in url: type += ' WEB-DL /'
    if '.web.' in url: type += ' WEB-DL /'
    if 'hdrip' in url: type += ' HDRip /'
    if 'bd-r' in url: type += ' BD-R /'
    if 'bd-rip' in url: type += ' BD-RIP /'
    if 'bd.r' in url: type += ' BD-R /'
    if 'bd.rip' in url: type += ' BD-RIP /'
    if 'bdr' in url: type += ' BD-R /'
    if 'bdrip' in url: type += ' BD-RIP /'
    if 'atmos' in url: type += ' ATMOS /'
    if 'truehd' in url: type += ' TRUEHD /'
    if '.dd' in url: type += ' DolbyDigital /'
    if '5.1' in url: type += ' 5.1 /'
    if '.xvid' in url: type += ' XVID /'
    if '.mp4' in url: type += ' MP4 /'
    if '.avi' in url: type += ' AVI /'
    if 'ac3' in url: type += ' AC3 /'
    if 'h.264' in url: type += ' H.264 /'
    if '.x264' in url: type += ' x264 /'
    if '.x265' in url: type += ' x265 /'
    if 'subs' in url: 
        if type != '': type += ' - WITH SUBS'
        else: type = 'SUBS'
    type = type.rstrip('/')
    return type

def check_sd_url(release_link):

    try:
        release_link = release_link.lower()
        if '1080' in release_link: quality = '1080p'
        elif '720' in release_link: quality = '720p'
        elif '.hd.' in release_link: quality = '720p'
        elif any(i in ['dvdscr', 'r5', 'r6'] for i in release_link): quality = 'SCR'
        elif any(i in ['camrip', 'tsrip', 'hdcam', 'hdts', 'dvdcam', 'dvdts', 'cam', 'telesync', 'ts'] for i in release_link): quality = 'CAM'
        else: quality = 'SD'
        return quality
    except:
        return 'SD'

def label_to_quality(label):
    try:
        try: label = int(re.search('(\d+)', label).group(1))
        except: label = 0

        if label >= 2160:
            return '4K'
        elif label >= 1440:
            return '1440p'
        elif label >= 1080:
            return '1080p'
        elif 720 <= label < 1080:
            return 'HD'
        elif label < 720:
            return 'SD'
    except:
        return 'SD'


def strip_domain(url):
    try:
        if url.lower().startswith('http') or url.startswith('/'):
            url = re.findall('(?://.+?|)(/.+)', url)[0]
        url = client.replaceHTMLCodes(url)
        url = url.encode('utf-8')
        return url
    except:
        return


def is_host_valid(url, domains):
    try:
        host = __top_domain(url)
        hosts = [domain.lower() for domain in domains if host and host in domain.lower()]
        if hosts and '.' not in host:
            host = hosts[0]
        if hosts and any([h for h in ['google', 'picasa', 'blogspot'] if h in host]):
            host = 'gvideo'
        return any(hosts), host
    except:
        return False, ''


def __top_domain(url):
    elements = urlparse.urlparse(url)
    domain = elements.netloc or elements.path
    domain = domain.split('@')[-1].split(':')[0]
    regex = "(?:www\.)?([\w\-]*\.[\w\-]{2,3}(?:\.[\w\-]{2,3})?)$"
    res = re.search(regex, domain)
    if res: domain = res.group(1)
    domain = domain.lower()
    return domain


def aliases_to_array(aliases, filter=None):
    try:
        if not filter:
            filter = []
        if isinstance(filter, str):
            filter = [filter]

        return [x.get('title') for x in aliases if not filter or x.get('country') in filter]
    except:
        return []


def append_headers(headers):
        return '|%s' % '&'.join(['%s=%s' % (key, urllib.quote_plus(headers[key])) for key in headers])

	def get_size(url):
    try:
        size = client.request(url, output='file_size')
        if size == '0': size = False
        size = convert_size(size)
        return size
    except: return False

def convert_size(size_bytes):
   import math
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   if size_name[i] == 'B' or size_name[i] == 'KB': return None
   return "%s %s" % (s, size_name[i])
   
def check_directstreams(url, hoster='', quality='SD'):
    urls = []
    host = hoster

    if 'google' in url or any(x in url for x in ['youtube.', 'docid=']):
        urls = directstream.google(url)
        if not urls:
            tag = directstream.googletag(url)
            if tag: urls = [{'quality': tag[0]['quality'], 'url': url}]
        if urls: host = 'gvideo'
    elif 'ok.ru' in url:
        urls = directstream.odnoklassniki(url)
        if urls: host = 'vk'
    elif 'vk.com' in url:
        urls = directstream.vk(url)
        if urls: host = 'vk'
    elif any(x in url for x in ['akamaized', 'blogspot', 'ocloud.stream']):
        urls = [{'url': url}]
        if urls: host = 'CDN'
        
    direct = True if urls else False

    if not urls: urls = [{'quality': quality, 'url': url}]

    return urls, host, direct


# if salt is provided, it should be string
# ciphertext is base64 and passphrase is string
def evp_decode(cipher_text, passphrase, salt=None):
    cipher_text = base64.b64decode(cipher_text)
    if not salt:
        salt = cipher_text[8:16]
        cipher_text = cipher_text[16:]
    data = evpKDF(passphrase, salt)
    decrypter = pyaes.Decrypter(pyaes.AESModeOfOperationCBC(data['key'], data['iv']))
    plain_text = decrypter.feed(cipher_text)
    plain_text += decrypter.feed()
    return plain_text


def evpKDF(passwd, salt, key_size=8, iv_size=4, iterations=1, hash_algorithm="md5"):
    target_key_size = key_size + iv_size
    derived_bytes = ""
    number_of_derived_words = 0
    block = None
    hasher = hashlib.new(hash_algorithm)
    while number_of_derived_words < target_key_size:
        if block is not None:
            hasher.update(block)

        hasher.update(passwd)
        hasher.update(salt)
        block = hasher.digest()
        hasher = hashlib.new(hash_algorithm)

        for _i in range(1, iterations):
            hasher.update(block)
            block = hasher.digest()
            hasher = hashlib.new(hash_algorithm)

        derived_bytes += block[0: min(len(block), (target_key_size - number_of_derived_words) * 4)]

        number_of_derived_words += len(block) / 4

    return {
        "key": derived_bytes[0: key_size * 4],
        "iv": derived_bytes[key_size * 4:]
    }