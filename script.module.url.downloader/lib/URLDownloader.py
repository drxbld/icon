# -*- coding: utf-8 -*-
import os, time
from SMUD_private import servicecontrol
from SMUD_private import util
from SMUD_private.schedulequeue import isDownloading, Download, ScheduleItem, ScheduleQueue #@analysis:ignore


def download(url,download_path,filename,display,minutes=0,direct=False,callback=None):
    ID = int(time.time())
    tmpPath = os.path.join(util.PROFILE,'tmp_{0}.mp4'.format(ID))
    if filename[-4:].lower() != '.mp4':
            util.DEBUG_LOG("Adding .mp4 to filename")
            filename += ".mp4"
    finalPath = os.path.join(download_path,filename)
    download = Download({'ID':ID,'display':display,'temp':tmpPath,'final':finalPath,'minutes':minutes,'url':url,'direct':direct,'callback':callback})
    servicecontrol.sendCommand('DOWNLOAD',download=download.serialize())

    return download

def canDownload():
    return not isDownloading()

def stopDownloading():
    servicecontrol.sendCommand('DOWNLOAD_STOP')

def schedule(item):
    tmpPath = os.path.join(util.PROFILE,'tmp_{0}.mp4'.format(item.ID))
    filename = item.filename
    if filename[-4:].lower() != '.mp4':
            util.DEBUG_LOG("Adding .mp4 to filename")
            filename += ".mp4"
    finalPath = os.path.join(item.targetPath,filename)
    item.temp = tmpPath
    item.final = finalPath    
    servicecontrol.sendCommand('SCHEDULE',item=item.serialize())

def unSchedule(item):
    with ScheduleQueue() as sq:
        sq.remove(item)
    servicecontrol.sendCommand('RESET')

def scheduledItems():
    return ScheduleQueue()._items