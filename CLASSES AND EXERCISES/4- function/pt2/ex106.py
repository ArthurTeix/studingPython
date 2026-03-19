# criar função de descrever Funções e Bibliotecas Python
def pyHelp():
    from time import sleep

    print("\033[3;34;47m SISTEMA DE AJUDA PyHELP \033[m")

    while True:
        funcao = str(input("Função ou Biblioteca: ")).strip().lower()
        if funcao == 'fim':
            print("\033[1;31m ATÉ MAIS! \033[m")
            break

        print("-=-" *15)
        print(f"{'Acessando o manual do'} {funcao}")
        print("-=-" *15)

        sleep(1)

        help(funcao)

        print("~~~" * 15)

pyHelp()