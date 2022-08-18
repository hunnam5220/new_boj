from sys import stdin

while 1:
    res = sum(map(int, stdin.readline().split()))
    if res == 0:
        break
    print(res)