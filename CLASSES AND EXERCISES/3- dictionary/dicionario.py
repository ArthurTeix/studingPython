dates = { # Criando dicionário
    'nome': 'Arthur',
    'idade': 17
}

dates['sexo'] = 'M' # Adicionar keys e values
del dates['idade'] # Usado para deletar keys
print(dates)

filme = {
    'titulo': 'Star Wars',
    'ano': '1977',
    'diretor': 'George Lucas'
}

print(filme.values()) # Retorna os Valores (dados dentro das categorias)
print(filme.keys()) # Retona as Keys (categorias criadas)
print(filme.items()) # Retorna os Values e Keys

print("-=-"*30)
for k,v in filme.items(): #para percorrer todo meu dicionário
    print(f"O {k} é {v}")

# também posso fazer uma lista com vários dicionários
brazil = []

state1 = {
    'nome': 'Pernambuco',
    'capital': 'Recife',
    'city': 'Jaboatão'}
state2 = {
    'nome': 'Distrito Federa',
    'capital': 'Brasília',
    'city': 'Gama'}

brazil.append(state1)
brazil.append(state2)

print(brazil)
print(brazil[0]['nome']) # primeiro o índice da lista e depois a key do dicionário
print(brazil[0]['capital'])
print(brazil[1]['city'])

# como adicionar valores inputados nos dicionários

estado = dict() # usar dict() é o mesmo de {}
pais = []

for c in range(3):
    estado['uf'] = str(input("Nome do estado: "))
    estado['sigla'] = str(input("Sigla: "))
    pais.append(estado.copy()) # copy() é um método exclusivo para dicionários entrarem em listas ou tuplas

for a in pais:
    print(a)

for a in pais: 
    for b, c in a.items():
        print(f"O campo {b} tem valor {c}")