def sumar_fibonacci(limit):
    a, b = 0, 1
    suma = 0
    while b <= limit:
        suma += b
        a, b = b, a + b
    return suma

resultado = sumar_fibonacci(1000000)
print(f"La suma de los números de Fibonacci hasta 1000000 es: {resultado}")
