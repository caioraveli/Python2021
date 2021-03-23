"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.
Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]
=================== resultado
lista_soma  = [2, 4, 6, 8]
"""

# NEWBIE
lista_a = [1,2,3,4,5,6,7]
lista_b = [1,2,3,4]

def menor(l1,l2):
    if len(l1) < len(l2):
        return l1,l2
    return l2,l1

men,mai = menor(lista_a,lista_b)
lista_soma = [ v + mai[n] for n,v in enumerate(men)]

print(lista_soma)


# BETTER

lista_a = [1,2,3,4,5,6,7]
lista_b = [1,2,3,4]

#lista_soma2 = zip(lista_a,lista_b)  # 
#res = [ v[0] + v[1] for v in lista_soma2 ]

res = [ v[0] + v[1] for v in zip(lista_a,lista_b) ]

print(res)


#  PROF SOLUTION - ALMOST THE SAME

prof_soma = [ x + y for x,y in zip(lista_a,lista_b) ]
print(prof_soma)