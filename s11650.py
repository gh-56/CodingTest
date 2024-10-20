N = int(input())
coordinates = []
for _ in range(N):
    coordinates.append(list(map(int, input().split())))
    
coordinates.sort(key=lambda x:(x[0], x[1]))

for c in coordinates:
    print(c[0], c[1])