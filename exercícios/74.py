from random import randint
num0 = randint(0,50)
num1 = randint (0,50)
num2 = randint (0,50)
num3 = randint (0,50)
num4 = randint (0,50)

lista = (num0,num1,num2,num3,num4)
print(f'Os valores escolhidos foram {lista}')
print(f'o maior valor foi {max(lista)}')
print(f'o menor valor foi {min(lista)}')

#for n in numeros:
    #print(f'{n}' , end='')