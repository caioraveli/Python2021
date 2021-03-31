# Reduce por padrão não vem nos builtins do python. Temos que importar do functools
# Acumulador compulsivo

from map25 import produtos,pessoas,lista 
from functools import reduce

#EX:

acumula = 0
for item in lista:
    acumula += item
print(acumula) # Print 55. Soma todos os valores e REDUZ em um valor só.. por isso reduce


# Entendi que com reduce tenho que passar no lambda necessariamente dois argumentos
soma_lista = reduce(lambda ac,l: ac + l,lista,0) # 0 é opcional, mas bom utilizar porque diz o inicio. 
print(soma_lista)

soma_precos = reduce(lambda ac,p: ac + p['preco'], produtos,0) # NEsse caso, se tirar o ZERO não funciona
print(soma_precos)


# COM IDADE

soma_idade = reduce(lambda ac,i: ac + i['idade'], pessoas, 0)
# TypeError: unsupported operand type(s) for +: 'dict' and 'int' -> corrigi o erro adicionado o ZERO para referenciar o incio
print(soma_idade)

print(f'Média de idades {soma_idade/len(pessoas)}')
