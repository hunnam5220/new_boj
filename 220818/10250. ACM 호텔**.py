from sys import stdin

for _ in range(int(stdin.readline())):
    h, w, n = map(int, stdin.readline().split())

    num = n // h + 1
    fl = n % h
    if n % h == 0:
        num = n // h
        fl = h

    print(fl * 100 + num)