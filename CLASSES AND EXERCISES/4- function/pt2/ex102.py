# criar função de receber um número e calcular seu fatorial | mostra o cálculo dependendo do valor de 'show'
def fatorial(num, show=False):
    """
    :num: o número a ser encontrado o fatorial
    :show: (opcional) valor para mostrar ou não o processo de cálculo
    """
    tot = 1
    if show == False:
        for a in range(num, 0, -1):
            tot *= a
        return f'O valor do fatorial de {num} é {tot}'
    else:
        for a in range (num, 0, -1):
            tot *= a
            if a == 1:
                print(f"{a} ", end="= ")
                break
            
            print(f"{a} ", end="x ")

        return tot

print(fatorial(6))
print(fatorial(6, True))