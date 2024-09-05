def collatz(startingNumber):
    if startingNumber<=0:
        return []
    lista=[]
    lista.append(startingNumber)
    n=startingNumber
    while n!=1:
        if n%2==0:
            n=n/2
            lista.append(int(n))
        else:
            n=(3*n)+1
            lista.append(int(n))
            
    
    return lista

print(collatz(12))
        
