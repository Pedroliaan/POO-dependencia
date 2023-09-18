lista = ['notas.txt', 'nomes.txt', 'agenda.txt', 'contas.txt']

for x in range(len(lista)):
    arq = open(lista[x], 'w')
    arq.close()