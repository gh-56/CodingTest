a, b = map(int, input().split())
def lcm(n, m):
    while m:
        n, m = m, n%m
    return n

print(lcm(a,b))
print(a * b // lcm(a,b))