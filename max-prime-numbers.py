x=input("This will convert your number given in a series of prime numbers: ")
def primeNumbers(n):
    i=2
    factors=[]
    while n>=i*i:
        if  n % i!=0:
            i+=1
        else:
            n=n//i
            factors.append(i)
    if n>1:
        factors.append(n)
    return max(factors)

print(primeNumbers(int(x))
