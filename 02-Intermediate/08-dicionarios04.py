clientes = {
    'cliente1' : {
        'nome': 'Caio',
        'sobrenome': 'Freitas'
    }, # posso deixar essa virgula sem problemas. Quando precisar duplicar é só copiar
    'cliente2' : {
        'nome': 'Fulano',
        'sobrenome': 'de Tal'
    },
    'cliente3' : {
        'nome': 'Joao',
        'sobrenome': 'E Maria'
    },
}


for clientes_k, clientes_v in clientes.items(): # proximo for, iterar sobre clientes_v
    print(f'Exibindo {clientes_k}')
    for dados_k, dados_v in clientes_v.items(): # veja que uso cliente_v como segundo dicionário
        print(f'\t{dados_k} =  {dados_v}')

    
# IMPORTANTE

d1 = {1: 'a', 2: 'b', 3: 'c'}

v = d1 
print(d1,v) # ambos tem o mesmo valor {1: 'a', 2: 'b', 3: 'c'} {1: 'a', 2: 'b', 3: 'c'}

# POREM, se eu alterar de um, vai alterar no outro também..

v[1]='Caio'
print(d1,v) # {1: 'Caio', 2: 'b', 3: 'c'} {1: 'Caio', 2: 'b', 3: 'c'}

print(v == d1) # True -> Ou seja, d1 e v apontam pro mesmo endereço na memória


# COPIANDO - cópia rasa

v2 = d1.copy()

v2[1] = 'Raveli' 
print(d1,v2) # Só mudou a copia.. {1: 'Caio', 2: 'b', 3: 'c'} {1: 'Raveli', 2: 'b', 3: 'c'}


# RASA porque se eu alterar um subitem, altera nos dois..

d2 = {1: 'a', 2: 'b', 3: 'c', 4: ['Caio','Raveli']} # 

print(d2) # {1: 'a', 2: 'b', 3: 'c', 4: ['Caio', 'Raveli']}

v3 = d2.copy()

print(v3) # {1: 'a', 2: 'b', 3: 'c', 4: ['Caio', 'Raveli']}

v3[4][0] = 'MUDAR' # Podemos ver que vai mudar os dois.. d2 e v3

print(d2,v3) # 1: 'a', 2: 'b', 3: 'c', 4: ['MUDAR', 'Raveli']} {1: 'a', 2: 'b', 3: 'c', 4: ['MUDAR', 'Raveli']}

# COPIA REAL!! 

import copy

d4 = {1: 'a', 2: 'b', 3: 'c', 4: ['Caio','Raveli']}
v4 = copy.deepcopy(d4)
v4[4][0] = 'MUDAR' # Podemos ver que agora sim sao independetes. Só vai mudar o v4
print(d4,v4) # {1: 'a', 2: 'b', 3: 'c', 4: ['Caio', 'Raveli']} {1: 'a', 2: 'b', 3: 'c', 4: ['MUDAR', 'Raveli']}