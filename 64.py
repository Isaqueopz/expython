numero = int(input('Digite um valor:'))

count = 0 
soma = 0

while numero != 999:
    

    if numero == 999:
        print('Você preferiu sair!')

    elif numero != 999:
        count += 1
        soma += numero
        numero = int(input('Digite um valor:'))    
    
    
print(f'a quantidade de números até sair foram de {count} e a soma entre eles foi de {soma}')

#para desconsiderar o FLAG, você coloca o input do lado de fora e outro dentro da condição na ultima linha 