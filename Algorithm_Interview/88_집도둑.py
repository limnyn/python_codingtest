# 당신은 전문털이범이다. 어느 집에서든 돈을 훔쳐올 수 있지만 경보 시스템 때문에 바로 옆집은 훔칠 수 없고 한 칸 이상 떨어진 집만 가능하다
# 각 집에는 훔칠 수 있는 돈의 액수가 입력값으로 표기되어 있다. 훔칠 수 있는 가장 큰 금액을 출력하라.

houses = [2,7,9,3,1]


def rob(houses):
    dp = [0] * len(houses) 
    dp[0], dp[1] = houses[0], max(houses[0], houses[1])
    for i in range(2, len(houses)):
        dp[i] = max(dp[i-1], houses[i]+dp[i-2])
    return dp[len(houses)-1]

print(rob(houses))

