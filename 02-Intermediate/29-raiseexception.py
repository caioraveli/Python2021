# Lançar minhas próprias exceções

def divide(n1,n2):
    try:
        return n1/ n2
    except ZeroDivisionError as error:
        print(error) # error = None 
        return False # posso mudar o retorno, no caso de None passou pra False
    except Exception:
        return f'Invalido'

# Supondo que um outro desenvolvedor queira fazer isso..

try:
    print(divide(2,0))
except:
    print('erro') # Podemos ver que mesmo com o erro acontecendo, ele nao passa pra esse excepet pois já está sendo tratado no try except da função

print()
print()

#### RAISE - Logar o que aconteceu dentro da função e relançar ela pra algum outro try/except que vem na frente.
# Serve para que outro dev ou eu mesmo possa capturar esta exceção que está dentro da função.

def divide(n1,n2):
    try:
        return n1/ n2
    except ZeroDivisionError as error:
        print('Log: ',error) # error = None 
        raise

try:
    print(divide(2,0))
except ZeroDivisionError as error:
    print(error)

### INFORMAR MINHA PROPRIA EXCEÇÃO


def divide(n1,n2):
    if n2 == 0:
        raise ValueError("N2 não pode ser 0.")
    return n1/n2

#print(divide(2,0)) # ValueError: N2 não pode ser 0

try:
    print(divide(2,0))
except ValueError as error:
    print(error) # Posso tratar da forma que eu quiser - BOA PRATICA, evitar mostrar mensagem técnica pra usuario!!!!
    print('Log: ',error) # melhor jogar em um arquivo de logs

