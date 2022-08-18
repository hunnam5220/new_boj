from sys import stdin

arr = [x for x in range(1, 31)]
for _ in range(28):
    arr.remove(int(stdin.readline()))

print(*arr, sep='\n')