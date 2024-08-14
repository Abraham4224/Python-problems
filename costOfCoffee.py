def getCostOfCoffee(numberOfCoffees,pricePerCoffee):
    cafes=numberOfCoffees
    contador=0
    if numberOfCoffees<=8:
        return numberOfCoffees*pricePerCoffee
    while cafes>8:
        cafes=cafes-8
        contador+=1
    return (numberOfCoffees-contador)*pricePerCoffee    
        
        

    
print(getCostOfCoffee(9,3)) 
