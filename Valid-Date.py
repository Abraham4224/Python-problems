def isValidDate(year,month,day):
    if month>12 or day>31 or month<=0 or day<=0: return False
    if (month==4 or month==6 or month==11) and day<=30:
        return True
    elif month==2 and isLeapYear(year) and day<=29:
        return True
    elif month==2 and isLeapYear(year)==False and day<=28:
        return True
    elif (month==1 or month==3 or month==5 or month==7 or month==9 or month==10 or month==12 or month==8) and day<=31:
        return True
    else: 
        return False

assert isValidDate(1999, 12, 31) == True
assert isValidDate(2000, 2, 29) == True
assert isValidDate(2001, 2, 29) == False
assert isValidDate(2029, 13, 1) == False
assert isValidDate(1000000, 1, 1) == True
assert isValidDate(2015, 4, 31) == False
assert isValidDate(1970, 5, 99) == False
assert isValidDate(1981, 0, 3) == False
assert isValidDate(1666, 4, 0) == False
