# FUNÇÕES podem retornar praticamente qualquer coisa

def f(var):
    print(var)

def dumb():
    return f

var = dumb() # IMPORTANTE var agora é uma função - <class 'function'>
#print(type(var))

if var == f:
    print('São iguais!!')

# Passar argumento para uma função que está dentro de uma variável
var2 = dumb()('Var2 recebe f(). E aqui eu passo o var de f(var)')

# É o mesmo que ..

var3 = dumb()
var3('Mesma coisa')


def dumbb():
    return ('Caio','Raveli')

print(dumbb())

v1,v2 = dumbb()
print(v1)