class Animal:
    x=0
    
    def __init__(self):
        print("I'm constructed")
        
    def plusone(self):
        self.x=self.x+1
        print("Until now",self.x)
        
    def __del__(self):
        print("I'm destroyed",self.x)
        
al = Animal()
al.plusone()
al.plusone()
al=44
print("al has",al)
