from sys import stdin

inp = stdin.readline
words = []

for _ in range(int(inp().rstrip())):
    words.append(inp().rstrip())

DEC, INC = sorted(words, reverse=True), sorted(words)
if DEC == words:
    print("DECREASING")
elif INC == words:
    print("INCREASING")
else:
    print('NEITHER')
