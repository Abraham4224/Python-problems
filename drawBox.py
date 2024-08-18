def drawBox(size):
    if size<1: print()
    n=size
    m=size
    print(''.rjust(size+1)+'+'+'-'*(size*2)+'+')
    for i in range(size):
        print(''.rjust(m)+'/'+''.rjust(size*2)+'/'+'|'.rjust(i+1))
        m-=1
    print('+'+'-'*(size*2)+'+'+'+'.rjust(size+1))
    for j in range(size):
        print('|'+''.rjust(size*2)+'|'+'/'.rjust(n))
        n-=1
    print('+'+'-'*(size*2)+'+')
    
   

drawBox(4)
