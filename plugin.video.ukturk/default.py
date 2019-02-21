# -*- coding: utf-8 -*-
import xbmc , xbmcaddon , xbmcgui , xbmcplugin , urllib , urllib2 , os , re , sys , datetime , random , liveresolver , base64 , pyxbmct , glob , net , json , requests
import resolveurl
from resources . lib . common_addon import Addon
from HTMLParser import HTMLParser
from metahandler import metahandlers
from resources . lib import scraper1
from resources . lib import scraper2
from resources . lib import scraper3
from resources . lib import trt
from resources . lib import kanald
from resources . lib import showt
from resources . lib import ddizi
from resources . lib import canlidizi
from resources . lib import latesttv
from resources . lib import footballh
from resources . lib import footballh2
from resources . lib import populartv
from resources . lib import newtv
from resources . lib import atoz
from resources . lib import wizard as wizz , downloader as downloadCool , notify
import time ; import ntpath ;
import shutil ; import zipfile ; import hashlib ;
import platform ;
import subprocess
import xbmcvfs
import atexit
import cookielib
import uuid
import plugintools
import webbrowser as wb
from uuid import getnode as get_mac
oo000 = get_mac ( )
ii = xbmcaddon . Addon ( 'plugin.video.ukturk' )
oOOo = 'plugin.video.ukturk'
O0 = xbmcgui . DialogProgress ( )
o0O = Addon ( oOOo , sys . argv )
iI11I1II1I1I = xbmcaddon . Addon ( id = oOOo )
oooo = xbmc . translatePath ( iI11I1II1I1I . getAddonInfo ( 'profile' ) )
iIIii1IIi = xbmcgui . Dialog ( )
o0OO00 = xbmcgui . Dialog ( )
oo = xbmc . translatePath ( 'special://home/addons/' ) + '/*.*'
i1iII1IiiIiI1 = xbmc . translatePath ( 'special://home/addons/' )
iIiiiI1IiI1I1 = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + oOOo , 'fanart.jpg' ) )
o0OoOoOO00 = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + oOOo , 'fanart.jpg' ) )
I11i = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + oOOo , 'icon.png' ) )
O0O = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + oOOo , 'icon.png' ) )
Oo = xbmc . translatePath ( 'special://home/' )
I1ii11iIi11i = os . path . join ( Oo , 'addons' )
I1IiI = os . path . join ( I1ii11iIi11i , 'packages' )
o0OOO = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + oOOo , 'next.png' ) )
iIiiiI = iI11I1II1I1I . getSetting ( 'adult' )
Iii1ii1II11i = iI11I1II1I1I . getSetting ( 'password' )
iIiiiI = iI11I1II1I1I . getSetting ( 'adult' )
iI111iI = iI11I1II1I1I . getSetting ( 'pin' )
IiII = int ( iI11I1II1I1I . getSetting ( 'count' ) )
iI1Ii11111iIi = iI11I1II1I1I . getSetting ( 'enable_meta' )
i1i1II = xbmc . translatePath ( 'special://home/userdata/addon_data/' + oOOo )
O0oo0OO0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata/Database' , 'UKTurk.db' ) )
I1i1iiI1 = 'https://addoncloud.org/ukturk/UKTurk/fanarts.jpg'
iiIIIII1i1iI = 'https://www.googleapis.com/youtube/v3/search?q='
o0oO0 = '&regionCode=US&part=snippet&hl=en_US&key=AIzaSyBgXfD0GxisjVhmV2j0jbDWIXKwo4Ac8ww&type=video&maxResults=50'
oo00 = 'https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&playlistId='
o00 = '&maxResults=50&key=AIzaSyBgXfD0GxisjVhmV2j0jbDWIXKwo4Ac8ww'
Oo0oO0ooo = open ( O0oo0OO0 , 'a' )
Oo0oO0ooo . close ( )
net = net . Net ( )
o0oOoO00o = 'https://addoncloud.org/wizard.php'
i1 = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36 ReplicantWizard/1.0.0'
oOOoo00O0O = "UKTurks"
i1111 = plugintools . get_setting ( 'pin' )
i11 = plugintools . get_setting ( 'submessage' )
if 41 - 41: O00o0o0000o0o . oOo0oooo00o * I1i1i1ii - IIIII
def I1 ( ) :
 iI11I1II1I1I . setSetting ( 'fav' , 'no' )
 if not os . path . exists ( i1i1II ) :
  os . mkdir ( i1i1II )
 O0OoOoo00o = iiiI11 ( I1i1iiI1 )
 OOooO = re . compile ( '<index>(.+?)</index>' ) . findall ( O0OoOoo00o ) [ 0 ]
 O0OoOoo00o = iiiI11 ( OOooO )
 OOoO00o = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)"' , re . DOTALL ) . findall ( O0OoOoo00o )
 for II111iiii , II , oOoOo00oOo in OOoO00o :
  if not 'XXX' in II111iiii :
   Ooo00O00O0O0O ( II111iiii , II , 1 , oOoOo00oOo , iIiiiI1IiI1I1 )
  if 'XXX' in II111iiii :
   if iIiiiI == 'true' :
    if Iii1ii1II11i == '' :
     o0OO00 = xbmcgui . Dialog ( )
     OooO0OO = o0OO00 . yesno ( 'Adult Content' , 'You have opted to show adult content' , '' , 'Please set a password to prevent accidental access' , 'Cancel' , 'Lets Go' )
     if OooO0OO == 1 :
      iiiIi = xbmc . Keyboard ( '' , 'Set Password' )
      iiiIi . doModal ( )
      if ( iiiIi . isConfirmed ( ) ) :
       IiIIIiI1I1 = iiiIi . getText ( )
       iI11I1II1I1I . setSetting ( 'password' , IiIIIiI1I1 )
      Ooo00O00O0O0O ( II111iiii , II , 1 , oOoOo00oOo , iIiiiI1IiI1I1 )
   if iIiiiI == 'true' :
    if Iii1ii1II11i <> '' :
     Ooo00O00O0O0O ( II111iiii , II , 1 , oOoOo00oOo , iIiiiI1IiI1I1 )
 Ooo00O00O0O0O ( 'Favourites' , O0oo0OO0 , 15 , 'http://addoncloud.org/ukturk/UKTurk/thumbs/new/Uk%20turk%20thumbnails%20favourites.jpg' , iIiiiI1IiI1I1 )
 Ooo00O00O0O0O ( 'Search' , 'url' , 5 , 'http://addoncloud.org/ukturk/UKTurk/thumbs/new/Uk%20turk%20thumbnails%20search.jpg' , iIiiiI1IiI1I1 )
 xbmc . executebuiltin ( 'Container.SetViewMode(500)' )
 OoO000 ( 'movies' , 'MAIN' , O0OoOoo00o )
 if 42 - 42: oOoO - iiIiIIi % iI - I11iii / OO0O00
def ii1 ( text ) :
 if 57 - 57: o0o00ooo0 % oo0Oo00Oo0
 text = str ( text )
 text = text . replace ( '\\r' , '' )
 text = text . replace ( '\\n' , '' )
 text = text . replace ( '\\t' , '' )
 text = text . replace ( '\\' , '' )
 text = text . replace ( '<br />' , '\n' )
 text = text . replace ( '<hr />' , '' )
 text = text . replace ( '&#039;' , "'" )
 text = text . replace ( '&#39;' , "'" )
 text = text . replace ( '&quot;' , '"' )
 text = text . replace ( '&rsquo;' , "'" )
 text = text . replace ( '&amp;' , "&" )
 text = text . replace ( '&#8211;' , "&" )
 text = text . replace ( '&#8217;' , "'" )
 text = text . replace ( '&#038;' , "&" )
 text = text . replace ( '&#8211;' , "-" )
 text = text . lstrip ( ' ' )
 text = text . lstrip ( '	' )
 if 79 - 79: I11i1I + o0o0OOO0o0 % ooOOOo0oo0O0
 return text
 if 71 - 71: oO00OO0oo0 . III1i1i
def iiI1 ( url ) :
 iI11I1II1I1I . setSetting ( 'fav' , 'yes' )
 i11Iiii = None
 file = open ( O0oo0OO0 , 'r' )
 i11Iiii = file . read ( )
 OOoO00o = re . compile ( "<item>(.+?)</item>" , re . DOTALL ) . findall ( i11Iiii )
 for iII1i1I1II in OOoO00o :
  i1IiIiiI = re . compile ( '<title>(.+?)</title>.+?link>(.+?)</link>.+?thumbnail>(.+?)</thumbnail>' , re . DOTALL ) . findall ( iII1i1I1II )
  for II111iiii , url , oOoOo00oOo in i1IiIiiI :
   if '.txt' in url :
    Ooo00O00O0O0O ( II111iiii , url , 1 , oOoOo00oOo , iIiiiI1IiI1I1 )
   else :
    I1I ( II111iiii , url , 2 , oOoOo00oOo , iIiiiI1IiI1I1 )
    if 80 - 80: i1iII11iiIii - iIii11I
def OOO0OOO00oo ( name , url , iconimage ) :
 url = url . replace ( ' ' , '%20' )
 iconimage = iconimage . replace ( ' ' , '%20' )
 Iii111II = '<FAV><item>\n<title>' + name + '</title>\n<link>' + url + '</link>\n' + '<thumbnail>' + iconimage + '</thumbnail>\n</item></FAV>\n'
 Oo0oO0ooo = open ( O0oo0OO0 , 'a' )
 Oo0oO0ooo . write ( Iii111II )
 Oo0oO0ooo . close ( )
 if 9 - 9: ii11I
def Ooo0OO0oOO ( name , url , iconimage ) :
 i11Iiii = None
 file = open ( O0oo0OO0 , 'r' )
 i11Iiii = file . read ( )
 ii11i1 = ''
 OOoO00o = re . compile ( '<item>(.+?)</item>' , re . DOTALL ) . findall ( i11Iiii )
 for i1IiIiiI in OOoO00o :
  Iii111II = '\n<FAV><item>\n' + i1IiIiiI + '</item>\n'
  if name in i1IiIiiI :
   Iii111II = Iii111II . replace ( 'item' , ' ' )
  ii11i1 = ii11i1 + Iii111II
 file = open ( O0oo0OO0 , 'w' )
 file . truncate ( )
 file . write ( ii11i1 )
 file . close ( )
 xbmc . executebuiltin ( 'Container.Refresh' )
 if 29 - 29: oo0OO % ooOOOo0oo0O0 * OO0O00 - I11iii / o0o0OOO0o0 % III1i1i
def II1i1IiiIIi11 ( name , url , iconimage , fanart ) :
 iI1Ii11iII1 = Oo0O0O0ooO0O ( name )
 iI11I1II1I1I . setSetting ( 'tv' , iI1Ii11iII1 )
 O0OoOoo00o = iiiI11 ( url )
 if '/UKTurk/TurkishTV.txt' in url : IIIIii ( )
 if '/UKTurk/TurkishTV.txt' in url : O0o0 ( )
 if '/UKTurk/TurkishTV.txt' in url : OO00Oo ( )
 if '/UKTurk/TurkishTV.txt' in url : O0OOO0OOoO0O ( )
 if '/UKTurk/TurkishTV.txt' in url : O00Oo000ooO0 ( )
 if '/UKTurk/tv%20shows/Index.txt' in url : OoO0O00 ( )
 if '/UKTurk/tv%20shows/Index.txt' in url : IIiII ( )
 if '/UKTurk/SportsList.txt' in url : o0 ( )
 if 62 - 62: I1i1i1ii * o0o00ooo0
 if '/UKTurk/movies/Index.txt' in url : i1OOO ( )
 if '/UKTurk/cartoons/Index.txt' in url : Oo0oOOo ( )
 if 'Index' in url :
  Oo0OoO00oOO0o ( url )
 if 'XXX' in name : OOO00O ( O0OoOoo00o )
 OOoO00o = re . compile ( '<item>(.+?)</item>' , re . DOTALL ) . findall ( O0OoOoo00o )
 IiII = str ( len ( OOoO00o ) )
 iI11I1II1I1I . setSetting ( 'count' , IiII )
 iI11I1II1I1I . setSetting ( 'fav' , 'no' )
 for iII1i1I1II in OOoO00o :
  try :
   if '<sportsdevil>' in iII1i1I1II : OOoOO0oo0ooO ( iII1i1I1II , url , iconimage )
   elif '<iptv>' in iII1i1I1II : O0o0O00Oo0o0 ( iII1i1I1II )
   elif '<Image>' in iII1i1I1II : O00O0oOO00O00 ( iII1i1I1II )
   elif '<text>' in iII1i1I1II : i1Oo00 ( iII1i1I1II )
   elif '<scraper>' in iII1i1I1II : i1i ( iII1i1I1II )
   elif '<redirect>' in iII1i1I1II : REDIRECT ( iII1i1I1II )
   elif '<oktitle>' in iII1i1I1II : iiI111I1iIiI ( iII1i1I1II )
   elif '<dl>' in iII1i1I1II : IIIi1I1IIii1II ( iII1i1I1II )
   elif '<scraper>' in iII1i1I1II : i1i ( iII1i1I1II )
   else : O0ii1ii1ii ( iII1i1I1II , url , iconimage )
  except : pass
  if 91 - 91: iIii11I
def iiIii ( apk , url ) :
 ooo0O = 'Browser required'
 wizz . log ( apk )
 wizz . log ( url )
 if wizz . platform ( ) == 'android' :
  oOoO0o00OO0 = iIIii1IIi . yesno ( ooo0O , "Would you like to download and install:" , apk , yeslabel = "Download" , nolabel = "Cancel" )
  if not oOoO0o00OO0 : wizz . LogNotify ( ooo0O , 'ERROR: Install Cancelled' ) ; return
  i1I1ii = apk
  if not os . path . exists ( I1IiI ) : os . makedirs ( I1IiI )
  if not wizz . workingURL ( url ) == True : wizz . LogNotify ( ooo0O , 'APK Installer: Invalid Apk Url!' % COLOR2 ) ; return
  O0 . create ( 'Chrome' , '[B]Downloading:[/B] Chrome' , '' , 'Please Wait' )
  oOOo0 = os . path . join ( I1IiI , "%s.apk" % apk . replace ( '\\' , '' ) . replace ( '/' , '' ) . replace ( ':' , '' ) . replace ( '*' , '' ) . replace ( '?' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( '|' , '' ) )
  try : os . remove ( oOOo0 )
  except : pass
  downloadCool . download ( url , oOOo0 , O0 )
  xbmc . sleep ( 100 )
  O0 . close ( )
  notify . apkInstaller ( apk )
  wizz . ebi ( 'StartAndroidActivity("","android.intent.action.VIEW","application/vnd.android.package-archive","file:' + oOOo0 + '")' )
 else : wizz . LogNotify ( ooo0O , 'ERROR: None Android Device' )
 if 54 - 54: oOo0oooo00o - iIii11I % ooOOOo0oo0O0
 if 77 - 77: o0o00ooo0 / iI / OO0O00 + OO0O00 . ooOOOo0oo0O0
def OoO0O00 ( ) :
 iI11I1II1I1I . setSetting ( 'fav' , 'no' )
 Ooo00O00O0O0O ( 'New Episodes of TV Shows' , 'https://ww1.watchseries-online.be/last-350-episodes' , 23 , 'http://addoncloud.org/ukturk/UKTurk/tv%20shows/Uk turk thumbnails new episodes tv shows1.jpg' , iIiiiI1IiI1I1 , description = '' )
 if 38 - 38: ii11I
def Ii1 ( url ) :
 if 82 - 82: I11i1I - I1i1i1ii / ooOOOo0oo0O0 + III1i1i
 iI11I1II1I1I . setSetting ( 'fav' , 'no' )
 OOOOoOoo0O0O0 = latesttv . TVShows ( url )
 OOoO00o = re . compile ( '<start>(.+?)<sep>(.+?)<end>' ) . findall ( str ( OOOOoOoo0O0O0 ) )
 for II111iiii , url in OOoO00o :
  I1I ( II111iiii , url , 24 , oOoOo00oOo , iIiiiI1IiI1I1 , description = '' )
 xbmc . executebuiltin ( 'Container.SetViewMode(50)' )
 if 85 - 85: o0o0OOO0o0 % O00o0o0000o0o - i1iII11iiIii * IIIII / iI % iI
def IIiIi1iI ( name , url , iconimage ) :
 if 35 - 35: III1i1i % oOo0oooo00o - oOo0oooo00o
 iI11I1II1I1I . setSetting ( 'fav' , 'no' )
 IiIIIi1iIi = [ 'vidzi' , 'estream' , 'streamango' , 'openload' , 'vidto' , 'gorillavid' , 'streamcherry' , 'vshare' , 'vodlock' ]
 IiII = [ ]
 ooOOoooooo = [ ]
 II1I = latesttv . Stream ( url )
 O0i1II1Iiii1I11 = 1
 if 9 - 9: I11i1I / I11iii - iI / IIIII / I1i1i1ii - oo0Oo00Oo0
 for O0OoOoo00o in II1I :
  if resolveurl . HostedMediaFile ( O0OoOoo00o ) . valid_url ( ) :
   for o00oooO0Oo in IiIIIi1iIi :
    if o00oooO0Oo in O0OoOoo00o :
     IiII . append ( 'Link ' + str ( O0i1II1Iiii1I11 ) )
     ooOOoooooo . append ( O0OoOoo00o )
     O0i1II1Iiii1I11 = O0i1II1Iiii1I11 + 1
 o0OO00 = xbmcgui . Dialog ( )
 o0O0OOO0Ooo = o0OO00 . select ( 'Choose a link..' , IiII )
 if o0O0OOO0Ooo < 0 : quit ( )
 url = ooOOoooooo [ o0O0OOO0Ooo ]
 iiIiI ( name , url , iconimage )
 if 6 - 6: iIii11I . o0o0OOO0o0 * o0o00ooo0 - III1i1i - iIii11I
def Oo0oOOo ( ) :
 Ooo00O00O0O0O ( '[B][COLOR white]Popular Cartoons[/COLOR][/B]' , 'https://watchepisodeseries.unblocked.vet/home/series?genres=animation' , 55 , 'https://i.imgur.com/LEDmp9w.jpg' , iIiiiI1IiI1I1 , description = '' )
 if 45 - 45: iI - IIIII + I1i1i1ii . iI * oO00OO0oo0
def oOOO ( url ) :
 if 16 - 16: OO0O00 / I11i1I + III1i1i
 O0OoOoo00o = requests . get ( url )
 o0o = '''<div class="wide-serie-box half">\s+<a\s+href=['"](.*?)['"].+?url\(['"](.*?)['"].+?<div\s+class=['"]wsbr-title['"].+?<a\s+href=['"].+?['"]>(.*?)</a>'''
 O0OOoO00OO0o = re . findall ( o0o , O0OoOoo00o . content , flags = re . DOTALL )
 for I1111IIIIIi , I11i , Iiii1i1 in O0OOoO00OO0o :
  Iiii1i1 = ii1 ( Iiii1i1 )
  Ooo00O00O0O0O ( Iiii1i1 , I1111IIIIIi , 56 , I11i , iIiiiI1IiI1I1 , description = '' )
  if 84 - 84: iI . I1i1i1ii % IIIII + III1i1i % IIIII % OO0O00
 try :
  IIi1 = '''<a\s*href=['"]([^'"]+)['"]\s*class="paginator-next"'''
  o0OOO = re . findall ( IIi1 , O0OoOoo00o . content ) [ 0 ]
  Ooo00O00O0O0O ( '[COLOR yellow]Next Page --->[/COLOR]' , o0OOO , 55 , O0O , iIiiiI1IiI1I1 , description = '' )
 except : pass
 if 45 - 45: i1iII11iiIii / i1iII11iiIii + ii11I + oo0OO
def iI111i ( url , iconimage ) :
 if 26 - 26: I11i1I * i1iII11iiIii . iiIiIIi * III1i1i
 O0OoOoo00o = requests . get ( url )
 o0o = '''<div\s+class=['"]watched['"].+?<a\s+href=['"](.*?)['"].+?<div\s+class="season">(.*?)</div>.+?<div class="episode">(.*?)</div>.+?<div class="name">(.*?)</div>'''
 O0OOoO00OO0o = re . findall ( o0o , O0OoOoo00o . content , flags = re . DOTALL )
 for I1111IIIIIi , II1 , iiiIi1 , Iiii1i1 in O0OOoO00OO0o :
  if not 'Season 0' in II1 :
   Iiii1i1 = ii1 ( Iiii1i1 )
   II111iiii = II1 + ' ' + iiiIi1 + ' | ' + Iiii1i1
   I1I ( II111iiii , I1111IIIIIi , 57 , iconimage , iIiiiI1IiI1I1 , description = '' )
   if 38 - 38: ii11I
def Ooo00o0Oooo ( url , iconimage ) :
 if 84 - 84: oo0Oo00Oo0 % iiIiIIi . O00o0o0000o0o / OO0O00
 O0OoOoo00o = requests . get ( url )
 o0o = '''<div\s+class="watch">.+?href=['"](.*?)['"].+?</a>(.*?)<'''
 O0OOoO00OO0o = re . findall ( o0o , O0OoOoo00o . content , flags = re . DOTALL )
 o0OIiII = 0
 IiII = [ ]
 ooOOoooooo = [ ]
 for I1111IIIIIi , ii1iII1II in O0OOoO00OO0o :
  o0OIiII += 1
  II111iiii = 'Link ' + str ( o0OIiII ) + ' | ' + ii1iII1II . strip ( )
  IiII . append ( II111iiii )
  ooOOoooooo . append ( I1111IIIIIi )
 o0OO00 = xbmcgui . Dialog ( )
 o0O0OOO0Ooo = o0OO00 . select ( 'Choose a link..' , IiII )
 if o0O0OOO0Ooo < 0 : quit ( )
 url = ooOOoooooo [ o0O0OOO0Ooo ]
 Iii1I1I11iiI1 ( II111iiii , url , iconimage )
 if 18 - 18: ooOOOo0oo0O0 + i1iII11iiIii - III1i1i . iiIiIIi + O00o0o0000o0o
def Iii1I1I11iiI1 ( name , url , iconimage ) :
 O0OoOoo00o = requests . get ( url )
 o0o = '''<div class="wb-main">.+?href=['"](.*?)['"]'''
 O0OOoO00OO0o = re . findall ( o0o , O0OoOoo00o . content , flags = re . DOTALL ) [ 0 ]
 iiIiI ( name , O0OOoO00OO0o , iconimage )
 if 20 - 20: ii11I
def IIiII ( ) :
 iI11I1II1I1I . setSetting ( 'fav' , 'no' )
 Ooo00O00O0O0O ( 'Popular TV Shows' , 'https://movie25.unblocked.vet/tv/popular-today/' , 27 , 'https://imgur.com/IxhttEZ.jpg' , iIiiiI1IiI1I1 , description = '' )
 Ooo00O00O0O0O ( '24/7 TV Shows' , 'http://www.ibrod.tv/tvshows.php?pageNum_GetName=0&totalRows_GetName=55' , 58 , 'https://i.imgur.com/BOM7z4H.jpg' , iIiiiI1IiI1I1 , description = '' )
 if 52 - 52: iiIiIIi - IIIII % III1i1i + iI * I11iii . iIii11I
def O0OO0O ( url ) :
 if 81 - 81: o0o0OOO0o0 . oo0Oo00Oo0 % oOo0oooo00o / iI - o0o0OOO0o0
 O0OoOoo00o = requests . get ( url )
 o0o = '''<span><img src=.+?title=['"](.*?)['"].+?<a\s+href=['"](.*?)['"]'''
 O0OOoO00OO0o = re . findall ( o0o , O0OoOoo00o . content , flags = re . DOTALL )
 I11i = 'https://i.imgur.com/BOM7z4H.jpg'
 for Iiii1i1 , I1111IIIIIi in O0OOoO00OO0o :
  if not 'http://ibrod.tv' in I1111IIIIIi :
   I1111IIIIIi = 'http://ibrod.tv/' + I1111IIIIIi
  I1I ( Iiii1i1 , I1111IIIIIi , 59 , I11i , iIiiiI1IiI1I1 , description = '' )
  if 43 - 43: O00o0o0000o0o + I11iii * iiIiIIi * ii11I * oOo0oooo00o
 try :
  IIi1 = '''<a\s*href=['"]([^'"]+)['"]>Next'''
  o0OOO = re . findall ( IIi1 , O0OoOoo00o . content ) [ 0 ]
  if not 'http://www.ibrod.tv/' in o0OOO :
   o0OOO = 'http://www.ibrod.tv/' + o0OOO
  Ooo00O00O0O0O ( '[COLOR yellow]Next Page --->[/COLOR]' , o0OOO , 58 , O0O , iIiiiI1IiI1I1 , description = '' )
 except : pass
 if 64 - 64: ooOOOo0oo0O0 % I1i1i1ii * o0o0OOO0o0
def o0iI11I1II ( name , url , iconimage ) :
 if 40 - 40: I1i1i1ii / o0o00ooo0 % I11i1I + iiIiIIi
 O0OoOoo00o = requests . get ( url )
 o0o = '''div class="player">.+?src=['"](.*?)['"]'''
 O0OOoO00OO0o = re . findall ( o0o , O0OoOoo00o . content , flags = re . DOTALL ) [ 0 ]
 I1111IIIIIi = requests . get ( O0OOoO00OO0o )
 ii1Ii1I1Ii11i = '''file:\s+['"](.*?)['"]'''
 O0OOoO00OO0o = re . findall ( ii1Ii1I1Ii11i , I1111IIIIIi . content , flags = re . DOTALL ) [ 0 ]
 iiIiI ( name , O0OOoO00OO0o , iconimage )
 if 35 - 35: oo0Oo00Oo0
def O0O0Oooo0o ( name , url , iconimage ) :
 iI11I1II1I1I . setSetting ( 'fav' , 'no' )
 if 56 - 56: I11i1I % oOo0oooo00o - iI
 OOOOoOoo0O0O0 = populartv . TVShows ( url )
 OOoO00o = re . compile ( '<start>(.+?)<sep>(.+?)<sep>(.+?)<end>' ) . findall ( str ( OOOOoOoo0O0O0 ) )
 for name , url , iconimage in OOoO00o :
  Ooo00O00O0O0O ( name , url , 28 , iconimage , iIiiiI1IiI1I1 , description = '' )
 xbmc . executebuiltin ( 'Container.SetViewMode(550)' )
 if 100 - 100: III1i1i - oOo0oooo00o % o0o0OOO0o0 * ooOOOo0oo0O0 + iI
def Oo0O0oooo ( name , url , iconimage ) :
 iI11I1II1I1I . setSetting ( 'fav' , 'no' )
 OOOOoOoo0O0O0 = populartv . TVSeasons ( name , url , iconimage )
 OOoO00o = re . compile ( '<start>(.+?)<sep>(.+?)<end>' ) . findall ( str ( OOOOoOoo0O0O0 ) )
 for name , url in OOoO00o :
  I1I ( name , url , 30 , iconimage , iIiiiI1IiI1I1 , description = '' )
 xbmc . executebuiltin ( 'Container.SetViewMode(50)' )
 if 33 - 33: ii11I + i1iII11iiIii * o0o0OOO0o0 / I1i1i1ii - iI
 if 54 - 54: ii11I / ooOOOo0oo0O0 . o0o0OOO0o0 % i1iII11iiIii
 if 57 - 57: O00o0o0000o0o . I11i1I - III1i1i - o0o0OOO0o0 + o0o00ooo0
 if 63 - 63: o0o00ooo0 * i1iII11iiIii
 if 69 - 69: oOo0oooo00o . OO0O00
 if 49 - 49: iI - oO00OO0oo0
 if 74 - 74: I1i1i1ii * I11i1I + o0o00ooo0 / oOoO / iiIiIIi . I11iii
 if 62 - 62: IIIII * iI
 if 58 - 58: o0o00ooo0 % oo0Oo00Oo0
def i1OOoO ( name , url , iconimage ) :
 if 89 - 89: oo0Oo00Oo0 + OO0O00 * oO00OO0oo0 * III1i1i
 iI11I1II1I1I . setSetting ( 'fav' , 'no' )
 O0OoOoo00o = iiiI11 ( url )
 iiIiI1i1 = [ ]
 oO0O00oOOoooO = [ ]
 IiIi11iI = [ ]
 O0OoOoo00o = iiiI11 ( url )
 o0o = '''<li class="link-button"><a\s+href="(.*?)"'''
 Oo0O00O000 = re . findall ( o0o , O0OoOoo00o )
 O0i1II1Iiii1I11 = 1
 for ooOOoooooo in Oo0O00O000 :
  ooOOoooooo = ooOOoooooo . replace ( '?' , '' )
  ooOOoooooo = 'https://movie25.unblocked.vet/getlink.php?Action=get&' + ooOOoooooo
  oO0O00oOOoooO . append ( 'Link ' + str ( O0i1II1Iiii1I11 ) )
  iiIiI1i1 . append ( ooOOoooooo )
  O0i1II1Iiii1I11 = O0i1II1Iiii1I11 + 1
 o0OO00 = xbmcgui . Dialog ( )
 o0O0OOO0Ooo = o0OO00 . select ( name , oO0O00oOOoooO )
 if o0O0OOO0Ooo < 0 : quit ( )
 else :
  url = iiIiI1i1 [ o0O0OOO0Ooo ]
  i11I1IiII1i1i = iiiI11 ( url )
  i11I1IiII1i1i = i11I1IiII1i1i . replace ( '//' , '' )
  if 'www.' in i11I1IiII1i1i : i11I1IiII1i1i = i11I1IiII1i1i . replace ( 'www.' , 'http://' )
  if not 'http' in i11I1IiII1i1i or 'https' in i11I1IiII1i1i : i11I1IiII1i1i = 'http://' + i11I1IiII1i1i
  iiIiI ( name , i11I1IiII1i1i , iconimage )
  if 95 - 95: O00o0o0000o0o
def iI1111iiii ( name , url , iconimage ) :
 O0OoOoo00o = iiiI11 ( url )
 OOoO00o = re . compile ( '<div class="item"><a href="(.+?)" title=".+?">.+?<img src="(.+?)" border=".+?" width=".+?" height=".+?" alt="Watch (.+?)"></a></div>' , re . DOTALL ) . findall ( O0OoOoo00o )
 for url , iconimage , name in OOoO00o :
  url = 'http://www.gowatchfreemovies.to' + url
  iconimage = 'http:' + iconimage
  name = name . replace ( "&#39;" , "'" ) . replace ( '&amp;' , ' & ' )
  if 'tv-show' in url :
   Ooo00O00O0O0O ( name , url , 28 , iconimage , iIiiiI1IiI1I1 )
   if 67 - 67: IIIII / iI * III1i1i + oO00OO0oo0
   if 65 - 65: IIIII - I11i1I / oo0OO / iiIiIIi / oOoO
def o00oo0 ( url ) :
 Iii111II = ''
 I11ii1IIiIi = xbmc . Keyboard ( Iii111II , '[COLOR white]Enter Search Term[/COLOR]' )
 I11ii1IIiIi . doModal ( )
 if I11ii1IIiIi . isConfirmed ( ) :
  Iii111II = I11ii1IIiIi . getText ( ) . replace ( ' ' , '+' )
  if len ( Iii111II ) > 1 :
   url = "http://www.gowatchfreemovies.to/?keyword=" + Iii111II
   iI1111iiii ( II111iiii , url , oOoOo00oOo )
  else : quit ( )
  if 54 - 54: I1i1i1ii % I11i1I - ooOOOo0oo0O0 / o0o0OOO0o0 - OO0O00 . oO00OO0oo0
def O0OOO0OOoO0O ( ) :
 II = '0'
 Ooo00O00O0O0O ( '[COLOR gold]**** Yerli Yeni Eklenenler Diziler 1 ****[/COLOR]' , II , 25 , 'https://imgur.com/sSsovgK.jpg' , iIiiiI1IiI1I1 , description = '' )
 if 11 - 11: I11i1I . OO0O00 * iIii11I * IIIII + oo0OO
def IiII111i1i11 ( url ) :
 OOOOoOoo0O0O0 = ddizi . TVShows ( url )
 OOoO00o = re . compile ( '<start>(.+?)<sep>(.+?)<sep>(.+?)<end>' ) . findall ( str ( OOOOoOoo0O0O0 ) )
 for II111iiii , url , oOoOo00oOo in OOoO00o :
  I1I ( II111iiii , url , 26 , oOoOo00oOo , iIiiiI1IiI1I1 , description = '' )
 try :
  i111iIi1i1II1 = re . compile ( '<np>(.+?)<np>' ) . findall ( str ( OOOOoOoo0O0O0 ) ) [ 0 ]
  Ooo00O00O0O0O ( '[COLOR red]Next Page >>>[/COLOR]' , i111iIi1i1II1 , 25 , o0OOO , iIiiiI1IiI1I1 , description = '' )
 except : pass
 xbmc . executebuiltin ( 'Container.SetViewMode(50)' )
 if 86 - 86: I1i1i1ii / o0o00ooo0 . iiIiIIi
def II1i111Ii1i ( name , url , iconimage ) :
 iii1 = ddizi . Parts ( url )
 iii1 = iii1 [ 1 : ]
 ooO0oooOO0 = len ( iii1 )
 if ooO0oooOO0 > 1 :
  IiII = [ ]
  O0i1II1Iiii1I11 = 1
  for o0ooo0 in iii1 :
   IiII . append ( 'Part ' + str ( O0i1II1Iiii1I11 ) )
   O0i1II1Iiii1I11 = O0i1II1Iiii1I11 + 1
   o0OO00 = xbmcgui . Dialog ( )
  o0O0OOO0Ooo = o0OO00 . select ( 'Choose a Part..' , IiII )
  if o0O0OOO0Ooo < 0 : quit ( )
  url = iii1 [ o0O0OOO0Ooo ]
 oOOOoo00 = ddizi . Stream ( url )
 iiIiI ( name , oOOOoo00 , iconimage )
 if 9 - 9: oOo0oooo00o % oOo0oooo00o - oo0Oo00Oo0
def O00Oo000ooO0 ( ) :
 Ooo00O00O0O0O ( '[COLOR gold]**** Yerli Yeni Eklenenler Diziler 2 ****[/COLOR]' , 'http://www.canlidizihd6.com/' , 36 , 'https://imgur.com/sSsovgK.jpg' , iIiiiI1IiI1I1 , description = '' )
 if 51 - 51: iI . I1i1i1ii - I11i1I / oOo0oooo00o
def OOOoO00 ( name , url , iconimage ) :
 OOOOoOoo0O0O0 = canlidizi . TVShows ( name , url , iconimage )
 OOoO00o = re . compile ( '<start>(.+?)<sep>(.+?)<sep>(.+?)<end>' ) . findall ( str ( OOOOoOoo0O0O0 ) )
 for name , url , iconimage in OOoO00o :
  I1I ( name , url , 37 , iconimage , iIiiiI1IiI1I1 , description = '' )
 try :
  i111iIi1i1II1 = re . compile ( '<np>(.+?)<np>' ) . findall ( str ( OOOOoOoo0O0O0 ) ) [ 0 ]
  Ooo00O00O0O0O ( '[COLOR red]Next Page >>>[/COLOR]' , i111iIi1i1II1 , 36 , o0OOO , iIiiiI1IiI1I1 , description = '' )
 except : pass
 xbmc . executebuiltin ( 'Container.SetViewMode(50)' )
 if 40 - 40: I11i1I % iI . oo0OO . oOo0oooo00o * ii11I
def i11II1I11I1 ( name , url , iconimage ) :
 iii1 = canlidizi . Parts ( url )
 ooO0oooOO0 = len ( iii1 )
 if ooO0oooOO0 > 1 :
  IiII = [ ]
  O0i1II1Iiii1I11 = 1
  for o0ooo0 in iii1 :
   IiII . append ( 'Part ' + str ( O0i1II1Iiii1I11 ) )
   O0i1II1Iiii1I11 = O0i1II1Iiii1I11 + 1
   o0OO00 = xbmcgui . Dialog ( )
  o0O0OOO0Ooo = o0OO00 . select ( 'Choose a Part..' , IiII )
  if o0O0OOO0Ooo < 0 : quit ( )
  url = iii1 [ o0O0OOO0Ooo ]
 oOOOoo00 = canlidizi . Stream ( url )
 iiIiI ( name , oOOOoo00 , iconimage )
 if 67 - 67: iI - oo0Oo00Oo0 / oO00OO0oo0 - oOoO
def IIIIii ( ) :
 Ooo00O00O0O0O ( '[COLOR gold]**** TRT Yerli Yeni Eklenenler Diziler ****[/COLOR]' , II , 45 , 'https://i.imgur.com/aj2qWim.jpg' , iIiiiI1IiI1I1 , description = '' )
 if 1 - 1: iiIiIIi
def O0oOo00o ( ) :
 Ooo00O00O0O0O ( '[COLOR gold]DIZI[/COLOR]' , 'https://www.trt.tv/2/diziler' , 21 , 'https://i.imgur.com/iPYtEw3.jpg' , iIiiiI1IiI1I1 , description = '' )
 Ooo00O00O0O0O ( '[COLOR gold]PROGRAM[/COLOR]' , 'https://www.trt.tv/20149/programlar' , 21 , 'https://i.imgur.com/4UqUUIg.jpg' , iIiiiI1IiI1I1 , description = '' )
 Ooo00O00O0O0O ( '[COLOR gold]BELGESEL[/COLOR]' , 'https://www.trt.tv/20153/belgesel' , 21 , 'https://i.imgur.com/HEI8Ctt.jpg' , iIiiiI1IiI1I1 , description = '' )
 Ooo00O00O0O0O ( '[COLOR gold]COCUK[/COLOR]' , 'https://www.trt.tv/20157/cocuk' , 21 , 'https://i.imgur.com/ZW5eOgl.jpg' , iIiiiI1IiI1I1 , description = '' )
 if 81 - 81: iIii11I % oOoO . I1i1i1ii
def Ii1Iii1iIi ( url ) :
 OOOOoOoo0O0O0 = trt . Shows ( url )
 OOoO00o = re . compile ( '<start>(.+?)<sep>(.+?)<sep>(.+?)<end>' ) . findall ( str ( OOOOoOoo0O0O0 ) )
 for II111iiii , url , oOoOo00oOo in OOoO00o :
  I1I ( II111iiii , url , 22 , oOoOo00oOo , iIiiiI1IiI1I1 , description = '' )
 xbmc . executebuiltin ( 'Container.SetViewMode(500)' )
 if 82 - 82: I11i1I / iI % I1i1i1ii / oOoO - iI
def I1III1111iIi ( name , url , iconimage ) :
 I1i111I = [ ]
 Ooo = [ ]
 Oo0oo0O0o00O = [ ]
 O0OoOoo00o = iiiI11 ( url )
 I1i11 = re . compile ( '<div class="item_height col-lg-2 col-md-2 col-sm-3 col-xs-4 col-xxs-6" title="">.+?<a href="(.+?)">.+?<img src=".+?" class="play" alt="izle" />.+?<img src="(.+?)?v=.+?" alt="(.+?)" class="img-responsive has_tooltip" />' , re . DOTALL ) . findall ( O0OoOoo00o )
 for url , iconimage , name in I1i11 :
  url = 'https://www.trt.tv' + url
  name = name . replace ( '&quot;' , '"' ) . replace ( "&#231;" , "c" ) . replace ( "&#199;" , "C" ) . replace ( "&#252;" , "u" ) . replace ( "&#220;" , "U" ) . replace ( "&#214;" , "O" ) . replace ( "&#246;" , "o" ) . replace ( "&#39;" , "'" )
  Ooo . append ( name )
  I1i111I . append ( url )
 o0OO00 = xbmcgui . Dialog ( )
 o0O0OOO0Ooo = o0OO00 . select ( 'Bolumler' , Ooo )
 if o0O0OOO0Ooo < 0 : quit ( )
 oOOOoo00 = trt . Stream ( url )
 iiIiI ( name , oOOOoo00 , iconimage )
 if 12 - 12: oOoO + oOoO - I11i1I * I11iii % I11iii - iiIiIIi
def O0o0 ( ) :
 Ooo00O00O0O0O ( '[COLOR gold]**** KANAL D Yerli Yeni Eklenenler Diziler ****[/COLOR]' , 'http://engelsiz.kanald.com.tr/' , 46 , 'https://i.imgur.com/dyXtiSo.jpg' , iIiiiI1IiI1I1 , description = '' )
 if 52 - 52: oo0OO . i1iII11iiIii + ii11I
def iiii1IIi ( url ) :
 OOOOoOoo0O0O0 = kanald . Shows ( url )
 OOoO00o = re . compile ( '<start>(.+?)<sep>(.+?)<sep>(.+?)<end>' ) . findall ( str ( OOOOoOoo0O0O0 ) )
 for II111iiii , url , oOoOo00oOo in OOoO00o :
  I1I ( II111iiii , url , 47 , oOoOo00oOo , iIiiiI1IiI1I1 , description = '' )
 xbmc . executebuiltin ( 'Container.SetViewMode(500)' )
 if 33 - 33: o0o00ooo0 * ooOOOo0oo0O0 - iiIiIIi
def OOo0o0O0O ( name , url ) :
 I1i111I = [ ]
 Ooo = [ ]
 O0OoOoo00o = iiiI11 ( url )
 o0OO0o0oOOO0O = re . compile ( '<div class="list">(.+?)</select>' , re . DOTALL ) . findall ( O0OoOoo00o ) [ 0 ]
 I1i11 = re . compile ( '<option value="(.+?)" >(.+?)</option>' ) . findall ( o0OO0o0oOOO0O )
 for url , name in I1i11 :
  url = 'http://engelsiz.kanald.com.tr/Video/Detail/' + url
  name = name . replace ( '&quot;' , '"' ) . replace ( "&#231;" , "c" ) . replace ( "&#199;" , "C" ) . replace ( "&#252;" , "u" ) . replace ( "&#220;" , "U" ) . replace ( "&#214;" , "O" ) . replace ( "&#246;" , "o" ) . replace ( "&#39;" , "'" )
  Ooo . append ( name )
  I1i111I . append ( url )
 o0OO00 = xbmcgui . Dialog ( )
 o0O0OOO0Ooo = o0OO00 . select ( 'Bolumler' , Ooo )
 if o0O0OOO0Ooo < 0 : quit ( )
 oOOOoo00 = kanald . Stream ( url )
 iiIiI ( name , oOOOoo00 , oOoOo00oOo )
 if 49 - 49: I11i1I . oo0Oo00Oo0 . iiIiIIi
def OO00Oo ( ) :
 Ooo00O00O0O0O ( '[COLOR gold]**** SHOWTV Yerli Yeni Eklenenler Diziler ****[/COLOR]' , 'http://www.showturk.com.tr/diziler/arsivdeki-diziler' , 48 , 'https://i.imgur.com/in8nCB9.jpg' , iIiiiI1IiI1I1 , description = '' )
 if 98 - 98: i1iII11iiIii
def OooooO0oOOOO ( name , url , iconimage ) :
 OOOOoOoo0O0O0 = showt . STShows ( url )
 OOoO00o = re . compile ( '<start>(.+?)<sep>(.+?)<sep>(.+?)<end>' ) . findall ( str ( OOOOoOoo0O0O0 ) )
 for name , url , iconimage in OOoO00o :
  Ooo00O00O0O0O ( name , url , 49 , iconimage , iIiiiI1IiI1I1 , description = '' )
 xbmc . executebuiltin ( 'Container.SetViewMode(500)' )
 if 100 - 100: i1iII11iiIii % ooOOOo0oo0O0
def OOO ( name , url , iconimage ) :
 OOOOoOoo0O0O0 = showt . STEpisodes ( name , url )
 OOoO00o = re . compile ( '<start>(.+?)<sep>(.+?)<end>' ) . findall ( str ( OOOOoOoo0O0O0 ) )
 for name , url in OOoO00o :
  Ooo00O00O0O0O ( name , url , 50 , iconimage , iIiiiI1IiI1I1 , description = '' )
 xbmc . executebuiltin ( 'Container.SetViewMode(50)' )
 if 6 - 6: IIIII
def iI1iIii11Ii ( url ) :
 IIi1i1I11Iii = [ ]
 O0OoOoo00o = iiiI11 ( url )
 IIi1i1I11Iii . append ( url )
 o0OO0o0oOOO0O = re . compile ( '<ul class="video-part-number">(.+?)</ul>' , re . DOTALL ) . findall ( O0OoOoo00o ) [ 0 ]
 I1i11 = re . compile ( '<a href="(.+?)">(.+?)</a></li>' ) . findall ( o0OO0o0oOOO0O )
 for I1i1i1 , II111iiii in I1i11 :
  I1i1i1 = 'http://www.showtv.com.tr' + I1i1i1
  IIi1i1I11Iii . append ( I1i1i1 )
  I1I ( 'Parca %s' % II111iiii , I1i1i1 , 51 , oOoOo00oOo , iIiiiI1IiI1I1 , description = '' )
  if 73 - 73: oOo0oooo00o * i1iII11iiIii + III1i1i + oo0OO
def Ii ( name , url , iconimage ) :
 O0OoOoo00o = iiiI11 ( url )
 OOoO00o = re . compile ( '<meta name="popcorn:stream" content="(.+?)" />' , re . DOTALL ) . findall ( O0OoOoo00o )
 for url in OOoO00o :
  o0O0Oo ( name , url , iconimage )
  if 62 - 62: oOo0oooo00o % oO00OO0oo0 . oO00OO0oo0 - I1i1i1ii / O00o0o0000o0o
def o0 ( ) :
 Ooo00O00O0O0O ( '[COLOR green]----- Football Highlights -----[/COLOR]' , 'null' , 60 , 'https://i.imgur.com/ngEfHX3.jpg' , iIiiiI1IiI1I1 )
 if 31 - 31: I1i1i1ii / OO0O00 / I11i1I
def iiIiIi ( ) :
 i11IiIiiIiII = [ '[COLOR white][B]Source 1[/B][/COLOR]' ]
 iiIIi = [ 'http://www.ngolos.com/' ]
 o0O0OOO0Ooo = o0OO00 . select ( '[B][COLOR white]What Source Would You Like?[/COLOR][/B]' , i11IiIiiIiII )
 if o0O0OOO0Ooo < 0 : quit ( )
 II = iiIIi [ o0O0OOO0Ooo ]
 if 'http://www.ngolos.com/' in II :
  iiI1iI111ii1i ( II111iiii , II , oOoOo00oOo )
 else : pass
 if 32 - 32: iiIiIIi * o0o00ooo0 % oOoO - i1iII11iiIii + I1i1i1ii + I11i1I
def iiI1iI111ii1i ( name , url , iconimage ) :
 OOOOoOoo0O0O0 = footballh2 . FHContent ( name , url , iconimage )
 OOoO00o = re . compile ( '<start>(.+?)<sep>(.+?)<end>' ) . findall ( str ( OOOOoOoo0O0O0 ) )
 for name , OO0O0Oo000 in OOoO00o :
  I1I ( name , OO0O0Oo000 , 53 , iconimage , iIiiiI1IiI1I1 , description = '' )
 try :
  o0OOO = requests . get ( url ) . content
  o0o = '''href=['"]([^'"]+)['"]\s*aria-label="Next"'''
  i111iIi1i1II1 = re . findall ( o0o , o0OOO ) [ 0 ]
  if not 'https' in i111iIi1i1II1 : i111iIi1i1II1 = 'https://www.ngolos.com' + i111iIi1i1II1
  Ooo00O00O0O0O ( '[COLOR white][B]Next Page -->[/B][/COLOR]' , i111iIi1i1II1 , 52 , iconimage , iIiiiI1IiI1I1 , description = '' )
 except : pass
 if 41 - 41: oOoO - oO00OO0oo0 - III1i1i
def III11I1 ( name , url , iconimage ) :
 O0OoOoo00o = iiiI11 ( url )
 OOoO00o = re . findall ( '<iframe.+?src="(.*?)"' , O0OoOoo00o , flags = re . DOTALL )
 O0OoOoo00o = 0
 IIi1IIIi = [ ]
 ooOOoooooo = [ ]
 o0OO00 = xbmcgui . Dialog ( )
 for O00Ooo in OOoO00o :
  if not 'http' in O00Ooo : O00Ooo = 'http:' + O00Ooo
  O0OoOoo00o += 1
  name = 'Link | ' + str ( O0OoOoo00o )
  IIi1IIIi . append ( name )
  if 'soccerclips' in O00Ooo :
   O00Ooo = OOOO0OOO ( O00Ooo )
  elif 'streamja' in O00Ooo :
   O00Ooo = OOOO0OOO ( O00Ooo )
  elif 'streamable' in O00Ooo :
   O00Ooo = OOOO0OOO ( O00Ooo )
  ooOOoooooo . append ( O00Ooo )
 o0OO00 = xbmcgui . Dialog ( )
 o0O0OOO0Ooo = o0OO00 . select ( '[B][COLOR white]Pick A Link[/COLOR][/B]' , IIi1IIIi )
 if o0O0OOO0Ooo < 0 : quit ( )
 else :
  OO0O0Oo000 = ooOOoooooo [ o0O0OOO0Ooo ]
  iiIiI ( 'UK Turks' , OO0O0Oo000 , iconimage )
  if 3 - 3: OO0O00
def OOOO0OOO ( games ) :
 if 97 - 97: ii11I
 if 'soccerclips' in games :
  O0OoOoo00o = requests . get ( games ) . content
  i11I1IiII1i1i = re . findall ( 'hls:"(.*?)"' , O0OoOoo00o ) [ 0 ]
  if not 'http' in i11I1IiII1i1i : i11I1IiII1i1i = 'http:' + i11I1IiII1i1i
  return i11I1IiII1i1i
 elif 'streamja' in games :
  O0OoOoo00o = requests . get ( games ) . content
  i11I1IiII1i1i = re . findall ( '<source src="(.*?)"' , O0OoOoo00o ) [ 0 ]
  return i11I1IiII1i1i
 elif 'streamable' in games :
  O0OoOoo00o = requests . get ( games ) . content
  o0o = '''href=['"]([^'"]+)['"].+?id="download"'''
  i11I1IiII1i1i = re . findall ( o0o , O0OoOoo00o ) [ 0 ]
  i11I1IiII1i1i = i11I1IiII1i1i . replace ( 'amp;' , '' )
  if not 'https' in i11I1IiII1i1i : i11I1IiII1i1i = 'https:' + i11I1IiII1i1i
  return i11I1IiII1i1i
  if 15 - 15: oOoO + o0o00ooo0
def iii1i1I1i1 ( name , url , iconimage ) :
 O0OoOoo00o = iiiI11 ( url )
 iiIiI1i1 = [ ]
 oO0O00oOOoooO = [ ]
 IiIi11iI = [ ]
 OOoO00o = re . compile ( 'addthis_inline_share_toolbox(.+?)%2Fstrong%3E%20' , re . DOTALL ) . findall ( O0OoOoo00o ) [ 0 ]
 ooOOoooooo = re . compile ( 'src%3D%22(.+?)%22' , re . DOTALL ) . findall ( OOoO00o )
 O0i1II1Iiii1I11 = 1
 for iI1 in ooOOoooooo :
  iI1 = iI1 . replace ( '%3A' , ':' ) . replace ( '%2F' , '/' )
  iIIi = iI1
  oO0o00oo0 = iI1
  if 'ok.ru' in iI1 :
   iI1 = 'http:' + iI1
   iiIiI1i1 . append ( iI1 )
   oO0O00oOOoooO . append ( 'Highlights' )
  elif 'streamable' in iI1 :
   iI1 = iI1 . replace ( '/e/' , '/' )
   iiIiI1i1 . append ( iI1 )
   oO0O00oOOoooO . append ( 'Highlights' )
  elif 'imgtc' in iI1 :
   iiIiI1i1 . append ( iI1 )
   oO0O00oOOoooO . append ( 'Goals' )
  elif 'mixtape' in iI1 :
   iiIiI1i1 . append ( iI1 )
   oO0O00oOOoooO . append ( 'Highlights' )
  elif 'youtube' in iI1 :
   iiIiI1i1 . append ( iI1 )
   oO0O00oOOoooO . append ( 'Highlights' )
  else :
   iiIiI1i1 . append ( iI1 )
   oO0O00oOOoooO . append ( oO0o00oo0 )
  O0i1II1Iiii1I11 = O0i1II1Iiii1I11 + 1
 o0OO00 = xbmcgui . Dialog ( )
 o0O0OOO0Ooo = o0OO00 . select ( name , oO0O00oOOoooO )
 if o0O0OOO0Ooo < 0 : quit ( )
 else :
  url = iiIiI1i1 [ o0O0OOO0Ooo ]
  iiIiI ( name , url , iconimage )
  if 19 - 19: iiIiIIi + iIii11I
  if 53 - 53: o0o0OOO0o0 - iI - o0o0OOO0o0 * i1iII11iiIii
  if 71 - 71: oOo0oooo00o - I1i1i1ii
  if 12 - 12: ooOOOo0oo0O0 / oo0Oo00Oo0
  if 42 - 42: I11iii
def II1IIiiIiI ( ) :
 Ooo00O00O0O0O ( 'Highlights' , 'http://www.fullmatchesandshows.com/category/highlights/' , 33 , 'https://imgur.com/BpSTg2U.jpg' , iIiiiI1IiI1I1 )
 Ooo00O00O0O0O ( 'More Highlights' , 'http://www.fullmatchesandshows.com/category/full-match/' , 33 , 'https://i.imgur.com/C9zY6wt.jpg' , iIiiiI1IiI1I1 )
 Ooo00O00O0O0O ( 'Premier League' , 'http://www.fullmatchesandshows.com/category/premier-league/' , 33 , 'https://imgur.com/GDmfQXD.jpg' , iIiiiI1IiI1I1 )
 Ooo00O00O0O0O ( 'England' , 'http://www.fullmatchesandshows.com/category/england/' , 33 , 'https://imgur.com/BrIh7BK.jpg' , iIiiiI1IiI1I1 )
 Ooo00O00O0O0O ( 'Spain' , 'http://www.fullmatchesandshows.com/category/spain/' , 33 , 'https://imgur.com/CjgZZi9.jpg' , iIiiiI1IiI1I1 )
 Ooo00O00O0O0O ( 'Italy' , 'http://www.fullmatchesandshows.com/category/italy' , 33 , 'https://imgur.com/Hj8QfvY.jpg' , iIiiiI1IiI1I1 )
 if 1 - 1: i1iII11iiIii
def O0O0Ooo ( name , url , iconimage ) :
 OOOOoOoo0O0O0 = footballh . FHighlights ( name , url , iconimage )
 OOoO00o = re . compile ( '<start>(.+?)<sep>(.+?)<sep>(.+?)<end>' ) . findall ( str ( OOOOoOoo0O0O0 ) )
 for name , url , iconimage in OOoO00o :
  I1I ( name , url , 34 , iconimage , iIiiiI1IiI1I1 , description = '' )
 try :
  i111iIi1i1II1 = re . compile ( '<np>(.+?)<np>' ) . findall ( str ( OOOOoOoo0O0O0 ) )
  for url in i111iIi1i1II1 :
   Ooo00O00O0O0O ( '[COLOR red]Next Page >>>[/COLOR]' , url , oOoO0 , o0OOO , iIiiiI1IiI1I1 )
 except : pass
 xbmc . executebuiltin ( 'Container.SetViewMode(500)' )
 if 77 - 77: I1i1i1ii . i1iII11iiIii % i1iII11iiIii + O00o0o0000o0o
def Oo00o0OO0O00o ( name , url , iconimage ) :
 O0OoOoo00o = iiiI11 ( url )
 iiIiI1i1 = [ ]
 oO0O00oOOoooO = [ ]
 IiIi11iI = [ ]
 ooOOoooooo = footballh . FHStream ( url )
 O0i1II1Iiii1I11 = 1
 for iI1 in ooOOoooooo :
  iIIi = iI1
  if 'ok.ru' in iI1 :
   iI1 = 'http:' + iI1
   oO0o00oo0 = iI1 . split ( '/' ) [ 2 ] . replace ( 'www.' , '' )
   iiIiI1i1 . append ( iI1 )
   oO0O00oOOoooO . append ( 'Link ' + str ( O0i1II1Iiii1I11 ) )
  else :
   oO0o00oo0 = iI1 . split ( '/' ) [ 2 ] . replace ( 'www.' , '' )
   iiIiI1i1 . append ( iI1 )
   oO0O00oOOoooO . append ( 'Link ' + str ( O0i1II1Iiii1I11 ) )
  O0i1II1Iiii1I11 = O0i1II1Iiii1I11 + 1
 o0OO00 = xbmcgui . Dialog ( )
 o0O0OOO0Ooo = o0OO00 . select ( name , oO0O00oOOoooO )
 if o0O0OOO0Ooo < 0 : quit ( )
 else :
  url = iiIiI1i1 [ o0O0OOO0Ooo ]
  iiIiI ( name , url , iconimage )
  if 82 - 82: oO00OO0oo0 + IIIII - oOoO . oOoO
def i1OOO ( ) :
 Ooo00O00O0O0O ( 'A-Z Movies' , 'https://movie4u.ch' , 39 , 'https://i.imgur.com/T7zT3pI.jpg' , iIiiiI1IiI1I1 )
 if 6 - 6: oo0Oo00Oo0 / oO00OO0oo0 / iiIiIIi
def I1i11111i1i11 ( name , url , iconimage ) :
 Ooo00O00O0O0O ( '[COLOR blue]SEARCH A-Z[/COLOR]' , 'https://movie4u.ch' , 42 , 'https://i.imgur.com/ca4Sx8p.jpg' , iIiiiI1IiI1I1 )
 O0OoOoo00o = iiiI11 ( url )
 OOoO00o = re . compile ( '<li><a href="(.+?)" >(.+?)</a></li>' ) . findall ( O0OoOoo00o )
 for url , name in OOoO00o :
  name = name . replace ( '#' , '0-9' )
  if '/?letter=' in url :
   Ooo00O00O0O0O ( '[B][COLOR white]%s[/COLOR][/B]' % name , url , 40 , 'https://i.imgur.com/5fUZukf.jpg' , iIiiiI1IiI1I1 )
   if 77 - 77: I11i1I + OO0O00 / o0o0OOO0o0 + oOo0oooo00o * oo0Oo00Oo0
def I1ii11 ( name , url , iconimage ) :
 OOOOoOoo0O0O0 = atoz . Content ( name , url , iconimage )
 OOoO00o = re . compile ( '<start>(.+?)<sep>(.+?)<sep>(.+?)<end>' ) . findall ( str ( OOOOoOoo0O0O0 ) )
 for name , url , iconimage in OOoO00o :
  I1I ( name , url , 41 , iconimage , iIiiiI1IiI1I1 , description = '' )
 try :
  i111iIi1i1II1 = re . compile ( '<np>(.+?)<np>(.+?)<np>' ) . findall ( str ( OOOOoOoo0O0O0 ) )
  for oOoOoOoo0 , url in i111iIi1i1II1 :
   Ooo00O00O0O0O ( '[COLOR red]%s[/COLOR]' % oOoOoOoo0 , url , 40 , o0OOO , iIiiiI1IiI1I1 )
 except : pass
 xbmc . executebuiltin ( 'Container.SetViewMode(500)' )
 if 34 - 34: o0o00ooo0 - ooOOOo0oo0O0 + oOo0oooo00o . III1i1i
def iIi1i1iIi1iI ( name , url , iconimage ) :
 O0OoOoo00o = iiiI11 ( url )
 iiIiI1i1 = [ ]
 oO0O00oOOoooO = [ ]
 IiIi11iI = [ ]
 ooOOoooooo = atoz . Stream ( url )
 O0i1II1Iiii1I11 = 1
 for iI1 in ooOOoooooo :
  iIIi = iI1
  oO0o00oo0 = iI1 . split ( '/' ) [ 2 ] . replace ( 'www.' , '' )
  iiIiI1i1 . append ( iI1 )
  oO0O00oOOoooO . append ( 'Link ' + str ( O0i1II1Iiii1I11 ) )
  O0i1II1Iiii1I11 = O0i1II1Iiii1I11 + 1
 o0OO00 = xbmcgui . Dialog ( )
 o0O0OOO0Ooo = o0OO00 . select ( name , oO0O00oOOoooO )
 if o0O0OOO0Ooo < 0 : quit ( )
 else :
  url = iiIiI1i1 [ o0O0OOO0Ooo ]
  iiIiI ( name , url , iconimage )
  if 26 - 26: IIIII * iI + ooOOOo0oo0O0
def IiIii1i111 ( name , url , iconimage ) :
 Iii111II = ''
 I11ii1IIiIi = xbmc . Keyboard ( Iii111II , '[COLOR white]Enter Search Term[/COLOR]' )
 I11ii1IIiIi . doModal ( )
 if I11ii1IIiIi . isConfirmed ( ) :
  Iii111II = I11ii1IIiIi . getText ( ) . replace ( ' ' , '+' )
  if len ( Iii111II ) > 1 :
   url = "https://movie4u.ch/?s=" + Iii111II
   iIo0o00 ( name , url , iconimage )
  else : quit ( )
  if 14 - 14: oo0Oo00Oo0 . ooOOOo0oo0O0 . oO00OO0oo0 + IIIII - ooOOOo0oo0O0 + iIii11I
def iIo0o00 ( name , url , iconimage ) :
 O0OoOoo00o = iiiI11 ( url )
 iII1iiiiIII = re . compile ( '<div class="thumbnail animation-2">.+?<a href="(.+?)">.+?<img src="(.+?)" alt="(.+?)" />' , re . DOTALL ) . findall ( O0OoOoo00o )
 for url , iconimage , name in iII1iiiiIII :
  name = name . replace ( "&#8217;" , "'" ) . replace ( "&#8211;" , "-" ) . replace ( "&#038;" , "&" )
  I1I ( name , url , 41 , iconimage , iIiiiI1IiI1I1 , description = '' )
  if 78 - 78: ooOOOo0oo0O0 * oo0Oo00Oo0 / oO00OO0oo0 - oOo0oooo00o / iIii11I
def i1i ( item ) :
 II111iiii = re . compile ( '<title>(.+?)</title>' ) . findall ( item ) [ 0 ]
 oOoOo00oOo = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( item ) [ 0 ]
 II = re . compile ( '<scraper>(.+?)</scraper>' ) . findall ( item ) [ 0 ]
 Ooo00O00O0O0O ( II111iiii , II , 20 , oOoOo00oOo , iIiiiI1IiI1I1 )
 if 96 - 96: o0o00ooo0 . oo0Oo00Oo0 - oo0OO
def O0OI11iiiii1II ( url , iconimage ) :
 Iii111II = url + '.scrape()'
 O0OoOoo00o = eval ( Iii111II )
 OOoO00o = re . compile ( '<item>(.+?)</item>' , re . DOTALL ) . findall ( O0OoOoo00o )
 IiII = str ( len ( OOoO00o ) )
 iI11I1II1I1I . setSetting ( 'count' , IiII )
 iI11I1II1I1I . setSetting ( 'fav' , 'no' )
 for iII1i1I1II in OOoO00o :
  try :
   if '<sportsdevil>' in iII1i1I1II : OOoOO0oo0ooO ( iII1i1I1II , url , iconimage )
   elif '<iptv>' in iII1i1I1II : O0o0O00Oo0o0 ( iII1i1I1II )
   elif '<Image>' in iII1i1I1II : O00O0oOO00O00 ( iII1i1I1II )
   elif '<text>' in iII1i1I1II : i1Oo00 ( iII1i1I1II )
   elif '<scraper>' in iII1i1I1II : i1i ( iII1i1I1II )
   elif '<redirect>' in iII1i1I1II : REDIRECT ( iII1i1I1II )
   elif '<oktitle>' in iII1i1I1II : iiI111I1iIiI ( iII1i1I1II )
   elif '<dl>' in iII1i1I1II : IIIi1I1IIii1II ( iII1i1I1II )
   elif '<scraper>' in iII1i1I1II : i1i ( iII1i1I1II , iconimage )
   else : O0ii1ii1ii ( iII1i1I1II , url , iconimage )
  except : pass
  if 51 - 51: oOo0oooo00o % o0o0OOO0o0 - iiIiIIi
def IIIi1I1IIii1II ( item ) :
 II111iiii = re . compile ( '<title>(.+?)</title>' ) . findall ( item ) [ 0 ]
 II = re . compile ( '<dl>(.+?)</dl>' ) . findall ( item ) [ 0 ]
 oOoOo00oOo = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( item ) [ 0 ]
 I1II ( II111iiii , II , 19 , oOoOo00oOo , iIiiiI1IiI1I1 )
 if 64 - 64: oOo0oooo00o % oO00OO0oo0 % oOo0oooo00o * OO0O00 . o0o0OOO0o0 + iI
def O00 ( name , url ) :
 I11ii1i1 = url . split ( '/' ) [ - 1 ]
 if I11ii1i1 == 'latest' : I11ii1i1 = 'AceStreamEngine.apk'
 import downloader
 o0OO00 = xbmcgui . Dialog ( )
 ooo0OoOOOOO = xbmcgui . DialogProgress ( )
 i1iIi1iI = o0OO00 . browse ( 0 , 'Select folder to download to' , 'myprograms' )
 oOOo0 = os . path . join ( i1iIi1iI , I11ii1i1 )
 ooo0OoOOOOO . create ( 'Downloading' , '' , '' , 'Please Wait' )
 downloader . download ( url , oOOo0 , ooo0OoOOOOO )
 ooo0OoOOOOO . close ( )
 o0OO00 = xbmcgui . Dialog ( )
 o0OO00 . ok ( 'Download complete' , 'Please install from..' , i1iIi1iI )
 if 39 - 39: ii11I
def iiI111I1iIiI ( item ) :
 II111iiii = re . compile ( '<title>(.+?)</title>' ) . findall ( item ) [ 0 ]
 O0OoO0ooOO0o = re . compile ( '<oktitle>(.+?)</oktitle>' ) . findall ( item ) [ 0 ]
 OoOo0oOooOoOO = re . compile ( '<line1>(.+?)</line1>' ) . findall ( item ) [ 0 ]
 oo00ooOoO00 = re . compile ( '<line2>(.+?)</line2>' ) . findall ( item ) [ 0 ]
 o00oOoOo0 = re . compile ( '<line3>(.+?)</line3>' ) . findall ( item ) [ 0 ]
 o0O0O0ooo0oOO = '##' + O0OoO0ooOO0o + '#' + OoOo0oOooOoOO + '#' + oo00ooOoO00 + '#' + o00oOoOo0 + '##'
 oOoOo00oOo = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( item ) [ 0 ]
 I1II ( II111iiii , o0O0O0ooo0oOO , 17 , oOoOo00oOo , iIiiiI1IiI1I1 )
 if 97 - 97: iI / i1iII11iiIii
def Oooo0 ( name , url ) :
 oOO = re . compile ( '##(.+?)##' ) . findall ( url ) [ 0 ] . split ( '#' )
 o0OO00 = xbmcgui . Dialog ( )
 o0OO00 . ok ( oOO [ 0 ] , oOO [ 1 ] , oOO [ 2 ] , oOO [ 3 ] )
 if 54 - 54: iI / I1i1i1ii / ooOOOo0oo0O0 . ooOOOo0oo0O0 % i1iII11iiIii . iI
def i1Oo00 ( item ) :
 II111iiii = re . compile ( '<title>(.+?)</title>' ) . findall ( item ) [ 0 ]
 o0O0O0ooo0oOO = re . compile ( '<text>(.+?)</text>' ) . findall ( item ) [ 0 ]
 oOoOo00oOo = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( item ) [ 0 ]
 I1II ( II111iiii , o0O0O0ooo0oOO , 9 , oOoOo00oOo , iIiiiI1IiI1I1 )
 if 10 - 10: oo0Oo00Oo0 + ooOOOo0oo0O0
def IIII1i ( name , url ) :
 Ii1IIIIi1ii1I = iiiI11 ( url )
 IiiIiI1Ii1i ( name , Ii1IIIIi1ii1I )
 if 22 - 22: iIii11I / O00o0o0000o0o
def O00O0oOO00O00 ( item ) :
 oOOoo = re . compile ( '<Image>(.+?)</Image>' ) . findall ( item )
 if len ( oOOoo ) == 1 :
  II111iiii = re . compile ( '<title>(.+?)</title>' ) . findall ( item ) [ 0 ]
  oOoOo00oOo = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( item ) [ 0 ]
  iII1111III1I = re . compile ( '<Image>(.+?)</Image>' ) . findall ( item ) [ 0 ]
  oOoOo00oOo = iII1111III1I . replace ( 'http://imgur.com/' , 'http://i.imgur.com/' ) + '.jpg'
  iII1111III1I = iII1111III1I . replace ( 'http://imgur.com/' , 'http://i.imgur.com/' ) + '.jpg'
  I1II ( II111iiii , iII1111III1I , 7 , oOoOo00oOo , iIiiiI1IiI1I1 )
 elif len ( oOOoo ) > 1 :
  II111iiii = re . compile ( '<title>(.+?)</title>' ) . findall ( item ) [ 0 ]
  oOoOo00oOo = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( item ) [ 0 ]
  ii11i = ''
  for iII1111III1I in oOOoo :
   oOoOo00oOo = iII1111III1I . replace ( 'http://imgur.com/' , 'http://i.imgur.com/' ) + '.jpg'
   iII1111III1I = iII1111III1I . replace ( 'http://imgur.com/' , 'http://i.imgur.com/' ) + '.jpg'
   ii11i = ii11i + '<Image>' + iII1111III1I + '</Image>'
  O00oOo00o0o = i1i1II
  II111iiii = Oo0O0O0ooO0O ( II111iiii )
  O00oO0 = os . path . join ( os . path . join ( O00oOo00o0o , '' ) , II111iiii + '.txt' )
  if not os . path . exists ( O00oO0 ) : file ( O00oO0 , 'w' ) . close ( )
  O0Oo00OoOo = open ( O00oO0 , "w" )
  O0Oo00OoOo . write ( ii11i )
  O0Oo00OoOo . close ( )
  I1II ( II111iiii , 'image' , 8 , oOoOo00oOo , iIiiiI1IiI1I1 )
  if 24 - 24: O00o0o0000o0o - ii11I
def O0o0O00Oo0o0 ( item ) :
 II111iiii = re . compile ( '<title>(.+?)</title>' ) . findall ( item ) [ 0 ]
 oOoOo00oOo = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( item ) [ 0 ]
 II = re . compile ( '<iptv>(.+?)</iptv>' ) . findall ( item ) [ 0 ]
 Ooo00O00O0O0O ( II111iiii , II , 6 , oOoOo00oOo , iIiiiI1IiI1I1 )
 if 21 - 21: oO00OO0oo0
def OoO00 ( url , iconimage ) :
 O0OoOoo00o = iiiI11 ( url )
 Oo0O00O000 = re . compile ( '^#.+?:-?[0-9]*(.*?),(.*?)\n(.*?)$' , re . I + re . M + re . U + re . S ) . findall ( O0OoOoo00o )
 OO0Ooooo000Oo = [ ]
 for O0oOoo0o000O0 , II111iiii , url in Oo0O00O000 :
  o00oO0o0o = { "params" : O0oOoo0o000O0 , "name" : II111iiii , "url" : url }
  OO0Ooooo000Oo . append ( o00oO0o0o )
 list = [ ]
 for oo0O0Ooooooo in OO0Ooooo000Oo :
  o00oO0o0o = { "name" : oo0O0Ooooooo [ "name" ] , "url" : oo0O0Ooooooo [ "url" ] }
  Oo0O00O000 = re . compile ( ' (.+?)="(.+?)"' , re . I + re . M + re . U + re . S ) . findall ( oo0O0Ooooooo [ "params" ] )
  for I1IIIiI1I1ii1 , iiiI1I1iIIIi1 in Oo0O00O000 :
   o00oO0o0o [ I1IIIiI1I1ii1 . strip ( ) . lower ( ) . replace ( '-' , '_' ) ] = iiiI1I1iIIIi1 . strip ( )
  list . append ( o00oO0o0o )
 for oo0O0Ooooooo in list :
  if '.ts' in oo0O0Ooooooo [ "url" ] : I1II ( oo0O0Ooooooo [ "name" ] , oo0O0Ooooooo [ "url" ] , 2 , iconimage , iIiiiI1IiI1I1 )
  else : I1I ( oo0O0Ooooooo [ "name" ] , oo0O0Ooooooo [ "url" ] , 2 , iconimage , iIiiiI1IiI1I1 )
  if 17 - 17: I1i1i1ii . IIIII / oO00OO0oo0 % iiIiIIi % oOoO / O00o0o0000o0o
def O0ii1ii1ii ( item , url , iconimage ) :
 OOOIiiiii1iI = iconimage
 IIi = url
 ooOOoooooo = re . compile ( '<link>(.+?)</link>' ) . findall ( item )
 i1IiIiiI = re . compile ( '<title>(.+?)</title>.+?link>(.+?)</link>.+?thumbnail>(.+?)</thumbnail>' , re . DOTALL ) . findall ( item )
 for II111iiii , OO0O0Oo000 , iconimage in i1IiIiiI :
  if 'youtube.com/playlist?' in OO0O0Oo000 :
   ooOooo0 = OO0O0Oo000 . split ( 'list=' ) [ 1 ]
   Ooo00O00O0O0O ( II111iiii , OO0O0Oo000 , oOoO0 , iconimage , iIiiiI1IiI1I1 , description = ooOooo0 )
 if len ( ooOOoooooo ) == 1 :
  II111iiii = re . compile ( '<title>(.+?)</title>' ) . findall ( item ) [ 0 ]
  url = re . compile ( '<link>(.+?)</link>' ) . findall ( item ) [ 0 ]
  iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( item ) [ 0 ]
  print iconimage
  if iconimage == 'ImageHere' : iconimage = OOOIiiiii1iI
  if '.ts' in url : I1II ( II111iiii , url , 16 , iconimage , iIiiiI1IiI1I1 , description = '' )
  elif 'movies' in IIi :
   oO0OO0 ( II111iiii , url , 2 , iconimage , int ( IiII ) , isFolder = False )
  else : I1I ( II111iiii , url , 2 , iconimage , iIiiiI1IiI1I1 )
 elif len ( ooOOoooooo ) > 1 :
  II111iiii = re . compile ( '<title>(.+?)</title>' ) . findall ( item ) [ 0 ]
  iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( item ) [ 0 ]
  if iconimage == 'ImageHere' : iconimage = OOOIiiiii1iI
  if '.ts' in url : I1II ( II111iiii , url , 16 , iconimage , iIiiiI1IiI1I1 , description = '' )
  elif 'movies' in IIi :
   oO0OO0 ( II111iiii , url , 3 , iconimage , int ( IiII ) , isFolder = False )
  else : I1I ( II111iiii , url , 3 , iconimage , iIiiiI1IiI1I1 )
  if 82 - 82: iIii11I - iIii11I + o0o00ooo0
def Oo0OoO00oOO0o ( url ) :
 O0OoOoo00o = iiiI11 ( url )
 II111Ii1i1 = False
 OOoO00o = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)"' , re . DOTALL ) . findall ( O0OoOoo00o )
 if 'tv%20shows' in url or 'cartoons' in url :
  OOoO00o = sorted ( OOoO00o )
  II111Ii1i1 = True
 for II111iiii , url , I11i in OOoO00o :
  if II111iiii [ 0 ] == '0' :
   if II111Ii1i1 == True :
    II111iiii = II111iiii [ 1 : ] + '[COLOR gold]   (New)[/COLOR]'
  if 'youtube.com/playlist?list=' in url :
   Ooo00O00O0O0O ( II111iiii , url , 18 , I11i , iIiiiI1IiI1I1 )
  elif 'youtube.com/results?search_query=' in url :
   Ooo00O00O0O0O ( II111iiii , url , 18 , I11i , iIiiiI1IiI1I1 )
  else :
   Ooo00O00O0O0O ( II111iiii , url , 1 , I11i , iIiiiI1IiI1I1 )
   if 98 - 98: OO0O00 . OO0O00 * o0o0OOO0o0 * iiIiIIi * ii11I
def oOooO0 ( name , url , iconimage ) :
 if 'youtube.com/results?search_query=' in url :
  ooOooo0 = url . split ( 'search_query=' ) [ 1 ]
  OOOoO000 = iiIIIII1i1iI + ooOooo0 + o0oO0
  oOOOO = urllib2 . Request ( OOOoO000 )
  oOOOO . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
  IiIi1ii111i1 = urllib2 . urlopen ( oOOOO )
  O0OoOoo00o = IiIi1ii111i1 . read ( )
  IiIi1ii111i1 . close ( )
  O0OoOoo00o = O0OoOoo00o . replace ( '\r' , '' ) . replace ( '\n' , '' ) . replace ( '  ' , '' )
  OOoO00o = re . compile ( '"videoId": "(.+?)".+?"title": "(.+?)"' , re . DOTALL ) . findall ( O0OoOoo00o )
  for i1i1i1I , name in OOoO00o :
   url = 'https://www.youtube.com/watch?v=' + i1i1i1I
   iconimage = 'https://i.ytimg.com/vi/%s/hqdefault.jpg' % i1i1i1I
   I1I ( name , url , 2 , iconimage , iIiiiI1IiI1I1 )
 elif 'youtube.com/playlist?list=' in url :
  ooOooo0 = url . split ( 'playlist?list=' ) [ 1 ]
  OOOoO000 = oo00 + ooOooo0 + o00
  oOOOO = urllib2 . Request ( OOOoO000 )
  oOOOO . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
  IiIi1ii111i1 = urllib2 . urlopen ( oOOOO )
  O0OoOoo00o = IiIi1ii111i1 . read ( )
  IiIi1ii111i1 . close ( )
  O0OoOoo00o = O0OoOoo00o . replace ( '\r' , '' ) . replace ( '\n' , '' ) . replace ( '  ' , '' )
  OOoO00o = re . compile ( '"title": "(.+?)".+?"videoId": "(.+?)"' , re . DOTALL ) . findall ( O0OoOoo00o )
  for name , i1i1i1I in OOoO00o :
   url = 'https://www.youtube.com/watch?v=' + i1i1i1I
   iconimage = 'https://i.ytimg.com/vi/%s/hqdefault.jpg' % i1i1i1I
   I1I ( name , url , 2 , iconimage , iIiiiI1IiI1I1 )
   if 83 - 83: o0o0OOO0o0 + IIIII
def I111IiiIi1 ( item ) :
 item = item . replace ( '\r' , '' ) . replace ( '\t' , '' ) . replace ( '&nbsp;' , '' ) . replace ( '\'' , '' ) . replace ( '\n' , '' )
 i1IiIiiI = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)"' , re . DOTALL ) . findall ( item )
 for II111iiii , II , oOoOo00oOo in i1IiIiiI :
  if 'youtube.com/channel/' in II :
   ooOooo0 = II . split ( 'channel/' ) [ 1 ]
   Ooo00O00O0O0O ( II111iiii , II , oOoO0 , oOoOo00oOo , iIiiiI1IiI1I1 , description = ooOooo0 )
  elif 'youtube.com/user/' in II :
   ooOooo0 = II . split ( 'user/' ) [ 1 ]
   Ooo00O00O0O0O ( II111iiii , II , oOoO0 , oOoOo00oOo , iIiiiI1IiI1I1 , description = ooOooo0 )
  elif 'youtube.com/playlist?' in II :
   ooOooo0 = II . split ( 'list=' ) [ 1 ]
   Ooo00O00O0O0O ( II111iiii , II , oOoO0 , oOoOo00oOo , iIiiiI1IiI1I1 , description = ooOooo0 )
  elif 'plugin://' in II :
   o00o = HTMLParser ( )
   II = o00o . unescape ( II )
   Ooo00O00O0O0O ( II111iiii , II , oOoO0 , oOoOo00oOo , iIiiiI1IiI1I1 )
  else :
   Ooo00O00O0O0O ( II111iiii , II , 1 , oOoOo00oOo , iIiiiI1IiI1I1 )
   if 46 - 46: iiIiIIi % oo0Oo00Oo0 % I1i1i1ii - I11iii . IIIII - iIii11I
def OOoOO0oo0ooO ( item , url , iconimage ) :
 OOOIiiiii1iI = iconimage
 ooOOoooooo = re . compile ( '<sportsdevil>(.+?)</sportsdevil>' ) . findall ( item )
 o00ooO00O = re . compile ( '<link>(.+?)</link>' ) . findall ( item )
 if len ( ooOOoooooo ) + len ( o00ooO00O ) == 1 :
  II111iiii = re . compile ( '<title>(.+?)</title>' ) . findall ( item ) [ 0 ]
  iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( item ) [ 0 ]
  url = re . compile ( '<sportsdevil>(.+?)</sportsdevil>' ) . findall ( item ) [ 0 ]
  url = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url=' + url
  if iconimage == 'ImageHere' : iconimage = OOOIiiiii1iI
  I1II ( II111iiii , url , 16 , iconimage , iIiiiI1IiI1I1 )
 elif len ( ooOOoooooo ) + len ( o00ooO00O ) > 1 :
  II111iiii = re . compile ( '<title>(.+?)</title>' ) . findall ( item ) [ 0 ]
  iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( item ) [ 0 ]
  if iconimage == 'ImageHere' : iconimage = OOOIiiiii1iI
  I1II ( II111iiii , url , 3 , iconimage , iIiiiI1IiI1I1 )
  if 68 - 68: O00o0o0000o0o + III1i1i
def OOO00O ( link ) :
 if Iii1ii1II11i == '' :
  o0OO00 = xbmcgui . Dialog ( )
  OooO0OO = o0OO00 . yesno ( 'Adult Content' , 'You have opted to show adult content' , '' , 'Please set a password to prevent accidental access' , 'Cancel' , 'OK' )
  if OooO0OO == 1 :
   iiiIi = xbmc . Keyboard ( '' , 'Set Password' )
   iiiIi . doModal ( )
   if ( iiiIi . isConfirmed ( ) ) :
    IiIIIiI1I1 = iiiIi . getText ( )
    ii . setSetting ( 'password' , IiIIIiI1I1 )
  else : quit ( )
 elif Iii1ii1II11i <> '' :
  o0OO00 = xbmcgui . Dialog ( )
  OooO0OO = o0OO00 . yesno ( 'Adult Content' , 'Please enter the password you set' , 'to continue' , '' , 'Cancel' , 'OK' )
  if OooO0OO == 1 :
   iiiIi = xbmc . Keyboard ( '' , 'Enter Password' )
   iiiIi . doModal ( )
   if ( iiiIi . isConfirmed ( ) ) :
    IiIIIiI1I1 = iiiIi . getText ( )
   if IiIIIiI1I1 <> Iii1ii1II11i :
    quit ( )
  else : quit ( )
  if 77 - 77: ii11I
def OooOOOOoO00OoOO ( ) :
 O0OoOoo00o = iiiI11 ( I1i1iiI1 )
 oOooo0O0o = [ 'Live TV' , 'Sports' , 'Movies' , 'TV Shows' , 'Cartoons' , 'Documentaries' , 'Standup' , 'Concerts' , 'Radio' , 'CCTV' , 'Turkish TV' , 'Turkish Movies' , 'Fitness' , 'Food Porn' ]
 iiiIi = xbmc . Keyboard ( '' , 'Search' )
 iiiIi . doModal ( )
 if ( iiiIi . isConfirmed ( ) ) :
  ooOooo0 = iiiIi . getText ( )
  ooOooo0 = ooOooo0 . upper ( )
 else : quit ( )
 Oo000 = [ ]
 O00O0oOOo = [ ]
 O0OoOoo00o = iiiI11 ( I1i1iiI1 )
 o0OO00 = xbmcgui . Dialog ( )
 OooO0OO = o0OO00 . multiselect ( "Select which categories to search" , oOooo0O0o )
 for O0oO in OooO0OO :
  Oo000 . append ( oOooo0O0o [ O0oO ] )
 for OO000oooo0 in Oo000 :
  Iii111II = '<' + OO000oooo0 + '>(.+?)</' + OO000oooo0 + '>'
  OOoO00o = re . compile ( Iii111II , re . DOTALL ) . findall ( O0OoOoo00o )
  for i1IiIiiI in OOoO00o :
   OOoO00o = re . compile ( '<cat>(.+?)</cat>' ) . findall ( i1IiIiiI )
   print OOoO00o
   for i1IiIiiI in OOoO00o :
    O00O0oOOo . append ( i1IiIiiI )
 for oOoO0o0ooo in O00O0oOOo :
  try :
   O0OoOoo00o = iiiI11 ( oOoO0o0ooo )
   OoO000 ( content , viewType , O0OoOoo00o )
   if 'Index' in oOoO0o0ooo :
    II111Ii1i1 = False
    OOoO00o = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)"' , re . DOTALL ) . findall ( O0OoOoo00o )
    for II111iiii , II , I11i in OOoO00o :
     if ooOooo0 in II111iiii . upper ( ) :
      if II111iiii [ 0 ] == '0' :
       II111iiii = II111iiii [ 1 : ] + '[COLOR gold]   (New)[/COLOR]'
      if 'youtube.com/playlist?list=' in II :
       Ooo00O00O0O0O ( II111iiii , II , 18 , I11i , iIiiiI1IiI1I1 )
      elif 'youtube.com/results?search_query=' in II :
       Ooo00O00O0O0O ( II111iiii , II , 18 , I11i , iIiiiI1IiI1I1 )
      else :
       Ooo00O00O0O0O ( II111iiii , II , 1 , I11i , iIiiiI1IiI1I1 )
   else :
    OOoO00o = re . compile ( '<item>(.+?)</item>' , re . DOTALL ) . findall ( O0OoOoo00o )
    IiII = str ( len ( OOoO00o ) )
    iI11I1II1I1I . setSetting ( 'count' , IiII )
    iI11I1II1I1I . setSetting ( 'fav' , 'no' )
    for iII1i1I1II in OOoO00o :
     Iiii1i1 = re . compile ( '<title>(.+?)</title>' ) . findall ( iII1i1I1II ) [ 0 ]
     if ooOooo0 in Iiii1i1 . upper ( ) :
      try :
       if '<sportsdevil>' in iII1i1I1II : OOoOO0oo0ooO ( iII1i1I1II , oOoO0o0ooo , oOoOo00oOo )
       elif '<iptv>' in iII1i1I1II : O0o0O00Oo0o0 ( iII1i1I1II )
       elif '<Image>' in iII1i1I1II : O00O0oOO00O00 ( iII1i1I1II )
       elif '<text>' in iII1i1I1II : i1Oo00 ( iII1i1I1II )
       elif '<scraper>' in iII1i1I1II : i1i ( iII1i1I1II )
       elif '<redirect>' in iII1i1I1II : REDIRECT ( iII1i1I1II )
       elif '<oktitle>' in iII1i1I1II : iiI111I1iIiI ( iII1i1I1II )
       elif '<dl>' in iII1i1I1II : IIIi1I1IIii1II ( iII1i1I1II )
       elif '<scraper>' in iII1i1I1II : i1i ( iII1i1I1II )
       else : O0ii1ii1ii ( iII1i1I1II , oOoO0o0ooo , oOoOo00oOo )
      except : pass
  except : pass
  if 86 - 86: I11i1I * oOo0oooo00o * iIii11I
def Ooo0oo ( name , url , iconimage ) :
 OOOIiiiii1iI = iconimage
 iiIiI1i1 = [ ]
 oO0O00oOOoooO = [ ]
 IiIi11iI = [ ]
 O0OoOoo00o = iiiI11 ( url )
 IIi11IIiIii1 = re . compile ( '<title>' + re . escape ( name ) + '</title>(.+?)</item>' , re . DOTALL ) . findall ( O0OoOoo00o ) [ 0 ]
 ooOOoooooo = [ ]
 if '<link>' in IIi11IIiIii1 :
  I1iIII1 = re . compile ( '<link>(.+?)</link>' ) . findall ( IIi11IIiIii1 )
  for iIii in I1iIII1 :
   ooOOoooooo . append ( iIii )
 if '<sportsdevil>' in IIi11IIiIii1 :
  oOo0OoOOo0 = re . compile ( '<sportsdevil>(.+?)</sportsdevil>' ) . findall ( IIi11IIiIii1 )
  for iII11I1Ii1 in oOo0OoOOo0 :
   iII11I1Ii1 = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url=' + iII11I1Ii1
   ooOOoooooo . append ( iII11I1Ii1 )
 O0i1II1Iiii1I11 = 1
 for iI1 in ooOOoooooo :
  iIIi = iI1
  if 'acestream://' in iI1 or '.acelive' in iI1 or 'sop://' in iI1 : o0o0 = ' (Acestreams)'
  else : o0o0 = ''
  if '(' in iI1 :
   iI1 = iI1 . split ( '(' ) [ 0 ]
   oOo0oO = str ( iIIi . split ( '(' ) [ 1 ] . replace ( ')' , '' ) + o0o0 )
   iiIiI1i1 . append ( iI1 )
   oO0O00oOOoooO . append ( oOo0oO )
  else :
   oO0o00oo0 = iI1 . split ( '/' ) [ 2 ] . replace ( 'www.' , '' )
   iiIiI1i1 . append ( iI1 )
   oO0O00oOOoooO . append ( 'Link ' + str ( O0i1II1Iiii1I11 ) + o0o0 )
  O0i1II1Iiii1I11 = O0i1II1Iiii1I11 + 1
 o0OO00 = xbmcgui . Dialog ( )
 o0O0OOO0Ooo = o0OO00 . select ( 'Choose a link..' , oO0O00oOOoooO )
 if o0O0OOO0Ooo < 0 : quit ( )
 else :
  url = iiIiI1i1 [ o0O0OOO0Ooo ]
  iiIiI ( name , url , iconimage )
  if 5 - 5: ooOOOo0oo0O0 - ooOOOo0oo0O0 . I11iii + o0o00ooo0 - ooOOOo0oo0O0 . o0o0OOO0o0
def IiIi1i1ii ( url ) :
 Iii111II = "ShowPicture(%s)" % url
 xbmc . executebuiltin ( Iii111II )
 if 11 - 11: iiIiIIi / oo0Oo00Oo0
def iiIiI ( name , url , iconimage ) :
 if 21 - 21: O00o0o0000o0o / oOoO + iI * ooOOOo0oo0O0 . ii11I
 try :
  if 'sop://' in url :
   url = urllib . quote ( url )
   url = 'plugin://program.plexus/?mode=2&url=%s&name=%s' % ( url , name . replace ( ' ' , '+' ) )
   OoO ( name , url , iconimage )
  elif 'acestream://' in url or '.acelive' in url :
   url = urllib . quote ( url )
   url = 'plugin://program.plexus/?mode=1&url=%s&name=%s' % ( url , name . replace ( ' ' , '+' ) )
   OoO ( name , url , iconimage )
  elif 'plugin://plugin.video.SportsDevil/' in url :
   OoO ( name , url , iconimage )
  elif '.ts' in url :
   url = 'plugin://plugin.video.f4mTester/?streamtype=TSDOWNLOADER&amp;name=' + name + '&amp;url=' + url
   OoO ( name , url , iconimage )
  elif resolveurl . HostedMediaFile ( url ) . valid_url ( ) :
   url = resolveurl . HostedMediaFile ( url ) . resolve ( )
   o0O0Oo ( name , url , iconimage )
  elif liveresolver . isValid ( url ) == True :
   url = liveresolver . resolve ( url )
   o0O0Oo ( name , url , iconimage )
  else : OoO ( name , url , iconimage )
 except :
  oo0oO ( 'UKTurk' , 'Stream Unavailable' , '3000' , I11i )
  if 10 - 10: iiIiIIi . i1iII11iiIii
def I1i ( url ) :
 if resolveurl . HostedMediaFile ( url ) . valid_url ( ) :
  url = resolveurl . HostedMediaFile ( url ) . resolve ( )
 xbmc . Player ( ) . play ( url )
 if 86 - 86: I11iii / o0o0OOO0o0 + oOo0oooo00o * i1iII11iiIii
def o0O0Oo ( name , url , iconimage ) :
 iiI11I1i1i1iI = True
 OoOOo000o0 = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage ) ; OoOOo000o0 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 iiI11I1i1i1iI = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = url , listitem = OoOOo000o0 )
 OoOOo000o0 . setPath ( str ( url ) )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , OoOOo000o0 )
 if 12 - 12: iiIiIIi . oO00OO0oo0 / ooOOOo0oo0O0
def OoO ( name , url , iconimage ) :
 xbmc . executebuiltin ( 'Dialog.Close(all,True)' )
 iiI11I1i1i1iI = True
 OoOOo000o0 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage ) ; OoOOo000o0 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 iiI11I1i1i1iI = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = url , listitem = OoOOo000o0 )
 xbmc . Player ( ) . play ( url , OoOOo000o0 , False )
 if 77 - 77: oo0OO - iI % oO00OO0oo0 - oOo0oooo00o
def o0O0O0 ( url ) :
 xbmc . executebuiltin ( "PlayMedia(%s)" % url )
 if 6 - 6: i1iII11iiIii . iIii11I * o0o00ooo0 . oOoO
def oOOoI1IiIIi ( url ) :
 i1I1ii = iI11I1II1I1I . getSetting ( 'layout' )
 if i1I1ii == 'Listers' : iI11I1II1I1I . setSetting ( 'layout' , 'Category' )
 else : iI11I1II1I1I . setSetting ( 'layout' , 'Listers' )
 xbmc . executebuiltin ( 'Container.Refresh' )
 if 42 - 42: oOo0oooo00o . o0o0OOO0o0 - oo0Oo00Oo0 / oOoO
def iiiI11 ( url ) :
 O0OoOoo00o = net . http_GET ( url ) . content
 O0OoOoo00o = O0OoOoo00o . replace ( '</fanart>' , '<fanart>x</fanart>' ) . replace ( '<thumbnail></thumbnail>' , '<thumbnail>x</thumbnail>' ) . replace ( '<utube>' , '<link>https://www.youtube.com/watch?v=' ) . replace ( '</utube>' , '</link>' )
 if '060105' in O0OoOoo00o : O0OoOoo00o = OooOOO ( O0OoOoo00o )
 return O0OoOoo00o
 if 48 - 48: I1i1i1ii % oOoO % i1iII11iiIii + oo0OO
def Iiii11iIi1 ( ) :
 i1iI11I1II1 = [ ]
 ii11II1i = sys . argv [ 2 ]
 if len ( ii11II1i ) >= 2 :
  O0oOoo0o000O0 = sys . argv [ 2 ]
  OOOO000o0 = O0oOoo0o000O0 . replace ( '?' , '' )
  if ( O0oOoo0o000O0 [ len ( O0oOoo0o000O0 ) - 1 ] == '/' ) :
   O0oOoo0o000O0 = O0oOoo0o000O0 [ 0 : len ( O0oOoo0o000O0 ) - 2 ]
  oO0 = OOOO000o0 . split ( '&' )
  i1iI11I1II1 = { }
  for O0i1II1Iiii1I11 in range ( len ( oO0 ) ) :
   o000OoOoO0 = { }
   o000OoOoO0 = oO0 [ O0i1II1Iiii1I11 ] . split ( '=' )
   if ( len ( o000OoOoO0 ) ) == 2 :
    i1iI11I1II1 [ o000OoOoO0 [ 0 ] ] = o000OoOoO0 [ 1 ]
 return i1iI11I1II1
O0oOoo0o000O0 = Iiii11iIi1 ( ) ; II = None ; II111iiii = None ; oOoO0 = None ; OO0ooOOO0O00o = None ; oOoOo00oOo = None
try : OO0ooOOO0O00o = urllib . unquote_plus ( O0oOoo0o000O0 [ "site" ] )
except : pass
try : II = urllib . unquote_plus ( O0oOoo0o000O0 [ "url" ] )
except : pass
try : II111iiii = urllib . unquote_plus ( O0oOoo0o000O0 [ "name" ] )
except : pass
try : oOoO0 = int ( O0oOoo0o000O0 [ "mode" ] )
except : pass
try : oOoOo00oOo = urllib . unquote_plus ( O0oOoo0o000O0 [ "iconimage" ] )
except : pass
try : iIiiiI1IiI1I1 = urllib . unquote_plus ( O0oOoo0o000O0 [ "fanart" ] )
except : pass
try : Ooo0o0oo = urllib . unquote_plus ( [ "description" ] )
except : pass
if 26 - 26: iiIiIIi % O00o0o0000o0o % I1i1i1ii % oO00OO0oo0 * oO00OO0oo0 * I11i1I
def oo0oO ( title , message , ms , nart ) :
 xbmc . executebuiltin ( "XBMC.notification(" + title + "," + message + "," + ms + "," + nart + ")" )
 if 24 - 24: iiIiIIi % ii11I - oo0OO + iI * I11i1I
def Oo0O0O0ooO0O ( string ) :
 i11111I1I = re . compile ( '\[(.+?)\]' ) . findall ( string )
 for Ooo0ooOOOOoOo in i11111I1I : string = string . replace ( Ooo0ooOOOOoOo , '' ) . replace ( '[/]' , '' ) . replace ( '[]' , '' )
 return string
 if 34 - 34: IIIII . oOo0oooo00o / o0o0OOO0o0 * o0o00ooo0 - I11i1I
def IiiiI ( string ) :
 string = string . split ( ' ' )
 Iii = ''
 for i1I1 in string :
  O0II11i11II = '[B][COLOR red]' + i1I1 [ 0 ] . upper ( ) + '[/COLOR][COLOR white]' + i1I1 [ 1 : ] + '[/COLOR][/B] '
  Iii = Iii + O0II11i11II
 return Iii
 if 29 - 29: I11iii % OO0O00 % iIii11I . oo0Oo00Oo0 / IIIII * oo0OO
def oO0OO0 ( name , url , mode , iconimage , itemcount , isFolder = False ) :
 url = url . replace ( ' ' , '%20' )
 iconimage = iconimage . replace ( ' ' , '%20' )
 if iI1Ii11111iIi == 'true' :
  if not 'COLOR' in name :
   o0OoO000O = name . partition ( '(' )
   OOo = ""
   iIIiiIIIi1I = ""
   if len ( o0OoO000O ) > 0 :
    OOo = o0OoO000O [ 0 ]
    iIIiiIIIi1I = o0OoO000O [ 2 ] . partition ( ')' )
   if len ( iIIiiIIIi1I ) > 0 :
    iIIiiIIIi1I = iIIiiIIIi1I [ 0 ]
   OO0o0o0oo0O = eval ( base64 . b64decode ( 'bWV0YWhhbmRsZXJzLk1ldGFEYXRhKHRtZGJfYXBpX2tleT0iZWNiYzg2YzkyZGEyMzdjYjlmYWZmNmQzZGRjNGJlNmQiKQ==' ) )
   IIiI1I1 = OO0o0o0oo0O . get_meta ( 'movie' , name = OOo , year = iIIiiIIIi1I )
   I11I1IIiiII1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&site=" + str ( OO0ooOOO0O00o ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
   iiI11I1i1i1iI = True
   OoOOo000o0 = xbmcgui . ListItem ( name , iconImage = IIiI1I1 [ 'cover_url' ] , thumbnailImage = IIiI1I1 [ 'cover_url' ] )
   OoOOo000o0 . setInfo ( type = "Video" , infoLabels = IIiI1I1 )
   OoOOo000o0 . setProperty ( "IsPlayable" , "true" )
   IIIIIii1ii11 = [ ]
   if iI11I1II1I1I . getSetting ( 'fav' ) == 'yes' : IIIIIii1ii11 . append ( ( '[COLOR red]Remove from UK Turk Favourites[/COLOR]' , 'XBMC.RunPlugin(%s?mode=14&name=%s&url=%s&iconimage=%s)' % ( sys . argv [ 0 ] , name , url , iconimage ) ) )
   if iI11I1II1I1I . getSetting ( 'fav' ) == 'no' : IIIIIii1ii11 . append ( ( '[COLOR white]Add to UK Turk Favourites[/COLOR]' , 'XBMC.RunPlugin(%s?mode=12&name=%s&url=%s&iconimage=%s)' % ( sys . argv [ 0 ] , name , url , iconimage ) ) )
   OoOOo000o0 . addContextMenuItems ( IIIIIii1ii11 , replaceItems = False )
   if not IIiI1I1 [ 'backdrop_url' ] == '' : OoOOo000o0 . setProperty ( 'fanart_image' , IIiI1I1 [ 'backdrop_url' ] )
   else : OoOOo000o0 . setProperty ( 'fanart_image' , iIiiiI1IiI1I1 )
   iiI11I1i1i1iI = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I11I1IIiiII1 , listitem = OoOOo000o0 , isFolder = isFolder , totalItems = itemcount )
   return iiI11I1i1i1iI
 else :
  I11I1IIiiII1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&site=" + str ( OO0ooOOO0O00o ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
  iiI11I1i1i1iI = True
  OoOOo000o0 = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage )
  OoOOo000o0 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
  OoOOo000o0 . setProperty ( 'fanart_image' , iIiiiI1IiI1I1 )
  OoOOo000o0 . setProperty ( "IsPlayable" , "true" )
  IIIIIii1ii11 = [ ]
  if iI11I1II1I1I . getSetting ( 'fav' ) == 'yes' : IIIIIii1ii11 . append ( ( '[COLOR red]Remove from UK Turk Favourites[/COLOR]' , 'XBMC.RunPlugin(%s?mode=14&name=%s&url=%s&iconimage=%s)' % ( sys . argv [ 0 ] , name , url , iconimage ) ) )
  if iI11I1II1I1I . getSetting ( 'fav' ) == 'no' : IIIIIii1ii11 . append ( ( '[COLOR white]Add to UK Turk Favourites[/COLOR]' , 'XBMC.RunPlugin(%s?mode=12&name=%s&url=%s&iconimage=%s)' % ( sys . argv [ 0 ] , name , url , iconimage ) ) )
  OoOOo000o0 . addContextMenuItems ( IIIIIii1ii11 , replaceItems = False )
  iiI11I1i1i1iI = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I11I1IIiiII1 , listitem = OoOOo000o0 , isFolder = isFolder )
  return iiI11I1i1i1iI
  if 86 - 86: o0o00ooo0 * iiIiIIi - oOo0oooo00o . o0o00ooo0 % I1i1i1ii / ooOOOo0oo0O0
def Ooo00O00O0O0O ( name , url , mode , iconimage , fanart , description = '' ) :
 url = url . replace ( ' ' , '%20' )
 iconimage = iconimage . replace ( ' ' , '%20' )
 I11I1IIiiII1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&description=" + str ( description ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&iconimage=" + urllib . quote_plus ( iconimage )
 iiI11I1i1i1iI = True
 OoOOo000o0 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 OoOOo000o0 . setInfo ( type = "Video" , infoLabels = { "Title" : name , 'plot' : description } )
 OoOOo000o0 . setProperty ( 'fanart_image' , fanart )
 IIIIIii1ii11 = [ ]
 if iI11I1II1I1I . getSetting ( 'fav' ) == 'yes' : IIIIIii1ii11 . append ( ( '[COLOR red]Remove from UK Turk Favourites[/COLOR]' , 'XBMC.RunPlugin(%s?mode=14&name=%s&url=%s&iconimage=%s)' % ( sys . argv [ 0 ] , name , url , iconimage ) ) )
 if iI11I1II1I1I . getSetting ( 'fav' ) == 'no' : IIIIIii1ii11 . append ( ( '[COLOR white]Add to UK Turk Favourites[/COLOR]' , 'XBMC.RunPlugin(%s?mode=12&name=%s&url=%s&iconimage=%s)' % ( sys . argv [ 0 ] , name , url , iconimage ) ) )
 OoOOo000o0 . addContextMenuItems ( IIIIIii1ii11 , replaceItems = False )
 if 'plugin://' in url :
  I11I1IIiiII1 = url
 iiI11I1i1i1iI = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I11I1IIiiII1 , listitem = OoOOo000o0 , isFolder = True )
 return iiI11I1i1i1iI
 if 11 - 11: iI * o0o0OOO0o0 + I11i1I / I11i1I
def I1II ( name , url , mode , iconimage , fanart , description = '' ) :
 url = url . replace ( ' ' , '%20' )
 iconimage = iconimage . replace ( ' ' , '%20' )
 I11I1IIiiII1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&description=" + str ( description ) + "&iconimage=" + urllib . quote_plus ( iconimage )
 iiI11I1i1i1iI = True
 OoOOo000o0 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 OoOOo000o0 . setProperty ( 'fanart_image' , fanart )
 IIIIIii1ii11 = [ ]
 if iI11I1II1I1I . getSetting ( 'fav' ) == 'yes' : IIIIIii1ii11 . append ( ( '[COLOR red]Remove from UK Turk Favourites[/COLOR]' , 'XBMC.RunPlugin(%s?mode=14&name=%s&url=%s&iconimage=%s)' % ( sys . argv [ 0 ] , name , url , iconimage ) ) )
 if iI11I1II1I1I . getSetting ( 'fav' ) == 'no' : IIIIIii1ii11 . append ( ( '[COLOR white]Add to UK Turk Favourites[/COLOR]' , 'XBMC.RunPlugin(%s?mode=12&name=%s&url=%s&iconimage=%s)' % ( sys . argv [ 0 ] , name , url , iconimage ) ) )
 OoOOo000o0 . addContextMenuItems ( IIIIIii1ii11 , replaceItems = False )
 iiI11I1i1i1iI = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I11I1IIiiII1 , listitem = OoOOo000o0 , isFolder = False )
 return iiI11I1i1i1iI
 if 37 - 37: O00o0o0000o0o + oOoO
def I1I ( name , url , mode , iconimage , fanart , description = '' ) :
 url = url . replace ( ' ' , '%20' )
 iconimage = iconimage . replace ( ' ' , '%20' )
 I11I1IIiiII1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&description=" + str ( description ) + "&iconimage=" + urllib . quote_plus ( iconimage )
 iiI11I1i1i1iI = True
 OoOOo000o0 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 OoOOo000o0 . setProperty ( 'fanart_image' , fanart )
 OoOOo000o0 . setProperty ( "IsPlayable" , "true" )
 IIIIIii1ii11 = [ ]
 if iI11I1II1I1I . getSetting ( 'fav' ) == 'yes' : IIIIIii1ii11 . append ( ( '[COLOR red]Remove from UK Turk Favourites[/COLOR]' , 'XBMC.RunPlugin(%s?mode=14&name=%s&url=%s&iconimage=%s)' % ( sys . argv [ 0 ] , name , url , iconimage ) ) )
 if iI11I1II1I1I . getSetting ( 'fav' ) == 'no' : IIIIIii1ii11 . append ( ( '[COLOR white]Add to UK Turk Favourites[/COLOR]' , 'XBMC.RunPlugin(%s?mode=12&name=%s&url=%s&iconimage=%s)' % ( sys . argv [ 0 ] , name , url , iconimage ) ) )
 OoOOo000o0 . addContextMenuItems ( IIIIIii1ii11 , replaceItems = False )
 iiI11I1i1i1iI = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I11I1IIiiII1 , listitem = OoOOo000o0 , isFolder = False )
 return iiI11I1i1i1iI
 if 23 - 23: i1iII11iiIii + oO00OO0oo0 . o0o00ooo0 * iI + I11i1I
def I1iIi1iiiIiI ( url , name ) :
 III1I1Ii11iI = iiiI11 ( url )
 if len ( III1I1Ii11iI ) > 1 :
  O00oOo00o0o = i1i1II
  O00oO0 = os . path . join ( os . path . join ( O00oOo00o0o , '' ) , name + '.txt' )
  if not os . path . exists ( O00oO0 ) :
   file ( O00oO0 , 'w' ) . close ( )
  oO00OoOO = open ( O00oO0 )
  I11IIiIiI = oO00OoOO . read ( )
  if I11IIiIiI == III1I1Ii11iI : pass
  else :
   IiiIiI1Ii1i ( 'UKTurk' , III1I1Ii11iI )
   O0Oo00OoOo = open ( O00oO0 , "w" )
   O0Oo00OoOo . write ( III1I1Ii11iI )
   O0Oo00OoOo . close ( )
   if 5 - 5: I11iii * o0o00ooo0
def IiiIiI1Ii1i ( heading , text ) :
 id = 10147
 xbmc . executebuiltin ( 'ActivateWindow(%d)' % id )
 xbmc . sleep ( 500 )
 ii1I11iIiIII1 = xbmcgui . Window ( id )
 oOO0OOOOoooO = 50
 while ( oOO0OOOOoooO > 0 ) :
  try :
   xbmc . sleep ( 10 )
   oOO0OOOOoooO -= 1
   ii1I11iIiIII1 . getControl ( 1 ) . setLabel ( heading )
   ii1I11iIiIII1 . getControl ( 5 ) . setText ( text )
   return
  except :
   pass
   if 22 - 22: oO00OO0oo0 + I1i1i1ii
def IIIii1iiIi ( name ) :
 global Icon
 global Next
 global Previous
 global window
 global Quit
 global images
 O00oO0 = os . path . join ( os . path . join ( i1i1II , '' ) , name + '.txt' )
 oO00OoOO = open ( O00oO0 )
 I11IIiIiI = oO00OoOO . read ( )
 images = re . compile ( '<image>(.+?)</image>' ) . findall ( I11IIiIiI )
 iI11I1II1I1I . setSetting ( 'pos' , '0' )
 window = pyxbmct . AddonDialogWindow ( '' )
 oooo0OOo = '/resources/art'
 OoO00I11iIi1II = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + oOOo + oooo0OOo , 'next_focus.png' ) )
 ooo0OO = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + oOOo + oooo0OOo , 'next1.png' ) )
 iIi1IiI = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + oOOo + oooo0OOo , 'previous_focus.png' ) )
 I11IIIiIi11 = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + oOOo + oooo0OOo , 'previous.png' ) )
 I11iiIi1i1 = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + oOOo + oooo0OOo , 'close_focus.png' ) )
 i1IiiI1iIi = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + oOOo + oooo0OOo , 'close.png' ) )
 oOOo00O0OOOo = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + oOOo + oooo0OOo , 'main-bg1.png' ) )
 window . setGeometry ( 1300 , 720 , 100 , 50 )
 i11I1I1iiI = pyxbmct . Image ( oOOo00O0OOOo )
 window . placeControl ( i11I1I1iiI , - 10 , - 10 , 130 , 70 )
 o0O0O0ooo0oOO = '0xFF000000'
 Previous = pyxbmct . Button ( '' , focusTexture = iIi1IiI , noFocusTexture = I11IIIiIi11 , textColor = o0O0O0ooo0oOO , focusedColor = o0O0O0ooo0oOO )
 Next = pyxbmct . Button ( '' , focusTexture = OoO00I11iIi1II , noFocusTexture = ooo0OO , textColor = o0O0O0ooo0oOO , focusedColor = o0O0O0ooo0oOO )
 Quit = pyxbmct . Button ( '' , focusTexture = I11iiIi1i1 , noFocusTexture = i1IiiI1iIi , textColor = o0O0O0ooo0oOO , focusedColor = o0O0O0ooo0oOO )
 Icon = pyxbmct . Image ( images [ 0 ] , aspectRatio = 1 )
 window . placeControl ( Previous , 102 , 1 , 10 , 10 )
 window . placeControl ( Next , 102 , 40 , 10 , 10 )
 window . placeControl ( Quit , 102 , 21 , 10 , 10 )
 window . placeControl ( Icon , 0 , 0 , 100 , 50 )
 Previous . controlRight ( Next )
 Previous . controlUp ( Quit )
 window . connect ( Previous , I1i1iii1Ii )
 window . connect ( Next , iIO0O00OOo )
 Previous . setVisible ( False )
 window . setFocus ( Quit )
 Previous . controlRight ( Quit )
 Quit . controlLeft ( Previous )
 Quit . controlRight ( Next )
 Next . controlLeft ( Quit )
 window . connect ( Quit , window . close )
 window . doModal ( )
 del window
 if 66 - 66: O00o0o0000o0o / oo0Oo00Oo0 - IIIII / oOoO . O00o0o0000o0o
def iIO0O00OOo ( ) :
 IIIII1iii11 = int ( iI11I1II1I1I . getSetting ( 'pos' ) )
 IIi1I = int ( IIIII1iii11 ) + 1
 iI11I1II1I1I . setSetting ( 'pos' , str ( IIi1I ) )
 iii = len ( images )
 Icon . setImage ( images [ int ( IIi1I ) ] )
 Previous . setVisible ( True )
 if int ( IIi1I ) == int ( iii ) - 1 :
  Next . setVisible ( False )
  if 95 - 95: iIii11I * I11i1I % oo0OO % III1i1i - III1i1i
def I1i1iii1Ii ( ) :
 IIIII1iii11 = int ( iI11I1II1I1I . getSetting ( 'pos' ) )
 oOoooO0 = int ( IIIII1iii11 ) - 1
 iI11I1II1I1I . setSetting ( 'pos' , str ( oOoooO0 ) )
 Icon . setImage ( images [ int ( oOoooO0 ) ] )
 Next . setVisible ( True )
 if int ( oOoooO0 ) == 0 :
  Previous . setVisible ( False )
  if 68 - 68: oo0OO / oo0Oo00Oo0
def OooOOO ( s ) :
 Ii11 = [ s [ O0i1II1Iiii1I11 : O0i1II1Iiii1I11 + 3 ] for O0i1II1Iiii1I11 in range ( 0 , len ( s ) , 3 ) ]
 return '' . join ( chr ( int ( val ) ) for val in Ii11 )
 if 8 - 8: I11iii + iiIiIIi * ooOOOo0oo0O0 * o0o00ooo0 * oO00OO0oo0 / iIii11I
def iIiiOO0OoOOO0 ( text ) :
 def O00ooOo ( m ) :
  o0O0O0ooo0oOO = m . group ( 0 )
  if o0O0O0ooo0oOO [ : 3 ] == "&#x" : return unichr ( int ( o0O0O0ooo0oOO [ 3 : - 1 ] , 16 ) ) . encode ( 'utf-8' )
  else : return unichr ( int ( o0O0O0ooo0oOO [ 2 : - 1 ] ) ) . encode ( 'utf-8' )
 try : return re . sub ( "(?i)&#\w+;" , O00ooOo , text . decode ( 'ISO-8859-1' ) . encode ( 'utf-8' ) )
 except : return re . sub ( "(?i)&#\w+;" , O00ooOo , text . encode ( "ascii" , "ignore" ) . encode ( 'utf-8' ) )
 if 80 - 80: oo0Oo00Oo0 - ooOOOo0oo0O0 + IIIII
def O0ooOoO ( ) :
 if xbmc . getCondVisibility ( 'system.platform.android' ) :
  return 'android'
 elif xbmc . getCondVisibility ( 'system.platform.linux' ) :
  return 'linux'
 elif xbmc . getCondVisibility ( 'system.platform.windows' ) :
  return 'windows'
 elif xbmc . getCondVisibility ( 'system.platform.osx' ) :
  return 'osx'
 elif xbmc . getCondVisibility ( 'system.platform.atv2' ) :
  return 'atv2'
 elif xbmc . getCondVisibility ( 'system.platform.ios' ) :
  return 'ios'
 else :
  return 'Other'
  if 26 - 26: o0o00ooo0 / I11iii - oOoO + oO00OO0oo0
def IiiIi ( url ) :
 iIIiooO00O00oOO = urllib2 . Request ( url )
 iIIiooO00O00oOO . add_header ( 'User-Agent' , i1 )
 IiIi1ii111i1 = urllib2 . urlopen ( iIIiooO00O00oOO )
 O0OoOoo00o = IiIi1ii111i1 . read ( )
 IiIi1ii111i1 . close ( )
 return O0OoOoo00o
 if 40 - 40: i1iII11iiIii . o0o0OOO0o0 + iI + I11i1I + ii11I
def iI111iI ( ) :
 II = 'https://addoncloud.org/pin.php'
 i11Ii1I1I11I = xbmc . getCondVisibility ( 'system.platform.windows' )
 Ii1I1iiiiii = xbmc . getCondVisibility ( 'system.platform.osx' )
 o0OO0Oo = xbmc . getCondVisibility ( 'system.platform.linux' )
 I11iiii1I = xbmc . getCondVisibility ( 'System.Platform.Android' )
 if 3 - 3: oOo0oooo00o % IIIII / ooOOOo0oo0O0
 if Ii1I1iiiiii :
  if 89 - 89: iiIiIIi / o0o0OOO0o0
  xbmc . executebuiltin ( "System.Exec(open " + II + ")" )
 elif i11Ii1I1I11I :
  if 14 - 14: ooOOOo0oo0O0 . iI * oo0OO + iiIiIIi - oo0OO + ooOOOo0oo0O0
  xbmc . executebuiltin ( "System.Exec(cmd.exe /c start " + II + ")" )
 elif I11iiii1I :
  try :
   xbmc . executebuiltin ( "StartAndroidActivity(com.android.chrome,android.intent.action.VIEW,," + II + ")" )
  except :
   xbmcgui . Dialog ( ) . ok ( '[COLOR red]!!!! ALERT !!!![/COLOR]' , "Your device doesn't have a browser. Please install a browser then use this addon" )
   if 18 - 18: o0o0OOO0o0 - oo0Oo00Oo0 - iI - iI
def OOooo00 ( P ) :
 if 35 - 35: ii11I . o0o00ooo0 * O00o0o0000o0o
 global PIN
 global MESSAGE_LABELS
 if P == "" :
  iiII = "You Need a [COLOR white][B]PIN[/B][/COLOR] to Access UK Turks!"
  o0Oii1111i = "Go to [COLOR blue][B]UTPIN.COM[/B][/COLOR] on your Mobile/PC to get your PIN number then click on yes to input your pin or click on No to exit"
  if wizz . platform ( ) == 'android' :
   oOoO0o00OO0 = iIIii1IIi . yesno ( '[COLOR red]!!Chrome Browser Required!![/COLOR]' , "If you already have Chrome installed then click [COLOR green]Continue[/COLOR]" , "Don't have Chrome installed? click [COLOR cyan]Download[/COLOR]" , yeslabel = "[B][COLOR cyan]Download[/COLOR][/B]" , nolabel = "[B][COLOR green]Continue[/COLOR][/B]" )
   if oOoO0o00OO0 :
    iiIii ( 'chrome' , 'https://addoncloud.org/ukturk/files/chrome_v61.0.3163.98.apk' )
   else :
    pass
  O0ooOO = plugintools . message_yes_no ( oOOoo00O0O + "  Pin Access System" , iiII , o0Oii1111i )
  if O0ooOO :
   iI111iI ( )
   IiiI ( )
  else :
   sys . exit ( )
 else :
  O0OoOoo00o = IiiIi ( o0oOoO00o + '?pin=' + plugintools . get_setting ( 'pin' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
  i11ii = re . compile ( 'install="(\d)"' ) . findall ( O0OoOoo00o )
  try :
   if ( str ( i11ii [ 0 ] ) == '1' ) :
    pass
  except :
   iiII = "Invalid PIN,"
   o0Oii1111i = "Press yes to enter PIN again or No to exit."
   O0ooOO = plugintools . message_yes_no ( oOOoo00O0O + "  Pin Access System" , iiII , o0Oii1111i )
   if O0ooOO :
    iI111iI ( )
    IiiI ( )
   else :
    sys . exit ( )
    if 50 - 50: III1i1i / o0o00ooo0 * III1i1i
def IiiI ( ) :
 Ii1iIi111i1i1 ( )
 global i1111
 i1111 = plugintools . get_setting ( 'pin' )
 OOooo00 ( i1111 )
 if 45 - 45: o0o00ooo0 . oo0Oo00Oo0 % o0o00ooo0 * iI % iI
def Ii1iIi111i1i1 ( ) :
 try :
  oOoOo00ooOooo = IioOoooO00O ( )
  if oOoOo00ooOooo == "" :
   plugintools . message ( oOOoo00O0O , "Your pin cannot be empty" )
   Ii1iIi111i1i1 ( )
  else :
   plugintools . set_setting ( "pin" , oOoOo00ooOooo )
   return
 except :
  Ii1iIi111i1i1 ( )
  if 6 - 6: III1i1i % oOoO . III1i1i * III1i1i
def IioOoooO00O ( ) :
 iiiIi = xbmc . Keyboard ( '' , 'Please enter your pin here' )
 iiiIi . doModal ( )
 if ( iiiIi . isConfirmed ( ) ) :
  IiIIIiI1I1 = iiiIi . getText ( )
  iI11I1II1I1I . setSetting ( 'pin' , IiIIIiI1I1 )
 return IiIIIiI1I1
 if 81 - 81: ooOOOo0oo0O0 / I1i1i1ii + iIii11I
def OoO000 ( content , viewType , link ) :
 try :
  if ( content ) :
   xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
  if ( ii . getSetting ( 'auto-view' ) == 'true' ) :
   xbmc . executebuiltin ( 'Container.SetViewMode(%s)' % ii . getSetting ( viewType ) )
 except : pass
 if 49 - 49: ooOOOo0oo0O0 / IIIII / iI
OOooo00 ( i1111 )
if ( ( oOoO0 == None ) or ( II == None ) or len ( II ) < 1 ) :
 OOooo00 ( i1111 )
 I1 ( )
elif oOoO0 == 1 : II1i1IiiIIi11 ( II111iiii , II , oOoOo00oOo , iIiiiI1IiI1I1 )
elif oOoO0 == 2 : iiIiI ( II111iiii , II , oOoOo00oOo )
elif oOoO0 == 3 : Ooo0oo ( II111iiii , II , oOoOo00oOo )
elif oOoO0 == 4 : o0O0Oo ( II111iiii , II , oOoOo00oOo )
elif oOoO0 == 5 : OooOOOOoO00OoOO ( )
elif oOoO0 == 6 : OoO00 ( II , oOoOo00oOo )
elif oOoO0 == 7 : IiIi1i1ii ( II )
elif oOoO0 == 8 : IIIii1iiIi ( II111iiii )
elif oOoO0 == 9 : IIII1i ( II111iiii , II )
elif oOoO0 == 10 : DOSCRAPER ( II111iiii , II )
elif oOoO0 == 11 : o0O0O0 ( II )
elif oOoO0 == 12 : OOO0OOO00oo ( II111iiii , II , oOoOo00oOo )
elif oOoO0 == 13 : oOOoI1IiIIi ( II )
elif oOoO0 == 14 : Ooo0OO0oOO ( II111iiii , II , oOoOo00oOo )
elif oOoO0 == 15 : iiI1 ( II )
elif oOoO0 == 16 : OoO ( II111iiii , II , oOoOo00oOo )
elif oOoO0 == 17 : Oooo0 ( II111iiii , II )
elif oOoO0 == 18 : oOooO0 ( II111iiii , II , oOoOo00oOo )
elif oOoO0 == 19 : O00 ( II111iiii , II )
elif oOoO0 == 20 : O0OI11iiiii1II ( II , oOoOo00oOo )
elif oOoO0 == 21 : Ii1Iii1iIi ( II )
elif oOoO0 == 22 : I1III1111iIi ( II111iiii , II , oOoOo00oOo )
elif oOoO0 == 23 : Ii1 ( II )
elif oOoO0 == 24 : IIiIi1iI ( II111iiii , II , oOoOo00oOo )
elif oOoO0 == 25 : IiII111i1i11 ( II )
elif oOoO0 == 26 : II1i111Ii1i ( II111iiii , II , oOoOo00oOo )
elif oOoO0 == 27 : O0O0Oooo0o ( II111iiii , II , oOoOo00oOo )
elif oOoO0 == 28 : Oo0O0oooo ( II111iiii , II , oOoOo00oOo )
elif oOoO0 == 29 : GETPOPULARTVEP ( II111iiii , II , oOoOo00oOo )
elif oOoO0 == 30 : i1OOoO ( II111iiii , II , oOoOo00oOo )
elif oOoO0 == 31 : FH2 ( )
elif oOoO0 == 32 : II1IIiiIiI ( )
elif oOoO0 == 33 : O0O0Ooo ( II111iiii , II , oOoOo00oOo )
elif oOoO0 == 34 : Oo00o0OO0O00o ( II111iiii , II , oOoOo00oOo )
elif oOoO0 == 35 : o00oo0 ( II )
elif oOoO0 == 36 : OOOoO00 ( II111iiii , II , oOoOo00oOo )
elif oOoO0 == 37 : i11II1I11I1 ( II111iiii , II , oOoOo00oOo )
elif oOoO0 == 38 : i1OOO ( )
elif oOoO0 == 39 : I1i11111i1i11 ( II111iiii , II , oOoOo00oOo )
elif oOoO0 == 40 : I1ii11 ( II111iiii , II , oOoOo00oOo )
elif oOoO0 == 41 : iIi1i1iIi1iI ( II111iiii , II , oOoOo00oOo )
elif oOoO0 == 42 : IiIii1i111 ( II111iiii , II , oOoOo00oOo )
elif oOoO0 == 43 : iIo0o00 ( II111iiii , II , oOoOo00oOo )
elif oOoO0 == 44 : iI1111iiii ( II111iiii , II , oOoOo00oOo )
elif oOoO0 == 45 : O0oOo00o ( )
elif oOoO0 == 46 : iiii1IIi ( II )
elif oOoO0 == 47 : OOo0o0O0O ( II111iiii , II )
elif oOoO0 == 48 : OooooO0oOOOO ( II111iiii , II , oOoOo00oOo )
elif oOoO0 == 49 : OOO ( II111iiii , II , oOoOo00oOo )
elif oOoO0 == 50 : iI1iIii11Ii ( II )
elif oOoO0 == 51 : Ii ( II111iiii , II , oOoOo00oOo )
elif oOoO0 == 52 : iiI1iI111ii1i ( II111iiii , II , oOoOo00oOo )
elif oOoO0 == 53 : III11I1 ( II111iiii , II , oOoOo00oOo )
elif oOoO0 == 54 : iii1i1I1i1 ( II111iiii , II , oOoOo00oOo )
elif oOoO0 == 55 : oOOO ( II )
elif oOoO0 == 56 : iI111i ( II , oOoOo00oOo )
elif oOoO0 == 57 : Ooo00o0Oooo ( II , oOoOo00oOo )
elif oOoO0 == 58 : O0OO0O ( II )
elif oOoO0 == 59 : o0iI11I1II ( II111iiii , II , oOoOo00oOo )
elif oOoO0 == 60 : iiIiIi ( )
if 74 - 74: ii11I % I11i1I
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
