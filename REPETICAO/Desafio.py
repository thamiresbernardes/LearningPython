
x = -1
y = 11

while x < 10 and y > 0 :
    x += 1
    y -= 1
    print(x , y)

#metodo com lista

lista = [9, 8, 7, 6, 5, 4, 3, 2, 1]
lis_enu = list(enumerate(lista, 1))
for n in lis_enu:
    print(n)

#solução do professor
for p , r in enumerate(range(10,-1,-1)):
     print (p, r)
#O tipo da classe range representa uma sequência imutável de números e é comumente usada para fazer um looping um número determinado de vezes por for.