from sys import stdin

n, m = map(int, stdin.readline().split())
nums = list(map(int, stdin.readline().split()))
nums.sort()
visited = [1 for _ in range(n)]
ans = 0


def solve(res, cnt):
    if res > m:
        return

    if cnt == 3:
        global ans
        ans = max(ans, res)
        return

    for i in range(n):
        if visited[i]:
            visited[i] = 0
            solve(res + nums[i], cnt + 1)
            visited[i] = 1


solve(0, 0)
print(ans)