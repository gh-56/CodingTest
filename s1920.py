N = int(input())
AN = list(map(int, input().split()))
M = int(input())
AM = list(map(int, input().split()))

AN_dict = {}
for i in range(N):
    AN_dict[AN[i]] = True

for i in AM:
    if i in AN_dict:
        print(1)
    else:
        print(0)

# print(N)
# print(AN)
# print(M)
# print(AM)