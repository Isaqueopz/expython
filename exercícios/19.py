import random
n1 = str(input('Qual é o primeiro nome ?'))
n2 = str(input('Qual é o segundo nome?'))
n3 = str(input('Qual é o terceiro nome?'))
n4 = str(input('Qual é o quarto nome?'))
lista = [n1,n2,n3,n4]
escolhido = random.sample(lista,k=3)
print ('O aluno escolhido foi {}!'.format(escolhido)) 