def area(a, b):
    are = a * b
    print(f'A área de um terreno {a}x{b} é de {are}m')


print('Controle de terrenos')
print('-'*30)


a = float(input('LARGURA(m): '))
b = float(input('COMPRIMENTO(m): '))
area (a, b)