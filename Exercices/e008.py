def saudacao(msg, nome):
    print(msg, nome)


saudacao('Olá,', 'Thata!')


def func(n1, n2, n3):
    soma = n1 + n2 + n3
    return soma


conta = func(7, 8, 9)
print(conta)


def porc(n1, n2):
    conta = n1+(n1*n2)
    return conta


valor = porc(8, 0.6)
print(valor)
