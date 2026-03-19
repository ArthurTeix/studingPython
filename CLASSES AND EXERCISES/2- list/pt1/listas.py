# LISTAS são variáveis onde posso guardar mais de um valor
# LISTAS SÃO MUTÁVEIS e usam COLCHETES
# As Listas em Python também podem guardar diferentes tipos de valores
lista = ['cheese', 'hot dog', 'cookie', 'rice', 'been', 'bread', 'bife']
lista1 = [1, "food", 4.45, False, "home"]

# MANIPULAÇÃO DE LISTA
print(f'''
Listas são mutáveis, então posso adicionar valores (no fim): {lista.append('milk shake')} -> {lista}
Posso adicionar itens em qualquer índice: {lista.insert(0, 'apple')} -> {lista}
Se quiser eliminar um item pelo índice, pode usar assim: {lista.pop(2)} -> {lista}
Se quiser eliminar um item pelo conteúdo, pode usar assim: {lista.remove("apple")} -> {lista}
Para eliminar o último elemento basta usar assim: {lista.pop()} -> {lista}
Posso criar listas por meio de um 'for':
''')

#Posso criar listas por meio de um 'for':
valores = list(range(4,11))
print(valores)

valores1 = [1, 3, 6, 8, 2, 5, 6, 0, 9]
print(f'''
Para organizar os valores em ordem crescente basta usar: {valores1.sort()} -> {valores1}
Para organizar os valores em ordem decrescente basta usar: {valores1.sort(reverse=True)} -> {valores1}
''')