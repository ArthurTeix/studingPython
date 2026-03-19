values = []

for c in range (0,5):
    num = int(input("Digite um valor: "))

    if c == 0 or num > (values[-1]):
        values.append(num)
        print("O valor foi adicionado ao fim da lista, por ser o maior digitado até o momento")
    
    else: 
        cont = 0
        while cont < (len(values)):
            if num <= values[cont]:
                values.insert(cont, num)
                if num == values[0]:
                    print("valor adicionado ao início da lista por ser o menor digitado")
                else:
                    print("Valor adicionado no meio da lista")
                break
            cont += 1

print("-=-" * 10)
print(f"Os valores ordenados digitados são: {values}")