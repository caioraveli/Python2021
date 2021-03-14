"""
Unpacking - desempacotamento
"""

lista = ['Caio','João','Maria']

n1, n2, n3 = lista # Praticamente atribuo cada valor da lista pra variáveis específicas

print(n2) # Imprime João

lista2 = ['Caio','João','Maria']

#n1, n2 = lista2 # Dá erro -> muitos objetos para serem desempacotados (3 pra duas variaveis..)

n1, n2, *outra_lista = lista2

print(n1,n2) # agora dá certo -> Imprime Caio e João

lista3 = ['Caio','João','Maria','Raveli',1,2,5,6,8,8,9,9]

n1,n2, *outra_lista = lista3

print(n1,n2) # Continua dando certo - Imprime Caio e joão
print(outra_lista)  # Imprime uma lista com o que sobrou - ['Maria', 'Raveli', 1, 2, 5, 6, 8, 8, 9, 9]

lista4 = ['Caio','João','Maria','Raveli',1,2,5,6,8,8,9,10]

n1,n2, *outra_lista, ultimo_da_lista = lista4

print(ultimo_da_lista) # Imprime só o 10

lista5 = ['Caio','João','Maria','Raveli',1,2,5,6,8,8,9,10]

*outra_lista, n1,n2,n3, ultimo_da_lista = lista5

print(n1,n2,n3,ultimo_da_lista) # imprime 8 8 9 10 - ou seja, o que nao foi especificado, está no *outra_lista

# Pratica comum.. utilizar *_ para informar que nao vou utilizar tais valores.