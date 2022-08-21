from sys import stdin

n, k = map(int, stdin.readline().split())
coins, ans = [], 0
for _ in range(n):
    coins.append(int(stdin.readline()))

while k != 0:
    coin = coins.pop()
    if coin > k:
        continue

    temp = k // coin
    ans += temp
    k -= temp * coin

print(ans)