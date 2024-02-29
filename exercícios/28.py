#from random import randint (escolhe um número aleatório)
from random import randint
c = randint (0,5)
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-'*20)
p = int(input('Em que número eu pensei ?'))
print('PROCESSANDO...')
from time import sleep
sleep(3)
if c == p:
    print('PARABÉNS!, o seu número conhecide com o meu!')
else:
    print('GANHEI, eu pensei no número {} e não no {}!'.format(c,p))
    
