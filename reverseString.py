def reverseString(text):
    if len(text)==0 or text==' ':
        return ' '
    text=list(text)
    texto=[]
    for i in range(len(text)-1,-1,-1):
        texto.append(text[i])
    return ''.join(texto)    
    
    
print(reverseString('Hello')) 
