print("This is the easiest and the very first problem that every programmer learns")
print("Hello, World!")
print("What is your name?")
name = input()
print("Hello, "+ name)



def fizzBuzz(upTo):
    for i in range(1,upTo+1):
            if i%3==0 and i%5==0:
                print( "FizzBuzz",end=" ")
            elif i%3==0:
                print( "Fizz", end=" ")
            elif i%5==0:
                print( "Buzz",end=" ")
            else:
                print(i, end=" ")

  

def writeToFile(text,code):
    with open(text,'w') as Txt:
        Txt.write(code)
    
def appendToFile(text,code):
    with open(text,'a') as App:
        App.write(code)
        
def readFromFile(text):
    with open(text) as leer:
        ok=leer.read()
    return ok

writeToFile('greet.txt','Hello!\n')
appendToFile('greet.txt','Goodbye!\n')
print(readFromFile('greet.txt'))

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