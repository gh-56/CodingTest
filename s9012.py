import sys
N = int(input())
parenthesis = [sys.stdin.readline().rstrip() for _ in range(N)]

stack = []

for i in range(N):
    for p in parenthesis[i]:
        if p == '(':
            stack.append(p)
        elif p == ')' and stack:
            stack.pop()
        elif not stack:
            stack.append(p)
            break
    if not stack:
        print('YES')
    else:
        print('NO')
    stack = []
        

    