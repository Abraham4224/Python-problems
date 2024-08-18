def getUppercase(text):
    if len(text)=='': return ''
    nuevacadena=''
    for i in range(len(text)):
        if text[i].isalpha():
            mayus=text[i].upper()
            nuevacadena=nuevacadena+mayus
        else:    
            nuevacadena=nuevacadena+text[i]
    return nuevacadena     
     
print(getUppercase('HellO12')) 
