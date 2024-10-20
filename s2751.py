import sys
N = int(input())
nums = [int(sys.stdin.readline().rstrip()) for _ in range(N)]
nums.sort(reverse=False)
for i in nums:
    print(i)