def calculateSum(numbers):
    if len(numbers)==0: return 0
    contador=0
    for i in numbers:
        contador=contador+i
    return contador

def calculateProduct(numbers):
    uno=1
    if len(numbers)==0: return 1
    for i in numbers:
        uno*=i
    return uno    
    
print(calculateSum(lis))
print(calculateProduct([2,4,6,2]))
