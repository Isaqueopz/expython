def notas(sit=False):
    """
    --> Função que analisa a nota e situação (BOA,RAZOÁVEL,RUIM) de varios alunos
        
    """
    inf = dict()
    lista = list()
    cont = soma = 0
    while True:
        nota = float(input('Digite uma nota:'))
        cont += 1 
        soma += nota
        lista.append(nota)
        resp = str(input('Quer continuar: [S/N] ')).strip().upper()[0]
        if resp == 'N':
            break
    maior = max(lista)
    menor = min(lista)
    inf['total'] = cont
    inf['maior'] = maior
    inf['menor'] = menor
    media = soma/len(lista)
    inf['média'] = (f'{media:.2f}')
    if sit == True:
        if media >= 7:
            inf['situação'] = ('BOA')
        elif  5 <= media < 7:
            inf['situação'] = ('RAZOÁVEL')
        else :
            inf['situação'] = ('RUIM')
    print(inf)
notas(sit=True)