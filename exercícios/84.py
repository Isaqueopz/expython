dados = list()
pesad = pespes = peslev = quant = 0 
while True:
    inf = []
    nome = str(input('Qual seu nome: '))
    inf.append(nome)
    peso = float(input('Qual é o seu peso: '))
    inf.append(peso)
    dados.append(inf[:]) 
    pesad += 1
    resp = str(input('Quer continuar [S/N]? ')).upper().strip()

    if resp in 'Nn':
        break
    
for p in dados:
    if p[1] == max:
        print(f'O maior peso foi {p[1]}kg peso do {p[0]}')
    elif p[1] == min:
        print(f'O menor peso foi {p[1]}kg peso do {p[0]}')

print(f'Teve-se o total de {pesad} pessoas registradas')





    