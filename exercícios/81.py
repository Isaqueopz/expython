lista = list()
while True:
    lista.append(int(input('Digite um valor: ')))
    pergunta = str(input('Você quer continuar [S/N]: ')).upper().strip()[0]
 
    if pergunta != 'S':
     break
odescresnte = lista.sort(reverse=True)
print(f'Foram digitados {len(lista)} números!')
print(f'A ordem da lista ficou da seguinte forma {lista}')
if 5 in lista:
   print('O valor 5 faz parte da lista!')
else:
   print('O valor 5 não se encontra na lista!')
