# list - método do python onde posso construir uma lista a partir de um objeto iterável

l1 = list(range(1,10)) # range(1,10) é um obj iterável. Logo, list constrói uma lista a partir do range
print(l1)

soma = 0
for valor in l1:
    print(valor, end=' ')
    soma += valor
print()
print(soma)