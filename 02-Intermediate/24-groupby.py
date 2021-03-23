from itertools import groupby,tee
# groupby precisa que o dicionário esteja ordenado


alunos = [
    {'nome': 'Caio', 'nota': 'A'},
    {'nome': 'Raveli', 'nota': 'C'},
    {'nome': 'Freitas', 'nota': 'D'},
    {'nome': 'Barbosa', 'nota': 'A'},
    {'nome': 'João', 'nota': 'C'},
    {'nome': 'Carol', 'nota': 'A'},
    {'nome': 'Fulano', 'nota': 'B'},
    {'nome': 'Karla', 'nota': 'D'},
    {'nome': 'Maria', 'nota': 'A'},
    {'nome': 'José', 'nota': 'C'},

]


ordena = lambda item: item['nota'] #recebo item e retorno nota
alunos.sort(key=ordena)

for aluno in alunos:
    print(aluno)

alunos_agrupados = groupby(alunos, ordena)

for agrupamento,valores_agrupados in alunos_agrupados:
    va1,va2 = tee(valores_agrupados) # tenho duas cópias de tee para resolver o problema de ter esgotado o iterador
    print(f'Agrupamento: {agrupamento}')
    #quantidade = len(list(valores_agrupados))
    quantidade = len(list(va1)) 
    print(f'{quantidade} tiraram a nota {agrupamento}')
    #for aluno in valores_agrupados:
    #    print(aluno['nome'],end=',') # Por que não imprime nada? Porque quantidade é um iterador e já está esgotado
    #print() # como resolver isso?? Podemos usar o tee do itertools
    for aluno in va2:
        print(f'\t{aluno}')
    
print()