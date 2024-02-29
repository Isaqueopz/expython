print (10*'=','LOJAS PINHEIRO',10*'=')
p = int(input('Preço das compras: R$')) 
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
o = int(input('Qual é a opção?'))
1 == p * 0.9
2 == p * 0.95
3 == p 
4 == (p * 1.2) + p

if o == 1:
  nv = p * 0.9
  print('Sua compra de R${} vai custar R${} no final.'.format(p,nv))

elif o == 2:
  nv = p * 0.95
  print('Sua compra de R${} vai custar R${} no final.'.format(p,nv))

elif o == 3:
  nv = p 
  parcela = p / 2
  print('Sua compra será parcelada em 2x de R${} SEM JUROS.'.format(parcela))

elif o == 4:
  total = p + (p * 0.2)
  m = int(input('Quantas parcelas ?'))
  parcela = total / m
  print ('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(m,parcela))
  nv = total 
  print('Sua compra de R${} vai custar R${} no final.'.format(p,nv)) 

else:
  print('''Opção inválida de pagamento
Escolha um valor entre os digitos acima!''')
