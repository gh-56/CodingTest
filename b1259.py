nums = []
while True:
    nums.append(input())
    if nums[-1] == '0':
        nums.pop()
        break

for num in nums:
    if num == num[::-1]:
        print('yes')
    else:
        print('no')