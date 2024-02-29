n = int(input('\033[35mDigite um número:\033[m'))
r = n % 2 # o resto da divisão por dois de todo número par é zero e de todo número impar é 1
if r == 0:
    print('O número {} é \033[34m PAR \033m'.format(n))
else:
    print('O número {} é \033[34m ÍMPAR \033m'.format(n))