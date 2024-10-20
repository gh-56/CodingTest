N, K = map(int, input().split())
N_total = 1
K_total = 1
for i in range(K):
    N_total *= N-i
    K_total *= i+1
    
print(int(N_total/K_total)) 