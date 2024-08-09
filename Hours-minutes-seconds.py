x=int(input("Introduce the total number of seconds:"))
def getHoursMinutesSeconds(totalSeconds):
    if totalSeconds == 0: return '0s'
    horas=0
    minutos=0
    segundos=0
    while totalSeconds>=3600:
        totalSeconds-=3600
        horas+=1
        
    while totalSeconds>=60:
        minutos+=1
        totalSeconds-=60
        
    segundos=totalSeconds
    
    lista=[]
    if horas>0:
        lista.append(str(horas)+'h')
    if minutos>0:
        lista.append(str(minutos)+'m')
    if segundos>0:
        lista.append(str(segundos)+'s')
        
    return ' '.join(lista)
        

print(getHoursMinutesSeconds(x))
