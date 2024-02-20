#from random import randint (escolhe um número aleatório)
from random import randint

computador = randint (0,10)

print('Estou pensando em alguns números.')
print('Será que você consegue adivinhar...')

count = 0

acertou = False

while not acertou:
    palpite = palpite = int(input('Em qual número eu pensei?'))
    count += 1
    if palpite == computador:
        acertou = True
    else:
        if palpite > computador:
            print('Um pouco menos... tente novamente')
        elif palpite < computador:
            print('Um pouco mais... tente novamente')

print(f'Acertou, precisando de {count} tentativas')
    