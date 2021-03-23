# Posso ter qualquer valor dentro de dicionários

d1 = {
    'str' : 'Valor',
    123: 'Outro valor',
    (1,2,3,4) : 'Tupla',

}

print(d1[(1,2,3,4)]) # Printa -> Tupla

#print(d1['chaveNaoExiste']) # usar chave que não existe o python retorna erro. Código para.print

# Melhor tratar
try:
    d1['chaveNaoExiste']
except:
    print('Chave nao existe')

print(d1.get('chaveNaoExiste')) # com o get, caso a chave nao exista, retorna None (codigo nao para)

# Tratando..

if d1.get('chaveNaoExiste') is None:
    print("Tentando acesso algo que nao existe")


#ATUALIZANDO DICIONARIOS

d1['str'] = 'New value'

# OU

d1.update({123:445}) # 

print(d1) # {'str': 'New value', 123: 445, (1, 2, 3, 4): 'Tupla'}

# DELETANDO

del d1['str']

print(d1) # {123: 445, (1, 2, 3, 4): 'Tupla'} -> SEM a chave str
