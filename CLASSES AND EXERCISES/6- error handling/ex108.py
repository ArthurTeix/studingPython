# melhorarar a função leiaInt e adiconar a função leiaFloat com tratamento de erros

def leiaInt(msg):
    """
    :msg: parâmetro a ser passado para checagem
    """
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print("\033[0;31mERRO: DIGITE UM NÚMERO INTEIRO!\033[m")
        else:
            return n

def leiaFloat(info):
    """
    :info: parâmetro a ser passado para checagem
    """
    while True:
        try:
            m = float(input(info))
        except (ValueError, TypeError):
            print("\033[0;31mERRO: DIGITE UM NÚMERO FLOAT!\033[m")
        else:
            return m


# programa principal
integer = leiaInt("Digite um número inteiro: ")
floating = leiaFloat("Digite um número float: ")
print(f"O número inteiro digitado foi {integer} e o float foi {floating}")
