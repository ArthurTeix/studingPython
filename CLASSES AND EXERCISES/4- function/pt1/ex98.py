# criar um contador 
from time import sleep
def contador(i=1, f=10, p=1):
    """
    essa função funciona como um contador
    i -> início
    f -> fim
    p -> passo
    """

    if p < 0: # passo negativo
        p = p * -1
    
    if i < f and p > 0: # início menor que o fim
        for a in range (i, f+1, p):
            print(f"{a} -> ", end='', flush=True)
            sleep(0.3)
        print("FIM!")

    elif i > f: # inicio maior que o fim
        for a in range (i, f-1, -p):
            print(f"{a} -> ", end='', flush=True)
            sleep(0.3)
        print("FIM!")

contador(2,18,4) # início menor que o fim
contador(30,5,5) # inicio maior que o fim
contador(40,10,-5) # passo negativo
contador() # caso não passe valores serão usados os padrões

print("-=-"*15)
print("!! PERSONALIZE O SEU CONTADOR !!")
contador(
    int(input("Início: ")),
    int(input("Fim:    ")),
    int(input("Passo:  "))
)