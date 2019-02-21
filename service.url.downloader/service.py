# -*- coding: utf-8 -*-
import xbmc
from SMUD_private import servicecontrol, schedulequeue
from lib import util
# from lib import rtmp
from  lib import hls, rtmp

class DownloadHandler:
    def __init__(self):
        self.downloader = None

    @property
    def active(self):
        return self.downloader and self.downloader.active

    def download(self,download=None,debug=False):
        download = schedulequeue.Download.deSerialize(download)
        self._download(download=download,debug=debug)

    def _download(self,download=None,debug=False):
        if not download: return
        if download['url'].startswith('rtmp'):
            self.downloader = rtmp.Downloader(download,debug=util.DEBUG())
        else:
            self.downloader = hls.Downloader(download,debug=util.DEBUG())
        self.downloader.startThreaded()

    def stopDownload(self):
        if self.downloader:
            self.downloader.stop()
            util.LOG('Downloader Finished')
        self.downloader = None

def waitForAbort(sec_float=0):
    if sec_float:
        ms = sec_float * 1000
        ct=0
        while not xbmc.abortRequested and ct < ms:
            xbmc.sleep(100)
            ct+=100
    else:
        while not xbmc.abortRequested:
            xbmc.sleep(100)

class DownloaderService(xbmc.Monitor):
    def __init__(self):
        self.downloader = DownloadHandler()
        self.timerItem = None
        if not hasattr(self,'waitForAbort'): self.waitForAbort = waitForAbort #For pre-Helix
        self.setVersion()
        self.service()

    def setVersion(self):
        import xbmcgui
        xbmcgui.Window(10000).setProperty('service.url.downloader.VERSION',util.ADDON.getAddonInfo('version'))

    def service(self):
        util.LOG("SERVICE: STARTED")
        self.checkSchedule()
        self.waitForAbort()
        util.LOG("SERVICE: SHUTTING DOWN...")
        self.downloader.stopDownload()
        util.LOG("SERVICE: FINISHED")

    def onNotification(self, sender, method, data):
        if not sender == 'service.url.downloader': return
        self.processCommand(method.split('.',1)[-1],servicecontrol.processCommandData(data)) #Remove the "Other." prefix

    def processCommand(self,command,args):
        if command == 'DOWNLOAD':
            self.downloader.download(**args)
        elif command == 'DOWNLOAD_STOP':
            self.downloader.stopDownload()
        elif command == 'SCHEDULE':
            self.schedule(**args)
        elif command == 'ON_DOWNLOAD_FINISHED':
            self.onDownloadFinished(**args)
        elif command == 'ON_TIMEOUT':
            self.onTimeout()
        elif command == 'RESET':
            self.reset()

    def schedule(self,item=None):
        item = schedulequeue.ScheduleItem.deSerialize(item)
        with schedulequeue.ScheduleQueue() as sched:
            if not sched.add(item): return
        self.reset()
        self.checkSchedule()

    def reset(self):
        self.cancelTimer()
        self.checkSchedule()

    def onDownloadFinished(self,ID=None):
        self.checkSchedule()

    def checkSchedule(self):
        if self.downloader.active: return
        if self.timerItem: return
        with schedulequeue.ScheduleQueue() as sched:
            item = sched.getNext()
            if not item: return
            if item.isScheduledNow():
                self.downloader._download(download=item)
                sched.removeIfNoRepeat(item)
            else:
                self.setTimer(item)

    def onTimeout(self):
        if self.downloader.active: return
        self.downloader._download(download=self.timerItem)
        with schedulequeue.ScheduleQueue() as sched:
            sched.removeIfNoRepeat(self.timerItem)
        self.timerItem = None

    def cancelTimer(self):
        self.timerItem = None
        xbmc.executebuiltin('CancelAlarm(service.url.downloader.SCHEDULE,true)')

    def setTimer(self,item):
        self.cancelTimer()
        command = '"XBMC.NotifyAll(service.url.downloader,ON_TIMEOUT)"'
        timeout = item.minutesUntilNextTime()
        self.timerItem = item
        xbmc.executebuiltin('AlarmClock(service.url.downloader.TIMER,{0},{1},true)'.format(command,timeout))
        util.LOG('Download scheduled for {0} minutes from now'.format(timeout))

DownloaderService()
