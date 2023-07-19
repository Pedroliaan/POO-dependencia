class Calculadora:
    def __init__ (self,x,y):
        self.x = x
        self.y = y
    def soma(self):
        result = self.x + self.y
        return result
    
    def subtracao(self):
        result = self.x - self.y
        return result

    c = Calculadora(3, 4)
    print(f"soma : {c.soma()}")
    print(f"subtracao : {c.subtracao()}")