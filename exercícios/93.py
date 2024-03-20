infor = {}
lista = list()
tot = 0
infor['nome']=str(input('Nome do jogador: '))
p = int(input(f'Quantas partidas {infor["nome"]} jogou? '))

for c in range (0,p):
    p2 = int(input(f'Quantos gols na partida {c+1}?  '))
    lista.append(p2)
    infor['gols'] = lista
    tot += p2 
infor['total'] = tot

print('-='*40)
print(infor)
print('-='*40)
print(f'O campo nome tem o valor {infor["nome"]}')
print(f'O campo gols tem o valor {infor["gols"]}')
print(f'O campo total tem o valor {tot}')
print('-='*40)
print(f'O jogador {infor["nome"]} jogou {p} partidas... ')

for k , v in enumerate(lista):
    print(f'     => Na partida {k+1}, fez {v} gols')


print(f'foi um total de {tot} gols')


