idades = 0
for inf in range (1,5):
    print(8*'-',f'{inf}PESSOA',8*'-')
    nome = str(input('Nome:'))

    idade = int(input('Idade:'))
    idades += idade

    Sexo = str(input('Sexo [M/F]:'))

média = idades / 4
print(f'Esta é a média do grupo{média}')







