n = 0
while True:
    n = int(input('De qual número você quer ver sua tabuada ?'))
    if n < 0:
        break
    else:
        for c in range (1,11):
            print(f'{n} x {c} = {n*c}')
print('PROGAMA DE TABUADA ENCERRADO. Volte sempre!')