p = float(input('Qual o preço do pagamento efetuado?'))
c = str(input('Qual é a condição de pagamento?'))
if c == 'a vista dinheiro' or 'a vista cheque': 
    v1 = p * 0.9
    print ('o seu valor era de {} e agora é de {}, pois teve um desconto de 10%'.format(p,v1))
elif c == 'a vista cartão':
    v2 =  p * 0.95
    print ('o seu valor era de {} e agora é de {}, pois teve um desconto de 5%'.format(p,v2))
elif c == 'uma vez no cartão' or 'duas vezes no cartão':
    print ('o seu valor era de {} e agora é de {}, pois não teve descontos'.format(p,p))
else: 
    c == 'duas vezes ou mais no cartão'
    v3 = p * 1,2
    print ('o seu valor era de {} e agora é de {}, pois não teve descontos'.format(p,v3))