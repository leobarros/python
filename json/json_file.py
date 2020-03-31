import json
# from urllib import request

tv = '''
{
  "timestamp": 1584328521931,
  "postInstallChecksum": [],
  "manufacturer": "Smart tv",
  "model": "Ue3",
  "os": "Linux",
  "version": "1.2.34",
  "format": "zip",
  "mode": "app_only",
  "appname": "app_name",
  "filename": "app_name.zip",
  "checksum": "108d9998f67697fdfeeed9236b6401736",
  "url": "http://example.com/app_name.zip"
}
'''

data = json.loads(tv)

print('%s: %s' % (data['manufacturer'], data['version']))
