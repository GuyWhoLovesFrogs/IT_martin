class Klasse2:    
    def op2(self, i):
        return i
    
class Klasse1:
    def __init__(self, objekt: Klasse2):
        self.objekt = objekt
    def op1(self):
        for i in range(0, 9):
            print(self.objekt.op2(i))
        
objekt2 = Klasse2()
objekt = Klasse1(objekt2)

objekt.op1()        ^^^                     ^^^^^^^^^^^^^^^                                 ^^      qw