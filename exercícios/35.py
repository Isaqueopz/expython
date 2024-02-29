a = float(input('Qual o primeiro valor para montar o triângulo?'))
b = float(input('Qual o segundo valor para montar o triângulo?'))
c = float(input('Qual o terceiro valor para montar o triângulo?'))
if a < b + c and b < a + c and c < b + a:
    print('Você ira conseguir montar um triângulo!')
else:
    print('Você não ira conseguir montar um triângulo!')


