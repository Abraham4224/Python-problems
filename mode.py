def mode(numbers):
    counts=dict()
    contador=None
    for number in numbers:
        counts[number]=counts.get(number,0)+1
    for key,valor in counts.items():
        if contador==None or valor>contador:
            contador=valor
            nombre=key
    return nombre       
print(mode([1,1,2,2,2,1,1,1]))   
