pessoas = {'nome':'Gustavo','sexo':'M','idade':22}
pessoas['peso'] = 98.5 #<<< para adicionar alguma coisa no dic 
pessoas['nome'] = 'Leandro' #<<< para mudar alguma variavel indiretamente
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.') #<<<< lembrar de colocar aspas duplas no {pessoas["idade"]}
print(pessoas.values()) #<<< mostra parte de cima do code
print(pessoas.keys()) #<<< mostra parte de baixo do code (índices)
del pessoas ['sexo'] #<<< para apagar 
for k, v in pessoas.items():
    print(f'{k} = {v}')


# lista c/ dicionário
brasil = []
estado1 = {'uf':'Rio de Janeiro','sigla':'RJ'}
estado2 = {'uf':'São Paulo','sigla':'SP'}
brasil.append(estado1.copy()) #<<< O .copy()    adiciona a cópia do estado1
brasil.append(estado2.copy()) #<<< O .copy()    adiciona a cópia do estado2  
print(brasil[1]['sigla'])


estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for v in e.values():
        print(v,end=' ')
    print()