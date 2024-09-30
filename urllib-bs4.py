import urllib.request, urllib.error, urllib.parse
import ssl
from bs4 import BeautifulSoup

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Introduzca url ' )
html = urllib.request.urlopen(url, context=ctx).read()
sopa = BeautifulSoup(html, 'html.parser')

etiquetas = sopa('a')
for etiqueta in etiquetas:
    print(etiqueta.get('href', None))
