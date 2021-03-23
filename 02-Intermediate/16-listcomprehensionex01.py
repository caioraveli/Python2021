string = '0123456789012345678901234567890123456789012345678901234567890123456789'

l1 = [ string[n:n+10] for n,v in enumerate(string) if v == '0' ]

retorno = '.'.join(l1)

print(l1)
print(retorno)


### SOLUÇÃO DO PROFESSOR
n=10
lista = [string[i:i+n] for i in range(0,len(string),n)]
retorno = '.'.join(lista)

print(lista)
print(retorno)