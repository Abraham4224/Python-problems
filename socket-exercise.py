import socket

url = input('Enter a URL:')
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dominio = url.split('/')
print(dominio)
try:
    mysock.connect((dominio[2], 80))
except:
    print('URL not valid')

cmd = f'GET /{dominio[3]} HTTP/1.1\r\nHost: {dominio[2]}\r\n\r\n'
cmd=cmd.encode()
mysock.send(cmd)

while True:
    datos = mysock.recv(512)
    if len(datos) < 1:
        break
    print(datos.decode(), end='')

mysock.close()
