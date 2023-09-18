arq = open('notas.txt', 'a')
for x in range (1,5):
    nota = float(input(f'insira a sua nota {x}: '))
    arq.write(f'{nota}\n')
arq.close()
arq = open('notas.txt', 'r')

media = (float(arq.readline()) + float(arq.readline()) + float(arq.readline()) + float(arq.readline()))/4

print(media)

