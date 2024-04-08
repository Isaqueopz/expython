from time import sleep
def maior(*num):
    if maior == 0:
        a = len(num)-1
    print('-='*25)
    print('Analisando os valores passados...')
    sleep(1)
    for c in (num):
        sleep(0.1)
        print(c,end=' ',flush=True)
        sleep(0.35)
    
    print(f' Foram informados {len(num)} valores ao todo')
    print(f'O maior valor informado foi o {max(num)}')
    print('-='*25)
    if maior == 0:
        print('Analisando os valores passaodos...')
        print(f'{num} Foram informados {a} valores ao todo')
        print('O maior valor informado foi 0.')




maior (2, 9, 4, 5, 7, 1)
maior (4, 7, 0)
maior (1, 2)
maior (6)
maior (0)