# Sempre inicia classe com letra Maiúscula

# SELF - quando criamos um objeto estamos utilizando um molde (classe). Sempre que eu chamo um objeto
# ou executo uma ação, o python vai chamar a classe para saber o que quero fazer dentro dol molde. Porém,
# a classe precisa saber qual instância está chamando-a, senão todas as instâncias terão os mesmos valores.
# Quando a gente cria uma classe, a gente automaticamente a gente está falando que estamos criando uma
# instância dessa classe (no nosso caso, p1 por exemplo). Então, a palavra self refere-se a essa instância
# que foi criada. Ex: se eu fizer, p2.falar() é como se eu tivesse fazendo p2.falar(p2). No momento, todo
# e qualquer método criado devemos passar o parâmetro self (pode ser qualquer nome, poŕem por padrão usamos self)
# Não precisamos enviar o parametro self quando formos instanciar um objeto

# Se eu quiser modificar o nome de uma das variáveis que foram passados no método, tenho que fazer
# self.qualquer_variavel = PARAMETRO. Ex: self.name = nome. Ai no objeto eu consigo fazer p1.name = 'Raveli'

# Com o self eu faço com que a variável de um método esteja disponível em todos os outros métodos.

# __init__ -> digo que cada instância vai ter seus próprios atributos e métodos. Ex: no nosso caso, vamos
# dizer que cada pessoa terá seu proprio nome, idade, etc. Em resumo, passar meus próprios parametros
# pro método da classe.

# Variável da classe - normalmente utilizada quando ela serve pra todo mundo. Ex: ano_atual

from datetime import datetime

class Pessoa:
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))
    def __init__(self, nome, idade, comendo=False, falando=False):
        self.name = nome
        self.age = idade
        self.eating = comendo
        self.speaking = falando

        # Posso criar uma variável sem a palavra self.. porém ela só é valida dentro do __init__
        # Porém, sempre que instancio um objeto o __init__ é executa, então no caso vai printa 'Valor'
        # assim que crio o objeto
        # Não tenho acesso a ela em outros métodos dentro da própria classe
        variavel = 'Valor'
        print(variavel)

    def outro_metodo(self):
        print(self.name)
        self.xau = 'Xau'

    def terceira(self):
        print(self.xau)

    def falar(self,assunto): #  # pra usar 'assunto' não precisa do self. Pois já é implicito no python
        if self.eating:
            print(f'{self.name} não pode falar comendo!!')
            return

        if self.speaking:
            print(f'{self.name} já está falando!')
            return

        print(f'{self.name} falando sobre {assunto} ')
        self.speaking = True

    def parar_falar(self):
        if not self.speaking:
            print(f'{self.name} não está falando!!')
            return

        print(f'{self.name} parou de falar!!')
        self.speaking = False

    def comer(self, alimento): # pra usar 'alimento' não precisa do self. Pois já é implicito no python
        if self.eating:
            print(f'{self.name} já está comendo.')
            return

        if self.speaking:
            print(f'{self.name} não pode comer falando!!')
            return
        print(f'{self.name} está comendo {alimento}!!') 
        self.eating = True

    def parar_comer(self):
        if not self.eating:
            print(f'{self.name} não está comendo!')
            return
        print(f'{self.name} parou de comer!!')
        self.eating = False

    def get_ano_nascimento(self):
        return self.ano_atual - self.age