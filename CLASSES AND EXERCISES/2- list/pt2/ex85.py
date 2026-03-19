# separador de ímpares e pares
values = [[], []]

for a in range (7):
    number = int(input(f"Digite o {a + 1}º número: "))

    if number%2 == 0:
        values[0].append(number)
    else:
        values[1].append(number)

print(f'''
Os valores ímpares digitados foram: {sorted(values[1])}
Os valores pares digitados foram: {sorted(values[0])}
''')

if (len(values[0]) > len(values[1])):
    print("Você digitou mais números pares do que ímpares") 
else:
    print("Você digitou mais números ímpares do que pares")