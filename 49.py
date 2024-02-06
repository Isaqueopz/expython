n = int(input('Digite um número para ver sua tabuada:'))
print ('-' * 12)
for c in range (0,11):
    r = n * c
    print ('{} x{:2} = {}'.format(n,c,r))