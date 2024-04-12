from math import factorial
def fatorial (n, show):
    """
    Fatorail(n,show=False)
        -> Calcula o fatorial de um número.
        :param  n: O número a ser calculado.
        :param show: (opcional) mostrar ou não a conta.
        :return: O valor do fatorial de um número n.

    """
    b = n
    a = factorial(n)
    print(a)
    for v in range(b,0,-1):
        if show == True:
            print(v,end='')
        if v > 1:
            print(' x ', end='')
        else:
            print(' = ', end='')
    print(f'{a}')


n = int(input('Escolha um valor: '))

print(fatorial(n, show=True))
