contagem = 0
 
with open('texto.txt', 'r') as f:
    for linha in f:
        palavras = linha.split()
        contagem += len(palavras)
print(f"numero de palavras: {contagem}")
