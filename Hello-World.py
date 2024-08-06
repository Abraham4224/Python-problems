print("This is the easiest and the very first problem that every programmer learns")
print("Hello, World!")
print("What is your name?")
name = input()
print("Hello, "+ name)


  

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

