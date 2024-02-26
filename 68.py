import random

impar = 'ímpar'
par = 'Par'

computador = random.choice([impar,par])

escolha = ''

print('='*55)
print('Bem vindo ao game, você ira jogar contra o computador!')
print('vamos ver que se sai melhor!... ')
print('='*55)



while True:
    escolha = str(input('Qual a sua escolha?[par/impar]')).strip().upper()
    if escolha == computador:
        print('Parabéns')




  #print(f'A escolha do computador foi {computador}')