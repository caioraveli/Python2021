# Funções lambda são funções/expressões anônimas.

def funcao(arg,arg2):
    return arg * arg2

var = funcao(2,2)
print(var) # print 4

a = lambda x,y: x * y # é exatamente a mesma função anterior
print(a(2,2)) # 4

# O interpretador do python não sabe ordenar a lista abaixo, porque são listas dentro de listas. O sort vai
# nos ajudar porque com o parametro key eu posso trabalhar com todas as mesmas posições nas sublistas como se fosse uma lista só
lista = [
    ['P1', 13],
    ['P2', 6],
    ['P3', 7],
    ['P4', 50],
    ['P5', 8]
]
lista.sort() # Altero mesmo a ordem da minha lista 
print(lista) # Porém, continua sem alterar baseado nos inteiros

lista2 = [
    ['P1', 13],
    ['P2', 6],
    ['P3', 7],
    ['P4', 50],
    ['P5', 8]
]

def fun3(arg):
    return arg[1]

lista2.sort(key=fun3) # key aplica pra cada posição na lista
print(lista2)

lista2.sort(key=fun3,reverse=True) # key aplica pra cada posição na lista. No caso aplicando pra todas as posições (arg[1])
print(lista2)

lista2.sort(key=lambda arg:arg[1]) # [['P2', 6], ['P3', 7], ['P5', 8], ['P1', 13], ['P4', 50]]
print(lista2)


### Ou posso usar a função sorted

lista3 = [
    ['P1', 13],
    ['P2', 6],
    ['P3', 7],
    ['P4', 50],
    ['P5', 8]
]
print(sorted(lista)) # Não ordena -> [['P1', 13], ['P2', 6], ['P3', 7], ['P4', 50], ['P5', 8]]
print(sorted(lista3, key = lambda x:x[1])) # [['P2', 6], ['P3', 7], ['P5', 8], ['P1', 13], ['P4', 50]]
print(sorted(lista3, key = lambda i:i[1], reverse=True)) # [['P4', 50], ['P1', 13], ['P5', 8], ['P3', 7], ['P2', 6]]