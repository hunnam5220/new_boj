from sys import stdin

n, x = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))
ans = []
for i in arr:
    if x > i:
        ans.append(i)

print(*ans)