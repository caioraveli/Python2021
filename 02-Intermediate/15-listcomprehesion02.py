# LIST COMPREHENSIONS - CONDICIONAIS

l1 = list(range(1,10))

pares = [ p for p in l1 if p % 2 == 0]

div3 = [ d3 for d3 in l1 if d3 % 3 == 0 if d3 % 8 == 0] # DOIS IFS - nao uso and.. Div por 3 E por 8

print(pares)
print(div3) #[24, 48, 72, 96] - divisiveis por 3 e 8

# SINTAXE COM ELSE - Parece que só funciona se tiver o else

ex7 = [ v if v % 7 == 0 else 0 for v in l1]

print(ex7) # [0, 0, 0, 0, 0, 0, 7, 0, 0]

ex8 = [ v if v % 3 == 0 or v % 5 == 0 else 0 for v in l1] # [0, 0, 3, 0, 5, 6, 0, 0, 9]

print(ex8)