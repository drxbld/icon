import xbmcaddon
import xbmcgui
import xbmc
import pyxbmct
import requests
import json
import sys
import os
    
addon_id = 'plugin.video.sports'
_addon = xbmcaddon.Addon(id=addon_id)
_path = 'special://home/addons/%s/' % addon_id
addonname = _addon.getAddonInfo('name')

QRbtc  = xbmc.translatePath(os.path.join(_path, "resources/donations/btc.png"))
QRbch  = xbmc.translatePath(os.path.join(_path, "resources/donations/bch.png"))
QReth  = xbmc.translatePath(os.path.join(_path, "resources/donations/eth.png"))
QRltc  = xbmc.translatePath(os.path.join(_path, "resources/donations/ltc.png"))
paypal = xbmc.translatePath(os.path.join(_path, "resources/donations/paypal.png"))
btcSpinner = xbmc.translatePath(os.path.join(_path, "resources/donations/bitcoin-spinner.png"))
ethSpinner = xbmc.translatePath(os.path.join(_path, "resources/donations/ethereum-spinner.png"))
ltcSpinner = xbmc.translatePath(os.path.join(_path, "resources/donations/litecoin-spinner.png"))

class DonationsDialog(pyxbmct.AddonDialogWindow):
    def __init__(self, title="[B]Donations[/B]"):
        super(DonationsDialog, self).__init__(title)
        self.setGeometry(800, 500, 10, 30)
        #Referral Links
        self.btcRef = 'http://coinspinner.me/c/U27P5D'
        self.ethRef = 'http://eth.coinspinner.me/c/6P2ZBK'
        self.ltcRef = 'http://ltc.coinspinner.me/c/DWQ50P'
        self.paypalAddr = 'https://www.paypal.me/LuciferOnKodi'
        self.coinbaseAddr = 'mhilluniversal@gmail.com'
        #Paper Wallet Addresses
        self.btcAddr = '1CbLch11HztjAQnCeBUyqJ7vxg7SooJpKo'
        self.bchAddr = '12aL8j4xoxS1JRjiU3aMxHibzNNzcEJwWP'
        self.ethAddr = '0xdb5449C7576a2A637892B38275bFcab8275aC36B'
        self.ltcAddr = 'LVRkgZKHSFb8RFjEQCseDhquA9iFSyCPPq'
        #Crypto Address Apis
        self.btcApi = 'http://api.blockcypher.com/v1/btc/main/addrs/%s' % self.btcAddr
        self.bchApi = 'https://blockdozer.com/insight-api/addr/%s/totalReceived' % self.bchAddr
        self.ethApi = 'http://api.blockcypher.com/v1/eth/main/addrs/%s' % self.ethAddr
        self.ltcApi = 'https://chain.so/api/v2/get_address_received/ltc/%s' % self.ltcAddr
        self.paypalApi = 'https://pastebin.com/raw/271M2wAt'
        #USD Price Api
        self.priceApi = 'https://min-api.cryptocompare.com/data/pricemulti?fsyms=BTC,ETH,LTC,BCH&tsyms=USD'
        self.get_balances()
        self.set_controls()
        self.set_navigation()
        self.connect(pyxbmct.ACTION_NAV_BACK, self.close)

    def get_balances(self):
        #Crypto Api Responses
        self.btcResult = json.loads(requests.get(self.btcApi).text)
        self.bchResult = requests.get(self.bchApi).text
        self.ethResult = json.loads(requests.get(self.ethApi).text)
        self.ltcResult = json.loads(requests.get(self.ltcApi).text)['data']
        self.paypalResult = requests.get(self.paypalApi).text
        self.priceResult = json.loads(requests.get(self.priceApi).text)
        #Total Balances
        tempValue = float(self.btcResult['total_received']) / 10**8
        self.btcValue = '%s BTC\n$%s' % (str(tempValue), str(round(tempValue * self.priceResult['BTC']['USD'], 2)))
        tempValue = float(self.bchResult) / 10**8
        self.bchValue = '%s BCH\n$%s' % (str(tempValue), str(round(tempValue * self.priceResult['BCH']['USD'], 2)))
        tempValue = float(self.ethResult['total_received']) / 10**18
        self.ethValue = '%s ETH\n$%s' % (str(tempValue), str(round(tempValue * self.priceResult['ETH']['USD'], 2)))
        tempValue = float(self.ltcResult['confirmed_received_value']) + \
                    float(self.ltcResult['unconfirmed_received_value'])
        self.ltcValue = '%s LTC\n$%s' % (str(tempValue), str(round(tempValue * self.priceResult['LTC']['USD'], 2)))
        #Set up a pastebin paste where we grab the raw value from it
        #to display paypal donations, so we can easily update it from our phone
        self.paypalValue = self.paypalResult
        
    def set_controls(self):
        ###Left Side###
        ###Section 1###
        ###  Money  ###
        ###Donations###
        self.Section1 = pyxbmct.Label('[B]If you have money to\nspare[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(self.Section1, 0, 0, columnspan=10)
        self.menu = pyxbmct.List()
        self.placeControl(self.menu, 1, 0, rowspan=6, columnspan=10)
        self.menu.addItems(['Paypal',
                            'Bitcoin (BTC)',
                            'Bitcoin Cash (BCH)',
                            'Ethereum (ETH)',
                            'Litecoin (LTC)'])
        ###Section 2###
        ###Referral ###
        ###Donations###
        self.Section2 = pyxbmct.Label('[B]You can donate for free\nif you own an android\ndevice[/B]', alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(self.Section2, 5, 0, rowspan=2, columnspan=10)
        self.menu2 = pyxbmct.List()
        self.placeControl(self.menu2, 7, 0, rowspan=10, columnspan=10)
        self.menu2.addItems(['Bitcoin Spinner',
                             'Ethereum Spinner',
                             'Litecoin Spinner'])
        ###Right Side###
        ###   Main   ###
        ###  Detail  ###
        self.QRcode = pyxbmct.Image(paypal, aspectRatio=2)
        self.placeControl(self.QRcode, 0, 16, rowspan=3, columnspan=10)
        self.Addr = pyxbmct.Label(self.paypalAddr, alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(self.Addr, 3, 11, columnspan=20)
        self.Balance = pyxbmct.Label('Total Donated:\n%s' % self.paypalValue, alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(self.Balance, 4, 16, rowspan=3, columnspan=10)
        self.Download = pyxbmct.Button('Download', alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(self.Download, 4, 16, rowspan=2, columnspan=10)
        self.connect(self.Download, self.downloadApp)
        self.Download.setVisible(False)
        self.Description = pyxbmct.Label('')
        self.placeControl(self.Description, 7, 11, rowspan=4, columnspan=20)
    
    def set_navigation(self):
        self.menu.controlUp(self.menu2)
        self.menu.controlDown(self.menu2)
        self.menu2.controlUp(self.menu)
        self.menu2.controlDown(self.menu)
        self.menu2.controlLeft(self.Download)
        self.menu2.controlRight(self.Download)
        self.Download.controlLeft(self.menu2)
        self.Download.controlRight(self.menu2)
        
        self.connectEventList(
            [pyxbmct.ACTION_MOVE_DOWN,
             pyxbmct.ACTION_MOVE_UP,
             pyxbmct.ACTION_MOUSE_WHEEL_DOWN,
             pyxbmct.ACTION_MOUSE_WHEEL_UP,
             pyxbmct.ACTION_MOUSE_MOVE],
            self.update_view)
        # Set initial focus
        self.setFocus(self.menu)
    
    def update_view(self):
        try:
            if self.getFocus() == self.menu:
                selection = self.menu.getListItem(self.menu.getSelectedPosition()).getLabel()
                if selection == 'Paypal':
                    self.QRcode.setImage(paypal)
                    self.Addr.setLabel(self.paypalAddr)
                    self.Balance.setLabel('Total Donated:\n%s' % self.paypalValue)
                    self.Description.setLabel('')
                elif selection == 'Bitcoin (BTC)':
                    self.QRcode.setImage(QRbtc)
                    self.Addr.setLabel(self.btcAddr)
                    self.Balance.setLabel('Total Donated:\n%s' % self.btcValue)
                    self.Description.setLabel('[B]Note:[/B] If you have a coinbase account you can send\ncrypto to my coinbase email to avoid any\ntransaction fees.\n[B]%s[/B]' % self.coinbaseAddr)
                elif selection == 'Bitcoin Cash (BCH)':
                    self.Addr.setLabel(self.bchAddr)
                    self.QRcode.setImage(QRbch)
                    self.Balance.setLabel('Total Donated:\n%s' % self.bchValue)
                    self.Description.setLabel('[B]Note:[/B] If you have a coinbase account you can send\ncrypto to my coinbase email to avoid any\ntransaction fees.\n[B]%s[/B]' % self.coinbaseAddr)
                elif selection == 'Ethereum (ETH)':
                    splitEth = '%s\n%s' % (self.ethAddr[:15], self.ethAddr[15:])
                    #self.Addr.setLabel(self.ethAddr)
                    self.Addr.setLabel(splitEth)
                    self.QRcode.setImage(QReth)
                    self.Balance.setLabel('Total Donated:\n%s' % self.ethValue)
                    self.Description.setLabel('[B]Note:[/B] If you have a coinbase account you can send\ncrypto to my coinbase email to avoid any\ntransaction fees.\n[B]%s[/B]' % self.coinbaseAddr)
                elif selection == 'Litecoin (LTC)':
                    self.Addr.setLabel(self.ltcAddr)
                    self.QRcode.setImage(QRltc)
                    self.Balance.setLabel('Total Donated:\n%s' % self.ltcValue)
                    self.Description.setLabel('[B]Note:[/B] If you have a coinbase account you can send\ncrypto to my coinbase email to avoid any\ntransaction fees.\n[B]%s[/B]' % self.coinbaseAddr)
                self.Balance.setVisible(True)
                self.Download.setVisible(False)
            elif self.getFocus() == self.menu2:
                selection = self.menu2.getListItem(self.menu2.getSelectedPosition()).getLabel()
                if selection == 'Bitcoin Spinner':
                    self.QRcode.setImage(btcSpinner)
                    self.Addr.setLabel(self.btcRef)
                elif selection == 'Ethereum Spinner':
                    self.QRcode.setImage(ethSpinner)
                    self.Addr.setLabel(self.ethRef)
                elif selection == 'Litecoin Spinner':
                    self.QRcode.setImage(ltcSpinner)
                    self.Addr.setLabel(self.ltcRef)
                self.Download.setVisible(True)
                self.Balance.setVisible(False)
                self.Description.setLabel('[B]Notes:[/B] (1) You need a gmail address in order to\nuse these apps. (2) You need to download the app\nby visiting the above link on your android device\nin order to become my referral. Then, simply\nplay daily to passively donate to me.')
            else: pass
        except (RuntimeError, SystemError):
            pass

    def downloadApp(self):
        url = self.Addr.getLabel()
        osAndroid = xbmc.getCondVisibility('System.Platform.Android')
        if osAndroid:
            xbmc.executebuiltin("StartAndroidActivity(com.android.browser,android.intent.action.VIEW,,%s)" % url)
        else:
            line1 = ('You are not on an android device. '
                     'Please visit the below link on an android '
                     'device to download the app.\n%s') % url
            xbmcgui.Dialog().ok('Incompatible Device', line1)

def load():
    dialog = DonationsDialog()
    dialog.doModal()
    del dialog