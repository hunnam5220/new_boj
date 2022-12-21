from sys import stdin

n, m = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))
prefix = [0 for _ in range(n + 1)]

for i in range(n):
    prefix[i + 1] = prefix[i] + arr[i]

for i in range(m):
    a, b = map(int, stdin.readline().split())
    print(prefix[b] - prefix[a - 1])