# continue -> qnd achar a palavra continue, pula pro próximo passo do laço
# break -> termina o loop

x = 0

while x < 5:
    if x==3:
        x=x+1
        continue
        print('Alguma coisa') #Provar que ele nao executa depois do continue
    print(x)
    x = x+1
print('Acabou')
print()

x=0
while x < 5:
    if x==3:
        x+=1
        break

    print(x)
    x=x+1
print('Acabou de novo')