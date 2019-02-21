import rtmpclient as client
import rtmp
import multitask
import threading
import xbmc, xbmcgui, xbmcvfs
import time, os, struct
from lib import util
from SMUD_private import servicecontrol

class vfsFile(xbmcvfs.File):
    def __init__(self,*args,**kwargs):
        xbmcvfs.File.__init__(self,*args,**kwargs)
        self._size = self.size() #size() returns size at open, so we need to keep track ourselves
        self._pos = 0

    def tell(self):
        return self._pos

    def read(self,nbytes=0):
        self._pos += nbytes
        if self._pos >= self._size or not nbytes: self._pos = self._size - 1
        xbmcvfs.File.read(self,nbytes)

    def write(self,data):
        self._pos += len(data)
        self._size = max(self._pos,self._size)
        xbmcvfs.File.write(self,data)

    def seek(self,offset,whence=0):
        if whence == 0:
            self._pos = 0
        elif whence == 2:
            self._pos = self._size - 1
        self._pos += offset
        xbmcvfs.File.seek(self,offset,whence)


class vfsFLV(rtmp.FLV):
    def open(self, path, type='read', mode=0775):
        '''Open the file for reading (type=read) or writing (type=record or append).'''
        if str(path).find('/../') >= 0 or str(path).find('\\..\\') >= 0: raise ValueError('Must not contain .. in name')
        if  util.DEBUG(): print 'opening file', path
        self.tsp = self.tsr = 0; self.tsr0 = None; self.type = type
        if type in ('record', 'append'):
            print path
            self.fp = vfsFile(path,('w' if type == 'record' else 'a')+'b')
            #self.fp = open(path, ('w' if type == 'record' else 'a')+'b')
            if type == 'record':
                self.fp.write('FLV\x01\x05\x00\x00\x00\x09\x00\x00\x00\x00') # the header and first previousTagSize
                self.writeDuration(0.0)
        else:
            self.fp = open(path, 'rb')
            magic, version, flags, offset = struct.unpack('!3sBBI', self.fp.read(9))
            if  util.DEBUG(): print 'FLV.open() hdr=', magic, version, flags, offset
            if magic != 'FLV': raise ValueError('This is not a FLV file')
            if version != 1: raise ValueError('Unsupported FLV file version')
            if offset > 9: self.fp.seek(offset-9, os.SEEK_CUR)
            self.fp.read(4) # ignore first previous tag size
        return self

class vfsFLVWriter(client.FLVWriter): # Write a vfs FLV file.
    def __init__(self):
        client.Resource.__init__(self)
        self.type = 'vfs_file'
        self.mode = 'w'

    def open(self, url):
        if util.DEBUG():
            print 'vfsFLVWriter.open {0}'.format(url)
        self.url = url
        self.fp = vfsFLV().open(url, 'record')
        yield # yield is needed since there is no other blocking operation.
        raise StopIteration, self if self.fp else None

def rtmpOpen(url, mode='r'):
    '''Open the given resource for read "r" or write "w" mode. Returns an object that has generator methods such as put(), get() and close().'''
    type = 'rtmp' if str(url).startswith('rtmp://') else 'http' if str(url).startswith('http://') else 'file'
    types = {'rtmp-r': client.RTMPReader, 'rtmp-w': client.RTMPWriter, 'http-r': client.HTTPReader, 'http-w': client.HTTPWriter, 'file-r': client.FLVReader, 'file-w': vfsFLVWriter }
    r = yield types[type + '-' + mode]().open(url=url)
    raise StopIteration, r

class Downloader(object):
    def __init__(self,download,direct=True,debug=False):
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
        client._debug = debug

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

    def _copy(self):
        '''Copy from given src url (str) to dest url (str).'''
        s  = yield client.open(self._download.url, 'r')
        if not s: raise client.Result, (False, 'Cannot open source %r'%(self._download.url))

        open_ = self._download.direct and rtmpOpen or client.open

        d = yield open_(self._currDest , 'w')
        if not d: yield s.close(); raise client.Result, (False, 'Cannot open destination %r'%(self._currDest))

        result = (True, 'Completed') # initialize the result
        try:
            msg = yield s.get()
            self._startTime = time.time() #Set _start_time after first message for better speed avg
            while msg and self._active and not xbmc.abortRequested and time.time() < self._stopTime:
                self._bytes += msg.size
                yield d.put(msg)
                self._updateProgress()
                msg = yield s.get()

        except client.Result, e:
            util.LOG('Download fail: {0}'.format(e))
            result = e
        finally:
            yield s.close()
            yield d.close()

        raise client.Result, result

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
            util.LOG('RTMP Download started')
            self._setStatus('ACTIVE')
            multitask.reset()
            multitask.add(self._copy())
            multitask.run()
        except client.Result, e:
            util.LOG('RTMP Download stopped: {0}'.format(e[1]))
            return e
        except:
            e = util.ERROR()
            util.LOG('RTMP Download stopped: {0}'.format(e))
        finally:
            self._progressDialog.update(100,self._heading, 'Finishing...')
            self._download.onDownloadComplete()
            self._done()
            self._setDownloadID('')
            self._setStatus('')
            self._progressDialog.close()

    def startThreaded(self):
        self._thread = threading.Thread(target=self.start,name='RTMP_Download')
        self._thread.start()

    def stop(self):
        self._active = False
        if self._thread: self._thread.join()
        self._thread = None

    @classmethod
    def downloading(cls):
        return cls._getStatus() == 'ACTIVE'

