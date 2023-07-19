mat= []

for i in range(2):
    linha = []
    for j in range(2):
        linha.append(int(input(f"digiteo elemento {i}{j}: " )))
    mat.append(linha)
for i in range (2):
    for j in range(2):
        if i == 0 and j == 0:
            maior = mat[i][j]
        else:
            if mat[i][j] > maior:
                maior = mat[i][j]
print(f"o maior numero da matriz é: {maior}")