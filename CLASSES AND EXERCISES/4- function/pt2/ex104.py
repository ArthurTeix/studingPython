# criar função que só autoriza declarar números inteiros
def leiaInt(msg):
    """
    :msg: parâmetro a ser passado para checagem
    """
    while True:
        n = input(msg)
        if n.isnumeric():
            return int(n)
        else:
            print("\033[0;31mERRO! DIGITE UM NÚMERO INTEIRO\033[m")
# programa principal
n = leiaInt("Digite um número inteiro: ")
print(f"O número digitado foi {n}")
