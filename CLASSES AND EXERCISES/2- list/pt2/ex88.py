# sorteador de quantos jogos quiser
from time import sleep
from random import randint

games = []
cont = 0

print("-^-"*10)
print("      JOGO DA MEGA SENA     ")
print("-~-"*10)

quant = int(input("Quantos jogos você quer que eu sorteie?: "))

print(f"-=-=-=>  SORTENDO {quant} JOGOS  <=-=-=-")

for a in range (quant):
    while cont < 6:
        x = randint(1,99)
        if x not in games: 
            games.append(x)
            cont += 1

    print(f"Jogo {a+1}: {games}")
    sleep(0.5)
    games.clear()
    cont = 0

print("-=-=-=-= < BOA SORTE! > =-=-=-=-")