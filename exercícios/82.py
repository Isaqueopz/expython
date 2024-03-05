lista = list()
listapar = list()
listaimpar = list()
while True:
    novonumero = (int(input('Digite um valor: ')))
    pergunta = str(input('Você quer continuar [S/N]: ')).upper().strip()[0]
    lista.append(novonumero)
    if novonumero % 2 == 0:
        listapar.append(novonumero)
    else:
        listaimpar.append(novonumero)
    if pergunta != 'S':
     break
print(f' A lista completa é {lista}')
print(f'A lista de pares é {listapar}')
print(f'A lista de ímpares é {listaimpar}')
