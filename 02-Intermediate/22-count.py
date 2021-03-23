# Count - Itertools - retorna um iterador. 
# Vai gerar um contador que é um iterador, logo podemos usar a função next com esse contador. Diferente da
# função range que não é um iterador (é um iterável, mas não é um iterador)

from itertools import count # LEMBRAR DE IMPORTAR ESTE MODULO

c1 = count() # MUITO CUIDADO pois este count não tem fim.!!!!

#print(next(c1)) # 0
#print(next(c1)) # 1 
#print(next(c1)) # 2
#print(next(c1)) # 3

# ME ENTREGA VALOR ENQUANTO NÃO HOUVER QUEBRA - INFINITO

c2 = count(start=5,step=2) 

for i in c2:
    print(i,end=',')
    if i >= 20:
        break
print("\n")

c3 = count(start=1,step=0.1) # step pode ser decimal, float, negativo (fazer voltando)

for j in c3:
    #print(round(j,4))
    print(round(j,2))
    if j >=2:
        break

# INDEXAR UMA LISTA

l1 = ['Caio','Raveli','Freitas']

ct = count()

#l2 = list(zip(ct,l1))

#print(l2) # [(0, 'Caio'), (1, 'Raveli'), (2, 'Freitas')]

l1.append('Joao')
l1.append('Maria')
l1.append('José')

l2 = list(zip(ct,l1))

print(l2) # [(0, 'Caio'), (1, 'Raveli'), (2, 'Freitas'), (3, 'Joao'), (4, 'Maria'), (5, 'José')]

# OBS:  Se eu nao comentasse a linha 38, usando o mesmo contador em outra lista ele ia continuar...
#[(0, 'Caio'), (1, 'Raveli'), (2, 'Freitas')]
#[(4, 'Caio'), (5, 'Raveli'), (6, 'Freitas'), (7, 'Joao'), (8, 'Maria'), (9, 'José')]