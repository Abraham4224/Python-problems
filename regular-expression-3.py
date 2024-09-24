import re
count=0
suma=0
intento=open("mbox-short.txt")
for line in intento:
    line=line.rstrip()
    x = re.findall(r"N.+R.+: ([0-9]+)",line)
    if len(x)> 0:
        for y in x:
            y=int(y)
            suma+=y
            count+=1
print('Average',(suma/count)) 
