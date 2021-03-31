from pessoa import Pessoa

# Dois objetos diferentes vindos (instanciados) da mesma classe
#p1 = Pessoa()
#p2 = Pessoa()

#p1.nome = 'Caio' # atributo da pessoa 1 - variavel de instância
#p2.nome = 'Raveli'
#print(nome) # erro
#print(p2.nome) # erro
#print(p1.nome) # Caio
#print(p2.nome) # Raveli

#p1.falar() # Pessoa está falando

p1 = Pessoa('Caio',28)
p1.name = 'Raveli'

print(p1.name)
p1.outro_metodo()
p1.terceira()



p1.comer('Maçã') # Raveli está comendo Maçã!!
p1.comer('Maçã') # Raveli já está comendo.
p1.parar_comer() # Raveli parou de comer!!
p1.parar_comer() # Raveli não está comendo!
p1.falar('POO') # Raveli falando sobre POO
p1.comer('Laranja') # Raveli não pode comer falando!!
p1.parar_comer() # Raveli não está comendo!
p1.falar('qualquer assunto novamente') # Raveli já está falando!
p1.comer('arroz') # Raveli não pode comer falando!!
p1.parar_falar() # Raveli parou de falar!!
p1.comer('arroz') # Raveli está comendo arroz!!

print(p1.ano_atual) # 2021 - Imprimindo variavel da classe
print(Pessoa.ano_atual) # 2021 - inclusive a classe em si

print(p1.get_ano_nascimento()) # 1993 - baseado so no ano
