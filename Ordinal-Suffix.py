number = int(input("Introduce a number:"))
def ordinalSuffix(number):
    num=str(number)
    if num.endswith("0") and len(num)==1:
        print(num+"th")
    elif num.endswith("1") and len(num)==1:
        print(num+"st")
    elif num.endswith("2") and len(num)==1:
        print(num+"nd")
    elif num.endswith("3") and len(num)==1:
        print(num+"rd")
    elif (number>=4 and number<=99): 
        print(num+"th")
    elif  number >=100:
        print(num+"st")

ordinalSuffix(number)
