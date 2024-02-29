v = int(input('Qual é a distância da sua viagem?'))
if v <= 200:
    v1 = 0.50*v
    print('O valor da sua viagem deu {}, boa viagem!'.format(v1))
else:
    v2 = 0.45*v
    print('O valor da sua viagem deu {}, boa viagem!'.format(v2))       