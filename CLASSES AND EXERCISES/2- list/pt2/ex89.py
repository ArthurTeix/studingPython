# cadastro de nomes e notas | boletim

record = []
counter = 0 

while True:
    nome = str(input("Nome: "))
    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))
    med = (n1+n2)/2

    record.append([nome, [n1, n2], med])
    counter += 1
    cont = str(input("Deseja continuar? [S/N]: ")).strip().upper()[0]
    while cont not in 'SN':
        cont = str(input("Resposta inválida! Deseja continuar? [S/N]: ")).strip().upper()[0]
    else:
        if cont == 'N':
            break

print("-=-"*15)

print(f"{'Nº':<4}{'Nome':<10}{'Média':>4}")
for a in range(0, counter):
    print(f"{a+1:<4}{record[a][0]:<10}{record[a][2]:.1f}")

print("---"*15)

while True:
    student = int(input("Mostrar as notas de qual aluno? (999 interrompe): "))

    if student == 999:
        break

    if student < 1 or student > len(record):
        print("Esse número de estudante não existe! Tente novamente!")
        continue

    print(f"Notas de {record[student-1][0]} são {record[student-1][1]}")

print("-=-"*15)
print("{'FIM DO PROJETO':^15}")