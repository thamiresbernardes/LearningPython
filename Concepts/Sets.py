s1 = set()  # conjuntos
s1.add(1)
s1.update([2, 4, 5, 6, 3])
print(s1)

l1 = [1, 6, 5, 5, 3, 2, 5, 6, 9, 8, 1]
print(l1)
l2 = set(l1)
print(l2)
l2 = list(l2)
print(l2)
print(l2[-1])

s3 = {2, 3, 6, 10}
s4 = {1, 2, 6, 8, 9, 12}
s5 = s3 | s4  # união
s6 = s3 & s4  # iguais
s7 = s3 - s4
s8 = s4 - s3
s9 = s3 ^ s4
print(s5)
print(s6)
print(s7)
print(s8)
print(s9)
