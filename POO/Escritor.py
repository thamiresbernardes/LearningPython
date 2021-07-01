# Associação

class Escritor:
    def __init__(self, nome):
        self.__nome = nome  # Por convenção em classes  privadasm usamos '_' antes do nome
        self.__ferramenta = None

    @property
    def nome(self):
        return self.__nome

    @property
    def ferramenta(self):
        return self.__ferramenta

    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self.__ferramenta = ferramenta


class Caneta:
    def __init__(self, marca):
        self.__marca = marca

    @property
    def marca(self):
        return self.__marca

    def escrever(self):
        print('Caneta está escrevendo ...')


class MaquinaDeEscrever:
    def escrever(self):
        print('Maquina está digitando ...')


# Fazendo as classes se associarem

escritor = Escritor('Thamires')
caneta = Caneta('Bic')
maquina = MaquinaDeEscrever()
print(escritor.nome)
print(caneta.marca)
maquina.escrever

escritor.ferramenta = caneta
escritor.ferramenta.escrever()
