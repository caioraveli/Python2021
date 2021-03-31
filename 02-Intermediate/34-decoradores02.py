# Decoradores pode ser utilizada para adicionar outras funcionalidades a função que será decorada
# Pode ser usada para verificar o tempo que a função decorada leva pra ser executada

from time import time,sleep

def velocidade(funcao):
    def interna(*args,**kwargs):
        start_time = time()
        resultado = funcao(*args,**kwargs)
        end_time = time()
        tempo = (end_time - start_time) * 1000
        print(f'A função {funcao.__name__} levou {tempo:.2f}ms para ser executada')
    return interna

@velocidade
def demora():
    for i in range(10000):
        print(i,end='')
    print()

demora()