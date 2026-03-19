# criar função de centralizar texto entre linhas
def texto(txt):
    tam = len(txt) + 4
    print("-" * tam)
    print(f'  {txt}')
    print("-" * tam)

texto("Arthur Teixeira")
texto("Olá")
texto("Bom dia")