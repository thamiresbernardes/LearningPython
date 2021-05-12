'''
count - cria um iterador
'''

from itertools import count, combinations, permutations, product

# para ser de trás pra frente, basta colocar o negativo no step
contador = count(start=1, step=3)

for n in contador:
    print(n)

    if n >= 35:
        break

pessoa = ['Camila', 'Celia', 'Thamires',
          'Juliana', 'Guilherme', 'Matheus', 'Fabio']
pessoa_1 = ['Camila', 'Celia', 'Thamires',
            'Juliana', 'Guilherme', 'Matheus', 'Fabio']
pessoa_2 = ['Camila', 'Celia', 'Thamires',
            'Juliana', 'Guilherme', 'Matheus', 'Fabio']

print("\n Combination")
for n in combinations(pessoa, 3):
    print(n)

print("\n Permutation")
for n in permutations(pessoa_1, 3):
    print(n)

print("\n Product")
for n in product(pessoa_2, repeat=2):
    print(n)
