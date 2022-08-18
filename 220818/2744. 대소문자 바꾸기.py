from sys import stdin

res = ''
for i in stdin.readline().rstrip():
    res += i.upper() if i.islower() else i.lower()
print(res)