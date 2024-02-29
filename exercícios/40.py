n1 = float(input('Qual a primeira nota do aluno ?'))
n2 = float(input('Qual a segunda nota do aluno?'))
m = (n1+n2)/2
if m < 5.0:
    print('Infelizmente, você foi reprovado, pois ficou com média {}!'.format(m))
elif 5 == m > 6.9:
    print('Você foi pra recuperação, ficando com média {}!, estude mais para na próxima passar!'.format(m))
else:
    m == 7 or 8 or 9 or 10
    print('Parabéns, você foi aprovado, ficando com média {}!'.format(m))