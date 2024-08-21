def convertToString(number):
    dicts={0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9'}
    respuesta=[]
    lista=[]
    while number>0:
        digito=number%10
        respuesta.append(dicts[digito])
        number=number//10
    for x in range((len(respuesta)-1),-1,-1):
        lista.append(respuesta[x])
    return ''.join(lista)   
