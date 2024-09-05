def drawPyramid(height):
    n=1
    m=1
    for j in range(height):
        m+=2
    for i in range(0,height):
        print(('#'*n).center(m))
        n=n+2
        
drawPyramid(5)
