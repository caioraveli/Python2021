import re
from random import randint


def remove_caracaterers(cnpj):
    return re.sub(r'[^0-9]','',cnpj)

 
def somatorio(cnpj):
    start = 5
    acum = 0
    for i in range(25):
        if i < 12:
            acum = (start * int(cnpj[i])) + acum
            start -= 1
            if start < 2 and i < 11:
                start = 9
                continue
            continue
        elif i == 12 and start < 2:
            digit = formula(acum)
            cnpj = cnpj+str(digit)
            acum = 0 
            start = 6
            acum = (start * int(cnpj[i-12])) + acum
            start -= 1
            continue
        else:
            acum = (start * int(cnpj[i-12])) + acum
            start -= 1
            if start < 2:
                start = 9
                continue
            continue
    digit = formula(acum)
    cnpj = cnpj+str(digit)
    return cnpj


def formula(valor):
    aplica = (11 - (valor % 11))
    res = 0 if aplica > 9 else aplica
    return res


def refaz_cnpj(cnpj):
    refeito = [ x for x in cnpj ]
    refeito.insert(2,'.')
    refeito.insert(6,'.')
    refeito.insert(10,'/')
    refeito.insert(15,'-')
    cnpj = ''.join(refeito)
    return cnpj
    
    
# Função necessária pois o algoritmo valida todas as sequencias.. Ex: 11111111111, 22222222222. Logo,
# se for sequencia, vai retornar True e onde a função for chamada vai tratar
def sequencia(cnpj):
    sequencia = cnpj[0] * len(cnpj)
    if sequencia == cnpj:
        return True
    else:
        False


def valida(cnpj):
    try:
        number = remove_caracaterers(cnpj)
        if sequencia(number):
            return f'{cnpj} é uma sequência!! Não pode!\n'
    except:
        return f'{cnpj} sintaxe errada. Verique o formato/sintaxe e tente novamente'
    number = number[:-2]
    try:
        new = somatorio(number)
        new = refaz_cnpj(new)
        if cnpj == new:
            return f'{new} - CNPJ VALIDADO COM SUCESSO!!!!'
        else:
            return f'{new} difere do {cnpj}'
    except Exception as e:
        return f'{cnpj} sintaxe errada. Verique o formato/sintaxe e tente novamente'


def gera():
    primeiro_digito = randint(0,9)
    segundo_digito = randint(0,9)
    segundo_bloco = randint(100,999)
    terceiro_bloco = randint(100,999)
    quarto_bloco = '0001'
    penultimo_digito = randint(0,9)
    ultimo_digito = randint(0,9)

    #inicio_cnpj = f'{primeiro_digito}{segundo_digito}{segundo_bloco}{terceiro_bloco}{quarto_bloco}{penultimo_digito}{ultimo_digito}'
    inicio_cnpj = f'{primeiro_digito}{segundo_digito}{segundo_bloco}{terceiro_bloco}{quarto_bloco}00'
    return inicio_cnpj


if __name__ == '__main__':
    ##print(valida('12.544.992/0001-03'))
    new_cnpj = gera()
    new_cnpj = refaz_cnpj(new_cnpj)
    print(new_cnpj)
    print(valida(new_cnpj))
    print(valida('15.769.667/0001-03'))
    print(valida('71.394.209/0001-25'))
