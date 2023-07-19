class Pessoa:
    def __init__(self, nome, idade,cpf) :
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
    def descreve_pessoa(self) -> str :
        print(f" nome {self.nome}\n idade: {self.idade} \n cpf: {self.cpf}")
    def envelhecer(self,valor) -> int:
        "resposável por envelhecer pessoas"
        return self.idade + valor
if __name__ == '__main__':
    c = Pessoa(input("insira o seu nome: "), int(input("insira a sua idade: ")), input("insira o seu cpf: "))
    c.descreve_pessoa()
    print(c.envelhecer(3))
    print(c.cpf)