from sys import stdin

dp = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]

for i in range(11, 101):
    dp.append(dp[i - 3] + dp[i - 4])

for _ in range(int(stdin.readline())):
    print(dp[int(stdin.readline()) - 1])