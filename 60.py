numero = int(input('Diga um número qualquer: '))

resultado = 1

count = 1

while count <= numero: 
    resultado *= count
    #resultado *= count é o mesmo que: resultado = resultado * count
    count += 1

print (f'o seu resultado do {numero} fatorial desejado é {resultado}')



#numero = int(input('Diga um número qualquer: '))
#resultado = 1
#for n in range ( 1, numero + 1):
#     resultado *= n
#print(resultado)