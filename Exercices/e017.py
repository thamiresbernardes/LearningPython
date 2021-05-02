# list comprehension

carrinho = []
carrinho.append(('P1', 10.4))
carrinho.append(('P2', 20))
carrinho.append(('P3', 30))
carrinho.append(('P4', 40.56))
carrinho.append(('P5', 50))

total = sum([float(y) for x, y in carrinho])
print(total)
