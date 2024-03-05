lista = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
    else:
        for pos in range (0,len(lista)):
            numero_atual_da_lista = lista[pos]
            if n <= lista[pos]:
                lista.insert(pos, n)
                break
            
print(f'Os valores digitados em ordem foram {lista}')
                

