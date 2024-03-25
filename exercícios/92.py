infor = {}
infor['Nome'] = str(input('Nome: '))
a = int(input('Ano de Nascimento: '))
infor['Idade'] = 2024 - a
infor['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if infor["ctps"] != 0:
    infor['Ano de contratação'] = int(input('Ano de contratação: '))
    infor['Salário'] = int(input('Salário: '))
    infor['Aposentadoria'] = (infor['Ano de contratação'] + 35) - a
    
print('-='*50)
print()
print(f'nome tem o valor {infor["Nome"]}')
print(f'idade tem o valor {infor["Idade"]}')
print(f'ctps tem o valor {infor["ctps"]}')
if infor["ctps"] != 0:
    print(f'contratação tem o valor {infor["Ano de contratação"]}')
    print(f'salário tem o valor {infor["Salário"]}')
    print(f'aposentadoria tem o valor {infor["Aposentadoria"]}')  
print()
