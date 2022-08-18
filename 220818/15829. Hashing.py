from sys import stdin

d = {chr(x): x - 96 for x in range(97, 123)}
n = int(stdin.readline())
ans, string = 0, stdin.readline().rstrip()
for s in range(len(string)):
    ans += (d[string[s]] * (31 ** s))
print(ans % 1234567891)