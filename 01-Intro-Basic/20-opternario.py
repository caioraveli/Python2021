# Operador Ternário

logged_user = False

if logged_user:
    msg = 'Usuário logado.'
else:
    msg = 'Usuário precisa logar'

print(msg)
print()

logged_user = True

msg = 'Usuário logado.' if logged_user else 'Usuário precisa logar'
print(msg)

idade = input('Qual sua idade: ')

if not idade.isnumeric():
    print('Voce precisa digitar um numero!!!')
else:
    idade = int(idade)
    maior = (idade >= 18)
    msg = 'Pode entrar' if maior else 'Não pode entrar'
    print(msg)

