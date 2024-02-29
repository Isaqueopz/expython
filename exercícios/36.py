print('''Bom dia, seja bem vindo ao banco santander...
primeiro quero fazer algumas perguntas a vocẽ 
antes de prosseguir com os procedimentos.''')
v = int(input('Qual o valor da casa que você irá comprar?'))
s = int(input('Qual o salário que você recebe?'))
a = int(input('Em quantos anos você pretende pagar esse empréstimo?'))


m = v/a     

if m * 1.3 < s:
    print('Infelizmente o valor ficou muito alto para seu orçamento, quem sabe em uma próxima...')
else:
    m * 1.3 > s
    print('Muito bem o seu empréstimo foi aprovado, sua prestação será de {}!!'.format(m))   