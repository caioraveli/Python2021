# Estrutura de dados baseada em chave e valor. Chave sendo o "indice" do dicionário (mas não é indice)
# As chaves precisam ser únicas. Caso repita, quando referenciar d1['chave'], só vou ter o valor última
# chave 'chave'.
d1 = {'chave1':'valor da chave'}

print(d1) # print -> {'chave1': 'valor da chave'}
print(d1['chave1']) # printa -> Valor da chave

d1['nova chave'] = 'Valor da nova chave'

print(d1) # printa -> {'chave1': 'valor da chave', 'nova chave': 'Valor da nova chave'}

#### OUTRA FORMA

d2 = dict(chave1='Valor da chave1', chave2='Valor da chave2')
print(d2) # printa -> {'chave1': 'Valor da chave1', 'chave2': 'Valor da chave2'}
 