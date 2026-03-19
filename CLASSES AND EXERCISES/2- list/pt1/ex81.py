# quantos elementos digitei | valores em ordem decrescente | se tem 5 na lista
values = []

while True:
    add = values.append(int(input("Digite um valor: ")))
    prox = str(input("Quer continuar? [S/N]: ")).strip().upper()[0]

    while prox not in "SN":
        prox = str(input("Valor Incompatível! Quer continuar? [S/N]: ")).strip().upper()[0]
    if prox == 'N':
        print("-=-" * 10)
        break

values.sort(reverse=True)
print(f'''
Você digitou {len(values)} elementos
Os valores em ordem decrescente são: {values} ''')
if 5 in values:
    print("O valor 5 faz parte da lista")
else:
    print("O valor 5 não foi encontrado na lista")
