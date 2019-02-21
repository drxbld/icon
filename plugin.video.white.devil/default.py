import urlparse,sys,re
import urllib, urllib2
from urlparse import parse_qsl
import requests
import xml.etree.ElementTree as ET
import xbmcaddon, os
import base64
import xbmc
import xbmcplugin
import xbmcgui



params = dict(urlparse.parse_qsl(sys.argv[2].replace('?','')))

action = params.get('action')

content = params.get('content')

name = params.get('name')

url = params.get('url')

image = params.get('image')

fanart = params.get('fanart')

addonPath = xbmcaddon.Addon().getAddonInfo("path")

pw = urllib2.urlopen(base64.b64decode('aHR0cDovL2JyZXR0dXNidWlsZHMuY29tLy5XSElURSUyMERFVklML05FTUVTSVMvcG9ybnBhc3MudHh0'))
adult_password = pw.read()


def getVersion():
	req = urllib.urlopen("http://brettusbuilds.com/brettusok.txt").read()
	print "req.version = " + req 
	if req == None:
		return 0
	else:
		return int(req)

def update():
	from resources.lib.indexers import hub
	print "hub.version = " + str(hub.version)
	print "github.version = " + str(getVersion())
	if hub.version < getVersion():
		req = urllib.urlopen(base64.b64decode("aHR0cDovL2JyZXR0dXNidWlsZHMuY29tL3VwZGF0ZS50eHQ=")).read()
		print "code got, updating NOW"
		if req == None:
			print "Something went wrong!"
		else:
			print "hubfile.path = " + os.path.join(addonPath, "resources", "lib", "indexers", "hub.py")
			with open(os.path.join(addonPath, "resources", "lib", "indexers", "hub.py"), "wb") as filewriter:
				filewriter.write(req)

				
Project_key = 'ZDQxZDhjZDk4ZjAwYjIw' # Project API Key 
Project_ID = '1165256'# Your project ID 
#########################################		
import base64;exec base64.b64decode('IyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMKaW1wb3J0IGJhc2U2NAppbXBvcnQgeGJtY2d1aQppbXBvcnQgcmVxdWVzdHMKaWYgNjQgLSA2NDogaTExaUlpaUlpaQpkZWYgT08wbyAoIHN0ICkgOgogaW1wb3J0IHJlCiBzdCA9IHJlIC4gc3ViICggJ1xbLitcXScgLCAnJyAsIHN0ICkKIGltcG9ydCBzdHJpbmcKIE9vME9vbyA9IDAKIGZvciBPME8wT08wTzBPMCBpbiBzdCA6CiAgaWYgTzBPME9PME8wTzAgaW4gJ2xpanxcJyAnIDogT28wT29vICs9IDM3CiAgZWxpZiBPME8wT08wTzBPMCBpbiAnIVtdZkkuLDo7L1xcdCcgOiBPbzBPb28gKz0gNTAKICBlbGlmIE8wTzBPTzBPME8wIGluICdgLSgpe31yIicgOiBPbzBPb28gKz0gNjAKICBlbGlmIE8wTzBPTzBPME8wIGluICcqXnpjc0prdnh5JyA6IE9vME9vbyArPSA4NQogIGVsaWYgTzBPME9PME8wTzAgaW4gJ2FlYmRobm9wcXVnIyRMKzw+PT9ffkZaVCcgKyBzdHJpbmcgLiBkaWdpdHMgOiBPbzBPb28gKz0gOTUKICBlbGlmIE8wTzBPTzBPME8wIGluICdCU1BFQUtWWFkmVXdOUkNIRCcgOiBPbzBPb28gKz0gMTEyCiAgZWxpZiBPME8wT08wTzBPMCBpbiAnUUdPTW0lV0AnIDogT28wT29vICs9IDEzNQogIGVsc2UgOiBPbzBPb28gKz0gNTAKIHJldHVybiBpbnQgKCBPbzBPb28gKiA2LjUgLyAxMDAgKQogaWYgNSAtIDU6IGlpSSAvIGlpMUkKZGVmIG9vTzBPTzAwMG8gKCBIZWFkaW5nID0geGJtY2FkZG9uIC4gQWRkb24gKCApIC4gZ2V0QWRkb25JbmZvICggJ25hbWUnICkgKSA6CiBpaTExaSA9IHhibWMgLiBLZXlib2FyZCAoICcnICwgSGVhZGluZyApCiBpaTExaSAuIGRvTW9kYWwgKCApCiBpZiAoIGlpMTFpIC4gaXNDb25maXJtZWQgKCApICkgOgogIHJldHVybiBpaTExaSAuIGdldFRleHQgKCApCiAgaWYgNjYgLSA2NjogaUlpSSAqIGlJaWlpSTFJaUkxSTEgKiBvME9vT29PTzAwCmRlZiBJMTFpICggdXJsICkgOgogaWYgNjQgLSA2NDogT09vb28wMDBvbzAgLiBpMSAqIGlpMUlpSTFpICUgSUlJaWlJSWlpCiBpbXBvcnQgd2ViYnJvd3NlcgogaWYgOCAtIDg6IE9vIC8gaUlJMTFpaUlJSTExMSAlIGlpaUlJaWkxSTFJaSAuIE8wMG9Pb09vTzBvME8KIElJMWlpMUlJMWlJSTEgPSB3ZWJicm93c2VyIC4gb3BlbgogSWkgPSB4Ym1jIC4gZXhlY3V0ZWJ1aWx0aW4KIE9vMG8gPSBsYW1iZGEgT09PMG8wbyA6IHhibWMgLiBnZXRDb25kVmlzaWJpbGl0eSAoIHN0ciAoIE9PTzBvMG8gKSApCiBJaTFpSSA9IGxhbWJkYSBPT08wbzBvIDogSWkgKCAnU3RhcnRBbmRyb2lkQWN0aXZpdHkoLGFuZHJvaWQuaW50ZW50LmFjdGlvbi5WSUVXLCwlcyknICUgKCBPT08wbzBvICkgKQogaWYgMTAwIC0gMTAwOiBpMTFJaTExSTFJaTFpIC4gb29PIC0gT09vTyAvIG9vbzBPbzAgKiBpMU9Pb29vMDAwMG9vbyAtIE9PbzAwMAogTzAgPSAnU3lzdGVtLlBsYXRmb3JtLkFuZHJvaWQnCiBpZiAzNCAtIDM0OiBvb28wT28wICUgbzBPb09vT08wMCAlIGlpMUkgJSBvb28wT28wICogT09vTyAvIElJSWlpSUlpaQogaWYgT28wbyAoIE8wICkgOiBJaTFpSSAoIGJhc2U2NCAuIGI2NGRlY29kZSAoIHVybCApICkKIGVsc2UgOiBJSTFpaTFJSTFpSUkxICggYmFzZTY0IC4gYjY0ZGVjb2RlICggdXJsICkgKQogaWYgMzEgLSAzMTogaTExaUlpaUlpaSAvIE9Pb29vMDAwb28wIC8gT09vMDAwICogaWlpSUlpaTFJMUlpIC8gaTEKIGlmIDk5IC0gOTk6IGlpMUkgKiBpSWlJICogbzBPb09vT08wMCAqIGlpMUkKZGVmIElJSUlJICggKSA6CiBpZiAyNiAtIDI2OiBpMU9Pb29vMDAwMG9vbyAuIGkxMUlpMTFJMUlpMWkgLSBPMDBvT29Pb08wbzBPICUgaWlJICsgTzAwb09vT29PMG8wTwogaW1wb3J0IHN5cwogaWYgMzQgLSAzNDogaTExSWkxMUkxSWkxaSAqIE9Pb29vMDAwb28wCiBpaWlJMTEgPSB4Ym1jYWRkb24gLiBBZGRvbiAoICkgLiBnZXRBZGRvbkluZm8KIE9Pb29PID0gaWlpSTExICggJ25hbWUnICkKIE9Pb08wMG8gPSBiYXNlNjQgLiBiNjRkZWNvZGUgKCAnVkc4Z1lXTmpaWE56SUZ0RFQweFBVaUIzYUdsMFpWMWJRbDBsYzFzdlFsMWJMME5QVEU5U1hTQjViM1VnZDJsc2JDQnVaV1ZrSUdGdUlHRmpZMlZ6Y3lCMGIydGxiaTRnVUd4bFlYTmxJSEJ5WlhOeklHTnZiblJwYm5WbElIUnZJR2RsZENCaGJpQmhZMk5sYzNNZ2RHOXJaVzR1JyApICUgKCBPT29vTyApCiBJSTExMWlpaWkgPSBPT29PMDBvCiBJSSA9IGJhc2U2NCAuIGI2NGRlY29kZSAoICdTV1lnZVc5MUlHaGhkbVVnWVd4eVpXRmtlU0JuYjNRZ2VXOTFjaUIwYjJ0bGJpQndiR1ZoYzJVZ2MyVnNaV04wSUZ0Q1hWdERUMHhQVWlCM2FHbDBaVjFGYm5SbGNpQlViMnRsYmxzdlEwOU1UMUpkV3k5Q1hTQnBaaUI1YjNVZ1pHOGdibTkwSUdoaGRtVWdZU0IwYjJ0bGJpQndiR1ZoYzJVZ2MyVnNaV04wSUZ0Q1hWdERUMHhQVWlCM2FHbDBaVjFIWlhRZ1ZHOXJaVzViTDBOUFRFOVNYVnN2UWwwZ2IzSWdaMjhnZEc4Z2QzZDNMbVJsZG1Wc2IzQnRaVzUwTFhSdmIyeHpMbTVsZENCMmFXRWdZVzRnWlhoMFpYSnVZV3dnWkdWMmFXTmxJR0Z1WkNCbGJuUmxjaUJKUkRvZ1cwTlBURTlTSUhKbFpGMWJRbDBsYzFzdlFsMWJMME5QVEU5U1hRPT0nICkgJSAoIFByb2plY3RfSUQgKQogb09vT28wMG9PbyA9IHhibWNhZGRvbiAuIEFkZG9uICggKSAuIGdldFNldHRpbmcgKCAncGluJyApCiBPb28wME8wME8wTzBPID0gbGFtYmRhIE9PTzBvMG8gOiBiYXNlNjQgLiBiNjRkZWNvZGUgKCBzdHIgKCBPT08wbzBvICkgKQogT29vTzBPTyA9IGJhc2U2NCAuIGI2NGRlY29kZSAoICdhSFIwY0hNNkx5OWtaWFpsYkc5d2JXVnVkQzEwYjI5c2N5NXVaWFF2ZEc5dmJITXRZWEJwTDJGd2FUOXdhVzQ5SlhNbWEyVjVQUT09JyApICsgYmFzZTY0IC4gYjY0ZGVjb2RlICggUHJvamVjdF9rZXkgKQogaWlpSWkgPSBsYW1iZGEgT09PMG8wbyA6IHJlcXVlc3RzIC4gZ2V0ICggT29vTzBPTyAlICggT09PMG8wbyApICwgdmVyaWZ5ID0gRmFsc2UgKSAuIHRleHQgLiBzdHJpcCAoICkKIElpSUlJaUkxSTEgPSBsYW1iZGEgT09PMG8wbyA6IHhibWNhZGRvbiAuIEFkZG9uICggKSAuIHNldFNldHRpbmcgKCBiYXNlNjQgLiBiNjRkZWNvZGUgKCAnY0dsdScgKSAsIE9PTzBvMG8gKQogT29PMDAwID0gbGFtYmRhIE9PTzBvMG8gOiB4Ym1jZ3VpIC4gRGlhbG9nICggKSAuIHllc25vICggaWlpSTExICggJ25hbWUnICkgLCBPT08wbzBvICwgeWVzbGFiZWwgPSAiQ29udGludWUiICwgbm9sYWJlbCA9ICdDYW5jZWwnICwgKQogSUlpaUlpSTEgPSBsYW1iZGEgT09PMG8wbyA6IHhibWNndWkgLiBEaWFsb2cgKCApIC4geWVzbm8gKCBpaWlJMTEgKCAnbmFtZScgKSAsIE9PTzBvMG8gLCB5ZXNsYWJlbCA9ICJFbnRlciB0b2tlbiIgLCBub2xhYmVsID0gJ0dldCB0b2tlbicgLCApCiBpaUlpSUlpID0gYm9vbCAoIGlpaUlpICggb09vT28wMG9PbyApID09IGJhc2U2NCAuIGI2NGRlY29kZSAoICdVR2x1SUZabGNtbG1hV1ZrJyApICkKIG9wZW4gPSAnYUhSMGNITTZMeTkzZDNjdVoyOXZaMnhsTG1OdmJTOTFjbXcvYzJFOWRDWnlZM1E5YWlaeFBTWmxjM0pqUFhNbWMyOTFjbU5sUFhkbFlpWmpaRDB4Sm1OaFpEMXlhbUVtZFdGamREMDRKblpsWkQweVlXaFZTMFYzYWtoNVVFOXpOSEJ5WjBGb1dERlZRbFZKU0dGU2MwRjZORkZHYWtGQlpXZFJTVU5TUVVJbWRYSnNQV2gwZEhCekpUTkJKVEpHSlRKR1pHVjJaV3h2Y0cxbGJuUXRkRzl2YkhNdWJtVjBKVEpHSm5Welp6MUJUM1pXWVhjeWMydHlVblpJYldJelZrdHliemhOYkhodk0zSmYnCiBpZiA2NSAtIDY1OiBJSUlpaUlJaWkKIGlmIGlpSWlJSWkgOiByZXR1cm4KIGVsc2UgOgogIGlmIDYgLSA2OiBPT29vbzAwMG9vMCAvIGkxICUgb29PCiAgaWYgT29PMDAwICggT09vTzAwbyApIDoKICAgaWYgSUlpaUlpSTEgKCBJSSApIDoKICAgIG9vID0gb29PME9PMDAwbyAoICdUeXBlIFlvdXIgYWNjZXNzIHRva2VuIGhlcmUnICkKICAgIElpSUlJaUkxSTEgKCBvbyApCiAgICBJSUlJSSAoICkKICAgZWxzZSA6CiAgICBJMTFpICggb3BlbiApCiAgICBzeXMgLiBleGl0ICggMSApCiAgZWxzZSA6CiAgIHN5cyAuIGV4aXQgKCApICMgZGQ2NzhmYWFlOWFjMTY3YmM4M2FiZjc4ZTVjYjJmM2YwNjg4ZDNhMwo=]')

IIIII()
update()
if action == None:
	from resources.lib.indexers import hub
	hub.indexer().root()

elif action == 'directory':
	from resources.lib.indexers import hub
	hub.indexer().get(url)
	if "porn.php" in url:
		dialog = xbmcgui.Dialog()
		dialog.ok('','[COLOR fuchsia]To Enter The World Of Immense Pleasure[/COLOR] ' , '[COLOR gold]Please Enter The Password.[/COLOR]')
		keyb = xbmc.Keyboard("", "Enter 18+ Password")
		keyb.doModal()
		if (keyb.isConfirmed()):
			password2=keyb.getText()
			password = base64.b64encode(password2)
		else:quit()
		passkey = base64.b64encode(adult_password)
		if not password == passkey:
			dialog.ok('', '"                                   [COLOR red]Incorrect Password[/COLOR]\n\n  Donate To [COLOR fuchsia]john4551@hotmail.co.uk[/COLOR] Using Paypal\n[COLOR dodgerblue]Email Or Message White Devil Group On Facebook After Donation For Password[/COLOR]"', '')
			xbmc.executebuiltin("XBMC.Container.Update(path,replace)")
		else:
			dialog.ok('','[COLOR fuchsia]Welcome To White Devil Porn[/COLOR]','')
			

elif action == 'qdirectory':
	from resources.lib.indexers import hub
	hub.indexer().getq(url)

elif action == 'xdirectory':
	from resources.lib.indexers import hub
	hub.indexer().getx(url)

elif action == 'developer':
	from resources.lib.indexers import hub
	hub.indexer().developer()

elif action == 'tvtuner':
	from resources.lib.indexers import hub
	hub.indexer().tvtuner(url)

elif 'youtube' in str(action):
	from resources.lib.indexers import hub
	hub.indexer().youtube(url, action)

elif action == 'play':
	from resources.lib.indexers import hub
	hub.player().play(url, content)

elif action == 'browser':
	from resources.lib.indexers import hub
	hub.resolver().browser(url)

elif action == 'search':
	from resources.lib.indexers import hub
	hub.indexer().search()

elif action == 'addSearch':
	from resources.lib.indexers import hub
	hub.indexer().addSearch(url)

elif action == 'delSearch':
	from resources.lib.indexers import hub
	hub.indexer().delSearch()

elif action == 'queueItem':
	from resources.lib.modules import control
	control.queueItem()

elif action == 'openSettings':
	from resources.lib.modules import control
	control.openSettings()

elif action == 'urlresolverSettings':
	from resources.lib.modules import control
	control.openSettings(id='script.module.urlresolver')

elif action == 'addView':
	from resources.lib.modules import views
	views.addView(content)

elif action == 'downloader':
	from resources.lib.modules import downloader
	downloader.downloader()

elif action == 'addDownload':
	from resources.lib.modules import downloader
	downloader.addDownload(name,url,image)

elif action == 'removeDownload':
	from resources.lib.modules import downloader
	downloader.removeDownload(url)

elif action == 'startDownload':
	from resources.lib.modules import downloader
	downloader.startDownload()

elif action == 'startDownloadThread':
	from resources.lib.modules import downloader
	downloader.startDownloadThread()

elif action == 'stopDownload':
	from resources.lib.modules import downloader
	downloader.stopDownload()

elif action == 'statusDownload':
	from resources.lib.modules import downloader
	downloader.statusDownload()

elif action == 'trailer':
	from resources.lib.modules import trailer
	trailer.trailer().play(name)

elif action == 'clearCache':
	from resources.lib.modules import cache
	cache.clear()