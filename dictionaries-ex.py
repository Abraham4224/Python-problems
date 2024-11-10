# First, a dictionary is created
crypto = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4: "Stellar", 5:"XRP"}
#Then, the value of the key 4 is stored in a variable
value = crypto[4]
print(value)
#Return a key-value using a function.
def ojos(n):
    return crypto[n]

valor = ojos(4)
print(valor)
#Returning a key-value using a method
val=crypto.get(4)
print(val)
#Rewrite the fourth key with a new value
crypto[4] = "Cardano"
print(crypto[4])
#Create a new key-value in dictionary
crypto[6]="Monero"
print(crypto[6])
#Counting the number of items in dictionary
number=len(crypto)
print(number)
#Deleting a key-value
del crypto[6]
print(crypto)
#Deleting a value using pop
crypto.pop(3)
print(crypto)
#Checking if a value is in the dictionary
check = 7 not in crypto
print(check)

result = crypto.items()
print(list(result))
#Clearing all values in dictionary
crypto.clear()
print(crypto)
