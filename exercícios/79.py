lista = list()
while True:
    lista.append(int(input('Digite um valor: ')))
    pergunta = str(input('Você quer continuar [S/N]: ')).upper().strip()[0]
 
    if pergunta != 'S':
     break
    # if lista.append in list():
    #     print('Valor repetido, não irá ser adicionado na lista!')

vorganizado = lista.sort()
print(f'Essa é sua lista {lista}' , end='')


# lista = [3, 1, 2]
# vorganizado = lista.sort()
# print(lista)  # Output: [1, 2, 3]
# print(vorganizado)  # Output: None