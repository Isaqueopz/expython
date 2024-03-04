# num = [2, 5, 9, 1]
# num [2]= 3
# num.append(7)
# num.sort(reverse=True)
# num.insert(2,0)
# if 3 in num:
#    num.remove(3)
# else:
#    print('Não achei o número 4')

# print(num)
# print(f'Essa lista tem {len(num)} elementos')

# valores = []
# valores.append(5)
# valores.append(9)
# valores.append(4)

valores = list()
for cont in range (0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')


# b = a[:] aqui não cria uma ligação, cria um cópia da list A


