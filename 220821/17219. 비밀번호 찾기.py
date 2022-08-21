from sys import stdin

n, m = map(int, stdin.readline().split())
key = {}
for _ in range(n):
    site, passwd = stdin.readline().rstrip().split()
    key[site] = passwd

for _ in range(m):
    site = stdin.readline().rstrip()
    print(key[site])