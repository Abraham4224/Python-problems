fname = open("romeo.txt")
counts=dict()
for palabra in fname:
    palabra = palabra.split()
    for word in palabra:
        counts[word] = counts.get(word,0)+1
        
        
print(counts)  
