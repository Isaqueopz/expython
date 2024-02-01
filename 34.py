s = int(input('Qual é o seu salário?'))
if s >= 1250:
   n = s*1.1
   print('o seu salário será aumentado, passando a ser {:.1f}'.format(n))
else:
   nv = s*1.15
   print(' o seu salário irá receber um grande aumento, agora ele é de {:.1f}'.format(nv))