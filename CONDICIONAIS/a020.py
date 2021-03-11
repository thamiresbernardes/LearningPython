#Condicionais
#Operadores relacionais
#== igualdade
#!= Diferença

nome = input('Entre com seu nome: ')
renda = float(input('Qual sua renda? '))
idade = int(input('Qual sua idade? '))
renda_m = 1000
if (2020 - idade) >= 18 and (renda >= renda_m):
    print('Olá {}, você pode pegar empréstimo.'.format(nome))
else:
    print('Olá {}, você NÃO pode pegar empréstimo.'.format(nome))

