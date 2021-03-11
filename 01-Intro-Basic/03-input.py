nome = input("Qual o seu nome? ")
idade = input("Digite suda idade: ") # INPUT SEMPRE GRAVA COMO STRING

nascimeno = 2020 - int(idade)
print()

print(f"{nome} tem {idade} anos, pois nasceu no ano {nascimeno}")