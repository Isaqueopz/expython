p = int(input('Qual seu ano de nascimento?'))
i = 2024 - p
f = 18 - i
a = i - 18

if i<18:
    print('''Constatei em meu progama que você ainda irá se alistar, visto que 
você tem apenas {} anos'''.format(i))
    print('Falta {} ano(s) para você se alistar!'.format(f))
elif i==18:
    print('A hora de se alistar é agora!!')
else:
    print('Você ja passou do tempo de se alistar!')
    print('Passaram {} ano(s) que você deveria ter ido se alistar!'.format(a))