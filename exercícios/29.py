v = int(input('Qual a velocidade do carro?'))
if v >= 80:

    n = v-80
    c = 7*n
    print('''MULTADO! Você excedeu o limite permitido que é de 80km/h 
você deve pagar uma multa de {}
Tenha um bom dia! Dirija com segurança! '''.format(c))
else:
    print('Tenha um bom dia! Dirija com segurança!')