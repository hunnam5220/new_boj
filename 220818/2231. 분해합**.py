from sys import stdin

n = int(stdin.readline())

for i in range(1, n + 1):
    if n == sum(list(map(int, list(str(i))))) + i:
        print(i)
        break

    if i == n:
        print(0)