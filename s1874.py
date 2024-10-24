import sys
N = int(input())
nums = [int(sys.stdin.readline()) for _ in range(N)]
stack = []
answer = []
pm_list = []

memo = {}
count = 0
for i in range(N):
    while nums[i] not in memo:
        pm_list.append('+')
        count += 1
        memo[count] = True
        stack.append(count)

    pm_list.append('-')
    answer.append(stack.pop())
    if answer[i] != nums[i]:
        break


if len(answer) == len(nums):
    for i in pm_list:
        print(i)
else:
    print('NO')