# sort() 정렬은 O(nlog(n))
# 자연수 범위 10000까지 정해져있음. for문 이용 시간복잡도 O(n)으로 풀이
# 수를 직접 리스트에 저장하는 게 아님
# count 리스트의 인덱스 번호에 +1씩 추가하여 인덱스로 수를, 배열 값으로 갯수를 알 수 있게 함
# 

import sys

N = int(input())
count = [0] * 10001

for _ in range(N):
    num = int(sys.stdin.readline())
    count[num] += 1


for i in range(10_001):
    if count[i] != 0:
        for _ in range(count[i]):
            print(i)
