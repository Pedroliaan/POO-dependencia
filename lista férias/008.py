soma = 0
while True:
    numero = int(input("insira um número (insira 0 para parar o programa): "))
    if numero == 0:
        break
    soma = soma + numero
print(soma)