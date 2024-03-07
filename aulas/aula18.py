# LISTAS PT2
# -------------------------------------------------------------------------------
# para dar uma cópia em alguma estrútura é só
# pessoas = list()
# pessoas.append(dados[:]) >>>> cópia de toda estrutura de dados
# pessoas= [['Pedro',25],['Maria',19],['João',32]]
          #   0 lista      1 lista      2 lista    (indices)
# -------------------------------------------------------------------------------


#prática

# teste = list()
# teste.append('Gustavo')
# teste.append(40)
# galera = list()
# galera.append(teste[:])
# teste [0] = 'Maria'
# teste [1] = 19
# galera.append(teste[:])
# print(galera)

galera = list()

totmaior = totmenor = 0

while True:
    dado = []
    nome = str(input('Qual é o seu nome? '))
    dado.append(nome)
    idade = int(input('Qual é sua idade ? '))
    dado.append(idade)
    galera.append(dado[:])
    resp = str(input('Quer continuar? [S/N ]')).upper().strip()
    if resp in 'Nn':
        break
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade. ')
        totmaior += 1
    else:
        print(f'{p[0]} é menor de idade. ')
        totmenor += 1
print(f'Temos {totmaior} maiores de idade e {totmenor} menores de idade')
print(galera)