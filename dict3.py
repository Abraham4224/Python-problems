import string 

try:
    archivo=open("romeo.txt")
except:
    print("El archivo no se puede abrir")
    exit()
    
counts=dict()
for line in archivo:
    line=line.rstrip()
    line=line.translate(line.maketrans('','',string.punctuation))
    line=line.lower()
    words=line.split()
    for word in words:
        if word not in counts:
            counts[word]=1
        else:
            counts[word]+=1
            
print(counts)
