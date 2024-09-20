document=open("mbox-short.txt")
doc=dict()
for line in document:
    line=line.rstrip()
    if line.startswith("From "):
        line=line.split()
        hora=line[5].split(":")
        hour=hora[0]
        doc[hour] = doc.get(hour,0)+1
        
lst=list(doc.items())
lst.sort()
for key,value in lst:
    print(key,value)
