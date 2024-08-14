import random
def rollDice(numberOfDice):
    if rollDice==0: return 0
    contenedor=0
    for i in range(numberOfDice):
        generico=random.randint(1,6)
        contenedor=contenedor+generico
    return contenedor    
    
print(rollDice(3))  
