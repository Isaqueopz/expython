# FUNÇÕES SEM PARAMETRO
def lin(): # <<< parenteses e dois pontos 
    print('-------------------------')


lin()
print('CURSO EM VÍDEO')
lin()
print('APRENDA PYTHON')
lin()
print('ISAQUE MISAEL')
lin()


# FUNÇÃO COM PARAMETRO 

def título(txt):
    print('-'*30)
    print(txt) 
    print('-'*30)


título('    CURSO EM VIDEO    ')
título('    PYTHON É MUITO BOM  ')
título('    OIII                 ')

def soma (a, b): #<<<< definiu quem ele vai somar ( esses são os parametros A e B )
    print(f'A = {a} e B = {b}')
    s = a + b 
    print(f'A soma A + B = {s}')


#progama principal
soma(b=4, a=5) #<<< posso definiar qual parametro é qual 
soma(8, 9)
soma(2, 1)

lin()


#EMPACOTAMENTO DE PARAMETROS <<< serve mais para quando eu não sei quantos termos vou ter como parametros

def contador(*num): #<<< *num é esse parametro 
    print(num)

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

lin()

def dobra(lst):
    pos = 0 
    while pos < len(lst):
        lst[pos] *=  2 
        pos += 1
        
    
valores = [6, 3, 9 ,1 ,0 , 2]
dobra(valores)
print(valores)

lin ()

def soma(*valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')


soma(5, 2)
soma(2, 9, 4)
