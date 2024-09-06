name=input("Enter the name of the file: ")
if len(name)<=0: 
    name = "mbox-short.txt"
file=open(name)  
suma=0
contador=0
for line in file:
    line1=line.rstrip()
    if line1.startswith("X-DSPAM-Confidence:"):
        found=line1.find(" ")
        sliced=line1[found+1:]
        #print(sliced)
        suma+=float(sliced)
        contador+=1
print("Promedio spam confidence: %f" % (suma/contador)) 
