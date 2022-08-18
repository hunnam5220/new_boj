from sys import stdin


def solve(sugar):
    ans = int(1e9)
    i = sugar // 5

    for i in range(i, -1, -1):
        if (sugar - 5 * i) % 3 == 0:
            ans = min(ans, i + (sugar - 5 * i) // 3)

    return ans


ans = solve(int(stdin.readline()))
print(ans if ans != int(1e9) else -1)