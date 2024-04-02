galera = list()
pessoa = dict()
listmulheres = list()
listmaioridade = list()
cont = 0 
contmulher = 0
idade = 0 
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    cont += 1 
    while True:
        pessoa ['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa ['sexo'] in 'MF':
            if pessoa['sexo'] in 'Ff':
                contmulher += 1 
                listmulheres.append(pessoa['nome'])
            break
        print('ERRO!, Por favor, digite apenas M ou F.')
        
    pessoa['idade'] = int(input('Idade:  '))
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    idade += pessoa['idade']

    media = (idade) / cont



    if resp == 'N':
        break



print('=-'*40)
print(galera)
print(f'O total de pessoas adicionadas foi de {cont} pessoas')
print(f'A média de idade foi de {media:.2f}')

if contmulher > 0:
    print(print(f'A lista de mulheres é {listmulheres}'))
else:
    print('Infelizmente, não teve mulheres nesse cadastro...')

for p in galera:
    if p['idade'] >= media:
        print('     ')
        for k, v in p.items():
            print(f'{k} = {v};', end='')
        print()
print('<<<<<ENCERRADO>>>>>')