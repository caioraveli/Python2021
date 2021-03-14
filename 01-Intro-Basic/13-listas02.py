l1 = [1,2,3]
l2 = [4,5,6]

#l3 = l1 + l2 # Concatenar as duas listas.. [1,2,3,4,5,6]
#print(l3)
l1.extend(l2) # mesma concatenação. seria l1 + l2, o argumento dentro de extend fica na frente
print(l1)

l2.extend(l1) # [4,5,6,1,2,3,4,5,6]
print(l2)

l4 = ['A','B',2]
l4.append('Caio') # Append - insere no fim
print(l4)

l4 = ['A','B',2]
l4.insert(1,'Caio') # Insiro no indice - o indice recebe o valor passado, e todos os antigos valores
# pra frente são movidos uma casa pra frente (shift)
print(l4) # ['A','Caio','B',2]

l4 = ['A','B',2]
l4.pop() # Append - Remove o último item da lista
print(l4) # ['A','B']

l4 = ['A','B',2,'Caio','Raveli',5,0.5]
del(l4[2:5]) # Delete de 2 até 5-1
print(l4) # ['A','B',5,0.5]

l4 = ['A','B',2,'Caio','Raveli',5,0.5]
l4[3] = 'Teste'
print(l4)
