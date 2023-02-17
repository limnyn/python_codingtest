# 피보나치 수를 구하라.

N = 10

# 타뷸레이션, 상향식
def fibo_dp(n):
    dp = [0]*(n+1)
    dp[1] = 1

    def fibo(i):
        dp[i] = dp[i-1] + dp[i-2]
    
    for i in range(2, n+1):
        fibo(i)
    return dp[n]

print(fibo_dp(N))

# 두 변수만 이용해 공간 절약
def fibo_dp(n):
    x, y = 0, 1

    for _ in range(0,n):
        x, y = y, x + y
    return x

print(fibo_dp(N))
    


    