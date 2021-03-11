usuario = input("Digite o seu usuário:")
qtde_carac = len(usuario)

if qtde_carac <6:
    print("Você precisa digitar pelo menos 6 caracteres")
else:
    print("Usuário cadastrado com sucesso.")
print(usuario, qtde_carac, type(qtde_carac))