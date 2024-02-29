from time import sleep

print('Primeiro quero que você escolha dois números...')

sleep(1)

primeiro = int(input('Qual o primeiro valor? '))
segundo = int(input('Qual o segundo valor? '))

sleep(1)

menu = '''Esse é o seu menu 
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa'''

print(menu)

opção = int(input('Qual a opção desejada: '))

while opção != 5:  # Continuar executando até que a opção de sair seja selecionada
    if opção == 1:
        print(f'A soma é: {primeiro + segundo}')
    elif opção == 2:
        print(f'O produto é: {primeiro * segundo}')
    elif opção == 3:
        print(f'O maior valor é: {max(primeiro, segundo)}')
                                #max retorna o valor maior 
    elif opção == 4:
        print('Você quer inserir novos números...')
        primeiro = int(input('Qual o novo primeiro valor? '))
        segundo = int(input('Qual o novo segundo valor? '))
    else:
        print('Opção inválida!')

    print(menu)
    opção = int(input('Qual a nova opção desejada: '))

print('Você saiu do programa!')

