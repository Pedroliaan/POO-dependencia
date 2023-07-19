mat1= []

for i in range(2):
    linha = []
    for j in range(2):
        linha.append(int(input(f"digiteo elemento {i}{j}: " )))
    mat1.append(linha)
menor = mat1[0][0]
for i in range(2):
    for j in range(2):
        if mat1[i][j] < menor:
            menor = mat1[i][j]
mat2 = []
for i in range(2):
    linha = []
    for j in range(2):
        linha.append(menor*mat1[i][j])
    mat2.append(linha)
for linha in range(2):
    for coluna in range(2):
        print(mat2[linha][coluna], end = " ")
    print("")
    