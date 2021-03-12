"""
AND, OR, NOT - and,or,not
IN e NOT IN

=> not é um inversor

"""
#nome = input('Qual o seu nome? ')
#idade = int(input('Qual sua idade? '))
nome = 'Caio Raveli'
a = 2
b = 3

if b > a and 'y':
    print('B é maior que A.')
else:
    print('A é maior que B.')

letras = 'aio'
if letras in nome:
    print(f'Existe {letras} em {nome}')
else:
    print(f'Não existe {letras} em {nome}')



