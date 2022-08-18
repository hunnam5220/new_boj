from sys import stdin


def check(st):
    res = 0
    for s in st:
        if s == '(':
            res += 1

        else:
            res -= 1
            if res < 0:
                return False

    return True if res == 0 else False


for _ in range(int(stdin.readline())):
    print('YES' if check(stdin.readline().rstrip()) else 'NO')