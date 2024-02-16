v2 = ''
resultado = str(input('Qual seu sexo [M/F]?')).strip().upper()

if resultado == 'M' or resultado == 'F':
    print('Obrigado o seu resultado está correto!')
else:
    while  v2 != 'M' and  v2 != 'F':
        v2 = str(input('Digite novamente o resultado [M/F]?')).strip().upper()
        if v2 == 'M' or v2 == 'F':
         print('Agora está correto!')
        else:
           print('Tente novamente')
           
    


