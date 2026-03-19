# criar função que deve suportar nome e gols vazios e com dados
def player(name, goals):
    """
    :name: nome do jogador
    :goals: quantidade de gols marcados
    """
    print(f"The player {name} scored {goals} in the games")


name = input('Name of the player: ')
goals = input("Number of goals: ")

if name == '':
    name = '<desconhecido>' # caso o nome não seja informado

if goals.isnumeric():
    goals = int(goals) # passando os gols para números
else:
    goals = 0 # caso os gols não sejam informados

player(name, goals)