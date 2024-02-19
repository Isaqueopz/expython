#from random import randint (escolhe um número aleatório)
from time import sleep
from random import randint
tentativa = 0
t = 0
lista = randint (0,10)
print(20*'-=-')
print('Vou pensar em um número de 0 a 10, qual será o número que eu pensei...')
print(20*'-=-')
sleep(2)
p = int(input('Qual número eu pensei:'))
if lista == p:
    print('Olha só parabéns, você acertou de primeira!!!')
else:
    while tentativa != p:  
        t += 1
        tentativa = int(input('''Você errou, tente novamente!!!
qual número deseja colocar agora:'''))
        if tentativa == p:
            print('Parabéns, agora você acertou!')
        else: 
            print('Tente novamente!')
print (f'Você precisou de {t} para vencer')
