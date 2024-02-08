idades = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for inf in range (1,5):
    print(8*'-',f'{inf}PESSOA',8*'-')
    nome = str(input('Nome:'))
    idade = int(input('Idade:'))
    Sexo = str(input('Sexo [M/F]:'))
    idades += idade
    if inf == 1 and Sexo in 'Mm':
        maioridadedehomem = idade
        nomevelho = nome
    if Sexo in 'Mm'and idade > maioridadedehomem:
        maioridadedehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
média = idades / 4
print(f'Esta é a média do grupo{média}')
print(f'O homem mais velho tem {maioridadedehomem} anos e se chama {nomevelho}.')
print(f'Ao todo são {totmulher20} mulheres com menos de 20 anos')






