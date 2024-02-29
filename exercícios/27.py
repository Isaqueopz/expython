n = str(input('Qual é o seu nome completo:')).strip()
s = n.split()
print('''Muito prazer em te conhecer
Seu primeiro nome é {}'''.format(s[0]))
print('Seu último nome é {}'.format(s[len(s)-1]))

