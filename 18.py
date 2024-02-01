import math
a = float(input('Qual o valor do ângulo?'))
s = math.sin(math.radians(a))
print('O Valor {} tem o sêno de {:.2f}'.format(a,s))
c = math.cos(math.radians(a))
print('O Valor {} tem o côsseno de {:.2f}'.format(a,c))
t = math.tan(math.radians(a))
print('O Valor {} tem a tangente de {:.2f}'.format(a,t))
 