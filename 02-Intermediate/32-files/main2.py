# https://docs.python.org/3.8/library/functions.html

file = open('teste.txt','w+')

file.write('Linha 1\n')
file.write('Linha 2\n')
file.write('Linha 3\n')

# Seek - Manipulo a posição do cursor. Digo onde (0,0) eu digo pra ir pro inicio do stream (topo do arquivo)
file.seek(0,0) 

print('Lendo linhas:')
print(file.read())

print('####################')

file.seek(0,0) # Volto novamente pro inicio do arquivo

print(file.readline(), end='') # Curso vai ate o fim da linha
print(file.readline(),end='') # Cursor vem do fim da linha anterior ate o fim da linha desta

file.seek(0,0)

print(file.readlines()) # Joga cada linha em uma posição de uma lista

file.seek(0,0)
for linha in file.readlines():
    print(linha)

file.seek(0,0)

for l in file: # É a mesma coisa do readlines
    print(l)


file.close()

