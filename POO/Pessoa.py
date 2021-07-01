from random import randint


class Pessoa:
    ano_atual = 2021

    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} já está comendo')
            return

        print(f'{self.nome} está comendo {alimento}.')
        self.comendo = True

    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} nao está comendo.')
            return

        print(f'{self.nome} parou de comer!')

    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome}, não pode falar comendo.')
            return

        print(f'{self.nome} está falandoo sobre {assunto}')
        self.falando = True

    def parar_falar(self):
        if not self.falando:
            print(f'{self.nome} nao está falandoo.')

        print(f'{self.nome} parou de falar!')
        self.falando = False

    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)

    @classmethod  # referente a classe
    def por_ano_nasc(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)

    @staticmethod  # não precisa de instancia nem de classe
    def gera_id():
        rand = randint(10000, 19999)
        return rand


p1 = Pessoa('Thamires', 32)
p2 = Pessoa('Ajani', 2)
p1.comer('palmito')
p2.falar('Varinha')
p1.falar('seriados')
p2.comer('ração')
p1.get_ano_nascimento()
print(Pessoa.gera_id())
