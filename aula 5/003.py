numeros = []  # Lista vazia para armazenar os números

# Solicita ao usuário digitar 5 números inteiros
for i in range(5):
    numero = int(input("Digite um número inteiro: "))
    numeros.append(numero)

# Encontra o maior e o menor número digitados e suas posições na lista
maior_numero = max(numeros)
menor_numero = min(numeros)
posicao_maior = numeros.index(maior_numero)
posicao_menor = numeros.index(menor_numero)

# Imprime o maior e o menor número seguidos de suas posições
print(f"O maior número digitado foi {maior_numero}, na posição {posicao_maior}.")
print(f"O menor número digitado foi {menor_numero}, na posição {posicao_menor}.")
