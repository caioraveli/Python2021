# Dividir uma string
# Posso dividir uma string e gerar uma lista dessa string

string = "O Brasil é o o o o  país do futebol, o Brasil é penta"

lista = string.split(' ')

print(lista) # ['O', 'Brasil', 'é', 'o', 'país', 'do', 'futebol,', 'o', 'Brasil', 'é', 'penta']


lista2 = string.split(',')
print(lista2) # ['O Brasil é o país do futebol', ' o Brasil é penta']

lista3 = string.split(';')
print(lista3) # ['O Brasil é o país do futebol, o Brasil é penta']

#for lis in lista:
#    print(f'A palavra {lis} apareceu {lista.count(lis)} vezes')

palavra_frequente=''
valor = 0
for palavra in lista:
    qtd_vezes = lista.count(palavra)

    if qtd_vezes > valor: 
        valor = qtd_vezes
        palavra_frequente = palavra
print(f'Palavra mais frequente é "{palavra_frequente}" e aparece {valor} vezes')

for word in lista2:
    print(word.strip().capitalize()) #Strip - remove espaço do inicio e do fim. Capitalize - faz a primeira ficar maisucula