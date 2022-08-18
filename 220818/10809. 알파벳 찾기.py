from sys import stdin

a = [-1 for _ in range(26)]
s = stdin.readline().rstrip()
for j in range(len(s)):
    i = ord(s[j]) - 97
    if a[i] == -1:
        a[i] = j

print(*a)