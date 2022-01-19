# Operadores relacionais
# == igualdade
# != Diferença

# SIMULA EMPRESTIMO


def emprestimo(nome, renda, anonascimento, anoatual=2021, renda_m=1000):
    if (anoatual - anonascimento) >= 18 and (renda >= renda_m):
        print('Olá {}, você pode pegar empréstimo.'.format(nome))
    else:
        print('Olá {}, você NÃO pode pegar empréstimo.'.format(nome))


renda_p1 = float(input("Entre com a renda mensal: "))
idade_p1 = int(input("Entre com seu ano de nasicmento: "))
nome_p1 = input("Entre com seu nome: ")
situacao_emprestimo = emprestimo(nome_p1, renda_p1, idade_p1)
