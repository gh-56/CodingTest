import math
afternoon, night, goal = map(int, input().split())

# count = 0
# total = 0

# while True:
#     total += afternoon
#     count += 1
#     if total >= goal:
#         break
#     else:
#         total -= night

# print(count)

if (goal - night) // (afternoon - night) == 0:
    print((goal - night) // (afternoon - night))
else:
    print(math.ceil((goal - night) / (afternoon - night)))