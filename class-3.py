class name:
    x=0
    name=''
    
    def __init__(self,nom):
        self.name = nom
        print(self.name,"construido")
        
    def masUno(self):
        self.x=self.x+1
        print(self.name,'recuento grupal',self.x)
    
s = name('Napoleon')
j= name('Arthur')

s.masUno()
j.masUno()
s.masUno()
j.masUno()
