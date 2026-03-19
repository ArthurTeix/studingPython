# cadastro de pessoas e pesos
names = []
weights = [] # pesos
heavy = [] #pesados
light = [] #leves
while True:
    names.append(str(input("Nome: ")))
    weights.append(float(input("Peso: ")))

    cont = str(input("Quer continuar? [S/N]: ")).strip().upper()[0]
    while cont not in 'SN':     
        cont = str(input("Valor inválido! Quer continuar? [S/N]: ")).strip().upper()[0]
    if cont == 'N':
        break

for a in range(len(weights)):
    if (weights[a]) == max(weights):
        heavy.append(names[a])
    elif (weights[a] == min(weights)):
        light.append(names[a])
        
print(f'''
Ao todo, você cadastrou {len(names)} pessoas.
O maior peso foi de {max(weights)}. Peso de {heavy}
O menor peso foi de {min(weights)}. Peso de {light}
''')