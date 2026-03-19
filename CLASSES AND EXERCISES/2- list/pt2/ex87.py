# projeto passado melhorado
matriz = [[0,0,0], [0,0,0], [0,0,0]]
totalpares = 0

for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f"Digite o número [{linha+1}, {coluna+1}]: "))
        if (matriz[linha][coluna] % 2 == 0):
            totalpares += matriz[linha][coluna]

print('-=-'*10)

for linha in range(0,3):
    for coluna in range(0,3):
        print(f"[{matriz[linha][coluna]:^5}]",end='')
    print()

print('-=-'*10)

print(f'''
A soma dos valores pares é {totalpares}
A soma dos valores da terceira coluna é {(matriz[0][2]) + matriz[1][2] + matriz[2][2]}
O maior valor da segunda linha é {max(matriz[1])}
''')