import sys
strings = []
while True:
    string = sys.stdin.readline().rstrip()
    if string == '.':
        break
    strings.append(string)

for st in strings:
    stack = []
    for s in st:
        if s == '(':
            stack.append(s)
        elif s == '[':
            stack.append(s)
        elif s == ')':
            if stack:
                if stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(s)
            else:
                stack.append(s)
                break
        elif s == ']':
            if stack:
                if stack[-1] == '[':
                    stack.pop()
                else:
                    stack.append(s)
            else:
                stack.append(s)
                break
    if not stack:
        print('yes')
    else:
        print('no')