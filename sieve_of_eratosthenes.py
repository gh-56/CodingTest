import math

n = int(input()) # 2부터 n까지의 모든 수에 대하여 소수 판별

# True면 소수 False면 소수가 아닌 걸로 봄
prime = [True for _ in range(n+1)] # 모든 수 True로 초기화

# 에라토스테네스의 체 알고리즘
for i in range(2, int(math.sqrt(n)) + 1):
    # i를 제외한 i의 모든 배수 지우기
    if prime[i] == True: 
        j = 2
        while i*j <= n:
            prime[i*j] = False
            j += 1
for i in range(2, n+1):
    if prime[i]:
        print(i, end=' ')