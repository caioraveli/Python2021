print("Calculadora simples!!")

exit = 'n'
while exit == 'n':
    num_1 = input('Digite primeiro numero: ')
    num_2 = input('Digite segundo numero: ')
    op = input('Digite o operador: ')
    
    if not num_1.isnumeric() or not num_2.isnumeric():
        print('Você precisa digitar um número!!')
    else:
        num_1 = int(num_1)
        num_2 = int(num_2)
        if op == '+':
            print(f'Resultado: {num_1 + num_2}')
        elif op == '-':
            print(f'Resultado: {num_1 - num_2}')
        elif op == '*':
            print(f'Resultado: {num_1 * num_2}')
        elif op == '/':
            print(f'Resultado: {num_1 /num_2}')
        else:
            print(f'Não foi possível efetuar o cálculo')
    exit = input('Deseja sair? [s]im ou [n]ão: ')
    if exit == 's':
        print('Até mais ....')
        break
