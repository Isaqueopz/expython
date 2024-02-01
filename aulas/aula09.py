#Fatiamento
frase = 'Curso em Vídeo Python'
frase[9]
#frase [9:13] vai do 9 até o 12 
#frase [9:21:2] pula de 2 em 2 
#frase [:5] começa do zero e termina em 4 ou [15:]

#Análise 
len(frase) #mostra a quantidade total de caracteres 
frase.count('o') #conta quantos o minúsculos existem na frase
frase.find('deo') # mostra a posição em q momento começou o 'deo'
'curso' in frase #true or false

#Transformação
frase.replace('Python','Android') #substitui o nome python por android
frase.upper() # tudo maiúsculo
frase.lower() # tudo minúsculo
frase.capitalize() #deixa só a primeira letra maíscula
frase.title() # Analisa palavra por palavra deixando suas respectivas iniciais maiúsculas
frase.strip() #remove espaços inúteis frase.rstrip() right remove os espaços da direita frase.lstrip() remove o espaços da esquerda

#Divisão
frase.split() # dividi a frase, e conta cada palavra com uma indexação particular, agrupando os blocos das palavras em uma nova lista
# para juntar usa 
'-'.join(frase)