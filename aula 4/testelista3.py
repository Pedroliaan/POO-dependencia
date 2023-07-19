print("digite PARE para terminar")
agenda = []
while True:
    nome = input("digite um nome para colocar na agenda: ")
    if nome == "PARE":
        break
    agenda.append(nome)
while True: 
    busca = input("nome para procura na agenda: ")
    if busca == "PARE":
        break
    elif busca in agenda:
        print(busca, "está na agenda")
    else:
        print(busca, "não está na agenda")
        pergunta = input("quer iserir o nome na agenda? [S|N]")
        if pergunta == "S":
            agenda.append(busca)