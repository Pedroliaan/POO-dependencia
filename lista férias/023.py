class ContaBancaria:
    def __init__(self, titular, saldo, limite):
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
    def sacar(self, valor):
        if self.limite > valor and valor <= self.saldo:
            self.saldo = self.saldo - valor
        else:
            print("limite indisponível")
    def deposito(self,valor):
        self.saldo = self.saldo + valor