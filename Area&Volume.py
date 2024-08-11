length=int(input("Enter the length"))
width=int(input("Enter the width"))
height=int(input("Enter the height"))
def area(length,width):
    return length*width

def perimeter(length,width):
    return (2*length)+(2*width)

def volume(length,width,height):
    return length*width*height

def surfaceArea(length,width,height):
    return (length*width*2)+(length*height*2)+(width*height*2)
print("The perimeter is:")
print(perimeter(length,width))
print("The area is:")
print(area(length,width))
print("The volume is:")
print(volume(length,width,height))
print("The surface area is:")
print(surfaceArea(length,width,height))
