import sys
from collections import deque
N = int(input())
queue_list = []
q = deque()
for _ in range(N):
    queue_list.append(sys.stdin.readline().rstrip())

for s in queue_list:
    if s.split()[0] == 'push':
        q.append(int(s.split()[1]))
    elif s.split()[0] == 'pop':
        if not q:
            print(-1)
        else:
            print(q.popleft())
    elif s.split()[0] == 'size':
        print(len(q))
    elif s.split()[0] == 'empty':
        if not q:
            print(1)
        else:
            print(0)
    elif s.split()[0] == 'front':
        if not q:
            print(-1)
        else:
            print(q[0])
    elif s.split()[0] == 'back':
        if not q:
            print(-1)
        else:
            print(q[-1])
