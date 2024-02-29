p = float(input('Qual é o seu peso?'))
a = float(input('Qual é a sua altura?'))
imc = p / (a*a)
if imc < 18.5:
    print('Você está abaixo do peso!, pesando {:.1f}KG'.format(imc))
elif 25<imc>30:
    print('Você está com sobrepeso!, pesando{:.1f}KG'.format(imc))
#elif 30<imc>40:
else:   
    18.5<imc>25
    print('Você está no peso ideal!, pesando {:.1f}KG'.format(imc))     