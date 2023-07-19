agenda = {
    "jeggerson": 111111111,
    "ricardo": 33333333333,
    "ingridy": 222222222222
}

while True:
    nome = input("digite um novo amigo, ou '0' para sair:")
    if nome == '0':
        break
    telefone = int(input(f"telefone de {nome}: " ))
    #agenda[nome] = telefone
    agenda.update({nome:telefone})
    print(agenda)