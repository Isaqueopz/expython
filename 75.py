núm =  (int(input('Digite um número: ')),
        int(input('Digite outro número: ')),
        int(input('Digite mais um número: ')),
        int(input('Digite o último número: ')))
print(f'Você digitou os valores {núm}')
print(f'O valor 9 apareceu {núm.count(9)} (vez)es')
print(f'O valor 3 apareceu na {núm.index(3)+1} posição')
print('Os valores pares digitados foram ', end='')
for n in núm:
    if n % 2 == 0:
        print( n )