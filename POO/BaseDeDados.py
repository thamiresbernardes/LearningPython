"""
public
protected : _ (um underline)
private: __ (dois underlines)
"""


class BaseDeDados:

    def __init__(self):
        self.dados = {}

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.dados:
            self.dados['clientes'] = {id: nome}
        else:
            self.dados['clientes'].update({id: nome})

    def lista_clientes(self):
        for id, nome in self.dados['clientes'].items():
            print(id, nome)

    def apaga_cliente(self, id):
        del self.dados['clientes'][id]


bd = BaseDeDados()
bd.inserir_cliente(1, 'Thamires')
bd.inserir_cliente(2, 'Celia')
bd.inserir_cliente(3, 'João')
bd.inserir_cliente(4, 'Ajani')
bd.lista_clientes
bd.apaga_cliente(2)
bd.lista_clientes

print(bd.dados)
