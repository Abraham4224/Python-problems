import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)
am = ''
headers_ended = False

while True:
    datos = mysock.recv(3000)
    if len(datos) < 1:
        break
    linea = datos.decode()
    if not headers_ended:
        pos = linea.find('\r\n\r\n')
        if pos != -1:
            headers_ended = True
            am += linea[pos+4:]
    else:
        am += linea

print(am)
mysock.close()
