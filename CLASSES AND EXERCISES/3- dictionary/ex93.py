player = {}
gols = []
total = 0

player['nome']= str(input("Nome do jogador: "))

matches = int(input(f"Quantas partidas {player['nome']} jogou: "))

for a in range(0,matches):
    quant = int(input(f'Quantos gols na {a+1}º partida?: '))
    total += quant
    gols.append(quant)

player['gols'] = gols
player['total'] = total

print("-=-"*15)

print(f"O jogador {player['nome']} jogou {matches} partidas.")
for a in range(0,matches):
    print(f"    => Na {a+1}º partida, fez {player['gols'][a]} gols.")
print(f"Fez um total de {total} gols.")
