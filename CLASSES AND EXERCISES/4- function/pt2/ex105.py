
def notas(*numeros, sit=False):
    """
    -> Função para cadastrar notas e descrever situação da turma
    :*numeros: ilimita a quantidade de notas a serem passadas
    :sit: (opcional) exibe a situação da turma de acordo com a média
    :return: retorna um dicionário com as notas e a situação opcionalmente
    """
    registros = {}
    registros['total'] = len(numeros)
    registros['maior'] = max(numeros)
    registros['menor'] = min(numeros)
    registros['média'] = (sum(numeros) / len(numeros))

    if sit == True:
        if registros['média'] > 7:
            registros['situação'] = 'BOA'

        elif registros['média'] < 6:
            registros['situação'] = 'RUIM'
        
        else:
            registros['situação'] = 'RAZOÁVEL'

    return f"\n{registros}"

print(notas(5, 4, 3), notas(4,4,6,1, sit=True), notas(6,7,sit=True), notas(9,8,7,sit=True))
