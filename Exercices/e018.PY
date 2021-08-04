from itertools import zip_longest, count

list_1 = [1, 3, 5, 7, 9, 10, 11]
list_2 = [2, 4, 6, 8]

soma = []
l_soma = [x + y for x, y in zip(list_1, list_2)]  # resolvendo com Python
for i in range(len(list_2)):
    soma.append(list_1[i] + list_2[i])
print(soma)

print(l_soma)
