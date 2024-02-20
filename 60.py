n = int(input('Digite um número para calcular seu Fatorial: '))
c = n
f = 1
print (f'Calculando {n}! = ', end='')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c>1 else ' = ', end='') # end='' para trazer para linha reta
    f *= c # fatorial mulplicado pelo numero 
    c -= 1 # para ir decrescendo
print (f'{f}')












#numero = int(input('Diga um número qualquer: '))

#resultado = 1

#count = 1

#while count <= numero: 
#    resultado *= count
#    #resultado *= count é o mesmo que: resultado = resultado * count
#    count += 1
#
#print (f'o seu resultado do {numero} fatorial desejado é {resultado}')



#numero = int(input('Diga um número qualquer: '))
#resultado = 1
#for n in range ( 1, numero + 1):
#     resultado *= n
#print(resultado)