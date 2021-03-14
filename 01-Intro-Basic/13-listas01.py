"""
Fatiamento - append, insert, pop, del, clear, extend, +
min, max
range
"""
#          0   1   2   3   4
lis_01 = ['A','B','C','D','E']
#    -     5   4   3   2   1 

lis_02 = ['A','CAIO',10.5,3,True,'B','C']


print(lis_02) # Imprime a lista toda
print(lis_02[3])

lis_02[5] = 'Raveli'
print(lis_02)
print(f'{lis_02[0:3]}') # Imprime A, CAIO, 10.5
print(lis_02[-1]) # Imprime o último item
print(lis_02[-5:-1])
print(lis_02[-3:]) # Imprime de True até o final
print(lis_02[::2]) # Imprime de dois em dois
print(lis_02[::-1]) # Imprime de trás pra frente

