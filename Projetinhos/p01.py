questions = {
    'Q1': {
        'question': 'Qual formato de magic você mais gosta?',
        'answer': {'a': 'Standard', 'b': 'Brawl', 'c': 'Commander', 'd': 'Modern', },
        'melhor': 'c',
    },
    'Q2': {
        'question': 'Você gosta de jogar no Arena ou Presencial?',
        'answer': {'a': 'Arena', 'b': 'Presencial', },
        'melhor': 'a',
    },
    'Q3': {
        'question': 'Já gastou na faixa de quanto?',
        'answer': {'a': 'Menos de 500 reais', 'b': 'Entre 500 e 1500', 'c': 'Mais de 1500 reais', },
        'melhor': 'b',
    },
}
print()
minhas = 0
for pk, pv in questions.items():
    print(f'{pk}: {pv["question"]}')

    print('Respostas:')
    for rk, rv in pv['answer'].items():
        print(f'[{rk}]: {rv}')

    usuario = input("Digite sua resposta: ")

    if usuario == pv['melhor']:
        print('Pensamos igual! que tal uma jogatina?')
        minhas += 1
    else:
        print('Legal, espero que encontre pessoas para jogar.')
    print()
