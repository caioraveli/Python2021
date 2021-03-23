"""
Combinations, Permutations e Product - Itertools
Combinação - Ordem não importa
Permutação - Ordem importa
Ambos não repetem valores únicos
Produto - Ordem importa e repete valores únicos
"""

from itertools import combinations,permutations, product

pessoas = ['Caio','Raveli','Freitas','Barbosa']

for grupo in combinations(pessoas,2): # ('Caio','Raveli') == ('Raveli','Caio') - ordem não importa
    print(grupo)


for grupo in permutations(pessoas,2): # ('Caio','Raveli') != ('Raveli','Caio') - ordem não importa. Logo, tem muito mais valores
    print(grupo) # Porém, como não repete valores, não vou encontrar ('Caio','Caio')

for grupo in product(pessoas,repeat=2): # Mesmo do permutations, só que agora aceita valores repetidos
    print(grupo)