from datetime import date 
a = int(input('Qual ano que você deseja analisar? Coloque 0 para analisar o ano atual: '))
if a == 0:
    a = date.today().year#pega o ano atual config na máquina 
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0: 
    print( 'o seu ano é bissexto!')
else:
    print ('o seu ano não é bissexto!')