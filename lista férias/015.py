class Aluno:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade 
class Turma:
    def __init__(self) -> None:
        self.alunos = []
    def adicionar(self, aluno):
        self.alunos.append(aluno)
    def lista(self):
        print(self.alunos)
        
if __name__ == '__main__':
    nome = input("insira o nome do aluno: ")
    idade = input("insira a idade do aluno: ")
    x = Aluno(nome, idade)
    y = Turma()
    print(x)
    y.adicionar(x)
    y.lista()
    
        