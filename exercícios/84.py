dados = list()
pesad = mai = men = quant = 0 
while True:
    inf = []
    nome = str(input('Qual seu nome: '))
    peso = float(input('Qual é o seu peso: '))
    inf.append(nome)
    inf.append(peso)
    if len(dados) == 0:
        mai = men = inf[1]
    else:
        if inf [1] > mai:
            mai = inf [1]
        if inf [1] < men:
            men = inf [1]
    dados.append(inf[:])
    inf.clear() 
    pesad += 1
    resp = str(input('Quer continuar [S/N]? ')).upper().strip()
    if resp in 'Nn':
        break

print(f'Teve-se o total de {pesad} pessoas registradas')
print(f'O maior peso foi de {mai}KG. Peso de ',end='')
for p in dados:
    if p[1] == mai:
        print(f'[{p[0]}] ')
print(f'O menor peso foi de {men}KG. Peso de ', end='')
for p in dados:
    if p[1] == men:
        print(f'[{p[0]}] ',end='')
print()