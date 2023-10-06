try:
    a = open('frase.txt', 'r', encoding='utf-8')
    l = a.readlines()
    print(len(l))
except FileNotFoundError:
    print('Olá camarada, infelizmente o arquivo não exite, tente novamente e tenha um bom dia')