from array import array
from math import nextafter


def sort(array):
    for i in range(len(array)):
        min_i = i

        for next in range(i + 1, len(array)):
            if array[next] < array[min_i]:
                min_i = next

        array[i], array[min_i] = array[min_i], array[i]


numeros = [-2, 1, 6, 8, 5, 9, 7, 2, 56, 3, 4, 56, 9]
sort(numeros)
print(numeros)
