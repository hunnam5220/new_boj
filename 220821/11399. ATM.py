from sys import stdin

n = int(stdin.readline())
t = list(map(int, stdin.readline().split()))
t.sort()
for i in range(1, n):
    t[i] += t[i - 1]
print(sum(t))