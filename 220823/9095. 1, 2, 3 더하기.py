from sys import stdin


def solve(n):
    if n == 0:
        global ans
        ans += 1
        return

    for i in range(1, 4):
        if n - i > -1:
            solve(n - i)


for _ in range(int(stdin.readline())):
    ans = 0
    n = int(stdin.readline())
    solve(n)
    print(ans)