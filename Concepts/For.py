variavel = ["Thamires" ,"Maria"]
T = False

for x in variavel:
    if x.lower().startswith('t'): #lower, transforma a variável em minúscula e startswith verifica primeiro caractere
        T = True
if T:
    print('Existe uma palavra que começa com T')
else:
    print('Nao existe uma palavra que começa com T')
#break quebra o laço
#continue o laço até a próxima iteração