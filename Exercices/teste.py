import math
import os
import random
import re
import sys

n = int(input())

if n % 2 != 0:  # odd is impar
    print('Weird')
elif(n >= 2) and (n <= 5):
    print("Not Weird")
elif (n >= 6) and (n <= 20):
    print("Weird")
elif n > 20 and n <= 100:
    print('Not Weird')
