
numero = 0

numero = int(input('Qual número deseja escolher:'))

pergunta = input('deseja continuar? S/N ')
count = 0
count2 = 0
while pergunta != 'não':
    numero1 = int(input('Qual número escolherá agora? '))
    pergunta = input('deseja continuar? S/N ')
    count += (1) + 1
    média = ((numero + numero1) / count)

print(f'A sua média foi {média}, o seu maior número foi {max(numero,numero1)} e o seu menor número foi {min(numero,numero1)}')
