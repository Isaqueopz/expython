idade = 0 
sexo = ''
continuar = 'sim'


while True:
    idade = int(input('Qual é a sua idade? '))
    sexo = str(input('Qual é o seu sexo: [M/F]')).strip().upper()[0]
    continuar = str(input('Você quer continuar? [SIM/NÃO] ')).strip().upper()[0]
    if continuar == 'não':
        break
    
  