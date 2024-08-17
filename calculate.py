#All natural numbers divisible by 5 or 7 less than 20 are: [0, 5, 7, 10, 14, 15].
#The sum of these numbers is: 51. In this exercise, we treat zero as a natural number.
#Find the sum of all numbers that are divisible by 5 or 7 less than 100

def calculate():
    suma=0
    for n in range(100):
        if n%7==0 or n%5==0:
            suma+=n
    return suma        
 
print(calculate())   

#Another way of doing it.

def calculate2():
    return sum([i for i in range(100) if i%5==0 or i%7==0])

print(calculate2())
