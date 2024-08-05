x=int(input("Enter a number to discover if it's odd or even: "))

def isOdd(number):
    if number%2!=0:
        return True
    else:
        return False

def isEven(number):
    if number%2==0:
        return True
    else:
        return False

print("Is it odd?: ")
print(isOdd(42))  
print("Is it even?: ")
print(isEven(42))