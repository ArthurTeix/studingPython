# nome e média com dict
student = {}

student['nome'] = str(input("Nome: "))
student['media'] = float(input(f"Média de {student['nome']}: "))

print(f'''
Nome é igual a {student['nome']}
Média é igual a {student['media']}
''', end='')

if student['media'] > 7:
    print("Sua situação é de Aprovado")
else:
    print("Sua situação é de Reprovado")