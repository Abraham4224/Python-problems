def median(numbers):
    if len(numbers)==0: return None
    if len(numbers)%2!=0: 
        return numbers[len(numbers)//2]
    if len(numbers)%2==0:
        numbers1=sorted(numbers)
        op=len(numbers1)//2
        os=op-1
        numero1=numbers1[op]
        numero2=numbers1[os]
        numero3=(numero1+numero2)/2
        return numero3
        
    
print(median([1,2,3,4,5,6,7]))   
print(median([]))
print(median([3, 7, 10, 4, 1, 9, 6, 5, 2, 8]))
