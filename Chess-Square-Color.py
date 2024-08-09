print("There are 8x8 squares on a chess board, they can be white and black, this code return the color of the square given")
x=int(input("Enter the number of the x-axis:"))
y=int(input("Enter the number of the y-axis:"))
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
print(getChessSquareColor(x,y))    
#This is another way to do it
def ChessSquareColor(x,y):
    if x>=8 or y>=8:
        return ''
    elif (x%2==0 and y%2==0) or (x%2!=0 and y%2!=0):
        return "white"
    else:
        return "black"
      
print(getChessSquareColor(4,4)) 
print(ChessSquareColor(4,4)) 
