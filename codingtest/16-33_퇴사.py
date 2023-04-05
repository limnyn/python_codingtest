# https://www.acmicpc.net/problem/14501

n = int(input())
time = [] # 각 상담을 완료하는데 걸리는 기간
price = [] # 각 상담을 완료했을 때 받을 수 있는 금액
dp = [0] * (n + 1) # 다이나믹 프로그래밍을 위한 1차원 dp 테이블 초기화

for _ in range(n):
    x, y = map(int, input().split())
    time.append(x)
    price.append(y)
    

max_value = 0
for i in range(n-1, -1, -1): # 6~0
    time_end = time[i] + i
    
    if time_end <= n:
        max_value =  max(price[i]+dp[time_end], max_value)
    dp[i] = max_value
    
print(max_value)
        