lista = [
    ['Item 1', 'Nacional', 12],
    ['Item 2', 'Nacional', 8],
    ['Item 3', 'Importado', 25],
    ['Item 4', 'Nacional', 35],
    ['Item 5', 'Importado', 26],
    ['Item 6', 'Importado', 36],
    ['Item 7', 'Nacional', 89],
    ['Item 8', 'Importado', 123],
    ['Item 9', 'Nacional', 1],
]

print(sorted(lista, key=lambda i: i[0]))
print('\n')
print(sorted(lista, key=lambda i: i[2], reverse=True))
print('\n')
print(sorted(lista, key=lambda i: i[1]))
