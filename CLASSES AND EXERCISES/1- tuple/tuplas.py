# TUPLAS são variáveis onde posso guardar mais de um valor
# TUPLAS SÃO IMUTÁVEIS e usam PARENTESES
tupla0 = ('Santa Cruz', 'Palmeiras', 'Santos', 'Flamengo', 'Jaguar', 'Central', 'Cruzeiro')

# As tuplas em Python podem guardar diferentes tipos de valores
tupla1 = ('Santa Cruz', 1914, 25.3, True)

# MANIPULAÇÃO DE TUPLA 
print(f'''
Primeiro item de uma Tupla: {tupla0[0]}
Último item de uma Tupla: {tupla0[-1]}
Mostrar o primeiro item, até o item de índice 3: {tupla0[0:4]}
Mostra todos os itens após o índice 3: {tupla0[3:]}
Mostra todos os itens antes do índice 5: {tupla0[:5]}
Organiza em ordem alfabética: {sorted(tupla0)}
Usado para encontrar o índice de algo na lista: {tupla0.index("Santos")}
Saber a quantidade de itens na tupla: {len(tupla0)}
Posso unir duas Tuplas: {tupla0 + tupla1}
Posso saber quantas vezes certo elemento aparace: {tupla0.count("Santa Cruz")}
''')

# para deletar Tuplas uso: 'del(tupla1)'