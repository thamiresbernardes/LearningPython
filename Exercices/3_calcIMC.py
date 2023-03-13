def calculo(peso, altura, ano_nascimento, anoatual=2023):
    peso = peso
    altura = altura
    ano_nascimento = ano_nascimento
    imc = peso / pow(altura, 2)
    idade = anoatual - ano_nascimento
    return print(f"Olá, sua idade é {idade} e seu IMC é {imc:.2f}!")


u1 = calculo(61.8, 1.67, 1989)
