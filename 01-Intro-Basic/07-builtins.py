# isdigit, isnumeric or isdecimal. Só vão checar número positivo e sem ponto flutuante.
# Solução mais simples é fazer a própria função com condições para corrigir isto

num1 = input('Diite um numero: ')
num2 = input('Digite outro número: ')

#print(num1.isnumeric())
#rint(num2.isnumeric())

if num1.isdigit() and num2.isdigit():
    num1 = int(num1)
    num2 = int(num2)
    
    print(num1 + num2)

else:
    print('Não foi possívl calcular.')