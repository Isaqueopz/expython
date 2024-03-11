lista = list()
listapre = list()
while True:
    nomes_notas = []
    nome = str(input('Nome: '))
    nomes_notas.append(nome)
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    mediacont = (nota1 + nota2) / 2 
    nomes_notas.append(nota1)
    nomes_notas.append(nota2)
    nomes_notas.append(mediacont)
    lista.append(nomes_notas[:])
    listapre.append(nomes_notas[:])
    resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    while resp not in 'SN':
        resp = str(input('Digite entre Sim ou Não? ')).strip().upper()[0]
    if resp in 'N':
        break 
print('-='*40)
print('No. NOME', end='       ')
print('MÉDIA')
print('-'*50)
for p, v in enumerate(listapre):
    print(f'{p} {v[0]:<12} {v[3]:<12.2f}')
while True:
    perg = int(input('Mostrar notas de qual aluno? (999 interrompe):  '))
    for p, v in enumerate(listapre):
        if p == perg:
            print(f'As notas do aluno {v[0]} são: Nota 1: {v[1]} e Nota 2: {v[2]}')
    if perg == 999:
        print('Você saiu do programa')
        break
