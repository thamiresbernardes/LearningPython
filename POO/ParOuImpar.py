# Exercício que verifica se um número é par ou ímpar


def verifica_par(num):
    if num.isnumeric():  # verifica se é um número
        num = int(num)  # Transforma em inteiro
        if num % 2 == 0:
            print("O número {} é par.".format(num))
        else:
            print("O número {} é ímpar.".format(num))
    else:
        print("Você não digitou um número inteiro")


number = input("Digite um número: ")
verifica = verifica_par(number)
