# Mando uma lista, se eu ja tíver uma lista, eu uno as duas
def lista_de_clientes(clientes_iteravel,lista=[]):
    lista.extend(clientes_iteravel)
    return lista

cliente1 = lista_de_clientes(['Caio','Raveli','Freitas'])
clientes2 = lista_de_clientes(['Joao','Maria','Jose'])

print(cliente1)  # ['Caio', 'Raveli', 'Freitas', 'Joao', 'Maria', 'Jose']
print(clientes2) # ['Caio', 'Raveli', 'Freitas', 'Joao', 'Maria', 'Jose']

# Problema, sempre que eu to passando uma lista, ele atribui a lista=[] esses valores novos como lista padrao
# Assim, ao inves de eu ter um valor padrão de inicio, eu vou ter sempre lista[]+clientes_iteravel+clientes_iteravel+...
# Por ser mutavel, gera este problema..
clientes3 = lista_de_clientes(['Messi','Neymar'])

print(clientes3) # ['Caio', 'Raveli', 'Freitas', 'Joao', 'Maria', 'Jose', 'Messi', 'Neymar']
print(cliente1)  # ['Caio', 'Raveli', 'Freitas', 'Joao', 'Maria', 'Jose', 'Messi', 'Neymar']

# Pra resolver o problema...
# Não utilizar um parametro mutavel

def lista_de_clientes(clientes_iteravel,lista=None): 
    if lista is None: # So o none retornaria o erro NoneType
        lista = [] # Ao inves de ta sempre extendendo, eu zero a lista aqui pra ter listas diferentes
    lista.extend(clientes_iteravel)
    return lista

cliente1 = lista_de_clientes(['Caio','Raveli','Freitas'])
clientes2 = lista_de_clientes(['Joao','Maria','Jose'])

print(cliente1)  # ['Caio', 'Raveli', 'Freitas']
print(clientes2) # ['Joao', 'Maria', 'Jose']

clientes4 = lista_de_clientes([])
print(clientes4) # []