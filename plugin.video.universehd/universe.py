#########################################
############CODE BY @NEMZZY668###########
############CODE BY @_DevKong############
if 64 - 64: i11iIiiIii
import xbmc , xbmcaddon , xbmcgui , xbmcplugin , urllib , urllib2 , os , re , sys , base64 , json , time
from resources . libs . common_addon import Addon
import requests
import resolveurl
from metahandler import metahandlers
from HTMLParser import HTMLParser
from datetime import datetime , timedelta
import xml . etree . ElementTree as ET
if 65 - 65: O0 / iIii1I11I1II1 % OoooooooOO - i1IIi
o0OO00 = 'plugin.video.universehd'
oo = Addon ( o0OO00 , sys . argv )
i1iII1IiiIiI1 = xbmcaddon . Addon ( id = o0OO00 )
iIiiiI1IiI1I1 = '[COLOR yellow][B]Universe HD[/B][/COLOR]'
o0OoOoOO00 = os . path . join ( os . path . join ( xbmc . translatePath ( 'special://home' ) , 'addons' ) , 'plugin.video.universehd' )
I11i = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + o0OO00 , 'fanart.jpg' ) )
O0O = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + o0OO00 , 'fanart.jpg' ) )
Oo = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + o0OO00 , 'iptvfanart.jpg' ) )
I1ii11iIi11i = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + o0OO00 , 'icon.png' ) )
I1IiI = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + o0OO00 , 'iptvicon.png' ) )
o0OOO = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + o0OO00 , 'icon.png' ) )
iIiiiI = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/' + o0OO00 , 'settings.xml' ) )
Iii1ii1II11i = xbmcgui . DialogProgress ( )
iI111iI = xbmcgui . Dialog ( )
if 34 - 34: iii1I1I / O00oOoOoO0o0O . O0oo0OO0 + Oo0ooO0oo0oO . I1i1iI1i - II
if 100 - 100: i11Ii11I1Ii1i . ooO - OOoO / ooo0Oo0 * i1 - OOooo0000ooo
global OOo000
global O0I11i1i11i1I
OOo000 = i1iII1IiiIiI1 . getSetting ( 'Username' )
O0I11i1i11i1I = i1iII1IiiIiI1 . getSetting ( 'Password' )
Iiii = base64 . b64decode ( b'aHR0cDovL3dvcmxka29kaS5jb20vVW5pdmVyc2VIRC9YbWwvQmFzZS54bWw=' )
OOO0O = base64 . b64decode ( b'aHR0cDovLzE0Ny4xMzUuMTMwLjE1Mjo4MDAw' )
oo0ooO0oOOOOo = base64 . b64decode ( b'L3BsYXllcl9hcGkucGhwP3VzZXJuYW1lPSVzJnBhc3N3b3JkPSVzJmFjdGlvbj1nZXRfbGl2ZV9jYXRlZ29yaWVz' ) % ( OOo000 , O0I11i1i11i1I )
oO000OoOoo00o = base64 . b64decode ( b'L2VuaWdtYTIucGhwP3VzZXJuYW1lPSVzJnBhc3N3b3JkPSVzJnR5cGU9Z2V0X2xpdmVfc3RyZWFtcyZjYXRfaWQ9' ) % ( OOo000 , O0I11i1i11i1I )
iiiI11 = base64 . b64decode ( b'L3BsYXllcl9hcGkucGhwP3VzZXJuYW1lPSVzJnBhc3N3b3JkPSVz' ) % ( OOo000 , O0I11i1i11i1I )
if 91 - 91: oOOOO / i1iiIII111ii + iiIIi1IiIi11 . iIii1I11I1II1
if 43 - 43: II * O0
if 25 - 25: OOooo0000ooo + iiIIi1IiIi11 % iiIIi1IiIi11 - ooO * II % OOooo0000ooo
if 55 - 55: I1i1iI1i % i1IIi / i1 - ooO - O0 / iii1I1I
def iii11iII ( ) :
 if 42 - 42: i1iiIII111ii + i11Ii11I1Ii1i
 if not os . path . exists ( os . path . dirname ( downloads ) ) :
  try :
   os . makedirs ( os . path . dirname ( downloads ) )
   with open ( iIiiiI , "w" ) as OOoO000O0OO :
    OOoO000O0OO . write ( "<date>000</date>" )
  except OSError as iiI1IiI :
   if iiI1IiI . errno != errno . EEXIST :
    raise
    if 13 - 13: O0oo0OO0 . i11iIiiIii - iIii1I11I1II1 - I1i1iI1i
def ii1I ( time ) :
 time = datetime . fromtimestamp ( int ( time ) ) . strftime ( '%d-%m-%Y - %H:%M' )
 return time
 if 76 - 76: O0 / II . O00oOoOoO0o0O * i1 - OOoO
def Oooo ( time ) :
 time = datetime . fromtimestamp ( int ( time ) ) . strftime ( '%Y-%m-%d' )
 return time
 if 67 - 67: OOoO / OoooooooOO % ooo0Oo0 - iIii1I11I1II1
def Ooo ( ) :
 if 68 - 68: ooo0Oo0 + OOoO . iIii1I11I1II1 - oOOOO % iIii1I11I1II1 - iiIIi1IiIi11
 oOOO00o = OOO0O + iiiI11
 O0O00o0OOO0 = Ii1iIIIi1ii ( oOOO00o )
 o0oo0o0O00OO = json . loads ( O0O00o0OOO0 )
 o0oO = o0oo0o0O00OO [ 'user_info' ] [ 'exp_date' ]
 o0oO = Oooo ( o0oO )
 I1i1iii = datetime . now ( )
 i1iiI11I = I1i1iii + timedelta ( days = 3 )
 if o0oO <= str ( i1iiI11I ) :
  iI111iI . notification ( iIiiiI1IiI1I1 , '[COLOR red]Your Sub Is Due To Expire Soon, Visit The Website To Renew[/COLOR]' , I1IiI , 5000 )
 else :
  return
  if 29 - 29: OoooooooOO
def iI ( ) :
 if 28 - 28: OOoO - oOOOO . oOOOO + I1i1iI1i - OoooooooOO + O0
 oOOO00o = OOO0O + iiiI11
 O0O00o0OOO0 = Ii1iIIIi1ii ( oOOO00o )
 o0oo0o0O00OO = json . loads ( O0O00o0OOO0 )
 oOoOooOo0o0 = o0oo0o0O00OO [ 'user_info' ] [ 'username' ]
 o0oO = o0oo0o0O00OO [ 'user_info' ] [ 'exp_date' ]
 OOOO = o0oo0o0O00OO [ 'user_info' ] [ 'max_connections' ]
 OOO00 = o0oo0o0O00OO [ 'user_info' ] [ 'active_cons' ]
 o0oO = ii1I ( o0oO )
 iI111iI . ok ( iIiiiI1IiI1I1 , "[COLOR red]UserName : [COLOR yellow]" + oOoOooOo0o0 + "[COLOR red]\nMax Connections Allowed : [COLOR yellow]"
 + OOOO + "\n[COLOR red]Active Connections : [COLOR yellow]" + OOO00 + "\n[COLOR red]Expiry Date : [COLOR yellow]" + o0oO + "[/COLOR]" )
 if 21 - 21: OoooooooOO - OoooooooOO
def iIii11I ( ) :
 if 69 - 69: ooO % i1iiIII111ii - II + i1iiIII111ii - O0 % OoooooooOO
 Iii111II ( iiii11I , Iiii )
 Ooo0OO0oOO ( "[COLOR red][B]Resolver Settings[/B][/COLOR]" , 'IPTVSUBONLY' , 6 , I1ii11iIi11i , I11i , 'Open Resolver Settings' )
 ii11i1 ( )
 if 29 - 29: i11Ii11I1Ii1i % O00oOoOoO0o0O + iiIIi1IiIi11 / II + OOoO * II
def i1I1iI ( ) :
 resolveurl . display_settings ( )
 if 93 - 93: iIii1I11I1II1 % ooO * i1IIi
def Iii111II ( name , url ) :
 if 16 - 16: O0 - i1iiIII111ii * iIii1I11I1II1 + OOooo0000ooo
 I1ii11iIi11i = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + o0OO00 , 'icon.png' ) )
 Ii11iII1 = url
 if 'worldkodi' in url :
  Oo0O0O0ooO0O ( "[COLOR red][B]Universe Streams[/B][/COLOR]" , 'IPTVSUBONLY' , 2 , I1IiI , Oo , 'Subscription Required' )
  O0O00o0OOO0 = Ii1iIIIi1ii ( url )
  try :
   IIIIii = re . compile ( '<item>(.+?)</item>' ) . findall ( O0O00o0OOO0 )
   for O0o0 in IIIIii :
    if 'folder' in O0o0 :
     o0oo0o0O00OO = re . compile ( '<title>(.+?)</title>.+?folder>(.+?)</folder>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>' ) . findall ( O0o0 )
     for name , url , OO00Oo , O0O in o0oo0o0O00OO :
      Oo0O0O0ooO0O ( name , url , 2 , OO00Oo , O0O )
    else :
     O0OOO0OOoO0O = re . compile ( '<link>(.+?)</link>' ) . findall ( O0o0 )
     if len ( O0OOO0OOoO0O ) == 1 :
      o0oo0o0O00OO = re . compile ( '<title>(.+?)</title>.+?link>(.+?)</link>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>' ) . findall ( O0o0 )
      O00Oo000ooO0 = len ( IIIIii )
      for name , url , OO00Oo , O0O in o0oo0o0O00OO :
       Ooo0OO0oOO ( name , url , 99 , OO00Oo , O0O )
     elif len ( O0OOO0OOoO0O ) > 1 :
      name = re . compile ( '<title>(.+?)</title>' ) . findall ( O0o0 ) [ 0 ]
      try :
       OO00Oo = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( O0o0 ) [ 0 ]
      except IndexError :
       OO00Oo = I1ii11iIi11i
      try :
       O0O = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( O0o0 ) [ 0 ]
      except IndexError :
       O0O = O0O
      Ooo0OO0oOO ( name , Ii11iII1 , 4 , OO00Oo , O0O )
  except : pass
 elif 'IPTVSUBONLY' in url :
  OoO0O00 ( url )
  if 5 - 5: O0oo0OO0 / II . i1 - O0 / oOOOO
def OoO0O00 ( url ) :
 if 62 - 62: iIii1I11I1II1 * I1i1iI1i
 if 'IPTVSUBONLY' in url :
  if OOo000 == '' or O0I11i1i11i1I == '' :
   i1OOO = xbmcgui . Dialog ( ) . yesno ( iIiiiI1IiI1I1 , '[COLOR yellow]Sorry You Need An Active Subscription To Enter This Area, Would You Like To Enter Those Details Now?[/COLOR]' , yeslabel = '[COLOR lime]Enter Details[/COLOR]' , nolabel = '[COLOR red]No Quit[/COLOR]' )
   if i1OOO :
    i1iII1IiiIiI1 . openSettings ( )
    xbmc . executebuiltin ( 'Container.Refresh' )
   else :
    quit ( )
  else :
   try :
    Ooo0OO0oOO ( "[COLOR red][B]Subscription Information[/B][/COLOR]" , 'url' , 5 , I1IiI , Oo , 'Subscription Required' )
    Oo0oOOo = OOO0O + oo0ooO0oOOOOo
    O0O00o0OOO0 = Ii1iIIIi1ii ( Oo0oOOo )
    o0oo0o0O00OO = json . loads ( O0O00o0OOO0 )
    for O0o0 in o0oo0o0O00OO :
     Oo0OoO00oOO0o = O0o0 [ 'category_name' ]
     OOO00O = O0o0 [ 'category_id' ]
     I1ii11iIi11i = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + o0OO00 , 'icon.png' ) )
     Oo0O0O0ooO0O ( Oo0OoO00oOO0o , str ( OOO00O ) , 3 , I1IiI , Oo )
    Ooo ( )
   except :
    iI111iI . notification ( iIiiiI1IiI1I1 , '[COLOR red]Your Sub Has Possibly Expired or The Service Is Temp Down[/COLOR]' , I1IiI , 2500 )
    i1iII1IiiIiI1 . openSettings ( )
 else :
  OOoOO0oo0ooO = OOO0O + oO000OoOoo00o + url
  O0O00o0OOO0 = Ii1iIIIi1ii ( OOoOO0oo0ooO )
  O0o0O00Oo0o0 = ET . ElementTree ( ET . fromstring ( O0O00o0OOO0 ) )
  O00O0oOO00O00 = O0o0O00Oo0o0 . getroot ( )
  for i1Oo00 in O00O0oOO00O00 . findall ( 'channel' ) :
   i1i = i1Oo00 . find ( 'title' ) . text
   i1i = base64 . b64decode ( i1i )
   try :
    I1ii11iIi11i = i1Oo00 . find ( 'desc_image' ) . text
   except :
    I1ii11iIi11i = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + o0OO00 , 'icon.png' ) )
   O0O00o0OOO0 = i1Oo00 . find ( 'stream_url' ) . text
   try :
    iiI111I1iIiI = i1Oo00 . find ( 'description' ) . text
    iiI111I1iIiI = base64 . b64decode ( iiI111I1iIiI )
   except : iiI111I1iIiI = 'No EPG Info Available For This Channel'
   Ooo0OO0oOO ( i1i , O0O00o0OOO0 , 99 , I1IiI , Oo , iiI111I1iIiI )
   if 41 - 41: O0oo0OO0 . iiIIi1IiIi11 + O0 * II % O0oo0OO0 * O0oo0OO0
def Ii1iIIIi1ii ( url ) :
 try :
  iIIIIi1iiIi1 = urllib2 . Request ( url )
  iIIIIi1iiIi1 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36' )
  iii1i1iiiiIi = urllib2 . urlopen ( iIIIIi1iiIi1 , timeout = 5 )
  O0O00o0OOO0 = iii1i1iiiiIi . read ( )
  iii1i1iiiiIi . close ( )
  O0O00o0OOO0 = O0O00o0OOO0 . replace ( '\n' , '' ) . replace ( '\r' , '' )
  return O0O00o0OOO0
 except : quit ( )
 if 2 - 2: O00oOoOoO0o0O / O0 / II % I1i1iI1i % i1
def Oo0O0O0ooO0O ( name , url , mode , iconimage , fanart , description = '' ) :
 if 52 - 52: II
 if not iconimage :
  iconimage = I1ii11iIi11i
 if not fanart :
  fanart = I11i
 description = description . encode ( encoding = 'UTF-8' , errors = 'strict' )
 o0OO0oOO0O0 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 iiiIIi1II = True
 o0O00oOoOO = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage , )
 o0O00oOoOO . setProperty ( "fanart_Image" , fanart )
 o0O00oOoOO . setProperty ( "icon_Image" , iconimage )
 o0O00oOoOO . setInfo ( 'video' , { 'Plot' : description } )
 iiiIIi1II = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = o0OO0oOO0O0 , listitem = o0O00oOoOO , isFolder = True )
 iIIi1i1 = xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , 'movies' )
 return iiiIIi1II
 if 10 - 10: ooo0Oo0
def Ooo0OO0oOO ( name , url , mode , iconimage , fanart , description = '' ) :
 if 82 - 82: i11Ii11I1Ii1i - iIii1I11I1II1 / OOoO + i1
 if not iconimage :
  iconimage = I1ii11iIi11i
 if not fanart :
  fanart = I11i
 o0OO0oOO0O0 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart )
 iiiIIi1II = True
 o0O00oOoOO = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage )
 o0O00oOoOO . setProperty ( "fanart_Image" , fanart )
 o0O00oOoOO . setProperty ( "icon_Image" , iconimage )
 o0O00oOoOO . setInfo ( 'video' , { 'Plot' : description } )
 OOOOoOoo0O0O0 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( '889' ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart )
 o0O00oOoOO . addContextMenuItems ( [ ( '[COLOR pink]Add To Bishop Favourites[/COLOR]' , 'xbmc.RunPlugin(' + OOOOoOoo0O0O0 + ')' ) ] )
 iIIi1i1 = xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , 'movies' )
 iiiIIi1II = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = o0OO0oOO0O0 , listitem = o0O00oOoOO , isFolder = False )
 return iiiIIi1II
 if 85 - 85: ooO % i11iIiiIii - OOooo0000ooo * OoooooooOO / O00oOoOoO0o0O % O00oOoOoO0o0O
def IIiIi1iI ( txt ) :
 if 35 - 35: i1 % O0 - O0
 txt = txt . replace ( "&quot;" , "\"" )
 txt = txt . replace ( "&amp;" , "&" )
 txt = txt . replace ( u"\u2018" , "'" ) . replace ( u"\u2019" , "'" )
 txt = txt . strip ( )
 return txt
 if 16 - 16: iii1I1I % I1i1iI1i - iii1I1I + i1
def i1I1i ( string ) :
 Ii = ( c for c in string if 0 < ord ( c ) < 127 )
 if 22 - 22: iii1I1I
 return '' . join ( Ii )
 if 33 - 33: ooo0Oo0
def iI11i1ii11 ( heading , text ) :
 if 58 - 58: Oo0ooO0oo0oO % i11iIiiIii . OOooo0000ooo / ooO
 text = text + "\n\nNews Updates Every 5 Seconds"
 id = 10147
 xbmc . executebuiltin ( 'ActivateWindow(%d)' % id )
 xbmc . sleep ( 500 )
 O0o = xbmcgui . Window ( id )
 OoOooO = 50
 while ( OoOooO > 0 ) :
  try :
   xbmc . sleep ( 10 )
   OoOooO -= 1
   O0o . getControl ( 1 ) . setLabel ( heading )
   O0o . getControl ( 5 ) . setText ( text )
   quit ( )
   return
  except : pass
  if 12 - 12: O00oOoOoO0o0O * OOooo0000ooo % i1IIi % iIii1I11I1II1
def IIi1I11I1II ( name , url , iconimage ) :
 if 63 - 63: OoooooooOO - Oo0ooO0oo0oO . iii1I1I / II . I1i1iI1i / O0
 iI111iI . notification ( iIiiiI1IiI1I1 , '[COLOR pink]Attempting To Resolve Link Now[/COLOR]' , I1ii11iIi11i , 5000 )
 if resolveurl . HostedMediaFile ( url ) . valid_url ( ) :
  o0OOOO00O0Oo = resolveurl . HostedMediaFile ( url ) . resolve ( )
  o0O00oOoOO = xbmcgui . ListItem ( name , iconImage = I1ii11iIi11i , thumbnailImage = I1ii11iIi11i )
  o0O00oOoOO . setPath ( o0OOOO00O0Oo )
  xbmc . Player ( ) . play ( o0OOOO00O0Oo , o0O00oOoOO , False )
  quit ( )
 else :
  o0OOOO00O0Oo = url
  o0O00oOoOO = xbmcgui . ListItem ( name , iconImage = I1ii11iIi11i , thumbnailImage = I1ii11iIi11i )
  o0O00oOoOO . setPath ( o0OOOO00O0Oo )
  xbmc . Player ( ) . play ( o0OOOO00O0Oo , o0O00oOoOO , False )
  quit ( )
  if 48 - 48: O0
def I1IiiI ( name , url , iconimage ) :
 if 44 - 44: O0oo0OO0 . Oo0ooO0oo0oO / i11Ii11I1Ii1i + i1
 iI111iI = xbmcgui . Dialog ( )
 o0o = [ ]
 O0OOoO00OO0o = [ ]
 I1111IIIIIi = [ ]
 O0O00o0OOO0 = Ii1iIIIi1ii ( url )
 Iiii1i1 = re . compile ( '<title>' + re . escape ( name ) + '</title>(.+?)</item>' , re . DOTALL ) . findall ( O0O00o0OOO0 ) [ 0 ]
 iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Iiii1i1 ) [ 0 ]
 O0OOO0OOoO0O = re . compile ( '<link>(.+?)</link>' ) . findall ( Iiii1i1 )
 OO = 1
 for oo000o in O0OOO0OOoO0O :
  iiIi1IIi1I = oo000o
  if '(' in oo000o :
   oo000o = oo000o . split ( '(' ) [ 0 ]
   o0OoOO000ooO0 = str ( iiIi1IIi1I . split ( '(' ) [ 1 ] . replace ( ')' , '' ) )
   o0o . append ( oo000o )
   O0OOoO00OO0o . append ( o0OoOO000ooO0 )
  else :
   o0o . append ( oo000o )
   O0OOoO00OO0o . append ( '[COLOR aqua]Link ' + str ( OO ) + '[/COLOR]' )
  OO = OO + 1
 name = '[COLOR aqua]' + name + '[/COLOR]'
 iI111iI = xbmcgui . Dialog ( )
 o0o0o0oO0oOO = iI111iI . select ( name , O0OOoO00OO0o )
 if o0o0o0oO0oOO < 0 :
  quit ( )
 else :
  url = o0o [ o0o0o0oO0oOO ]
  print url
  if resolveurl . HostedMediaFile ( url ) . valid_url ( ) : o0OOOO00O0Oo = resolveurl . HostedMediaFile ( url ) . resolve ( )
  elif liveresolver . isValid ( url ) == True : o0OOOO00O0Oo = liveresolver . resolve ( url )
  else : o0OOOO00O0Oo = url
  o0O00oOoOO = xbmcgui . ListItem ( name , iconImage = 'DefaultVideo.png' , thumbnailImage = iconimage )
  o0O00oOoOO . setPath ( o0OOOO00O0Oo )
  xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , o0O00oOoOO )
  iI111iI . notification ( iIiiiI1IiI1I1 , '[COLOR red]Attempting To Resolve Link Now[/COLOR]' , I1ii11iIi11i , 5000 )
  time . sleep ( 1 )
  xbmc . Player ( ) . play ( o0OOOO00O0Oo )
  if 3 - 3: II
def ii11i1 ( ) :
 if 24 - 24: i11iIiiIii + OOooo0000ooo * i1 - iii1I1I . OOoO % iIii1I11I1II1
 ooI1IiiiiI = xbmc . getInfoLabel ( "System.BuildVersion" )
 o0O = float ( ooI1IiiiiI [ : 4 ] )
 if o0O >= 11.0 and o0O <= 11.9 :
  IiII = 'Eden'
 elif o0O >= 12.0 and o0O <= 12.9 :
  IiII = 'Frodo'
 elif o0O >= 13.0 and o0O <= 13.9 :
  IiII = 'Gotham'
 elif o0O >= 14.0 and o0O <= 14.9 :
  IiII = 'Helix'
 elif o0O >= 15.0 and o0O <= 15.9 :
  IiII = 'Isengard'
 elif o0O >= 16.0 and o0O <= 16.9 :
  IiII = 'Jarvis'
 elif o0O >= 17.0 and o0O <= 17.9 :
  IiII = 'Krypton'
 else : IiII = "Decline"
 if IiII == "Jarvis" :
  xbmc . executebuiltin ( 'Container.SetViewMode(55)' )
 elif IiII == "Krypton" :
  xbmc . executebuiltin ( 'Container.SetViewMode(55)' )
 else : xbmc . executebuiltin ( 'Container.SetViewMode(55)' )
 if 25 - 25: O0 - O0 * II
def OOOO0oo0 ( text ) :
 if 35 - 35: i1 - O00oOoOoO0o0O % II . OoooooooOO % i1
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
 text = text . replace ( '&#8216;' , "'" )
 text = text . replace ( '&#8230;' , "..." )
 text = text . replace ( '&#8220;' , "'" )
 text = text . replace ( '&#8221;' , "'" )
 text = text . replace ( '&#8212;' , "_" )
 text = text . lstrip ( ' ' )
 text = text . lstrip ( '	' )
 text = i1I1i ( text )
 return text
 if 47 - 47: OOooo0000ooo - i1 . iii1I1I + OoooooooOO . i11iIiiIii
 if 94 - 94: II * i1 / O0oo0OO0 / i1
 if 87 - 87: O0oo0OO0 . oOOOO
 if 75 - 75: iiIIi1IiIi11 + I1i1iI1i + II * ooo0Oo0 % ooO . OOooo0000ooo
def oO ( ) :
 if 31 - 31: OOoO + i11iIiiIii + O0oo0OO0 * iiIIi1IiIi11
 IiII111iI1ii1 = [ ]
 iI11I1II = sys . argv [ 2 ]
 if len ( iI11I1II ) >= 2 :
  Ii1I = sys . argv [ 2 ]
  IiI1i = Ii1I . replace ( '?' , '' )
  if ( Ii1I [ len ( Ii1I ) - 1 ] == '/' ) :
   Ii1I = Ii1I [ 0 : len ( Ii1I ) - 2 ]
  o0Oo00 = IiI1i . split ( '&' )
  IiII111iI1ii1 = { }
  for OO in range ( len ( o0Oo00 ) ) :
   iIO0O0Oooo0o = { }
   iIO0O0Oooo0o = o0Oo00 [ OO ] . split ( '=' )
   if ( len ( iIO0O0Oooo0o ) ) == 2 :
    IiII111iI1ii1 [ iIO0O0Oooo0o [ 0 ] ] = iIO0O0Oooo0o [ 1 ]
 return IiII111iI1ii1
 if 56 - 56: i11Ii11I1Ii1i % O0 - O00oOoOoO0o0O
Ii1I = oO ( ) ; oOOO00o = None ; iiii11I = None ; O00o0OO0 = None ; IIi1I1iiiii = None ; OO00Oo = None ; iiI111I1iIiI = None
try : IIi1I1iiiii = urllib . unquote_plus ( Ii1I [ "site" ] )
except : pass
try : oOOO00o = urllib . unquote_plus ( Ii1I [ "url" ] )
except : pass
try : iiii11I = urllib . unquote_plus ( Ii1I [ "name" ] )
except : pass
try : O00o0OO0 = int ( Ii1I [ "mode" ] )
except : pass
try : OO00Oo = urllib . unquote_plus ( Ii1I [ "iconimage" ] )
except : pass
try : O0O = urllib . unquote_plus ( Ii1I [ "fanart" ] )
except : pass
try : iiI111I1iIiI = urllib . unquote_plus ( Ii1I [ "description" ] )
except : pass
if 71 - 71: oOOOO * iii1I1I * ooO
if O00o0OO0 == None or oOOO00o == None or len ( oOOO00o ) < 1 : iIii11I ( )
if 56 - 56: O00oOoOoO0o0O
elif O00o0OO0 == 2 : Iii111II ( iiii11I , oOOO00o )
elif O00o0OO0 == 3 : OoO0O00 ( oOOO00o )
elif O00o0OO0 == 4 : I1IiiI ( iiii11I , oOOO00o , OO00Oo )
elif O00o0OO0 == 5 : iI ( )
elif O00o0OO0 == 6 : i1I1iI ( )
if 54 - 54: i1iiIII111ii / OOoO . ooO % OOooo0000ooo
elif O00o0OO0 == 99 : IIi1I11I1II ( iiii11I , oOOO00o , OO00Oo )
if 57 - 57: i11iIiiIii . i11Ii11I1Ii1i - i1 - ooO + I1i1iI1i
if O00o0OO0 == None or oOOO00o == None or len ( oOOO00o ) < 1 : xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) , cacheToDisc = False )
else : xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) , cacheToDisc = True ) # dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
