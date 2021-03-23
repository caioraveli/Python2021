lista = [
    ['c1',1],
    ['c2',2],
    ['c3',4],
    ['c4',4],
]

d1 = dict(lista)

print(d1) # cast de lista -> {'c1': 1, 'c2': 2, 'c3': 4, 'c4': 4}

t1 = tuple(lista) 
d2 = dict(t1) # cast de tupla -> {'c1': 1, 'c2': 2, 'c3': 4, 'c4': 4}
print(d2)

d3 = {
    1: 2,
    2: 3,
    4: 5,
}

d3.pop(4) # elimino a chave de nome 4 -> {1: 2, 2: 3}
print(d3)

d4 = {
    1: 2,
    2: 3,
    4: 5,
}
d4.popitem() # elimina o ultimo item -> {1: 2, 2: 3}
print(d4)

# Concatenar dicionarios

d5 = {1:2,2:3,3:5}
d6 = {'a':'b','c':'d'}
d5.update(d6)
print(d5) # {1: 2, 2: 3, 3: 5, 'a': 'b', 'c': 'd'}