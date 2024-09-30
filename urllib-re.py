import urllib.request, urllib.error, urllib.parse
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
html = urllib.request.urlopen(url).read()
enlaces = re.findall(b'href="(http[s]?://.*?)"',html)
for enlace in enlaces:
    print(enlace.decode())
