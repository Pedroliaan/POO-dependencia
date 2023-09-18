import os


caminho = 'lista poo/arquivo'

if not os.path.exists(caminho):
    os.makedirs(caminho)    
    
caminho_completo = os.path.join(caminho, 'dados.txt')

arq = open(caminho_completo, 'w', encoding='utf-8')
arq.write("python é massa demais")
arq.close() 
arq = open(caminho_completo, 'r', encoding='utf-8')
print(arq.read())
arq.close() 

