# positivos   [0123456789]
text        = "Caio Raveli"
# negativos  -[987654321]
print(f'{text[9]}')

print(f'{text[0]}') # imprime C
print(f'{text[-1]}') # imprime i

print(f'{text[1:4]}') # 1 ao 3 -> note que inclui o 1 mas nao o 4 
print(f'{text[:4]}') # imprime Caio.. do inicio ate o valor passado menos 1

print(f'{text[-6:]}') # imprime Raveli.. mesma coisa, so que com negativo.
print(f'{text[-6:-1]}') # imprime Ravel

print(f'{text[:9:2]}') # imprime Ci ae -> ::N -> N é o passo.
print(f'{text[::4]}') 