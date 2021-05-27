from itertools import groupby

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'amanda', 'nota': 'C'},
    {'nome': 'Carlos', 'nota': 'A'},
    {'nome': 'Breno', 'nota': 'B'},
    {'nome': 'Celia', 'nota': 'A'},
    {'nome': 'Thamires', 'nota': 'B'},
    {'nome': 'Camila', 'nota': 'A'},
]  # lista contendo vários dicionários

# como ordenar a lista então?


def ordena(item): return item['nota']  # cria uma função pra ordenar


# alunos.sort(key=lambda item: item['nota'])
alunos.sort(key=ordena)
for aluno in alunos:
    print(aluno)

# usando groupby
alunos_agrupados = groupby(alunos, ordena)
for agrupamento, valor_agrupados in alunos_agrupados:
    print(f'Agrupamento: {agrupamento}')
    for aluno in valor_agrupados:
        print(aluno)
    print()
