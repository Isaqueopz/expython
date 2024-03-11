from time import sleep
from random import randint

print('-'*30)
print('JOGA NA MEGA SENA')
print('-'*30)

pergunta = int(input('Quantos jogos você quer que eu sorteie? '))
sleep(1)
print('-='*3,end=' ')
print(f'SORTEANDO {pergunta} JOGOS',end=' ')
print('-='*3)

a = randint(0,100)
b = randint(0,100)
c = randint(0,100)
d = randint(0,100)
e = randint(0,100)
g = randint(0,100)

lista = [a,b,c,d,e,g]
jogos = 0
while True:
    jogos += 1
    lista.append(a)
    lista.append(b)
    lista.append(c)
    lista.append(d)
    lista.append(e)
    lista.append(g)
    if jogos == pergunta: 
        break
print(lista)