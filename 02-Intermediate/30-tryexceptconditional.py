# https://docs.python.org/3/library/exceptions.html

def converte_numer(num): # Com esta função, sempre que nao for int ou float vai retornar NoneType
    try:
        num = int(num)
        return num
    except ValueError as erro:
        try:
            num = float(num)
            return num
        except:
            pass
       # print('Precisa digitar um numero', erro)


while True:
    n = converte_numer(input('Digite um numero: '))
    if n is None:  # Logo, só chamar a função anterior e se Não for None, calcula.. se nao, printa erro
        print("Isso não é numero")
    else:
        print(n * 5)     