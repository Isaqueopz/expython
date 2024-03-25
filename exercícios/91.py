from random import randint
from time import sleep
from operator import itemgetter
print('           SORTEANDO VALORES           ')
jogo = {'Jogador 1':randint(0,6),
        'Jogador 2':randint(0,6),
        'Jogador 3':randint(0,6),
        'Jogador 4':randint(0,6)}
ranking = list()
print('-='*20)
for k, v in jogo.items():
    print(f'O jogador {k} tirou {v} no dado.')
    sleep(1)
print('-='*20)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i+1} lugar: {v[0]} com {v[1]}.')
    sleep(1)
