class Contato:
    def __init__(self, nome, telefone) :
        self.nome = nome
        self.telefone = telefone
class Agenda:
    def __init__(self,titular_agenda, lista_contatos = []):
        self.titular_agenda = titular_agenda
        self.lista_contatos = lista_contatos
    def adicionar_contato(self,telefone):
        self.lista_contatos.append(Contato(telefone))
    def detalhar_agenda(self):
        print(f"A agenda de{self.titular_agenda} contém {len(self.lista_contatos)} contatos cadastrados")
if __name__ == '__main__':
    c = Contato(input("insira o nome do contato: ", input("insira o telefone do contato: ")))
    a = Agenda(input("insira o nome do dono da agenda: "))
    a.adicionar_contato()
    a.detalhar_agenda()