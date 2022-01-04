class IMC:
   
def calculo(peso, altura, ano_nascimento, anoatual=2021):
    peso = peso
    altura = altura
    ano_nascimento = ano_nascimento
    imc = peso / pow(altura, 2)
    idade = anoatual - ano_nascimento
    return print(f"Olá, sua idade é {idade} e seu IMC é {imc:.2f}!")


u1 = calculo(61.8, 1.67, 1989)


# print('Exercício teste')
# nome = str(input("Qual seu nome?"))
# idade = int(input('Qual sua idade:'))
# altura = float(input('Qual sua altura?'))
# peso = float(input('E seu peso?'))
# anoa = int(input('Entre com o ano atual'))
# nasc = anoa - idade
# imc = peso / pow(altura, 2)
# print(
#     'Olá {}! Seu ano de nascimento é {}, logo você já tem incríveis {} anos vividos. '
#     '\nSua altura é {} e seu peso {}, com essas informações calculamos o seu imc, que é {:.2f}.'
#     .format(nome, nasc, idade, altura, peso, imc))
