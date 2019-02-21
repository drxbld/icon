import os
import time
import urllib2
import threading
import xbmc
import xbmcgui
from lib import util
from SMUD_private import servicecontrol

import compat
import hls
import fake


class Downloader(fake.FakeYDL):
    def __init__(self, download, direct=True, debug=False):
        self.active = True
        self._active = True
        self._download = download
        self._currDest = download.initialForWrite()
        self._debug = debug
        self._startTime = time.time()
        self._totalTime = download.minutes * 60
        self._stopTime = self._startTime + self._totalTime
        self._progressDialog = xbmcgui.DialogProgressBG()
        self._freeSpace = util.freeSpaceString(os.path.dirname(self._currDest))
        self._bytes = 0
        self._lastSecond = int(time.time())
        self._checkCounter = 0
        self._display = u'{0}%   {1} left    -    {2}   {3}/s    {4}'
        self._heading = u'SS Recording: {0}'.format(download.display)
        self._thread = None
        self._progressDialog.create(self._heading,'Initializing...')

    def _updateProgress(self):
        now = time.time()
        int_now = int(now)
        if int_now == self._lastSecond: return
        self._checkCounter+=1
        if self._checkCounter > 29:
            self._checkCounter = 0
            self._freeSpace = util.freeSpaceString(self._currDest)
        sofar = max(now - self._startTime,1) #So far or 1 to prevent div by 0
        pct = int((sofar / self._totalTime) * 100)
        size = util.simpleSize(self._bytes)
        left = util.durationToShortText(self._totalTime - sofar)
        speed = util.simpleSize(int(self._bytes/sofar))
        self._lastSecond = int_now
        self._progressDialog.update(pct,self._heading,self._display.format(pct, left, size, speed, self._freeSpace))

    def handleMessage(self, message, skip_eol=False):
        # self._progressDialog.update(0, 'Downloading', message)
        if not skip_eol:
            util.DEBUG_LOG(message)

    def progressHook(self, state):
        self._bytes = state.get('downloaded_bytes', 0)
        self._updateProgress()

    def download(self):
        path = "special://userdata/addon_data/script.smoothstreams-v3/hash"
        path = xbmc.translatePath(path)
        if os.path.exists(path):    os.remove(path)
        xbmc.executebuiltin("RunScript(script.smoothstreams-v3,REFRESH_HASH)")
        url = self._download.url
        xbmc.log(url,2)
        try:
            while 1:
                if os.path.exists(path):    break
                xbmc.sleep(100)
            with open(path,'r') as f:
                hash = f.read()
                url = url.split('wmsAuthSign=')[0] + "wmsAuthSign=" + hash
        except Exception as e:
            xbmc.log(str(e),2)
        xbmc.log(url,2)
        m3u8 = urllib2.urlopen(url).read()
        #m3u8 = urllib2.urlopen(self._download.url).read()
        url = compat.compat_urlparse.urljoin(self._download.url, m3u8.strip().splitlines()[-1])

        fd = hls.HlsFD(self, {})
        fd.add_progress_hook(self.progressHook)

        self._startTime = time.time() #Set _start_time after first message for better speed avg

        fd.real_download(self._currDest, {'url': url, 'is_live': True, 'id': '1'})
        

    def shouldStop(self):
        return not self._active or xbmc.abortRequested or time.time() >= self._stopTime
        # self._updateProgress()


    @staticmethod
    def _getStatus():
        return xbmc.getInfoLabel('Window(10000).Property(service.url.downloader.DOWNLOAD_STATUS)')

    @staticmethod
    def _setStatus(value):
        xbmcgui.Window(10000).setProperty('service.url.downloader.DOWNLOAD_STATUS',value)

    @staticmethod
    def _setDownloadID(ID):
        xbmcgui.Window(10000).setProperty('service.url.downloader.DOWNLOAD_ID',str(ID))

    def _done(self):
        self.active = False
        servicecontrol.sendCommand('ON_DOWNLOAD_FINISHED',ID=self._download.ID)

    def start(self):
        self._setDownloadID(self._download.ID)
        try:
            util.LOG('HLS Download started')
            self._setStatus('ACTIVE')
            self.download()
        except:
            e = util.ERROR()
            util.LOG('HLS Download stopped: {0}'.format(e))
        finally:
            self._progressDialog.update(100, self._heading, 'Finishing...')
            self._download.onDownloadComplete()
            self._done()
            self._setDownloadID('')
            self._setStatus('')
            self._progressDialog.close()

    def startThreaded(self):
        self._thread = threading.Thread(target=self.start,name='HLS_Download')
        self._thread.start()

    def stop(self):
        self._active = False
        if self._thread: self._thread.join()
        self._thread = None

    @classmethod
    def downloading(cls):
        return cls._getStatus() == 'ACTIVE'