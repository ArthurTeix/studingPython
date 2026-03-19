values = list()
for v in range(0,5):
    values.append(int(input("Digite um número: ")))

print(f"O maior valor digitado foi {max(values)} e ele está na posição {values.index(max(values))}")
print(f"O menor valor digitado foi {min(values)} e ele está na posição {values.index(min(values))}")

