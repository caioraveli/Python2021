# Filter muito similar ao map.
# Filter vai retornar verdadeiro ou falso pra expressão que eu passar.

# FUNÇÃO no lugar de lambda é que posso reutilizar em outro lugar, desvantagem é que tem mais código pra escrever

from map25 import produtos,pessoas,lista 

nova_lista = filter(lambda x: x > 5, lista)
print(list(nova_lista)) # [6, 7, 8, 9, 10]


# WITH LIST COMPREEHENSION

nova_lista2 = [ x for x in lista if x > 5 ]
print(nova_lista2) # [6, 7, 8, 9, 10]

# COM DICIONARIOS

nova_lista3 = filter(lambda p: p['preco'] > 50, produtos)

for produto in nova_lista3:
    print(produto)

# SE PRECISAR ALGO MAIS COMPLEXO
# Acho que não dá pra passar multiplos argumentos pra uma função usada no filter.. melhor list comprehension

def filtrar(produto):
    if produto['preco'] > 50:
        return True

nova_lista4 = filter(filtrar, produtos)
nova_lista4 = list(nova_lista4)
for produto in nova_lista4:
    print(produto)


# Filtrando maiores de idade

nova_lista5 = filter(lambda pes: pes['idade'] > 18, pessoas)

for pessoa in nova_lista5:
    print(pessoa)