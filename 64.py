numero = int(input('Digite um valor:'))

count = 0
soma = 0

while numero != 999:
    numero = int(input('Digite outro valor:'))

    if numero == 999:
        print('Você preferiu sair!')

    elif numero != 999:
        count =+ numero
        
    
print(f'a quantidade de números até sair foram de {count}')