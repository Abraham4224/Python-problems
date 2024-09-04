def drawBorder(width,height):
    if height<2 or width<2: print('')
    horizontal='-'*(width-2)
    print('+'+horizontal+'+')
    for i in range(height//2):
        print('|'+''.rjust(width-2)+'|')
    print('+'+horizontal+'+')
drawBorder(16,4)
