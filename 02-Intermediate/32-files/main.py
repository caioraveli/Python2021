# Com with não preciso fechar, ele se encarrega disso
# Modos -> w+ tenho leitura e escrita - ele apaga tudo do arquivo e escreve de novo
# r -> abre para somente leitura
# a+ -> escreve no arquivo sem apagar.. append
with open('teste2.txt','a+') as file:
    file.write('Fazeno apppend\n')
    file.write('Linha 1\n')
    file.write('Linha 2\n')
    file.write('Linha 3 \n')
    file.seek(0)
    for l in file.readlines():
        print(l)


# COM JSON

import json

d1 = {
    'Pessoa 1': {
        'nome': 'Caio',
        'idade': 28,
    },
    'Pessoa 2': {
        'nome': 'Raveli',
        'idade': 29,
    },
}

d1_json = json.dumps(d1, indent=True) # dumps -> converte dict para json

with open('teste3.json','w+') as file:
    file.write(d1_json)