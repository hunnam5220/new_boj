from sys import stdin

res = 0
for i in list(map(int, stdin.readline().split())):
    if i == 0:
        continue
    else:
        res += i ** 2

print(str(res)[-1])