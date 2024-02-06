from datetime import date
 
count_maiores = 0
count_menores = 0

for c in range(0, 7):
    a = int(input('Qual o seu ano de nascimento? '))
    idade = date.today().year - a

    if idade >= 18:
        count_maiores += 1
    else:
        count_menores += 1

print('A quantidade de pessoas maiores ou iguais a 18 anos é de {} pessoas'.format(count_maiores))
print('A quantidade de pessoas menores de 18 anos é de {} pessoas'.format(count_menores))
