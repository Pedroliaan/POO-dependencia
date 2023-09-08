def contagem(self, texto):
    dic = {}

    palavras = texto.split()
    for palavra in palavras:
         palavra = palavra.strip(".,!?").lower()
         if palavra in dic:
            dic[palavra] += 1
         else:
            dic[palavra] = 1
    
    return dic