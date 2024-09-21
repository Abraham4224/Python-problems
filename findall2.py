import re
man = open("mbox-short.txt")
for line in man:
    line=line.rstrip()
    x = re.findall(r'^From .* ([0-9][0-9]):',line)
    if len(x) > 0:
        print(x)
