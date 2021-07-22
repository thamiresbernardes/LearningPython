"""
HERANÇAS:
    Animal -> respirar
        Lobo(Animal) -> respirar / uivar
        Cachorro(Lobo) -> respirar / uivar / latir
"""
# Heranças Multiplas

class A:
    def falar(self):
        print("Estou falando em A!")


class B(A):
    def falar(self):
        print("Estou falando em B!")


class C(A):
    def falar(self):
        print("Estou falando em C!")


class D(C, B):
    pass


d = D()
d.falar()
