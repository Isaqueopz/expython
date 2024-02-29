frase = str(input('Digite uma frase:')).strip().upper()
palavras = frase.split()
frase_sem_espaço = ''.join(palavras)
inverso = '' #iniciar p/ somar 
for letra_inversa in range(len(frase_sem_espaço)-1,-1,-1):
    inverso += frase_sem_espaço[letra_inversa]
print('O inverso de {} é {}'.format(frase_sem_espaço,inverso))
if inverso == frase_sem_espaço:
    print('Temos um palíndromo!')
else: 
    print('A frase digitada não é um palíndromo!')
