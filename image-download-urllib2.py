import urllib.request, urllib.parse, urllib.error

imagen='https://www.biografiasyvidas.com/monografia/julio_cesar/fotos/cesar_asesinato.jpg'
gaius=urllib.request.urlopen(imagen)
tamano=0
julius=open('caesar.JPG','wb')
while True:
    info=gaius.read(100000)
    if len(info) < 1:
        break
    tamano+=len(info)
    julius.write(info)
    
print('Esta imagen tiene',tamano,'caracteres')
julius.close()
