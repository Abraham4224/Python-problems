def getChessSquareColor(x,y):
    if x>=8 or y>=8:
        return ''
    elif x%2==0 and y%2==0:
        return "white"
    elif x%2==0 and y%2!=0:
        return "black"
    elif x%2!=0 and y%2==0:
        return "black"
    elif x%2!=0 and y%2!=0:
        return "white"
print(getChessSquareColor(4,8))    

def ChessSquareColor(x,y):
    if x>=8 or y>=8:
        return ''
    elif (x%2==0 and y%2==0) or (x%2!=0 and y%2!=0):
        return "white"
    else:
        return "black"
      
print(getChessSquareColor(4,4)) 
print(ChessSquareColor(4,4)) 
