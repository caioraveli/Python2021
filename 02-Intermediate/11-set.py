# Sets só suportam elementos unicos (maior diferença entre listas,tuplas e sets)
# Não tenho indices. Então não consigo acessar um valor específico do SET. Itero, mas não acesso diretamente
# Se fizer s1 ={}, estou criando um dicionário. Criando set vazio: set()
# Não respeitam ordem
# Não aceitam elementos duplicados
# Normalmente utilizados para remover elementos duplicados de uma Lista - fazer o cast
# Só recebem valores (não chaves e valores)
# Suportam apenas elementros imutáveis.. Numeros, tuplas, strings, etc
# union ou | -> une dois sets
# intersection & -> retorna todos os elementos presentes nos dois sets
# Difference - a ordem importa. Fico so com os elementos que estão so no primeiro
# symmetric_difference -> elementos unicos de cada set. Está mas não no outro

s1 = {1,2,3,4,5} # print {1, 2, 3, 4, 5}
print(s1)

for v in s1:
    print(v)

s2 = set()
s2.add((1,2,3))
s2.add('Caio')

print(s2) # {(1, 2, 3), 'Caio'}
s2.discard('Caio')
print(s2) # {(1, 2, 3)}

s2.update('Raveli') # Itera sobre o argumento passado
s2.update('Caio')
print(s2) # 'l', 'e', 'v', (1, 2, 3), 'o', 'C', 'R', 'i', 'a'} - sem elementos duplicados e fora de ordem

l1 = [1,2,3,4,3,2,1,1,1,1,2,3,4,5,6,7,'Caio','Raveli']
l1 = set(l1) # {1, 2, 3, 4, 5, 6, 7, 'Raveli', 'Caio'}
l1 = list(l1)
print(l1) # ['Caio', 1, 2, 3, 4, 5, 6, 7, 'Raveli'] - remove duplicados mas volta fora de ordem

s3 = {1,2,3,4,5}
s4 = {1,2,3,4,5,6}
s5 = s3 | s4 # união
print(s5)  # {1, 2, 3, 4, 5, 6}
s6 = s3 & s4 # intersection
print(s6) # {1, 2, 3, 4, 5}
s7 = s4 - s3
print(s7) # {6}

s8 = {1,2,3,4,5,6}
s9 = {4,5,6,7,8,9}
s10 = s8 ^ s9
print(s10) # {1, 2, 3, 7, 8, 9}