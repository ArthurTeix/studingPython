# posso criar funções SEM parâmetros
def mostraLinha():
    print("<->"*15)

mostraLinha()

# posso criar funções COM parâmetros
def mensagem(msg):
    print("-=-"*6)
    print(msg)
    print("-=-"*6)

mensagem('sistema de notas')

# posso criar parâmetros e desempacotar
def contador(* num):
    print(num)

contador(1,2)
contador(5,4,6)
contador(9,2,4,7)


