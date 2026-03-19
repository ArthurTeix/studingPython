# criar um programa de lançamento de dos e rankear
from random import randint
from time import sleep
from operator import itemgetter

players ={
    'jogador 1': randint(1,6),
    'jogador 2': randint(1,6),
    'jogador 3': randint(1,6),
    'jogador 4': randint(1,6)
}
rank = []

print("Valores sorteados: ")

for a,b in players.items():
    print(f"    O {a} tirou {b} no dado.")
    sleep(0.5)

rank = sorted(players.items(), key=itemgetter(1), reverse=True)

print("\n=> RANKING DE PONTOS <=")
for c,d in enumerate(rank):
    print(f"    {c+1}º LUGAR: {d[0]} com {d[1]} pontos.")
    sleep(0.5)