import random
def shuffle(values):
    for i in range(len(values)):
        posicion1=random.randint(0,len(values)-1)
        posicion2=random.randint(0,len(values)-1)
        if posicion1==posicion2: continue
        valor1=values[posicion1]
        valor2=values[posicion2]
        values[posicion1]=valor2
        values[posicion2]=valor1
        
    return values

lista=[1,2,3,4,5,6,7,8]
shuffle(lista)
print(lista)
