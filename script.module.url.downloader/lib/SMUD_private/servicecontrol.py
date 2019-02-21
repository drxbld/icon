# -*- coding: utf-8 -*-
import xbmc
import binascii
import json

BASE_COMMAND = 'XBMC.NotifyAll(service.url.downloader,{0},"{{{1}}}")'
BASE_ARG = '\\"{0}\\":\\"{1}\\"'

def safeEncode(text):
    return binascii.hexlify(json.dumps(text))

def safeDecode(enc_text):
    return json.loads(binascii.unhexlify(enc_text))

def sendCommand(command,**kwargs):
    args = []
    for k,v in kwargs.items():
        args.append(BASE_ARG.format(k,safeEncode(v)))
    command = BASE_COMMAND.format(command,','.join(args))
    xbmc.executebuiltin(command)

def processCommandData(data):
    args = json.loads(data)
    if not args: return []
    for k in args.keys():
        v = args[k]
        args[k] = safeDecode(v)
    return args
