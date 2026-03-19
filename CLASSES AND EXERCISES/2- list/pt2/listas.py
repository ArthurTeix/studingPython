# Listas dentro de listas
peoples = [['Arthur', 17], ['Jullio', 16], ['Miguel', 15]]

# O primeiro índice é para definir a listra aninhada a ser acessada
# O segundo índice é para definir o item da lista a ser acessado
print(peoples[0][0])

# Para adicionar dados numa lista composta
values = []
date = []
for a in range (3):
    date.append(str(input("Digite seu nome: ")))
    date.append(int(input("Digite sua idade: ")))
    values.append(date[:])
    date.clear()

print(values)