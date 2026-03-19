# Lista com todos os nº digitados | list de pares | lista de ímpares
values = []
pares = []
impares = []
while True:
    add = int(input("Digite um valor: "))
    values.append(add)
    cont = str(input("Quer Continuar? [S/N]: ")).strip().upper()[0]

    while cont not in 'SN':
        cont = str(input("Valor incompatível! Quer Continuar? [S/N]: ")).strip().upper()[0]
    
    if add % 2 == 0:
        pares.append(add)
    else:
        impares.append(add)

    if cont == 'N':
        print('-=-'*12)
        print("PROGRAMA ENCERRADO")
        break

print(f'''
Todos os valores digitados foram: {values}
Todos os valores pares foram: {pares}
Todos os valores ímpares foram: {impares}
''')