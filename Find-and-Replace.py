t="Firefox"
o='fox'
n='dog'
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
