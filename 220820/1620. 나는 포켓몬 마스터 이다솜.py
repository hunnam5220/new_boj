from sys import stdin
name_num = {}
num_name = {}
n, m = map(int, stdin.readline().split())
for x in range(1, n + 1):
    name = stdin.readline().rstrip()
    name_num[name] = x
    num_name[x] = name

for _ in range(m):
    data = stdin.readline().rstrip()
    if data.isdigit():
        print(num_name[int(data)])
    else:
        print(name_num[data])