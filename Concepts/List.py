l1 = [1, 2, 3, 6, 5, 8, 9, 12]
l2 = [v * 2 for v in l1]
l3 = [(v, v2) for v in l1 for v2 in range(2)]
l4 = ['Thamires', 'Bernardes', 'Estuda', 'Python']
l5 = [v.replace('a', '@').upper() for v in l4]

print(l1)
print(l2)
print(l3)
print(l4)
print(l5)
