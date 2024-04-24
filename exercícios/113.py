def leiaint(msg):
    ok = False
    valor = 0 
    while True:
        n = str(input(msg))
        try:
            n.isnumeric()
            valor = int(n)
            ok = True
        except Exception as erro:
             print('\033[0;31mERRO: por favor, Digite um número inteiro válido. \033[m')
        if ok == True:
            break
    return valor

def leiaint2(msg):
    ok = False
    valor = 0 
    while True:
        r = str(input(msg))
        try:
            r.isnumeric()
            valor = float(r)
            ok = True
        except(ValueError,TypeError):
             print('\033[0;31mERRO: por favor, Digite um número real válido. \033[m')
        except KeyboardInterrupt:
            print('\033[0;31mO Usuário preferiu não digitar esse número. \033[m')
            r == 0
        if ok == True:
            break
    return valor


n = leiaint('Digite um número: ')
r = leiaint2('Digite um real:')
print(f'O valor inteiro digitado foi {n} e o real foi {r}')
