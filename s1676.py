N = int(input())

def factorial(num):
    if num > 1:
        return num * factorial(num-1)
    else:
        return 1
    
number = str(factorial(N))
length_number = len(number)
count_zero = 0
for i in range(length_number-1, 1, -1):
    if number[i] != '0':
        break
    else:
        count_zero += 1

print(count_zero)