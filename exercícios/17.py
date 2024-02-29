from math import sqrt
o = int(input('Qual o valor do cateto oposto ?'))
a = int(input('Qual o valor do cateto adjacente?'))
i = ((o*o)+(a*a))
print('O valor do da hipotenusa é de {}!'.format(sqrt(i)))
