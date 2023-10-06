try:
    while True:
        i = int(input('escolha a opção \n 1. escrever\n 2.sair\n'))
        if i ==2:
            break
        if i ==1:
            f = str(input('insira uma frase: '))
            a = open('frase.txt', 'a', encoding='utf-8')
            a.write(f'{f}\n')
            a.close()


except Exception:
    print('ERRO')
            