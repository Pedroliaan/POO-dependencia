mat = []

for linha in range(3):
    linhadedentro = []
    for coluna in range(3):
        linhadedentro.append(int(input(f"insira o elemrnto{[(linha)][(coluna)]}: ")))        
    mat.append(linhadedentro)

for linha in range(3):
    for coluna in range(3):
        print(mat[linha][coluna], end = " ")
    print("")