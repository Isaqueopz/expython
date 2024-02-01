f = str(input('Digite uma frase:')).strip()
print('A letra A aparece {} vezes na frase.'.format(f.upper().count('A')))
print('A primeira letra A aparece na posição {}'.format(f.upper().find('A')+1))
print('A última letra A aparece na posição {}'.format(f.upper().rfind('A')+1))
