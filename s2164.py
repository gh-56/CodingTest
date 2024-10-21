from collections import deque
N = int(input())
q = deque()
for i in range(1, N+1):
    q.append(i)

while len(q) > 1:
    q.popleft()
    q.append(q.popleft())

print(q.pop())
# N_list = []
# new = []
# answer = 0
# for i in range(N, 0, -1):
    # N_list.append(i)


# while True:
#     N_list.pop()
#     new.append(N_list.pop())
#     new.extend(N_list)
#     N_list = new
#     new = []

#     if len(N_list) == 1:
#         answer = N_list.pop()
#         break
    
# print(answer)