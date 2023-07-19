nomes = []

while True :
    digi = input("sisira nomes para a lista, '0 para parar': ")
    if digi == "0":
        break
    nomes.append(digi)

for nome in range(len(nomes)):
    print(nomes[nome])
