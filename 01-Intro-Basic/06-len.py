# Não funciona com tipos numéricos nem booleano.
# Sempre retorna inteiro.
# Espaço também conta

usuario = input('Digite seu usário: ')
qtd_char = len(usuario)

print(usuario,qtd_char,type(qtd_char))

if qtd_char < 6:
    print('Precisa digitar pelo menos 6 caracteres')
else:
    print(f'{usuario} cadastrado no sistema. Digitado {len(usuario)} caracteres')