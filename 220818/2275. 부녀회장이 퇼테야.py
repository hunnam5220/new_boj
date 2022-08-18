from sys import stdin

for _ in range(int(stdin.readline())):
    a, b = int(stdin.readline()), int(stdin.readline())
    first = [i for i in range(1, b + 1)]
    for i in range(a):
        for i in range(1, b):
            first[i] += first[i - 1]

    print(first[-1])