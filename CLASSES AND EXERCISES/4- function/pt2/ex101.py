# criar uma função que diz a situação de votação pela idade
def voto(ano= 2008):
    """
    :ano: recebe o ano de nascimento
    """
    if (2026 - ano) < 16:
        return f"\nCom {2026-ano} o voto é PROIBIDO"
    
    elif (2026 - ano) >= 18 and (2026 - ano) <= 69:
        return f"\nCom {2026-ano} anos o voto é OBRIGATÓRIO"

    else:
        return f"\nCom {2026-ano} anos o voto é OPCIONAL"


print(voto(2015), voto(2010), voto(), voto(2000), voto(1950))
