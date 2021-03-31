# Master e slave é só pra ilustar que uma está dentro de outra.. pode ser qualquer nome

def fala_oi():
    print('Oi')

variavel = fala_oi # Variavel fica igual a função

variavel() # fala_oi . Class function


def master():
    def slave(): # So isso nao vai fazer nada.. pois neste ponto a função slave está somente sendo criada
        print('Oi')
    slave() # Aqui executo a função

master() # agora printa oi

def master():
    def slave():
        print('OI')
    return slave

variavel = master() # Praticamente estou dizendo que variavel = slave (retorno de master)
variavel()
print()
# print dentro de slave é uma função.. então, eu posso criar minha propria função e chamar no mesmo lugar

def master(funcao_qualquer): #função master está decorando função_qualquer
    def slave():
        print('Função decorada')
        funcao_qualquer()
    return slave

def fala_ola():
    print('Olá')

fala_ola = master(fala_ola) # Executando a função fala_ola de forma decorada. fala_ola torna-se escrava de master
fala_ola()

fala_ola() #Imprime também a função decorada. Se eu comentar a linha 37 ele executa direto agora
print()

########### FORMA CORRETA ###########

def master(funcao_qualquer): #função master está decorando função_qualquer
    def slave():
        print('Função decorada da forma certa')
        funcao_qualquer()
    return slave

@master   # Estou deocrando com a função master. Pode ser feito com qualquer função
def fala_ola():
    print('Ola fulano')
    print()

fala_ola()

## USANDO PARAMETROS


def master(funcao_qualquer): #função master está decorando função_qualquer
    def slave(*args,**kwargs): #Praticamente so repassando o que receber para a função na linha 64
        print('Função decorada da forma certa')
        funcao_qualquer(*args,**kwargs)
    return slave

#DECORANDO
@master
def outra_funcao(msg):
    print(msg)
    print()

outra_funcao('Ola, função decorada. Eu sou o caio')