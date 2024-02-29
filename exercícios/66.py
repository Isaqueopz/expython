n = soma = quant = 0
while True:
    n = int(input('Digite um valor [Ao digitar 999, para]: '))    
    if n == 999:
        break
    soma += n
    quant += 1
print(f'{quant} valores foram digitados, somando {soma} entre eles... ')
