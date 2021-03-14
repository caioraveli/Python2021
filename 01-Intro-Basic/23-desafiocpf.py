"""
CPF = 168.995.350-09
"""
cpf_ini='16899535009'
array1=[1,6,8,9,9,5,3,5,0]
dec=11
soma=0

for i in array1:
    dec -= 1 
    soma = soma + (i*dec)

#digit1 = 0 if ((11 - (soma %11) >9)) else (11 - (soma %11)) 
digit1 = (11 - (soma %11))
digit1 = 0 if digit1 > 9

array2=array1
array2.append(digit1)
dec2=12
soma2 = 0

for j in array2:
    dec2 -= 1
    soma2 = soma2 + (j* dec2)

digit2 = (11 - (soma2 %11))
digit2 = 0 if digit2 > 9 

array2.append(digit2)
cpf = ''.join(map(str,array2))

print(cpf or 'Cpf nao deu certo')