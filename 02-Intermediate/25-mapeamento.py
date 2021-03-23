from map25 import produtos,pessoas,lista 

# map recebe uma função como primeiro argumento
# vai passar em cada posição da lista, aplicar a função e retornar o valor
# Não retorna uma lista pronta.. retorna um iterador, tem que iterar sob cada elemento.. ou fazer um type cast

nova_lista = map(lambda x:x*2, lista) 
print(list(nova_lista))

# O exemplo anterior pode ser resolvido facilmente com list comprehensions

nova_lista2 = [ x * 2 for x in lista]
print(nova_lista2)

# FUnção MAP faz mais sentido com dicionários

for produto in produtos:
    print(produto)

precos = map(lambda p:round(p['preco']*1.05), produtos) # so o preco de cada produto
print(list(precos))

# Se eu quiser aumentar 5% do valor dos produtos, nao dá pra usar lambda porque vou retornar a linha toda "p" e não só p['preco']
# Faço uma função comum

def aumenta_preco(p):
    p['preco'] = round(p['preco'] * 1.05,2)
    return p #retornar a lista toda só que com os preços alterados

precos2 = map(aumenta_preco,produtos)
print(list(precos2))


nomes = map(lambda p: p['nome'],pessoas)

for pessoa in nomes:
    print(pessoa)