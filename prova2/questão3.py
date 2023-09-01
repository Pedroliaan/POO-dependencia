class Caneta:
    def __init__(self,marca, cortinta, quantidade_tinta = 100):
        self.marca = marca
        self.cortinta = cortinta
        self.quantidade_tinta = quantidade_tinta
    def remover_tinta(self):
        self.quantidade_tinta = self.quantidade_tinta - 20
    def adicionar_tinta(self):
        self.quantidade_tinta = self.quantidade_tinta + 20
        if self.quantidade_tinta > 100:
            self.quantidade_tinta = 100
    def escrever(self):
        if self.quantidade_tinta > 20: 
           pass
        else:
            print("a caneta não tem tinta o suficiente para escrever")
    def dados_caneta(self):
        print(f"Marca da caneta: {self.marca}\n Cor da tinta: {self.cortinta}\n Quantidade de tinta: {self.quantidade_tinta}")

if __name__ == '__main__':
    mar = input("insira a marca da caneta: ")
    cor = input("insira a cor da tinta: ")
    can = Caneta(mar,cor)
    while True:
        escolha = int(input(f"escolha sua ação:\n 1. escrever\n 2.adicionar tinta\n 3.ver os dados da tinta\n 4. sair\n"))
        if escolha == 4:
            break
        elif escolha == 1:
            can.escrever()
            can.remover_tinta()
        elif escolha == 2:
            can.adicionar_tinta()
        elif escolha == 3:
            can.dados_caneta()