
t=input("Enter a word or a sentence:")
o=input("Introduce the old word:")
n=input("Introduce the new word:")
if o in t:
    print("Found")
    long=len(o)
    encontrar=t.find(o)
    sliced=t[encontrar:(encontrar+long)]
    print(sliced)
    nuevotextoinicial=t[:encontrar]
    print(nuevotextoinicial)
    nuevotextofinal=t[(encontrar+long):]
    print(nuevotextofinal)
    sentencia=nuevotextoinicial+n+nuevotextofinal
    print(sentencia)
