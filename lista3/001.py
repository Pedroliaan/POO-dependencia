try: 
    while True:
        i = int(input('escolha aopção: \n 1.escrever\n 2.ler \n 3. sair\n'))
        if i == 3:
            break
        if i ==1:
            e = str(input('frase que deseja escrever: '))
            a = open('arquivo.txt', 'a', encoding='utf-8')
            a.write(f'{e}\n')
            a.close
        if i ==2:
            a = open('arquivo.txt', 'r', encoding='utf-8')
            f = a.readlines()
            for x in range (len(f)):
                print(f'linha {x+1} -> {f[x]}')
            a.close()
except Exception:
    print('ERRO')