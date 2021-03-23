# Basicamente é um for que vai iterar sobre algo e retornar uma lista
# na sintaxe, o que vem antes do for seria o retorno

l1 = [1,2,3,4,5,6,7,8,9]
l2 = [ var for var in l1] # Fazendo exatamente nada alem de iterando sobre l1 e jogando cada valor em l2

print(l2) # l1 == l2

l3 = [ v * 2 for v in l1 ] # retorno seria v * 2

print(l3) # [2, 4, 6, 8, 10, 12, 14, 16, 18]

# for abaixo é o mesmo da linha 9
#v4 = []
#for v3 in l1:
#    v4.append(v3*2) # [2, 4, 6, 8, 10, 12, 14, 16, 18]

# POSSO USAR MAIS DE UM FOR PRA RETORNAR MAIS DE UM VALOR.. FOR DENTRO DE OUTRO

l4 = [ (cord1,cord2) for cord1 in l1 for cord2 in range(3) ]

print(l4)

#(1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2), (3, 0), (3, 1), (3, 2), (4, 0), (4, 1), (4, 2), (5, 0), (5, 1), (5, 2), (6, 0), (6, 1), (6, 2), (7, 0), (7, 1), (7, 2), (8, 0), (8, 1), (8, 2), (9, 0), (9, 1), (9, 2)]

l4 = ['Caio','Raveli','Freitas']

l5 = [v.replace('a','@') for v in l4]

print(l5) # ['C@io', 'R@veli', 'Freit@s']

tupla = (
    ('chave','valor'),
    ('chave2','valor2'),

)

ex1 = [ (x,y) for x,y in tupla ] # [('chave', 'valor'), ('chave2', 'valor2')]
ex2 = [ (x,y) for y,x in tupla[:] ] # [('valor', 'chave'), ('valor2', 'chave2')]
print(ex1)

d1 = dict(ex2)

print(d1['valor2']) # chave2