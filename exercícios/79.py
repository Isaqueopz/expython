números = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in números:
        números.append(n)
    else:   
        print('Esse valor ja foi digitado, digite novamente... ')
    r = str(input('Quer continuar [S/N]? '))
    if r in 'Nn':
        break

valororganizado = números.sort()
print(f'{números}')
