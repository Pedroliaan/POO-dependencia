class Caderno:
    __numero_folhas = None
    __cor_capa = None
    __preco = None
    def __init__(self):
       pass
    def setnumero_folhas(self,valor):
        self.__numero_folhas = valor
    def getnumero_folhas(self):
        print(self.__numero_folhas)
    def setcor_capas(self,valor):
        self.__cor_capa = valor
    def getcor_capa(self):
        print(self.__cor_capa)
    def setpreco(self,valor):
        self.__preco = valor
    def getpreco(self):
        print(self.__preco)
        
if __name__ == '__main__':
    c = Caderno()
    c.setcor_capas(input("insira a cor da capa: "))
    c.setnumero_folhas(input("insira o número de folhas: "))
    c.setpreco(input("insira o preço do caderno: "))
    c.getcor_capa()
    c.getnumero_folhas()
    c.getpreco()
    
    