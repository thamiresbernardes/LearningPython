from itertools import zip_longest, count

l_a = [1, 3, 5, 7, 9, 10, 11]
l_b = [2, 4, 6, 8]

soma = []
l_soma = [x + y for x, y in zip(l_a, l_b)]  # resolvendo com Python
for i in range(len(l_b)):
    soma.append(l_a[i]+l_b[i])
print(soma)

print(l_soma)
