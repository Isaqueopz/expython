# help(input) <<<- para ajudar em algum comando
# DOCSTRINGS
# abaixo do def usa aspas duplas três vezes, e define para 
# que serve a sua função

def contador(i,f,p):
    """
    -> Faz uma contagem e mostra na tela.
    :I : inicio da contagem
    :F : fim da contagem
    :p : passo da contagem
    :return: sem retorno
    função criada por Isaque Misael
    """
    
    c = i
    while c <= f:
        print(f'{c} ',end='')
        c += p
    print('FIM!')




#PARÂMETROS OPCIONAIS
# def somar(a=0,b=0,c=0) #<<<- os iguais a zero são parametros opcionais que ajudam
# para caso precisasse somar e só tivesse o valor de dois parametros e  não dos tres completos


def somar (a=0,b=0,c=0):
    """
    Faz a soma de três valores e mostra o resultado na tela.
    A - primeiro valor
    B - segundo valor
    C - terceiro valor
    Função criada por Isaque Misael
    """
    s = a + b + c
    print(f'A soma vale {s}')


somar(3)


#ESCOPO DE VARIÁVEIS

# variavel/escopo global = aquela variavel startada no 'começo'
# variavel/escopo local = aquela variavel startada na identação 'fechada'

# caso eu use o global a, mesmo usando de dentro o a fora vai passar a ser o de dentro


#RETORNO DE VALORES (return)
# Eu quero que ele me mande o resultado para eu armazena-lo, não quero que ele printe
def somar(a=0,b=0,c=0):
    s = a + b + c
    return s

r1 = somar(3,2,5)
r2 = somar(2,2)
r3 = somar(6)

print(f'Os resultados foram {r1}, {r2} e {r3}')