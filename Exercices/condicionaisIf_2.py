print("Exercício 01")
num = input('Entre com um número inteiro:')

if num.isnumeric():
    num = int(num)
    if num // 2 == 0:
        print("O número {} é par.".format(num))
    else:
        print("O número {} é ímpar.".format(num))
else:
    print("O número não é um inteiro")

