# Agregação -- uma classe depende da outra (Aqui Carrinho precisa de produto)

class CarrindoDeCompra:
    def __init__(self):
        self.produtos = []

    def inserir_produto(self, produto):
        self.produtos.append(produto)

    def lista_produto(self):
        for produto in self.produtos:
            print(produto.nome, produto.valor)

    def soma_total(self):
        total = 0
        for produto in self.produtos:
            total += produto.valor
        return total


class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor


carrinho = CarrindoDeCompra()

p1 = Produto('Teste', 1)
p2 = Produto('Blusdifri', 120.3)
p3 = Produto('Meia', 55)

carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p3)
carrinho.lista_produto()

print(carrinho.soma_total())
