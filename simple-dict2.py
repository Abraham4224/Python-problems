archivo = open("words.txt")
diccionario=dict()
for linea in archivo:
    linea=linea.rstrip()
    linea=linea.split()
    for palabra in linea:
        diccionario[palabra]=0
        
        
print("is" in diccionario)   
