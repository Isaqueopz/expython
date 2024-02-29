print('='*30)
print('BANCO CEV')
print('='*30)

vorig = 0
soma = 0
valor = 0 


while valor < vorig:
    vorig = int(input('Qual valor você quer sacar: R$'))
    valor += vorig
    soma += 1 
print (f'Total de {soma} cédulas de R$50')


