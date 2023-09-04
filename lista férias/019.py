class Veiculo:
    def __init__(self, marca, modelo) :
        self.modelo = modelo
        self.marca = marca 
class Carro(Veiculo):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
    def ligar_motor(self):
        print("motor ligado")
class Moto(Veiculo):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
    def ligar_motor(self):
        print("motor ligado")