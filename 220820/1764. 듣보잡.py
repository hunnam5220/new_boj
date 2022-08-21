from sys import stdin
n, m = map(int, stdin.readline().split())
allp = {}

for _ in range(m + n):
    s = stdin.readline().rstrip()
    if s in allp:
        allp[s] += 1
    else:
        allp[s] = 1

ans = []
for k, v in allp.items():
    if v != 1:
        ans.append(k)

ans.sort()
print(len(ans))
print(*ans, sep='\n')