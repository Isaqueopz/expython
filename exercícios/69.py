homem = 0
idade1 = 0
mulher = 0
while True:
    idade = int(input('Qual é sua idade? '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Qual é seu sexo? [M/F] ')).strip().upper()[0]
        if sexo == 'M':
            homem += 1
        if idade >= 18:
            idade1 += 1
        if sexo in 'F' and idade < 20:
            mulher += 1
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar != 'S':
        break
print (f'{idade1} tinham mais de 18 anos...')
print (f'O total de homens foi de {homem} pessoas')
print (f'O total de mulheres com menos de 20 anos foi(foram) de {mulher} mulher(es)')

