infordict = dict()
lista = list()
lista_gols = []
tot = 0
while True:
    infordict['nome'] = str(input('Nome:'))
    infordict['partidas'] = int(input(f'Quantas partidas {infordict["nome"]} jogou?: '))
    for p in range (0,infordict['partidas']):
        p2 = int(input(f'Quantos gols na partida {p+1}:'))
        tot += p2
        lista_gols.append(p2)
        infordict['gols'] = lista_gols.copy()
        
    lista_gols.clear()
    infordict['total'] = tot
    lista.append(infordict.copy())
    perg = str(input('Quer continuar: [S/N] ')).upper().strip()[0]
    tot = 0 
    if perg in 'Nn':
        break

print('-='*30)
print(' nome ',' gols ',' total ')
for p in range (len(lista)):
    print(f'{p }{lista[p]["nome"]},{lista[p]["gols"]},{lista[p][  "total"]}\n ')

while True:
    p3 = (int(input('Mostrar dados de qual jogador? ')))
    if p3 not in range (len(lista)):
        p3 = (int(input('ERRO!, escolha um jogador dentro da lista!:  ')))
    player = lista[p3]
    print(f'--Levantamento do jogador {player["nome"]}')
    for i in range(len(player["gols"])):
        print(f'     => Na partida {i+1}, fez {player["gols"][i]} gols')
    perg1 = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    if perg1 not in 'SN':
      perg1 = str(input('Responda com [S/N]: ')).strip().upper()[0]
    if perg1 == 'N':
        break



    
    






# {['nome'= isaque, 'gols' = [3,2], 'total' = 5]}
