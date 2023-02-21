# 당신은 계단을 오르고 있다. 정상에 도달하기 위해 n 계단을 올라야 한다.
# 매번 각각 1계단 또는 2계단씩 오를 수 있다면 정상에 도달하기 위한 방법은 몇 가지 경로가 되는지 계산하라.


num = 7

def climbStairs(n):
    sum = [0]*(n+1)
    sum[1] = 1
    sum[2] = 2
    for i in range(3, n+1):
        sum[i] = sum[i-1] + sum[i-2] 
    
    return sum[n]

print(climbStairs(num))
        
