# Enumerate  - somente usado também com elemento iteravel. Que tem valores onde podemos percorrer..

string = "O Brasil é o o o o  país do futebol, o Brasil é penta"

lista = string.split(' ')

for indice,valor in enumerate(lista): # unpacking
    print(indice, valor, lista[indice]) # valor = lista[indice]

print()
lista2 = [ #listas dentro de outra
    [0, 'Caio'],
    [1,'Raveli'],
    [2,'Freitas']
]

# Os dois for's abaixo fazem exatamente a mesma coisa
for v in lista2: 
    print(v[0], v[1])

print()

# exatamente o que a função enumerate faz. So que com enumerate nao preciso ter um campo representando indices
# pois o enumarate já cria o campo de enumeração (não são indices). Enumerate simplesmente
# enumera os campos de uma lista e, se eu não estipulo um valor para começar a enumeração, os valores
# criados pelo enumerate, somente bate com os indices.
for ind,val in lista2: 
    print(ind,val)

print()


# Manipulando o enumerate para começar do 53
for ind2,val2 in enumerate(lista2,53):
    print(ind2,val2)

