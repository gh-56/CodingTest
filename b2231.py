N = int(input())

a = 0
for num in range(N):
    answer = 0
    num = str(num)
    for n in num:
        answer += int(n)
    num = int(num)
    answer += num
    if answer == N:
        a = num
        break
    else:
        answer = 0
        
print(a)

