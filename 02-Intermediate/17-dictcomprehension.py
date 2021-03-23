lista = [
    ('chave','valor'),
    ('chave2','valor2'),
]

# x chave e y valor
d1 = {x:y for x,y in lista} # é o mesmo que dict(lista)

print(d1) #{'chave': 'valor', 'chave2': 'valor2'}

lista2 = [
    ('chave', 4),
    ('chave2', 'duplicar')
]

d2 = {x:y*2 for x,y in lista2} # {'chave': 8, 'chave2': 'duplicarduplicar'}
print(d2) 

d3 = {x.upper():y for x,y in lista2} # {'CHAVE': 4, 'CHAVE2': 'duplicar'}
print(d3)

d4 = {x for x in range(5)}
print(d4) # SET

d5 = {f'chave_{x}': y**2 for x,y in enumerate(range(3,8))} # {'chave_0': 9, 'chave_1': 16, 'chave_2': 25, 'chave_3': 36, 'chave_4': 49}
print(d5)