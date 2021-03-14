# :s - Texto (string)
# :d - Inteiros (int)
# :f - Float/ Ponto flutuante (float)
# :.(NUMERO)f - Quantidade de casas decimais (float)
# :(CARACTERE) (> ou < ou ^)(QUANTIDADE)(TIPO -s,d ou f)

num_1 = 10
num_2 = 3

divisao = num_1 /num_2

print(divisao)
print('{:.2f}'.format(divisao))
print(f'{divisao:.2f}')

nome = "Caio Raveli"
print(f'{nome:.2s}')
print(f'{num_2:0>10}') # IMPORTANTE.  VAI FICAR COM 10 CASAS.. 1 numero 3 + 9 zeros
print(f'{num_2:0<7}') # QUISER QUE FIQUE PRO OUTRO LADO
print(f'{num_2:5>9}')
print(f'{num_2:6^4}')

print(f'{num_2:.2f}') # FORMATANDO COMO FLOAT

print(f'{nome:#^36}')

print(f'{nome.lower()}')
print(f'{nome.upper()}')

nome = nome.split('a')
print(f'{nome}')