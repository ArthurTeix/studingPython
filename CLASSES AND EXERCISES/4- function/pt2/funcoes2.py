def linha():
    print("-=-"*15)

# sempre que criar uma função posso descrever seu funcionamento usando 3 aspas duplas
def sub(a,b):
    """
    essa função subtrai dois números
    """
    print(a-b)

help(sub) # a função help me mostra o que tem na descrição do funcionamento da minha função

linha()

def mult(a=4,b=2): # posso passar valores padrões aos parâmetros caso não sejam declarados os valores
    print(a*b)
mult()

linha()

def somar(a=0,b=0,c=0):
    s = a+b+c
    return s # com o return tenho que guardar o valor numa variável ou usar o print

r1 = somar(3,2,1)
print(f"O primeiro número é {r1}")
r2 = somar(5,6,7)
print(f"O segundo número é {r2}")

print(f"o valor das somas é {r1+r2}") # vantagem pois consigo guardar valores e operar depois

print(somar(8,9,2)) # usando no print