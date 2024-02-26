print ('-'*20)
print ('LOJA SUPER BARATÃO')
print ('-'*20)

preço = 0
total = 0 
maior = 0
continuar = ""
produto = 0
produto = produto < preço
barato = 0

while continuar != 'N':
    nome = str(input('Nome do Produto: '))

    preço = int(input('Preço: R$'))

    total += preço

    continuar = str(input('Quer continuar: [S/N] ')).upper().strip() [0]

    if preço > 1000:

        maior += 1  
    
    
    
print (f'o total da compra foi R${total}')
print (f'Temos {maior} produtos custando mais de R$1000.00')



