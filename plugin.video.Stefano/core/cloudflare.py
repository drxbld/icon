# -*- coding: utf-8 -*-
# ------------------------------------------------------------
# pelisalacarta 4
# Copyright 2015 tvalacarta@gmail.com
# http://blog.tvalacarta.info/plugin-xbmc/pelisalacarta/
#
# Distributed under the terms of GNU General Public License v3 (GPLv3)
# http://www.gnu.org/licenses/gpl-3.0.html
# ------------------------------------------------------------
# This file is part of pelisalacarta 4.
#
# pelisalacarta 4 is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# pelisalacarta 4 is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with pelisalacarta 4.  If not, see <http://www.gnu.org/licenses/>.
# --------------------------------------------------------------------------------
# Cloudflare decoder
# --------------------------------------------------------------------------------

import re
import urllib
import urlparse

import xbmc

from core import logger


class Cloudflare:
    def __init__(self, response):
        self.timeout = 5
        self.domain = urlparse.urlparse(response["url"])[1]
        self.protocol = urlparse.urlparse(response["url"])[0]
        self.js_data = {}
        self.header_data = {}

        if "var s,t,o,p,b,r,e,a,k,i,n,g,f" not in response["data"] or "chk_jschl" in response["url"]:
            return

        try:
            self.js_data["auth_url"] = \
                re.compile('<form id="challenge-form" action="([^"]+)" method="get">').findall(response["data"])[0]
            self.js_data["params"] = {}
            self.js_data["params"]["jschl_vc"] = \
                re.compile('<input type="hidden" name="jschl_vc" value="([^"]+)"/>').findall(response["data"])[0]
            self.js_data["params"]["pass"] = \
                re.compile('<input type="hidden" name="pass" value="([^"]+)"/>').findall(response["data"])[0]
            var, self.js_data["value"] = \
                re.compile('var s,t,o,p,b,r,e,a,k,i,n,g,f[^:]+"([^"]+)":([^\n]+)};', re.DOTALL).findall(
                    response["data"])[0]
            self.js_data["op"] = re.compile(var + "([\+|\-|\*|\/])=([^;]+)", re.MULTILINE).findall(response["data"])
            self.js_data["wait"] = int(re.compile("\}, ([\d]+)\);", re.MULTILINE).findall(response["data"])[0]) / 1000
        except:
            logger.debug("Metodo #1 (javascript): NO disponible")
            self.js_data = {}

        if "refresh" in response["headers"]:
            try:
                self.header_data["wait"] = int(response["headers"]["refresh"].split(";")[0])
                self.header_data["auth_url"] = response["headers"]["refresh"].split("=")[1].split("?")[0]
                self.header_data["params"] = {}
                self.header_data["params"]["pass"] = response["headers"]["refresh"].split("=")[2]
            except:
                logger.debug("Metodo #2 (headers): NO disponible")
                self.header_data = {}

    @property
    def wait_time(self):
        if self.js_data.get("wait", 0):
            return self.js_data["wait"]
        else:
            return self.header_data.get("wait", 0)

    @property
    def is_cloudflare(self):
        return self.header_data.get("wait", 0) > 0 or self.js_data.get("wait", 0) > 0

    def get_url(self):
        # Metodo #1 (javascript)
        if self.js_data.get("wait", 0):
            jschl_answer = self.decode(self.js_data["value"])

            for op, v in self.js_data["op"]:
                jschl_answer = eval(str(jschl_answer) + op + str(self.decode(v)))

            self.js_data["params"]["jschl_answer"] = jschl_answer + len(self.domain)

            response = "%s://%s%s?%s" % (
                self.protocol, self.domain, self.js_data["auth_url"], urllib.urlencode(self.js_data["params"]))

            xbmc.sleep(self.js_data["wait"] * 1000)

            return response

        # Metodo #2 (headers)
        if self.header_data.get("wait", 0):
            response = "%s://%s%s?%s" % (
                self.protocol, self.domain, self.header_data["auth_url"], urllib.urlencode(self.header_data["params"]))

            xbmc.sleep(self.header_data["wait"] * 1000)

            return response

    def decode(self, s):
        i = s.find('/')
        if i > 0:
            return self.decode(s[:i]) / self.decode(s[i + 1:])
        i = s.find('*')
        if i > 0:
            return self.decode(s[:i]) * self.decode(s[i + 1:])
        offset = 1 if s[0] == '+' else 0
        val = float(eval(s.replace('!+[]', '1').replace('!![]', '1').replace('[]', '0').replace('(', 'str(')[offset:]))
        return val
