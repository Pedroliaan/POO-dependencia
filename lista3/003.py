try:
    a = open('frase.txt', 'r', encoding='utf-8')
    l = a.readlines()
    print(len(l))
except Exception:
    print('ERRO')