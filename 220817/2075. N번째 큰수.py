from sys import stdin
import heapq

n = int(stdin.readline())
nums = []

for _ in range(n):
    arr = list(map(int, stdin.readline().split()))
    for i in arr:
        if len(nums) < n:
            heapq.heappush(nums, i)
        else:
            if nums[0] < i:
                heapq.heappop(nums)
                heapq.heappush(nums, i)

nums.sort()
print(nums[0])