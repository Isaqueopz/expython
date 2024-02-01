#n = str(input('Qual é o seu nome?')).strip()
#if n == 'isaque'or'pedro'or'gustavo':
    #print('Que nome lindo você tem!')
#else: 
    #print('Seu nome é comum!')
#print('Bom dia,{}'.format(n)) 
# lembrar de que o if n == 'isaque': <<< tem que ser acompanhado de dois pontos.
n1 = float(input('Qual o valor da sua primeira nota?'))
n2 = float(input('Qual o valor da sua segunda nota?'))
m = (n1 + n2)/2
print('A sua média foi de {:.1f}'.format(m))
if m >= 6:
    print('A sua média foi ótima, parabéns!!!')
else:
    print('A sua média foi abaixo do esperado, melhorar!')