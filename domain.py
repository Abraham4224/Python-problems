file=open("mbox-short.txt")
dominio=dict()
for line in file:
    line=line.rstrip()
    if line.startswith("From "):
        domain=line.split()
        domain2=domain[1].split("@")
        dominio[domain2[1]]=dominio.get(domain2[1],0)+1
print(dominio) 
