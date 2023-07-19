print("digite PARE para terminar")
agenda = []
while True:
    nome = input("digite um nome para colocar na agenda: ")
    if nome == "PARE":
        break
    agenda.append(nome)
print(agenda)