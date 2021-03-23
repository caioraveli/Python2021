# Zip retorna um iterador de tuples que tem o next()
# String é iterável
# Se eu quero saber se algo é um gerador

# Gerador != Iterador != iterável

from types import GeneratorType

variavel = zip('Alo','Alo')

#print(next(variavel)) # ('A', 'A')
#print(next(variavel)) # ('l', 'l')
#print(next(variavel)) # ('o', 'o')

print(isinstance(variavel,GeneratorType)) # False. Não é um gerador

v2 = ((x,y) for x,y in zip('Alo','Alo')) # Construindo o Gerador

print(isinstance(v2,GeneratorType)) # True

print(next(v2))
