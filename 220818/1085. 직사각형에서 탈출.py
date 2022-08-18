from sys import stdin
x, y, w, h = map(int, stdin.readline().split())


ans = min(abs(0 - x), abs(w - x), abs(0 - y), abs(h - y))
print(ans)