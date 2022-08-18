from sys import stdin
from math import factorial
a, b = map(int, stdin.readline().split())
print(factorial(a) // factorial(b) // factorial(a - b))