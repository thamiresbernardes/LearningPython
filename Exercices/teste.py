def verifica(n1):
    if n1 % 3 == 0 and n1 % 5 == 0:
        return "FizzBuzz"
    if n1 % 3 == 0:
        return "Fizz"
    if n1 % 5 == 0:
        return "Buzz"
    return n1


print(verifica(30))
