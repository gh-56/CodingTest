from collections import deque
N, K = map(int, input().split())
q = deque()
new = []
for i in range(1, N+1):
    q.append(i)

count = 0
while len(new) < N:
    a = q.popleft()
    count += 1
    if count == K:
        new.append(a)
        count = 0
    else:
        q.append(a)

print('<', end='')
for i in range(N):
    if i != N-1:
        print(f'{new[i]},', end=' ')
    else:
        print(f'{new[i]}', end='')

print('>', end='')
        

# class Node
#     def __init__(self, value):
#         self.value = value
#         self.next = None
#         self.prev = None

# class DoublyLinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None

#     def append(self, value):
#         new_node = Node(value)
#         if self.head is None:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.next = new_node
#             new_node.prev = self.tail
#             self.tail = new_node
    
#     def pop_at(value, index):
#         curr = Node(value)
#         if self.head