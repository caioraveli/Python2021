secreto = 'Raveli'
digitadas = []

while True:
    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print("Você deve digitar apenas uma letra... ")
        continue

    digitadas.append(letra)
    if letra in secreto:        
        print(f'Letra {letra} está na palavra secreta')
        print(digitadas)
    else:
        print(f'Letra {letra} não está na palavra secreta')
        digitadas.pop()
    
    secreto_temp = ''
    for i in secreto:
        if i in digitadas:
            secreto_temp+=i
        else:
            secreto_temp+='*'
    print(secreto_temp)

    if secreto_temp == secreto:
        print("VOCE GANHOU!!!")
        break
