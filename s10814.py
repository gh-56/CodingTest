import sys
N = int(input())
people = []
for i in range(N):
    age, name = map(str, sys.stdin.readline().split())
    age = int(age)
    people.append((age, name))

people.sort(key=lambda x: (x[0]))

for person in people:
    print(person[0], person[1])