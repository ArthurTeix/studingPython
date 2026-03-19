jogadores = []
player = {}
gols = []
total = 0

while True:
    player.clear()
    total = 0
    gols.clear()

    player['nome']= str(input("Nome do jogador: "))

    matches = int(input(f"Quantas partidas {player['nome']} jogou: "))

    for a in range(0,matches):
        quant = int(input(f'Quantos gols na {a+1}º partida?: '))
        total += quant
        gols.append(quant)

    player['gols'] = gols[:]
    player['total'] = total

    jogadores.append(player.copy())

    print("-=-"*15)

    resp = str(input("Quer continuar cadastrando? [S/N]: ")).upper()[0]
    while resp not in 'SN':
        resp = str(input("Valor inválido! Quer continuar cadastrando? [S/N]: ")).upper()[0]
    print("-=-"*15)
    if resp == 'N':
        break
    
print(f"{'Nº':<5} {'Nome':<12} {'Gols':<10} {'Total':>7}")

for a in range (0,len(jogadores)):
    print(f"{a+1:<5} {jogadores[a]['nome']:<12} {str(jogadores[a]['gols']):<10} {jogadores[a]['total']:>7}")

print("-=-"*15)

while True: 
    play = int(input("Mostrar dados de qual jogador? (999 para parar): "))

    while play > (len(jogadores)):
        print("Jogador inexistente!")
        play = int(input("Mostrar dados de qual jogador? (999 para parar): "))
        break

    if play == 999:
        print("-=-"*15)
        print("PROGRAMA ENCERRADO!")
        break

    print(f" --> Levantamento do jogador {jogadores[play-1]['nome']}:")

    for a in range (0, len(jogadores[play-1]['gols'])):
        print(f"Jogo {a+1}: {jogadores[play-1]['gols'][a]} gols")