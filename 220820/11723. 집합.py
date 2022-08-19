from sys import stdin

res = set()

for _ in range(int(stdin.readline())):
    data = stdin.readline().rstrip().split()

    if len(data) == 2:
        c, x = data[0], int(data[1])
        if c == 'add':
            res.add(x)

        elif c == 'remove':
            res.discard(x)

        elif c == 'check':
            print(1 if x in res else 0)

        elif c == 'toggle':
            if x in res:
                res.discard(x)

            else:
                res.add(x)

    else:
        c = data[0]
        if c == 'all':
            res = set(x for x in range(1, 21))

        elif c == 'empty':
            res = set()
