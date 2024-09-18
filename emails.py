fi=open("mbox-short.txt")
correos=dict()
for line in fi:
    line=line.rstrip()
    if line.startswith("From "):
        direction=line.split()
        correos[direction[1]]=correos.get(direction[1],0)+1
        
listOfValues=list(correos.values())
maximo=max(listOfValues)
#print(maximo)
for n in correos:
    if correos[n] == maximo:
        print(n,maximo)
