#This code doesn't ask for any parameter, just shows a simple file
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
