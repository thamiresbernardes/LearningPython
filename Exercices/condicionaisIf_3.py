print("Exercise one")
number_1 = int(input("Choose a number: "))
number_2 = int(input("Choose other number: "))
if number_1 >= number_2:
    print(f"The {number_1} is higher or equal to the { number_2}")
else:
    print(f"The {number_2} is higher or equal to the { number_1}")
print("======================================================")

print("Exercício 02")
hora = input('Entre com uma hora:')

if hora.isnumeric():
    hora = int(hora)
    if hora < 0 or hora >= 24:
        print("Horário deve estar entre 0 e 23!")
    else:
        if hora <= 11:
            print("Agora são {} horas. Bom dia!".format(hora))
        elif hora <= 17:
            print("Agora são {}horas. Boa tarde!".format(hora))
        else:
            print("Agora são {}horas. Boa noite!".format(hora))
else:
    print("Digite um horário válido!")

print("Exercício 03")
nome = input("Entre com seu nome:")
if len(nome) <= 4:
    print("Seu nome {}, é pqueno.".format(nome))
elif len(nome) > 6:
    print("Seu nome {}, é enorme.".format(nome))
else:
    print("Seu nome {}, é normal".format(nome))
