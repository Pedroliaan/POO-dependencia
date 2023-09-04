class Pessoa:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco
class Cliente(Pessoa):
    def __init__(self, nome, endereco, codigo):
        self.codigo = codigo
        super().__init__(nome, endereco)
class Funcionario(Pessoa):
    def __init__(self, nome, endereco, setor):
        self.setor = setor
        super().__init__(nome, endereco)