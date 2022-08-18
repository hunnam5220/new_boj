from sys import stdin

while 1:
    try:
        a, b = map(int, stdin.readline().split())
        print(a + b)
    except:
        break