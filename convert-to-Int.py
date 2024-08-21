def convertToInt(snumber):
    dictn={'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'0':0}
    listadesuma=[]
    digitos=len(snumber)
    for j in range(digitos-1,-1,-1):
        exponente=10**j
        listadesuma.append(exponente)
    numero=0
    for i in range(len(snumber)):
        indice=snumber[i]
        resultado=dictn[indice]*listadesuma[i]
        numero+=resultado
    return numero
