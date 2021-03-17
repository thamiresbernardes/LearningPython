nome = input('Qual seu nome? ')
hora = input('Que horas são? ')


def funcao_que_executa(funcao_executada, *args, **kwargs):
    return funcao_executada(*args, **kwargs)


def saudacao(nome, hora):
    if not hora.isdigit():
        print(
            f'Olá {nome} você não digitou certifique'
            f'que tenha digitado números.'
        )
        return

    hora = int(hora)

    if hora <= 24 and hora > 18:
        msg = 'Boa noite'
        return f'{msg} {nome}'
    elif hora <= 18 and hora > 12:
        msg = 'Boa tarde'
        return f'{msg} {nome}'
    elif hora <= 12 and hora >= 0:
        msg = 'Bom dia'
        return f'{msg} {nome}'
    else:
        return 'Hora inválida.'


executa = funcao_que_executa(saudacao, nome, hora)
print(executa)
