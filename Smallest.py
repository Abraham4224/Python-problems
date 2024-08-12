def getSmallest(numbers):
    if len(numbers)==0: return 0
    menor=None
    for i in numbers:
        if menor==None or i<menor:
            menor=i
    return menor
lis=[3,2,1,4]
print(getSmallest(lista))
