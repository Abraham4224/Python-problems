import random 

length=input("How long do you want your password to be?")

def generatePassword(length):
    lista=[]
    if length<12: 
        length=12
    for i in range(length):
        aleatorio=random.randint(32,127)
        lista.append(chr(aleatorio))
    contraseña=''.join(lista)
    return contraseña


print(generatePassword(length))
