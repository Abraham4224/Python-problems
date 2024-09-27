import urllib.request, urllib.parse, urllib.error

img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg')
tamaño=0
man=open('portada.jpg','wb')
while True:
    info = img.read(100000)
    if len(info) < 1:
        break
    tamaño+=len(info) 
    man.write(info)
    
print('Tamaño:',tamaño)
man.close()
