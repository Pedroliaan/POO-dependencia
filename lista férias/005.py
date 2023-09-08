def parimpar(lista):
    par = []
    impar = []
    for x in range(len(lista)):
        if lista[x]%2 == 0:
            par.append(lista[x]) 
        else:
            impar.append(lista[x])
    print(f"par: {par} impar: {impar}")
