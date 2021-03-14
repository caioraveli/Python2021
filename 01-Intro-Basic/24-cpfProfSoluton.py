cpf_ini='16899535009'

cpf_novo = cpf_ini[:-2]
reverso = 11
total = 0
for index in range(19): # o range é de 0 - 18, modificando o index abaixo não impacta no loop
    if index >8:
        index -= 9
    reverso = reverso -1
    total = total + (int(cpf_novo[index]) * reverso)
    #print(index,cpf_novo[index],reverso, total)

    if (reverso <= 2):
        reverso = 12
        d = (11 - (total %11))
        d = 0 if d > 9 else d
        cpf_novo = cpf_novo + str(d)
        total = 0

if cpf_novo == cpf_ini:
    print("CPF válido!!")
else:
    print("CPF Inválido!!")