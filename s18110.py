from collections import deque
import math
import sys
N = int(input())
nums = []
k = math.floor((N * 0.15) + 0.5)
for _ in range(N):
    nums.append(int(sys.stdin.readline()))

nums.sort()
nums = deque(nums) 
for i in range(k):
    nums.popleft()
    nums.pop()

total = 0
for num in nums:
    total += num

if total == 0:
    print(0)
else:
    print(math.floor((total / len(nums)) + 0.5))