import sys
import math
N = int(input())
nums = [int(sys.stdin.readline()) for _ in range(N)]

# 평균
total = 0
for num in nums:
    total += num

mean = math.floor(total / N + 0.5)

# 중앙값
nums.sort()
median = nums[len(nums) // 2]

# 최빈값
moderate = {}
for i in nums:
    if i not in moderate:
        moderate[i] = 1
    else:
        moderate[i] += 1

max_moderate = max(moderate.values())
modes = [k for k, v in moderate.items() if v == max_moderate]
modes.sort()

# 범위
maximum = -4001
minimum = 4001
for i in nums:
    if i > maximum:
        maximum = i
    if i < minimum:
        minimum = i

print(mean)
print(median)
if len(modes) < 2:
    print(modes[0])
else:
    print(modes[1])
print(maximum - minimum)