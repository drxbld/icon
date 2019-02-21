# coding: UTF-8
import sys
l11l11l1_thegroove = sys.version_info [0] == 2
l1lll1lll_thegroove = 2048
l1ll1l11_thegroove = 7
def l11ll111_thegroove (l1111l_thegroove):
    global l1lll111l_thegroove
    l1l111l1_thegroove = ord (l1111l_thegroove [-1])
    l1111l11_thegroove = l1111l_thegroove [:-1]
    l1llll1l_thegroove = l1l111l1_thegroove % len (l1111l11_thegroove)
    l1lll11_thegroove = l1111l11_thegroove [:l1llll1l_thegroove] + l1111l11_thegroove [l1llll1l_thegroove:]
    if l11l11l1_thegroove:
        l1ll1l_thegroove = unicode () .join ([unichr (ord (char) - l1lll1lll_thegroove - (l1l11_thegroove + l1l111l1_thegroove) % l1ll1l11_thegroove) for l1l11_thegroove, char in enumerate (l1lll11_thegroove)])
    else:
        l1ll1l_thegroove = str () .join ([chr (ord (char) - l1lll1lll_thegroove - (l1l11_thegroove + l1l111l1_thegroove) % l1ll1l11_thegroove) for l1l11_thegroove, char in enumerate (l1lll11_thegroove)])
    return eval (l1ll1l_thegroove)
import base64
import hashlib
import json
import os
import urllib2
import sys
try:
    from Cryptodome import Random
    from Cryptodome.Cipher import AES
except:
    import resources.lib.stemodules.pyaes as pyaes
try:
    import xbmc
    import xbmcaddon
    import xbmcgui
except:
    pass
class l1l1l1ll1_thegroove:
    def __init__(self):
        self.name = l11ll111_thegroove (u"ࠢࡱ࡮ࡸ࡫࡮ࡴ࠮ࡷ࡫ࡧࡩࡴ࠴ࡓࡵࡧࡩࡥࡳࡵࠢࡳ")
        self.token = l11ll111_thegroove (u"ࠣࠤࡴ")
        self.l1l1lllll_thegroove = l11ll111_thegroove (u"ࠤ࠶࠷࠷࡙ࡅࡄࡔࡈࡘࡦࡨࡣ࠲࠴࠶࠸ࠧࡵ")
        self.l1ll1l111_thegroove = l11ll111_thegroove (u"ࠥࡗࡹ࡫ࡦࡢࡰࡲࠤ࡙࡮ࡥࡨࡴࡲࡳࡻ࡫ࠠ࠴࠸࠳ࠦࡶ")
        self.result = l11ll111_thegroove (u"ࠦࠧࡷ")
        self.l1l1l11ll_thegroove = 0
    def l1ll1l11l_thegroove(self):
        __caller__ = sys._getframe().f_back.f_code.co_name
        self.l1l11llll_thegroove(__caller__)
        content = urllib2.urlopen(l11ll111_thegroove (u"ࠧ࡮ࡴࡵࡲ࠽࠳࠴ࡽࡷࡸ࠰ࡶࡸࡪ࡬ࡡ࡯ࡱࡤࡨࡩࡵ࡮࠯࡫ࡱࡪࡴ࠵ࡔࡩࡧࡳࡥࡸࡺ࡯࠰ࡶ࡬ࡱࡪ࠴ࡰࡩࡲࠥࡸ")).read()
        l1l1l1l1l_thegroove = json.loads(str.encode(content, l11ll111_thegroove (u"ࠨࡵࡵࡨ࠰࠼ࠧࡹ")))
        l1l1ll11l_thegroove = l1l1l1l1l_thegroove[l11ll111_thegroove (u"ࠢࡵ࡫ࡰࡩࡸࡺࡡ࡮ࡲࠥࡺ")]
        l1l11l1ll_thegroove = int(l1l1ll11l_thegroove - int(l11ll111_thegroove (u"ࠣ࠶࠹࠸࠶࠶࠲࠲࠲࠳ࠦࡻ")))
        return l1l11l1ll_thegroove
    def l1l11lll1_thegroove(self, l1l11l1ll_thegroove):
        __caller__ = sys._getframe().f_back.f_code.co_name
        self.l1l11llll_thegroove(__caller__)
        try:
            __addon__ = xbmcaddon.Addon(id=self.name)
            cwd = xbmc.translatePath(__addon__.getAddonInfo(l11ll111_thegroove (u"ࠩࡳࡥࡹ࡮ࠧࡼ")))
        except:
            cwd = os.getcwd() + l11ll111_thegroove (u"ࠥ࠳ࡹ࡫ࡳࡵࠤࡽ")
        path = l11ll111_thegroove (u"ࠦࡷ࡫ࡳࡰࡷࡵࡧࡪࡹࠬ࡭࡫ࡥ࠰࡮ࡴࡤࡦࡺࡨࡶࡸ࠲ࡴࡩࡧࡪࡶࡴࡵࡶࡦ࠵࠹࠴࠳ࡶࡹࠣࡾ").split(l11ll111_thegroove (u"ࠧ࠲ࠢࡿ"))
        l1l1l1l11_thegroove = cwd + os.sep + os.path.join(*path)
        l1l1l1111_thegroove = len(open(l1l1l1l11_thegroove).read().splitlines())
        l1ll1111l_thegroove = l1l11l1ll_thegroove % l1l1l1111_thegroove
        self.l1l1l11ll_thegroove = l1ll1111l_thegroove
        line = self.l1ll11lll_thegroove(l1l1l1l11_thegroove, l1ll1111l_thegroove)
        return line
    @staticmethod
    def l1ll11lll_thegroove(l1l1ll1l1_thegroove, l1ll1111l_thegroove):
        try:
            with open(l1l1ll1l1_thegroove, l11ll111_thegroove (u"࠭ࡲࠨࢀ")) as f:
                for l1ll1lll1_thegroove, line in enumerate(f):
                    if l1ll1lll1_thegroove == l1ll1111l_thegroove:
                        return str(line)
        except Exception as e:
            print(l11ll111_thegroove (u"ࠧࡆࡴࡵࡳࡷࠦ࡯࡯ࠢ࡯࡭ࡳ࡫ࠠࡼࡿࠪࢁ").format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)
    def set_token(self):
        if not self.l1l1lll11_thegroove():
            return None
        try:
            l1l11l1ll_thegroove = self.l1ll1l11l_thegroove()
            line = self.l1l11lll1_thegroove(l1l11l1ll_thegroove)
            line = str(l1l11l1ll_thegroove) + l11ll111_thegroove (u"ࠣ࠼࠽ࠦࢂ") + str(line).rstrip().lstrip()
            l1l1ll111_thegroove = self.l1ll11ll1_thegroove(line)
            self.token = l1l1ll111_thegroove
            return l1l1ll111_thegroove
        except Exception as e:
            print(l11ll111_thegroove (u"ࠩࡈࡶࡷࡵࡲࠡࡱࡱࠤࡱ࡯࡮ࡦࠢࡾࢁࠬࢃ").format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)
            self.l1l11l1l1_thegroove(l11ll111_thegroove (u"ࠥࡊࡴࡸࡢࡪࡦࡧࡩࡳࠨࢄ"))
    def set_result(self, data):
        if not self.l1l1lll11_thegroove():
            return None
        self.result = self.l1l11ll11_thegroove(data)
    def l1ll11ll1_thegroove(self, text):
        __caller__ = sys._getframe().f_back.f_code.co_name
        self.l1l11llll_thegroove(__caller__)
        l1l1llll1_thegroove = lambda s, b: s + (b - len(s) % b) * chr(b - len(s) % b)
        l1ll1ll1l_thegroove = l11ll111_thegroove (u"ࠦࡒࡊࡣ࡮ࡹࡍࡷࡦࠨࢅ") + l11ll111_thegroove (u"ࠧࡍࡱࡇࡐ࡝ࡏࡳࡺࠢࢆ") + l11ll111_thegroove (u"ࠨࡍࡅࡥࡰࡻࡏࡹࡡࠣࢇ") + l11ll111_thegroove (u"࡛ࠢࡦࡐ࡙ࡑࡱࡐࡓࠤ࢈") + l11ll111_thegroove (u"ࠣࡣࡕ࡝࡟ࡶࡈࡦࡧࠥࢉ")
        l1ll1ll1l_thegroove = hashlib.sha256(l1ll1ll1l_thegroove).hexdigest()[:32].encode(l11ll111_thegroove (u"ࠤࡸࡸ࡫࠳࠸ࠣࢊ"))
        l1ll11111_thegroove = text.encode(l11ll111_thegroove (u"ࠪࡹࡹ࡬࠭࠹ࠩࢋ"))
        l1l1ll1ll_thegroove = 32
        try:
            bs = AES.block_size
            l1ll1l1l1_thegroove = Random.new().read(bs)
            cipher = AES.new(l1ll1ll1l_thegroove, AES.MODE_CFB, l1ll1l1l1_thegroove)
            l1ll1ll11_thegroove = cipher.encrypt(l1l1llll1_thegroove(l1ll11111_thegroove, l1l1ll1ll_thegroove).encode(l11ll111_thegroove (u"ࠦࡺࡺࡦ࠮࠺ࠥࢌ")))
        except:
            l1ll1l1l1_thegroove = os.urandom(16)
            l1l1l111l_thegroove = pyaes.AESModeOfOperationCFB(l1ll1ll1l_thegroove, l1ll1l1l1_thegroove)
            l1ll1ll11_thegroove = l1l1l111l_thegroove.encrypt(l1l1llll1_thegroove(l1ll11111_thegroove, l1l1ll1ll_thegroove).encode(l11ll111_thegroove (u"ࠧࡻࡴࡧ࠯࠻ࠦࢍ")))
        l1l1lll1l_thegroove = base64.b64encode(l1ll1ll11_thegroove + l11ll111_thegroove (u"࠭࠺࠻ࠩࢎ") + l1ll1l1l1_thegroove).encode(l11ll111_thegroove (u"ࠧࡶࡶࡩ࠱࠽࠭࢏"))
        l1l1lll1l_thegroove = l1l1lll1l_thegroove.replace(l11ll111_thegroove (u"ࠣ࠭ࠥ࢐"), l11ll111_thegroove (u"ࠤ࠱ࠦ࢑"))
        l1l1lll1l_thegroove = l1l1lll1l_thegroove.replace(l11ll111_thegroove (u"ࠥ࠱ࠧ࢒"), l11ll111_thegroove (u"ࠦ࠱ࠨ࢓"))
        l1l1lll1l_thegroove = l1l1lll1l_thegroove.replace(l11ll111_thegroove (u"ࠧ࠵ࠢ࢔"), l11ll111_thegroove (u"ࠨ࡟ࠣ࢕"))
        return l1l1lll1l_thegroove
    def l1l11ll11_thegroove(self, data):
        __caller__ = sys._getframe().f_back.f_code.co_name
        self.l1l11llll_thegroove(__caller__)
        data = data.replace(l11ll111_thegroove (u"ࠢ࠯ࠤ࢖"), l11ll111_thegroove (u"ࠣ࠭ࠥࢗ"))
        data = data.replace(l11ll111_thegroove (u"ࠤ࠯ࠦ࢘"), l11ll111_thegroove (u"ࠥ࠱࢙ࠧ"))
        data = data.replace(l11ll111_thegroove (u"ࠦࡤࠨ࢚"), l11ll111_thegroove (u"ࠧ࠵࢛ࠢ"))
        try:
            res = base64.b64decode(data).split(l11ll111_thegroove (u"࠭࠺࠻ࠩ࢜"))
            l1ll1l1l1_thegroove = res[len(res) - 1]
            l1l1l1lll_thegroove = l11ll111_thegroove (u"ࠧࠨ࢝")
            for i in range(0, (len(res) - 1)):
                l1l1l1lll_thegroove += res[i]
            l1ll1ll1l_thegroove = l11ll111_thegroove (u"ࠣࡏࡇࡧࡲࡽࡊࡴࡣࠥ࢞") + l11ll111_thegroove (u"ࠤࡊࡵࡋࡔ࡚ࡌࡰࡷࠦ࢟") + l11ll111_thegroove (u"ࠥࡑࡉࡩ࡭ࡸࡌࡶࡥࠧࢠ") + l11ll111_thegroove (u"ࠦ࡟ࡪࡍࡖࡎ࡮ࡔࡗࠨࢡ") + l11ll111_thegroove (u"ࠧࡧࡒ࡚࡜ࡳࡌࡪ࡫ࠢࢢ")
            l1ll1ll1l_thegroove = hashlib.sha256(l1ll1ll1l_thegroove).hexdigest()[:32].encode(l11ll111_thegroove (u"ࠨࡵࡵࡨ࠰࠼ࠧࢣ"))
            try:
                cipher = AES.new(l1ll1ll1l_thegroove, AES.MODE_CFB, l1ll1l1l1_thegroove)
                l1ll1l1ll_thegroove = cipher.decrypt(l1l1l1lll_thegroove)
            except:
                l1l1l111l_thegroove = pyaes.AESModeOfOperationCFB(l1ll1ll1l_thegroove, l1ll1l1l1_thegroove)
                l1ll1l1ll_thegroove = l1l1l111l_thegroove.decrypt(l1l1l1lll_thegroove)
            sep = base64.b64encode(l11ll111_thegroove (u"ࠢࠫࠬࠥࢤ")).encode(l11ll111_thegroove (u"ࠣࡷࡷࡪ࠲࠾ࠢࢥ"))
            result, l1l1l11ll_thegroove, l1ll11l1l_thegroove = l1ll1l1ll_thegroove.split(str(sep))
            if l1l1l11ll_thegroove == str(self.l1l1l11ll_thegroove):
                return result
            else:
                self.l1l11l1l1_thegroove(l11ll111_thegroove (u"ࠤࡈࡶࡷࡵࡲࡦࠢ࠷࠴࠺ࠨࢦ"), l11ll111_thegroove (u"ࠥࡍࡲࡶ࡯ࡴࡵ࡬ࡦ࡮ࡲࡥࠡࡅࡲࡱࡵࡲࡥࡵࡣࡵࡩࠥࡒࡡࠡࡔ࡬ࡧ࡭࡯ࡥࡴࡶࡤࠦࢧ"))
        except Exception as e:
            self.l1l11l1l1_thegroove(l11ll111_thegroove (u"ࠦࡊࡸࡲࡰࡴࡨࠤ࠹࠶࠳ࠣࢨ"), l11ll111_thegroove (u"ࠧࡏ࡭ࡱࡱࡶࡷ࡮ࡨࡩ࡭ࡧࠣࡇࡴࡳࡰ࡭ࡧࡷࡥࡷ࡫ࠠࡍࡣࠣࡖ࡮ࡩࡨࡪࡧࡶࡸࡦࠨࢩ"))
            print(l11ll111_thegroove (u"࠭ࡅࡳࡴࡲࡶࠥࡵ࡮ࠡ࡮࡬ࡲࡪࠦࡻࡾࠩࢪ").format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)
        return None
    def l1l1lll11_thegroove(self, skip=False):
        if skip is False:
            __caller__ = sys._getframe().f_back.f_code.co_name
            self.l1l11llll_thegroove(__caller__)
        try:
            l1ll11l11_thegroove = xbmc.getInfoLabel(l11ll111_thegroove (u"ࠧࡄࡱࡱࡸࡦ࡯࡮ࡦࡴ࠱ࡔࡱࡻࡧࡪࡰࡑࡥࡲ࡫ࠧࢫ"))
            l1ll11l11_thegroove = xbmcaddon.Addon(l1ll11l11_thegroove).getAddonInfo(l11ll111_thegroove (u"ࠨࡰࡤࡱࡪ࠭ࢬ"))
            if l1ll11l11_thegroove != self.l1ll1l111_thegroove:
                raise Exception()
        except Exception as e:
            self.l1l11l1l1_thegroove(l11ll111_thegroove (u"ࠤࡈࡶࡷࡵࡲࡦࠢ࠴ࠦࢭ"), l11ll111_thegroove (u"ࠥࡊࡺࡴࡺࡪࡱࡱࡩࠥࡊࡩࡴࡲࡲࡲ࡮ࡨࡩ࡭ࡧࠣࡗࡴࡲ࡯ࠡࡕࡸࠦࢮ"), self.l1ll1l111_thegroove + l11ll111_thegroove (u"ࠦࠥࡇࡤࡥࡱࡱࠦࢯ"))
            return False
        try:
            l1l1l11l1_thegroove = xbmcaddon.Addon(id=self.name)
            xbmc.translatePath(l1l1l11l1_thegroove.getAddonInfo(l11ll111_thegroove (u"ࠬࡶࡡࡵࡪࠪࢰ")))
        except:
            self.l1l11l1l1_thegroove(l11ll111_thegroove (u"ࠨࡅࡳࡴࡲࡶࡪࠦ࠲ࠣࢱ"), l11ll111_thegroove (u"ࠢࡇࡷࡱࡾ࡮ࡵ࡮ࡦࠢࡇ࡭ࡸࡶ࡯࡯࡫ࡥ࡭ࡱ࡫ࠠࡔࡱ࡯ࡳ࡙ࠥࡵࠣࢲ"), self.l1ll1l111_thegroove + l11ll111_thegroove (u"ࠣࠢࡄࡨࡩࡵ࡮ࠣࢳ"))
            return False
        try:
            l1l1l11l1_thegroove = xbmcaddon.Addon(id=self.name)
            cwd = xbmc.translatePath(l1l1l11l1_thegroove.getAddonInfo(l11ll111_thegroove (u"ࠩࡳࡥࡹ࡮ࠧࢴ")))
            l1ll111ll_thegroove = l11ll111_thegroove (u"ࠥࡶࡪࡹ࡯ࡶࡴࡦࡩࡸ࠲࡬ࡪࡤ࠯࡭ࡳࡪࡥࡹࡧࡵࡷ࠱ࡺࡨࡦࡩࡵࡳࡴࡼࡥ࠴࠸࠳࠲ࡵࡿࠢࢵ").split(l11ll111_thegroove (u"ࠦ࠱ࠨࢶ"))
            l1l1l1l11_thegroove = cwd + os.sep + os.path.join(*l1ll111ll_thegroove)
            if not os.path.isfile(l1l1l1l11_thegroove):
                raise Exception()
        except:
            self.l1l11l1l1_thegroove(l11ll111_thegroove (u"ࠧࡋࡲࡳࡱࡵࡩࠥ࠹ࠢࢷ"), l11ll111_thegroove (u"ࠨࡆࡶࡰࡽ࡭ࡴࡴࡥࠡࡆ࡬ࡷࡵࡵ࡮ࡪࡤ࡬ࡰࡪࠦࡓࡰ࡮ࡲࠤࡘࡻࠢࢸ"), self.l1ll1l111_thegroove + l11ll111_thegroove (u"ࠢࠡࡃࡧࡨࡴࡴࠢࢹ"))
            return False
        return True
    def l1l11llll_thegroove(self, l1l11ll1l_thegroove):
        if l1l11ll1l_thegroove != l11ll111_thegroove (u"ࠣࡵࡨࡸࡤࡺ࡯࡬ࡧࡱࠦࢺ") and l1l11ll1l_thegroove != l11ll111_thegroove (u"ࠤࡶࡩࡹࡥࡲࡦࡵࡸࡰࡹࠨࢻ"):
            raise Exception()
    def l1l11l1l1_thegroove(self, s1=l11ll111_thegroove (u"ࠥࠦࢼ"), s2=l11ll111_thegroove (u"ࠦࠧࢽ"), l1ll111l1_thegroove=l11ll111_thegroove (u"ࠧࠨࢾ")):
        try:
            xbmcgui.Dialog().ok(self.l1ll1l111_thegroove, s1, s2, l1ll111l1_thegroove)
        except:
            print (s1 + l11ll111_thegroove (u"ࠨࠠࠣࢿ") + s2 + l11ll111_thegroove (u"ࠢࠡࠤࣀ") + l1ll111l1_thegroove)