import math

PI = math.pi

def dobra_lista(lista):
    return [x*2 for x in lista]

def multiplica(lista):
    r = 1
    for i in lista:
        r *=i
    return r



# 2
# O código abaixo é sempre utilizado para que o que estiver debaixo do if só seja executado se eu tiver
# utilizando este arquivo diretamente. Serve de controle, se eu quiser fazer teste embaixo do if, quando
# alguem importar este módulo, o que foi feito embaixo do if não será importado la pois neste outro arquivo
# este módulo em questão não será __main__ e sim calculos

if __name__ == '__main__':
    lista = [1,2,3,4,5]
    print(dobra_lista(lista))
    print(multiplica(lista))
