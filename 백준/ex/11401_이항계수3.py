# https://www.acmicpc.net/problem/11401
# 유사한 문제 boj 이항계수2, swea 5607
n, k = map(int, input().split())
P = 1000000007
def mod_factorial(n, p):
    result = 1
    for i in range(1, n+1):
        result = result * i % p
    return result

top = mod_factorial(n, P)

kfact = mod_factorial(k, P)
n_min_rfact = mod_factorial(n-k, P)
r_n_min_rfact = kfact * n_min_rfact % P
bottom = pow(r_n_min_rfact, P-2, P)
result = top * bottom % P
print(result)


