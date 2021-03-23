# stk = []

class stack:
    def __init__(self):
        pass
        #self.nome = nome
    
    def startStk(self,nome):
        self.nome = nome
    
    def stk(self):
        self.nome = []


stk1 = stack()
var1 = stk1.startStk('stk01')
print(type(stk1.startStk('stk01')))

