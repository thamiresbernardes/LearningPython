from random import randint


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


def verifica(n1):
    if n1 % 3 == 0 and n1 % 5 == 0:
        return f'FizzBuzz: {n1} é divisível por 3 e por 5'
    if n1 % 3 == 0:
        return f'Fizz: : {n1} é divisível por 3'
    if n1 % 5 == 0:
        return f'Buzz: {n1} é divisível por 5'
    return f'{n1} não é divísivel por 3 nem por 5'


for i in range(100):
    aleatorio = randint(0, 100)
    print(verifica(aleatorio))
