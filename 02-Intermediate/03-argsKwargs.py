# *args - empacota parametros (pode ser qualquer nome, por convenção usamos args)

def func(*args): # args é uma tupla, eu não consigo alterar
    print(args) # (1, 2, 3, 4, 5)
    print(args[0])
    print(args[1])
    print(len(args))
    # args[0] - 20 dá erro
    args = list(args) # posso transformar numa lista se houver necessidade de mudar os valores
    args[0] = 20
    print(args) # [20, 2, 3, 4, 5]

func(1,2,3,4,5)

# lembrando
lista = [1,2,3,4,5]
print(*lista) # o * desempacota a lista, valores individuais - 1 2 3 4 5
print(*lista,sep=',') # 1,2,3,4,5

def func2(*args):
    print(args)

func2(lista) # Podemos ver que toda a lista virou o primeiro indice da tupla - ([1, 2, 3, 4, 5],)

# Se eu quiser que cada indice da lista torne-se um unuco indice na tupla, basta enviar a lista
# desempacotada.

func2(*lista) # (1, 2, 3, 4, 5)
func2(*lista, 6,7,8,9) # cada elemento que eu enviar agora posteriormente serão indices diferentes também

lista2=['Caio','Raveli','Freitas','Barbosa']

func2(*lista,*lista2) # (1, 2, 3, 4, 5, 'Caio', 'Raveli', 'Freitas', 'Barbosa')


########## KWARGS #### 
# Usando somente o *args, se eu passar um argumento nomeado vai dar erro
# Usando **kwargs, não dá erro mais.. porém, podemos ver que os parametros nomeados não estão no args

def func3(*args,**kwargs):
    print(args)

func3(1,2,3,nome='Caio',sobrenome='Raveli') # (1, 2, 3) - args não tem os parametros nomeados


def func4(*args,**kwargs):
    print(args)
    print(kwargs) # {'nome': 'Caio', 'sobrenome': 'Raveli'}
    print(kwargs['nome'],kwargs['sobrenome']) # Caio Raveli - basta passar o nome do parametro pra acessar indiviualmente

    nome = kwargs.get('nome')
    idade = kwargs.get('idade')
    
    if idade is not None:
        print(idade) # printa idade 

func4(1,2,3,nome='Caio',sobrenome='Raveli') 
func4(1,2,3,nome='Caio',sobrenome='Raveli',idade=30)

def func5(*args,**kwargs):
    print(kwargs['idade']) # se a chave usada não for passada na função, um erro ocorre. Melhor usar .get se não tiver certeza que existe.

func5(nome='Caio')
