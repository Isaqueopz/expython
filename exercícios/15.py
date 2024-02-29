k = float(input('Quantos km você andou ?'))
d = int(input('Quantos dias você viajou?'))
p = int((k*0.15) + (60*d))
print('Você andou {}KM, viajando por {} dias, assim o total a pagar é de: R${}!'
      .format(k,d,p))

