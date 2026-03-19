# Criar uma Lista de valores únicos e sem repetições
values = []

while True:
    add = int(input("Digite um valor: "))

    if add not in values:
        values.append(add)
        print("Valor adicionado com sucesso!")
    else:
        print('Valor já existente na lista! Não adicionado!')

    prox = str(input("Quer continuar? [S/N]: ")).strip().upper()[0]

    if prox == "N":
        break

print("-=-"*10)

print(f"Você digitou os valores", values)