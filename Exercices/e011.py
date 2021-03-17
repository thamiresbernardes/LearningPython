
def mestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)


def nome(name):
    return f'Olá, {name}'


def comp(name, saudacao):
    return f'{saudacao}, {name}'


exe = mestre(nome, 'Thamires')
exe1 = mestre(comp, 'Thamires', saudacao='Oin')
print(exe)
print(exe1)
