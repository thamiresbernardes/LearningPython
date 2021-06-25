def funcao():
    print("Esse é um exemplo de função!")
funcao()


def func(n1=7, n2=2):
    soma = n1 + n2
    return soma
def dumb():
    return func
var = dumb()
if var:
    print(var())
else:
    print('Digite algo!')