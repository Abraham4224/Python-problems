x=int(input("Enter the Celsius degrees:"))
y=int(input("Enter Farenheit degrees:"))

def convertToFarenheit(degreesCelsius):
    faren=degreesCelsius*(9/5)+32
    return faren

def convertToCelsius(degreesFarenheit):
    celsius=(degreesFarenheit-32)*(5/9)
    return celsius

print("First, here are the Farenheit degrees converted into Celsius degrees")
print(convertToCelsius(x))
print("Celsius degrees entered converted into Farenheit degrees")
print(convertToFarenheit(y))