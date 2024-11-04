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

crypto[6]="Monero"
print(crypto[6])

number=len(crypto)
print(number)

del crypto[6]
print(crypto)

crypto.pop(3)
print(crypto)

check = 7 not in crypto
print(check)

result = crypto.items()
print(list(result))

crypto.clear()
print(crypto)
