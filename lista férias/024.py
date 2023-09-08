class CarrinhodeCompras:
    def __init__(self) -> None:
        self.lista = []
    def adicionaproduto(self,nome, preco, desconto):
        produto = [nome, int(preco), int(desconto)]
        self.lista.append(produto)
    def totalproduto(self): 
        total = 0
        for x in range(len(self.lista)):
            total = total + self.lista[x][1]
        desconto = 0
        for x in range(len(self.lista)):
            desconto = desconto + self.lista[x][2]
        totaldesc = total - desconto
        return total, totaldesc
    def listaprodutos(self):
        for x in range(len(self.lista)):
            print(f'produto {self.lista[x]}')