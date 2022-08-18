from sys import stdin

nums = {}
num_max = 0

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    if num_max < n:
        num_max = n

    if n not in nums:
        nums[n] = 1
    else:
        nums[n] += 1


for i in range(1, num_max + 1):
    if i in nums:
        for j in range(nums[i]):
            print(i)
