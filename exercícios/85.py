
listapar = list()
listaimpar = list()


for c in range (0,7): 
    valores = []
    num = int(input('Digite um valor:  '))
    if num % 2 == 0:
        listapar.append(num)
    else:
        listaimpar.append(num)
listapar.sort()
listaimpar.sort()
print(listapar)
print(listaimpar)