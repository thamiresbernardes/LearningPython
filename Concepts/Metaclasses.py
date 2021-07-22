# Em Python tudo é um objeto: isso inclui classes , e metaclasses (que são classes, que criam classes)


class Meta(type):
    def __new__(mcs, name, bases, namespace):
        if name == "A":
            return type.__new__(mcs, name, bases, namespace)

        if "b_fala" not in namespace:
            print(f"Método b_fala não criado em {name}")
        else:
            if not callable(namespace["b_fala"]):
                print(f"b_fala precisa ser um método em {name}")
        return type.__new__(mcs, name, bases, namespace)


class A(metaclass=Meta):
    def fala(self):
        self.b_fala()


class B(A):
    teste = "valor"

    def b_fala(self):
        print("Falando")

    def outro(self):
        pass
