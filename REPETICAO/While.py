#utilizado para realizar ações enquanto uma condição for verdadeira


n = int(input("Entre com um número: "))
x = n
f = 1
while x > 0:
    f *= x # f= f*x
    x -= 1 # x = x-1
print("o fatorial do número {} é {}:" .format(n,f))