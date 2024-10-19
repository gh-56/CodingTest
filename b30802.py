N = int(input())
sizes = list(map(int, input().split()))
T, P = map(int, input().split())
count = 0
for s in sizes:
    if s == 0:
        continue
    if s > T:
        count += s // T
        if s % T > 0:
            count += 1
    else:
        count += 1

p_count_1 = N // P
p_count_2 = N % P
        
print(count)
print(p_count_1, p_count_2)