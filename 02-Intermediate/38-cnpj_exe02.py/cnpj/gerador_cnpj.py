import cnpj
from random import randint


def gera():
    primeiro_digito = randint(0,9)
    segundo_digito = randint(0,9)
    segundo_bloco = randint(100,999)
    terceiro_bloco = randint(100,999)
    quarto_bloco = '0001'
    penultimo_digito = randint(0,9)
    ultimo_digito = randint(0,9)

    inicio_cnpj = f'{primeiro_digito}{segundo_digito}{segundo_bloco}{terceiro_bloco}{quarto_bloco}{penultimo_digito}{ultimo_digito}'
    return inicio_cnpj

if __name__ == '__main__':
    new_cnpj = gera()
    
    