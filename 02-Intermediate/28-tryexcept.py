# Tratamento de exceções. Exceções são erros no programa e o erro vai travar o programa
# Vou executar o que tá no bloco try.. se ocorrer erro, cai pro bloco except e trato do jeito que quiser

# FORMA MAIS SIMPLES - MAS NÃO É UMA BOA PRATICA
try:
    print(a)
except:
    print('Erro')

# MELHORANDO.. Pegar o erro retornado na execução do programa e passar no except
# Podemos criar arquivo de log com data e hora do erro.. Mandar mensagem pro usuário (se for o caso)


#print(a) -> Erro aqui é o NameError
print()
try:
    print(a)
except NameError as erro: # jogar o erro na variável erro
    print(erro) # name 'a' is not defined
    print('Erro do desenvovledoro')
except Exception as erro: # VAI CAPTURAR QUALQUER TIPO D ERRO NO BLOCK TRY, POIS NÃO ESTOU ESPECIFICANDO A EXCEÇÃO QUE QUERO
    print('Ocorreu um erro inesperado')

# O código vai continuar se ocorrer a exceção... Não vai parar por conta do erro
print('Bota continuar...')


try:
    a = []
    print(a[1])
except IndexError as erro:
    print('Erro de indice') # tratando um erro que eu ja conhecia. Erro esperado
except Exception as erro:
    print('FUMO')

# Mais de uma exceção na mesma exceção
try:
    a = {}
    print(a[1])
except (IndexError,KeyError) as erro:
    print('Erro de KEY') # tratando um erro que eu ja conhecia. Erro esperado
except Exception as erro:
    print('FUMO')

# COM ELSE

try:
    a = {}
    print(a)
except NameError as erro:
    print('Erro de Nome')
except (IndexError,KeyError) as erro:
    print('Erro de KEY') # tratando um erro que eu ja conhecia. Erro esperado
except Exception as erro:
    print('FUMO')
else:
    print('Seu código foi executado com sucesso!')


# COM FINALLY - > Diferente do else, o finally vai ser executado SEMPRE. Pode ser bem útil por exemplo
# pra fechar um arquivo que foi aberto dentro de qualquer uma das cláusulas do bloco try, ou 
# conexões pra base de dados, etc.. 

try:
    a = 1/0
    print(a)
except NameError as erro:
    print('Erro de Nome')
except (IndexError,KeyError) as erro:
    print('Erro de KEY') # tratando um erro que eu ja conhecia. Erro esperado
except Exception as erro:
    print('FUMO')
else:
    print('Seu código foi executado com sucesso!')
finally: 
    print('Finalmente...') # NO TRY ou em qualquer EXCEPT o FINALLY sempre será executado 

print('Bora continuar ....')

# OUTRA BOA UTILIDADE DO FINALLY ... ATRIBIR VALOR PADRÃO PARA ALGUMA VARIAVEL

try:
    a = 1/0
    print(a)
except NameError as erro:
    print('Erro de Nome')
except (IndexError,KeyError) as erro:
    print('Erro de KEY') # tratando um erro que eu ja conhecia. Erro esperado
except Exception as erro:
    print('FUMO')
else:
    pass
finally: 
    a= None # ou a = ''

print(a) # printou None
print('Bora continuar ....')

print()
print()
print()

# TRY/ EXCEPT DENTRO DE TRY/EXCEPT

try:
    a = 0
    try: # EVITA que esse erro se propague pra dentro do bloco TRY MAIOR
        a = 1/0
    except:
        print('Erro') 
except NameError as erro:
    print('Erro de Nome')
except (IndexError,KeyError) as erro:
    print('Erro de KEY') # tratando um erro que eu ja conhecia. Erro esperado
except Exception as erro:
    print('FUMO')
else:
    pass
finally: 
    a= None # ou a = ''

print(a) # printou None
print('Bora continuar ....')