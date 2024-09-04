print('Rotate 13 Exercise')
def rot13(text):
    cadena=''
    mayu13='ABCDEFGHIJKLM'
    mayu26='NOPQRSTUVWXYZ'
    minu13='abcdefghijklm'
    minu26='nopqrstuvwxyz'
    for i in range(len(text)):
        if text[i].isupper() and ord(text[i])<=77:
            indice=mayu13.find(text[i])
            cadena=cadena+mayu26[indice]
        elif text[i].isupper() and ord(text[i])>77:
            indice=mayu26.find(text[i])
            cadena=cadena+mayu13[indice]
        elif text[i].islower() and ord(text[i])<=109:
            indice=minu13.find(text[i])
            cadena=cadena+minu26[indice]
        elif text[i].islower() and ord(text[i])>109:
            indice=minu26.find(text[i])
            cadena=cadena+minu13[indice]
        else:
            cadena=cadena+text[i]
    return cadena        
         
       

print(rot13('Hello, world'))  
print(rot13('Uryyb, jbeyq'))
