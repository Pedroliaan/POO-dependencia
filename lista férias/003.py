def palindromo (palavra):
    invertido =  palavra[::-1]
    if palavra == invertido:
        print("sua palavra é um palíndromo")
    else:
        print("sua palavra não é um palíndromo")