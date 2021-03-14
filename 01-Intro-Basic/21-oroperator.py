nome = input('Digite seu nome: ')

if nome:
    print(nome)
else:
    print('Voce precisa digitar seu nome!!')

nome = input('Digite seu nome: ')

# Exatamente o mesmo if anterior. Se nome true, exibe.. senao, manda a frase Voce precisa...
print(nome or 'Você precisa digitar seu nome!!') 


a = 0
b = None
c = False
d = []
e = {}
f = 28
g = 'Caio'

variavel = a or b or c or d or e or f or g
print(variavel) # Vai pegar o primeiro verdadeiro, no caso f = 28