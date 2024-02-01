a = int(input('Qual é o primeiro número?'))
b = int(input('Qual é o segundo número?'))
c = int(input('Qual é o segundo número?'))
#menor número
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c

#maior número
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c

print('O maior valor é {}'.format(maior))
print('O menor valor é {}'.format(menor))