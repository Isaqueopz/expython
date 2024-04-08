from random import randint 
from time import sleep
numeros = list()
listapar = list()
def sorteio():
    numeros1 = list()
    cont = 0
    while cont < 5:
        a = randint(0,20) 
        if a % 2 == 0:
            listapar.append(a)
        numeros.append(a)
        cont += 1 
numeros.append(sorteio())
def somapar():
    print(sum(listapar))
print('Sorteando 5 valores da lista: ',end='')
sleep(1)
for v in numeros[0:5]:
    print(f' {v} ',end='',flush=True)
    sleep(1)
print()
print(f'Somandos os valores pares de {numeros[0:5]}, temos ',end='')
somapar()
