from sys import stdin

for _ in range(100):
    try:
        s = stdin.readline().rstrip()
        print(s)
    except:
        break