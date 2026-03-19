def monetary(value):
    return f'R$ {value:.2f}'

def half(value, mon=True):
    if mon == False:
        return value/2
    else:
        return monetary(value/2)

def doble(value, mon=True):
    if mon == False:
        return value*2
    else:
        return monetary(value*2)

def increase(value, p, mon=True):
    if mon == False:
        return (value+(value*(p/100)))
    else:
        return monetary(value+(value*(p/100)))
    

def decrease(value, p, mon=True):
    if mon == False:
        return (value - (value* (p/100)))
    else:
        return monetary(value - (value * (p/100)))
    
def resume(value, aum, red):
    print("~"*40)
    print("RESUMO DO VALOR".center(40))
    print("~"*40)

    print(f'''
Valor analisado: {value}
Dobro do Valor: {doble(value)}
Metade do valor: {half(value)}
Aumento de {aum}% no valor: {increase(value, aum)}
Redução de {red}% no valor: {decrease(value, red)}''')
    
    print("-"*40)