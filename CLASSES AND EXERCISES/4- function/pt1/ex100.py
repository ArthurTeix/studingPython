# sortear 5 valores dentro de uma lista | somar os valores pares
from random import randint

lista = []

def sorteia(numbers):
    for a in range(0,5):
        numbers.append(randint(1,20))
    
    print(f"Os 5 valores sorteados foram -> {numbers}")

def somaPar(soma):
    total = 0
    for a in range (0,5):
        if soma[a] % 2 == 0:
            total += soma[a]
    
    print(f"A soma dos valores pares da lista é: {total}")

sorteia(lista)
somaPar(lista)