from sys import stdin
from math import factorial
ans = 0
for i in str(factorial(int(stdin.readline())))[::-1]:
    if i != '0':
        break
    ans += 1
print(ans)