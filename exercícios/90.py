situação = {}
nota = list()
for c in range (0,1):
    situação['nome'] = str(input('Nome: '))
    situação['média'] = float(input(f'Média de {situação["nome"]}: '))
    nota.append(situação["média"])

print(f'O nome é igual a {situação["nome"]}')
print(f'Média é igual a {situação["média"]}')
if nota[0] >= 7:
     print(f'{situação["nome"]} foi APROVADO!')
else:  
    print(f'{situação["nome"]} foi REPROVADO!') 
