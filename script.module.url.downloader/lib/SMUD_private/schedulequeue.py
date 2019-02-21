# -*- coding: utf-8 -*-
import util
import xbmc, xbmcaddon, xbmcvfs
import os, json, time, binascii

def _downloading():
    return xbmc.getInfoLabel('Window(10000).Property(service.url.downloader.DOWNLOAD_STATUS)') == 'ACTIVE'

def isDownloading(item=None):
    if item == None: return _downloading()
    return xbmc.getInfoLabel('Window(10000).Property(service.url.downloader.DOWNLOAD_ID)') == str(item.ID)

class Download(dict):
    _udType = 'DOWNLOAD'

    def __init__(self,*args,**kwargs):
        self['ID'] = time.time()
        dict.__init__(self,*args,**kwargs)

    def __getattr__(self,name):
        return self.get(name)

    def __setattr__(self, name, value):
        self[name] = value

    @classmethod
    def deSerialize(cls,serial_data):
        new = cls(json.loads(binascii.unhexlify(serial_data)))
        if 'start' in new: return ScheduleItem(new)
        return new

    def serialize(self):
        return binascii.hexlify(json.dumps(self))

    @property
    def path(self):
        if self.finalExists():
            return self.final
        elif self.tempExists():
            return self.temp
        else:
            return self.partExists()

    def partExists(self):
        if self.finalExists(part=True):
            return self.final + '.part'
        elif self.tempExists(part=True):
            return self.temp + '.part'

        return False

    def initialForWrite(self):
        if self.direct: return self._finalForWrite()
        return self.temp

    def _finalForWrite(self):
        final,ext = os.path.splitext(self.final)
        ct=1
        while self.finalExists():
            ct+=1
            self.final = final + u'-' + str(ct) + ext
        if ct > 1:
            self.display += u' ({0})'.format(ct)
            self.onUpdate()
        return self.final

    def onDownloadComplete(self):
        if not self.direct:
            try:
                xbmcvfs.copy(self.temp,self._finalForWrite())
                os.remove(self.temp)
            except:
                util.ERROR()

    def onUpdate(self):
        if self.callback:
            xbmc.executebuiltin(self.callback.format(download=self.serialize()))

    def exists(self):
        return self.finalExists() or self.tempExists() or self.partExists()

    def clean(self):
        if self.isDownloading(): return False
        try:
            if self.tempExists: xbmcvfs.delete(self.temp)
            if self.finalExists: xbmcvfs.delete(self.final)
            return True
        except:
            util.ERROR()
        return False

    def isDownloading(self):
        return isDownloading(self)

    def tempExists(self, part=False):
        return xbmcvfs.exists(self['temp'] + (part and '.part' or ''))

    def finalExists(self, part=False):
        return xbmcvfs.exists(self['final'] + (part and '.part' or ''))

class ScheduleItem(Download):
    _udType = 'SCHEDULE_ITEM'

    @classmethod
    def _deSerialize(cls,data):
        return cls(json.loads(data))

    def _serialize(self):
        return json.dumps(self)

    @property
    def nextTime(self): #TODO: Implement day(s) of week scheduling
        return self.start

    @property
    def offset_time(self):
        return self.offset

    @property
    def end(self):
        return self.nextTime + (self['minutes'] * 60)

    @property
    def repeats(self): #TODO: Implement stuff here
        return False

    @property
    def minutes(self):
        if not self.isScheduledNow(): return self['minutes']
        return self['minutes'] - int((time.time() - self.start)/60)

    def isScheduledNow(self):
        now = time.time()
        return self.nextTime <= now < self.end

    def isOld(self):
        if self.repeats: return False
        if self.end < time.time(): return True
        return False

    def minutesUntilNextTime(self):
        diff = time.time() + (self.offset_time * 60)
        return int((self.nextTime - diff)/60)

class ScheduleQueue(object):
    _filepath = os.path.join(xbmc.translatePath(xbmcaddon.Addon('service.url.downloader').getAddonInfo('profile')).decode('utf-8'),'schedulequeue')

    def __init__(self):
        self.loadItems()

    def __enter__(self):
        return self

    def __exit__(self,exc_type,exc_value,traceback):
        self.close()

    def loadItems(self):
        self._items = []
        if not os.path.exists(self._filepath): return
        with open(self._filepath,'r') as f:
            for line in f:
                item = ScheduleItem._deSerialize(line)
                if not item.isOld(): self._items.append(item)

    def saveItems(self):
        with open(self._filepath,'w') as f:
            for i in self._items:
                f.writelines([i._serialize() + '\n'])

    def close(self):
        self.saveItems()

    def append(self,item):
        self._items.append(item)

    def add(self,item):
        for i in self._items:
            if i.start == item.start: return False
        self.append(item)
        return True

    def remove(self,item):
        for idx, i in enumerate(self._items):
            if i.ID == item.ID:
                return self._items.pop(idx)

    def removeIfNoRepeat(self,item):
        if item.repeats: return
        self.remove(item)

    def getNext(self):
        if not self._items: return None
        lowest = self._items[0]
        for i in self._items:
            if i.nextTime < lowest.nextTime:
                lowest = i
        return lowest

    def takeNext(self):
        item = None
        while not item:
            item = self.getNext()
            if not item: return None
            if not item.repeats: self.remove(item)
            if not item.isOld(): return item
            item = None
