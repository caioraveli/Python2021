nome = 'Caio Raveli'
idade = 28
altura = 1.77
peso = 107
imc = float(peso/(altura**2))
print('Nome %s, Idade: %d' % (nome,idade)) # PYTHON2
print('Nome {}, Idade: {}'.format(nome,idade))
print('Nome {1}, Idade: {0}'.format(nome,idade)) #PYTHON3
print('Nome {i}, Idade: {n}'.format(n=nome,i=idade)) #PYTHON3
print(f'Nome {nome}, Idade: {idade}') #PYTHON3 >= 3.6

print(f'{10/3:.2f}')
print(f'Nome: {nome}'
    f'\nIdade: {idade}'
    f'\nIMC: {imc:.2f}') #Duas casas decimais