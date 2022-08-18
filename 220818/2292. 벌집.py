from sys import stdin

n = int(stdin.readline())
p, cnt = 1, 1
while n > p:
    p += 6 * cnt
    cnt += 1
print(cnt)