"""
Zip = une iteráveis considerando os dados da menor lista
Zip_longest = intertools
"""
from itertools import zip_longest, count

citys = ['Uberlândia', 'Rio Verde', 'Uberaba',
         'São Paulo', 'Ribeirão Preto', 'Monte Belo']
states = ['MG', 'GO', 'MG', 'SP', 'SP']

city_states = zip(citys, states)
for valor in city_states:
    print(valor)

cidade_estado = zip_longest(citys, states)
for valor in cidade_estado:
    print(valor)
