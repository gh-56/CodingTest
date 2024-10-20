import sys
N = int(input())
stack_list = []
stack = []

for _ in range(N):
    command = sys.stdin.readline()
    stack_list.append(command)

for s in stack_list:
    if s.split()[0] == 'push':
        stack.append(s.split()[1])
    elif s.split()[0] == 'pop':
        if not stack:
            print(-1)
        else:
            print(stack.pop())
    elif s.split()[0] == 'size':
        print(len(stack))
    elif s.split()[0] == 'empty':
        if not stack:
            print(1)
        else:
            print(0)
    elif s.split()[0] == 'top':
        if not stack:
            print(-1)
        else:
            print(stack[-1])