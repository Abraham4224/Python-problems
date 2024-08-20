import urllib.request, urllib.parse, urllib.error
import ssl
import xml.etree.ElementTree as ET

#este codigo toma una pagina web en xml usando el urllib, luego lo lee y lo pasa al xml tree, para manejar el archivo xml encontrar todos
#los count y después archivarlos en una lista,iteramos y al contrario de otras ocasiones no necesitamos usar find solo text
#creo que porque ya sacamos de una los count
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url= 'https://py4e-data.dr-chuck.net/comments_1950238.xml'
xml = urllib.request.urlopen(url, context=ctx)
data=xml.read()
tree = ET.fromstring(data)
counts = tree.findall('.//count')
x=0
for count in counts:
    count_int= int(count.text)
    x=x+count_int
    
print(x)    
