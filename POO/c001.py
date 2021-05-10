class Poligono:
    def __init__(self, n_lados):
        self.n = n_lados
        self.lados = [0 for i in range(n_lados)]

    def le_lados(self):
        self.lados = [float(input("Digite o tamanho do lado" + str(i+1)))
                      for i in range(self.n)]

    def mostra_lados(self):
        for i in range(self.n):
            print("Lado", i+1, "tem comprimento", self.lados[i])


class Triangulo(Poligono):
    def __init__(self):
        Poligono.__init__(self, 3)

    def area(self):
        a, b, c = self.lados
        s = (a+b+c)/2
        area = (s*(s-a)*(s-b)((s-c))) ** 0.5
        print("A área do triângulo é %0.2f" % area)


pent = Poligono(5)
pent.le_lados()
pent.mostra_lados()
