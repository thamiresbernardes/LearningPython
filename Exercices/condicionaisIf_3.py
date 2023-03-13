def checando_inteiros(numero, hora, nome):
    numero = int(numero)
    if numero % 2 == 0:
        print(f'O número {numero} é um {type(numero)} e é par!')
    else:
        print(f'O número {numero} é um {type(numero)} e é ímpar!')    
    hora = int(hora)
    if (hora > 0 and hora <= 24):
        print("Horário deve estar entre 0 e 23!")
        if hora <= 11:
            print("Agora são {} horas. Bom dia!".format(hora))
        elif hora <= 17:
            print("Agora são {} horas. Boa tarde!".format(hora))
        else:
            print("Agora são {} horas. Boa noite!".format(hora))
    else:
        print("Digite um horário válido!")
    if len(nome) <= 4:
        print("Seu nome {}, é pqueno.".format(nome))
    elif len(nome) > 6:
        print("Seu nome {}, é enorme.".format(nome))
    else:
        print("Seu nome {}, é normal".format(nome))

user_1 = checando_inteiros(24, -6,'thamires')

