# classmethod - métodos referente a classe e não a instância. 
# não utilizo self.. sim cls (convenção tb). Tenho que decorar com @classmethod
# Não precisa estar disponivel pras intâncias, e sim pra classe em si. No caso, Pessoa   
# repeti idade porque não estou usando self, logo só vai ser valido na função.
# Se usar o cls. posso usar atributo de classe.

# Em resumo, o método de classe é criado se ele for um método geral (da classe). Se for algo
# específico por instnacia, crio método de instância. Factory, fabricado de objeto


class Pessoa:
    ano_atual = 2021
    def __init__(self,nome,idade):
        self.name = nome
        self.age = idade

    def get_ano_nascimento(self):
        print(self.ano_atual - self.age)

    @classmethod
    def por_ano_nascimento(cls,nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome,idade) # como se tivesse execuando a classe Pessoa, igual na instancia p1 = Pessoa('Fulano',30)


p1 = Pessoa('Caio',28)
print(p1.age)
p1.get_ano_nascimento()
p2 = Pessoa.por_ano_nascimento('Raveli',1992)
p2.get_ano_nascimento()
print(p2.age)
