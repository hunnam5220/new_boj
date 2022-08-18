from sys import stdin

n, m = map(int, stdin.readline().split())
a, b = [], []
for _ in range(n):
    a.append(list(map(int, stdin.readline().split())))

for _ in range(n):
    b.append(list(map(int, stdin.readline().split())))

for i in range(n):
    for j in range(m):
        a[i][j] += b[i][j]

for i in range(n):
    print(*a[i])