def funcao():
    print('Aprendendo sobre funções!')


funcao()


def fraseMotivacional(msg):
    msg = msg.replace('e', '3')  # troca os caracteres
    return msg


x = fraseMotivacional(
    "Somos o que repetidamente fazemos.Portanto a existência não é umfeito, é um hábito")
print(x)


def teste(a, b, c, d=None):
    print(a, b, c, d)
    return a, b, c, d


y = teste(1, 2, 4, d="Ola")
print(y)
print(y[1], y[3])


def naoSei(*args, **kwargs):
    idade = kwargs.get('idade')  # usa get quando não sei se a chave existe
    return args, kwargs


z = naoSei('quantos', 'eu', 'quiser', idade=25)
print(z)

t = 'valorQualquer'


def func():
    return (t)


print(t)
