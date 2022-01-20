#contando letras de uma string
"""
Métodos dos dicionários:


"""


def count_string(palavra):
    palavra = str(palavra)
    dic = {}
    for letra in palavra:
        dic[letra] = dic.get(letra, 0) + 1
    print(dic)


palavra = input("Digite uma palavra: ")
check = count_string(palavra)
