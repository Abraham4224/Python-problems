import socket

SERVIDOR = "data.pr4e.org"
PUERTO=80
mysock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((SERVIDOR,PUERTO))
mysock.sendall(b'GET http://data.pr4e.org/cover3.jpg HTTP/1.0\r\n\r\n')
contador=0
imagen=b""

while True:
    datos = mysock.recv(5120)
    if len(datos) < 1: 
        break
    contador = contador + len(datos)
    print(len(datos),contador)
    imagen = imagen + datos
    
mysock.close()

pos=imagen.find(b"\r\n\r\n")
print('Header length', pos)
print(imagen[:pos].decode())

imagen = imagen[pos+4:]
fhand =open("cosa.jpg", "wb")
fhand.write(imagen)
fhand.close()
