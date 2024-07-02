# https://www.acmicpc.net/problem/2624
'''
[문제]
    금액, 동전의 가지 수, 각 동전 하나의 금액과 갸수가 주어질 때
    지폐를 동전으로 교환하는 방법의 가지 수를 계산하는 프로그램
[입력]
    지폐의 금액 0 < T <= 10,000
    동전의 가지 수 0 < k <= 100
    동전의 금액 0 < pi < T
    동전의 개수 0 < ni < 1000
[DP]
    wage가 20부터 0까지에 대해
    만약 9원짜리 동전 4개라고 가정하면
    20이 넘지 않기 위해서는 2개 까지만 필요하다. 3개는 27로 초과한다.
    dp[0] = 1로 초기화 한다
    for wage in range(T, -1, -1):
        for k in range(1, 2+1):
            dp[20] += dp[20 - 9*k]
        결과적으로 dp[18]일때 해당값을 수행한다
        dp[18] = dp[18 - 18] + dp [18 - 9] + dp[20] # dp[18-18]은 dp[0], 9원짜리 동전 2개를 사용해서 18원을 만드는 경우를 체크하기위해 dp[0] = 1 값으로 초기화해놓았다.
'''
import sys
def input(): return sys.stdin.readline().rstrip()

if __name__ == "__main__":
    T = int(input())
    k = int(input())
    money = []
    for _ in range(k):
        cost, quantity = map(int, input().split())
        money.append((cost, quantity))

    dp = [0] * (T + 1)
    dp[0] = 1
    for cost, quantity in money:
        for wage in range(T, -1, -1):
            for k in range(1, quantity+1):
                if k * cost <= wage:
                    dp[wage] += dp[wage - cost * k]

    print(dp[-1])
