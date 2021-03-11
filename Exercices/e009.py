cpf = input('Entre com seu cpf, use apenas os números: ')
newcpf = cpf[:9]
reverse = 10 #contagem regressiva para multiplicação
Total = 0 #variáel para guardar a soma
for x in range(19): # 19 é o número de laços
    if x > 8:
        x -= 9
    Total += int(newcpf[x])*reverse
    reverse -= 1
    if reverse < 2:
        reverse = 11
        d = 11 - (Total % 11)
        if d > 9:
            d = 0
            Total = 0
            newcpf += str(d)
print(cpf)
print(newcpf)