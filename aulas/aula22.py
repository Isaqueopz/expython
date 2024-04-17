#MÓDULOS E PACOTES
#--> dividir o código em pequenos pedaços ajudando em manutenção e legibilidade 
from uteis import numeros



num = int(input('Digite um valor: '))
fat = numeros.fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {numeros.dobro(num)}')


#PACOTES
# --> ajuda a separar os módulos em pacotes ajudando ainda mais na organização 

#para inicilizar um pacote abre um novo arquivo e coloca o __init__.py