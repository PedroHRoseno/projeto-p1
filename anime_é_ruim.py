lista = [5, 3, 6, 2, 1]
for passnum in range(len(lista)-1,0,-1):
    for i in range(passnum):
        if lista[i]> lista[i+1]:
            temp = lista[i]
            lista[i] = lista[i+1]
            lista[i+1] = temp
print(lista)
