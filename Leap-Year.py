print("This will print if the year introduced was leap: ")
year=int(input())
def isLeapYear(year):
    if year%4!=0:
        return False
    elif year%4==0 and year%100!=0:
        return True
    elif year%100==0 and year%400==0:
        return True
    else:
        return False

print(isLeapYear(year))
