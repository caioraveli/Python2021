d1 = {
    'str' : 'Valor',
    123: 'Outro valor',
    (1,2,3,4) : 'Tupla',

}

# Trabalhando só com os valores - coluna da direita
print(d1.values()) # dict_values(['Valor', 'Outro valor', 'Tupla'])

print('str' in d1) # retorna True
print('Valor' in d1.values()) # retorna True

# Mesma coisa só que pra chaves

print(123 in d1.keys()) # Retorna True

# Quantidade de pares

print(len(d1)) # no caso, printa 3

# Iterando sobreo dicionario

d1 = {
    'chave1' : 'Valor',
    'chave2': 'Outro valor',
    'chave3' : 'Mais um valor',

}

for k in d1:
    print(k) # printa só as chaves

for v in d1.values():
    print(v) # printa só os valores

for i in d1.items(): 
    print(i) # printa todos os pares ('chave1', 'Valor') ..

for k,v in d1.items(): # desempacotando
    print(f'Essa é a chave: {k} e esse é o valor {v}') 

# ou 

for k in d1.items(): # mesma coisa do anterior
    print(f'Essa é a chave: {k[0]} e esse é o valor {k[1]}')