"""
Split: dividir uma string;
Join: juntar uma lista;
Enumerate: enumerar elementos.
"""
string = "Brasil é o país do futebol, o Brasil é penta"
print(len(string))
# entre as aspas vai o caracter padrão usado para fazer a divisão.
lista = string.split(',')
lista1 = string.split(' ')
print(lista, lista1)

string_1 = 'O Brasil é penta.'
lista2 = string_1.split(' ')
string_2 = '|'.join(lista2)
print(string_2)

for indice, valor in enumerate(lista2):
    print(indice, valor)
