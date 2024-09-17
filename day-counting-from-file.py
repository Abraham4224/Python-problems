fil=open("mbox-short.txt")
dias=dict()
for line in fil:
    line=line.rstrip()
    if line.startswith("From "):
        roster = line.split()
        #print(roster[2])
        dias[roster[2]]=dias.get(roster[2],0)+1
        
        
print(dias)        
