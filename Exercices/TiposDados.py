# Tipos de dados

print("Thamires", type("Thamires"))
print(30, type(30))
print(12.58, type(12.58))
print(10 == 10, type(10 == 10))

# Exercício aula

print("Exercícios aula")
print('Thamires', type("Thamires"))
print(int(30), type(30))
print(float(1.68), type(1.68))
print(bool(30 > 18), type(30 > 18))

print('\n Exercício IMC')
nome = str(input('Entre com seu nome:'))
idade = int(input("Qual sua idade?"))
altura = float(input('Qual sua altura?'))
peso = float(input('Qual seu peso? '))
imc = (peso / (pow(altura, 2)))
print('Olá {}. Você tem {} anos e seu imc é {:.2f}!'.format(nome, idade, imc))
