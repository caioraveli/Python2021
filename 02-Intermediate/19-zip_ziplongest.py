"""
Zup - unindo iteráveis - RETURN ITERADOR DE TUPLES. (iterator1,iterator2,iterator3...)
Zip_longest - Itertools

Função next - retornar o próximo item do iterador. É como se fosse um passo do loop for (O foor faz exatamente
isso, porém de forma automática e transparente para o usuario.. percorre todos os "next")

OBS: Zip nivela o tamanho do zip resultante de acordo com o tamanho da menor lista
Zip_longest completa com None ou com o que passarmos no fillvalue

Vantagem - > zip e zip longest são geradores, ou seja, consomem pouquissimo recursos de memória
"""

cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo']
estados = ['SP','MG','BA']

estados_cidades = zip(estados,cidades)
print(estados_cidades) #printa o tipo de objeto -> <zip object at 0x7fbae9010980>

print(next(estados_cidades)) # retorna o próximo iterador de estados_cidades. ('SP', 'São Paulo')
print(next(estados_cidades)) # ('MG', 'Belo Horizonte')
print(next(estados_cidades)) # ('BA', 'Salvador')
#print(next(estados_cidades)) # Exceção de erro.. pois acabou a pilha de iteradores do estados_cidades

from itertools import zip_longest

cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo']
estados = ['SP','MG','BA']
estados_cidades = zip_longest(estados,cidades)

print(list(estados_cidades)) # [('SP', 'São Paulo'), ('MG', 'Belo Horizonte'), ('BA', 'Salvador'), (None, 'Monte Belo')]

estados_cidades2= zip_longest(estados,cidades,fillvalue='Estado') # Preenche com o parametro passado
print(list(estados_cidades2)) # [('SP', 'São Paulo'), ('MG', 'Belo Horizonte'), ('BA', 'Salvador'), ('Estado', 'Monte Belo')]


#### CUIDADO COM O ZIP_LONGEST

from itertools import zip_longest,count

# COUNT É UM GERADOR - NÃO TEM FIM

indice = count()
cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo','Outra']
estados = ['SP','MG','BA']

# COMO O INDICE NÃO TEM FIM O ZIP_LONGEST VAI COMPLETAR ETERNAMENTE COM ESTADO.. Melhor usar zip
#estados_cidades3 = zip_longest(
estados_cidades3 = zip(
    indice,
    estados,
    cidades,
    #fillvalue='Estado'
)

# COM ZIP_LONGEST
#for valor in estados_cidades3:
#    print(valor)
# ...
# (79117, 'Estado', 'Estado')
#(79118, 'Estado', 'Estado')
#(79119, 'Estado', 'Estado') ....

# COM ZIP
for indice,estado,cidade in estados_cidades3:
    print(indice,estado,cidade)

#0 SP São Paulo
#1 MG Belo Horizonte
#2 BA Salvador