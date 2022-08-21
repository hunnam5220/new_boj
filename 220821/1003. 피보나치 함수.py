from sys import stdin

dp_z = [1, 0, 1, 1]
dp_o = [0, 1, 1, 2]

for i in range(4, 41):
    dp_z.append(dp_z[i - 1] + dp_z[i - 2])
    dp_o.append(dp_o[i - 1] + dp_o[i - 2])

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    print(dp_z[n], dp_o[n])