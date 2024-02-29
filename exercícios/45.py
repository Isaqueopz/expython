import random
from time import sleep
print ('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL 
[ 2 ] TESOURA''')

o = int(input('Qual é sua jogada ??'))

print ('JO')
sleep(1)
print ('KEN')
sleep(1)
print ('PO')
sleep(1)

print (20 * '-=')
lista = ('Pedra','Papel','Tesoura')
ln = random.choice(lista)

print('Computador jogou {}'.format(ln))

if o == 0:
    print('Jogador jogou Pedra')
elif o == 1:
    print('Jogador jogou Papel')
elif o == 2:
    print('Jogador jogou Tesoura')
else: 
    print('O jogador não escolheu uma das opções válidas, tente novamente!')
print (20 * '-=')

if ln == 'Pedra' and o == 2:
    print('JOGADOR PERDEU')
elif ln == 'Pedra' and o == 1:
    print('JOGADOR VENCEU')
elif ln == 'Pedra' and o == 0:
    print('DEU EMPATE')
elif ln == 'Papel' and o == 0:
    print('JOGADOR PERDEU')
elif ln == 'Papel' and o == 1:
    print('DEU EMPATE')
elif ln == 'Papel' and o == 2:
    print('JOGADOR VENCEU')
elif ln == 'Tesoura' and o == 0:
    print('JOGADOR VENCEU')
elif ln == 'Tesoura' and o == 1:
    print('JOGADOR PERDEU')
elif ln == 'Tesoura' and o == 2:
    print('DEU EMPATE')


    