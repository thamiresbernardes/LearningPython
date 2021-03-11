#Função range (Start, Stop, Step)
# continue - pula para o próximo laço
#break - termina o laço

for n in range(1,100,5):
    print(n)

print("Testando For")
string = 'thamires'
novastring = ''

for letra in string:
    if letra == 'h':
        novastring = novastring + letra.upper() #upper coloca a letra em maiusculo
    elif letra == 'i':
        novastring += letra.upper()
    else:
        novastring += letra
print(novastring)