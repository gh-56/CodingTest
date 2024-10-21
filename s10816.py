N = int(input())
num_cards = list(map(int, input().split()))
M = int(input())
my_cards = list(map(int, input().split()))

num_cards_dict = {}
for i in range(N):
    if num_cards[i] not in num_cards_dict:
        num_cards_dict[num_cards[i]] = 1
    else:
        num_cards_dict[num_cards[i]] += 1

count = [0] * M

for i in range(M):
    if my_cards[i] in num_cards_dict:
        count[i] = num_cards_dict[my_cards[i]]
            
for c in count:
    print(c, end=' ')