def getTitleCase(text):
    frase = ''
    es_nueva_palabra = True
    
    for i in range(len(text)):
        if text[i].isalpha():
            if es_nueva_palabra:
                frase += text[i].upper()
                es_nueva_palabra = False
            else:
                frase += text[i].lower()
        else:
            frase += text[i]
            es_nueva_palabra = True  
    
    return frase   

print(getTitleCase(' cat,dog,RAT'))
