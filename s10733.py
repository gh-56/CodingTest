import sys
K = int(input())
nums = [int(sys.stdin.readline()) for _ in range(K)]
new = []

for n in nums:
    if n != 0:
        new.append(n)
    elif n == 0:
        if not new:
            continue
        new.pop()

total = 0
for n in new:
    total += n

print(total)