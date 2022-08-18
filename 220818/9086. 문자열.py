from sys import stdin

for _ in range(int(stdin.readline())):
    s = stdin.readline().rstrip()
    print(s[0] + s[-1])