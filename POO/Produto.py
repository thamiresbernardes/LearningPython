class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual/100))

# GETTER
    @property
    def preco(self):
        return self._preco

# SETTER
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$', ''))
        self._preco = valor


p1 = Produto('Camiseta', 152)
p1.desconto(5)
print(p1.preco)

p2 = Produto('Moletom', 'R$365')  # usando o getter e setter
p2.desconto(15)
print(p2.preco)
