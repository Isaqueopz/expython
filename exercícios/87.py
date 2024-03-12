somatot = 0
lista = [int(input('Digite um valor para [0,0] ')), int(input('Digite um valor para [0,1] ')), int(input('Digite um valor para [0,2] ')), 
    int(input('Digite um valor para [1,0] ')), int(input('Digite um valor para [1,1] ')), int(input('Digite um valor para [1,2] ')), 
    int(input('Digite um valor para [2,0] ')), int(input('Digite um valor para [2,1] ')), int(input('Digite um valor para [2,2] '))]
print('-='*40)
print( f'[{lista[ 0 ]:^5}]',end=' ')
print( f'[{lista[ 1 ]:^5}]',end=' ')
print( f'[{lista[ 2 ]:^5}]' )
print( f'[{lista[ 3 ]:^5}]',end=' ')
print( f'[{lista[ 4 ]:^5}]',end=' ')
print( f'[{lista[ 5 ]:^5}]')
print( f'[{lista[ 6 ]:^5}]',end=' ')
print( f'[{lista[ 7 ]:^5}]',end=' ')
print( f'[{lista[ 8 ]:^5}]',end=' ')
print()

for v in lista:
    if v % 2 == 0:
        somatot += v

somater = lista[2]+lista[5]+lista[8] 


print(f'A soma dos valores pares é de {somatot}')
print(f'A soma dos valores da terceira coluna é de {somater}')
if lista[3] > lista[4] and lista[3] >  lista[5]:
    print(f'O Maior valor da segunda linha é {lista[3]}')
elif lista[4] > lista[3] and lista [4] > lista[5]:
    print(f'O Maior valor da segunda linha é {lista[4]}')
elif lista[5] > lista[3] and  lista[5] > lista[4]:
    print(f'O Maior valor da segunda linha é {lista[5]}')

