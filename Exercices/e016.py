l1 = '0123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789'
l2 = [i for i in l1]
print(l2)
print(l1[:10])
l = len(l1)
print(l)
n = 10  # tamanho que quero trazer
l3 = [l1[i:i + n] for i in range(0, l, n)]
l4 = '.'.join(l3)
print(l3)
print()
print(l4)
