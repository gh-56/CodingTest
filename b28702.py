str1 = input()
str2 = input()
str3 = input()
target = 0

if str1 != 'Fizz' and str1 != 'Buzz' and str1 != 'FizzBuzz':
    target = int(str1) + 3
elif str2 != 'Fizz' and str2 != 'Buzz' and str2 != 'FizzBuzz':
    target = int(str2) + 2
elif str3 != 'Fizz' and str3 != 'Buzz' and str3 != 'FizzBuzz':
    target = int(str3) + 1

if target % 3 == 0 and target % 5 == 0:
    print('FizzBuzz')
elif target % 3 == 0:
    print('Fizz')
elif target % 5 == 0:
    print('Buzz')
else:
    print(str(target))