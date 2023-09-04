class Celular:
    def __init__(self, preco, modelo) :
        self.preco = preco
        self.modelo = preco
    def desconto(self):
        descontado = self.preco - (self.preco * 0,1)
        return descontado
    def acrescimo(self):
        aumentado = self.preco + (self.preco * 0,1)
        return aumentado
    