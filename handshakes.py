def printHandshakes(people):
    contador=0
    for i in range(len(people)):
        for j in range(i+1,len(people)):
            print(people[i]+' shakes hands with '+people[j])
            contador+=1
    print('Handshake counting:',contador)        
    
printHandshakes(['Alice','Roman','David','Carlos','Caesar','Napoleon'])   
