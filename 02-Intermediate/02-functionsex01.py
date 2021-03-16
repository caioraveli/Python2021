def soma(n1=0,n2=0,n3=0):
    return n1+n2+n3

print(soma(3,4,5))

def percent(n1=0,pc=100):
    if pc[-1] == '%':
        pc=int(pc[:-1])
    return n1+(n1*(pc/100))

print(percent(1232,'37%'))

def fizzMine(n=0):
    if n % 5 == 0 and n % 3 == 0:
        return f'fizzBuzzz - {n} é divisivel por 3 e por 5'
    if n %3 == 0:
        return f'fizz - {n} é divisivel por 3'
    if n %5 == 0:
        return f'buzzz - {n} é divisivel por 5'
    else:
        return f'{n} não é divisivel por 3 e nem por 5'

from random import randint
print(fizzMine(randint(0,100)))