import re
man=open("mbox-short.txt")
for linea in man:
    linea=linea.rstrip()
    x=re.findall(r'[a-zA-Z0-9]\S*@\S*[a-zA-Z]',linea)
    if len(x) > 0:
        print(x)
