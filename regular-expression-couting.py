import re
contador=0
example=open("mbox-short.txt")
regular=input("Enter a regular expression: ")
for line in example:
    line=line.rstrip()
    if re.search(regular,line):
        contador+=1
        
        
print("mbox-short.txt has",contador, " lines that match with",regular)  
