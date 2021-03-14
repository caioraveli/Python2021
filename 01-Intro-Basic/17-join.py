# Join - juntar/transformar uma lista em uma string.

string = "O Brasil é o o o o  país do futebol, o Brasil é penta"

lista = string.split(' ')

string2 = ' '.join(lista) # digo o caractere que será baseado a junção, .join(nome_da_Lista)

print(string) # O Brasil é o o o o  país do futebol, o Brasil é penta
print(lista) # ['O', 'Brasil', 'é', 'o', 'o', 'o', 'o', '', 'país', 'do', 'futebol,', 'o', 'Brasil', 'é', 'penta']
print(string2) # O Brasil é o o o o  país do futebol, o Brasil é penta

string3 = ','.join(lista)

print(string3) # O,Brasil,é,o,o,o,o,,país,do,futebol,,o,Brasil,é,penta