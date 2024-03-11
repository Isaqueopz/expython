totsoma = 0




a = [int(input('Digite um valor para [0,0] '))]
b = [int(input('Digite um valor para [0,1] '))]
c = [int(input('Digite um valor para [0,2] '))]
d = [int(input('Digite um valor para [1,0] '))]
e = [int(input('Digite um valor para [1,1] '))]
f = [int(input('Digite um valor para [1,2] '))]
g = [int(input('Digite um valor para [2,0] '))]
h = [int(input('Digite um valor para [2,1] '))]
i = [int(input('Digite um valor para [2,2] '))]



lista =  [a,b,c,d,e,f,g,h,i]

elementos = [a,b,c,d,e,f,g,h,i]


soma = c + f + i
totsoma += soma

print('-='*40)
print( lista[ 0 ],end=' ' )
print( lista[ 1 ],end=' ' )
print( lista[ 2 ] )
print( lista[ 3 ],end=' ')
print( lista[ 4 ],end=' ' )
print( lista[ 5 ])
print( lista[ 6 ],end=' ' )
print( lista[ 7 ],end=' ' )
print( lista[ 8 ])

if lista[3] > lista[4] and lista[3] > lista[5]:
    print(f'O Maior valor da segunda linha é {lista[3]}')
elif lista[4] > lista[3] and lista[4] > lista[5]:
    print(f'O Maior valor da segunda linha é {lista[4]}')
elif lista[5] > lista[3] and lista[5] > lista[4]:
    print(f'O Maior valor da segunda linha é {lista[5]}')

print(f'a soma dos valores da terceira coluna são {soma}')