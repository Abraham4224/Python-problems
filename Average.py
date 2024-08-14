print("Enter a list of numbers separated by a comma: ")

def average(numbers):
    if len(numbers)==0: return None
    contador=0
    for u in numbers:
        contador=contador+u
    return contador/len(numbers)

print(average([12,20,37]))
