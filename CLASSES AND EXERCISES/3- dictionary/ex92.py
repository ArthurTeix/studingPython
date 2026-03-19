from datetime import datetime

while True:
    people = {}

    people['nome'] = str(input("Nome: "))
    idade = int(input("Ano de Nascimento: "))
    people['idade'] = datetime.now().year - idade
    people['ctps'] = int(input("Carteira de Trabalho (0 não tem): "))

    if people['ctps'] == 0:
        break
    
    people['contratação'] = int(input("Ano de Contratação: "))
    people['aposentadoria'] = people['contratação'] - idade + 35
    people['salário'] = int(input("Salário: R$"))
    break

print("-=-"*15)
for a, b in people.items():
    print(f" -> {a}: {b}")