def primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def numeros_primos_ate_n(n):
    primos = []
    for numero in range(2, n + 1):
        if primo(numero):
            primos.append(numero)
    return primos


n = int(input("Digite um número inteiro positivo: "))
if n < 1:
    print("Por favor, digite um número inteiro positivo.")
else:
    primos = numeros_primos_ate_n(n)
    print(f"Números primos de 1 até {n}: {primos}")
