valores = list()
for cont in range (0, 5):
    valores.append(int(input('Digite um valor:'))) # nn precisa por = quando por o valores.append
for cont, v in enumerate(valores):
    print('',end='')
    maior = max(valores)
    menor = min(valores)
    if v == maior:
        print(f'O maior valor foi {v} e sua posição foi {cont}')
    if v == menor: 
        print(f'O menor valor foi {v} e sua posição foi {cont}')
        