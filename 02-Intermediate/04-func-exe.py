def ola_mundo():
    return 'Olá mundo!'

def mestre(funcao):
    return funcao()

executando = mestre(ola_mundo)
print(executando)


# args e kwargs no caso abaixo ajudam a remover o erro de quantidade faltando de parametros. 
# Recebo em mestre os parametros função e qualquer coisa pelo args e kwargs
# Quando retorno em mestre a função com os parametros args e kwargs, eu consigo trabalhar com qualquer
# quantidade de parametros (QUE LEGAL). 
# Em resumo, nesse caso, com o args ou kwargs eu posso eu nao receber alguma coisa.
# O args e o kwargs me dá possibilidade de passar uma função com um parametro (fala_oi) ou dois parametros
# (saudacao) sem ter que alterar a função mestre. Obvio, quem controla são as funções que passo pra mestre.
# Com isto, mesmo usando mestre(fala_oi) só vai dar certo se eu passar um argumento pra fala_oi. A função 
# mestre recebe a função e o argumento e desce pro return. Por isso posso fazer mestre(fala_oi,'Caio').
def mestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)

def fala_oi(nome):
    return f'Oi {nome}'

def saudacao(nome,saudacao):
    return f'{saudacao} {nome}'

# Logo, quando eu posso usar mestre com duas outras funções
executando = mestre(fala_oi,'Caio')
print(executando)

teste = mestre(saudacao,'Caio','Ola')
print(teste)