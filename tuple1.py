cadena="Pero que luz que se deja ver allí"
palabras=cadena.split()
t=list()
for palabra in palabras:
    t.append((len(palabra),palabra))
    
t.sort(reverse=True) 

res=list()
for longitud,palabra in t:
    res.append(palabra)
    
print(res)    
print(t)
