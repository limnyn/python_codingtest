# https://swexpertacademy.com/main/solvingProblem/solvingProblem.do

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.

for test_case in range(1, T + 1):
    days = int(input())
    costs = list(map(int, input().split()))
    acount = 0
    while costs:
        idx = costs.index(max(costs))
        if idx != 0:
            acount += costs[idx] * (idx) - sum(costs[:idx])
            if idx + 1 == len(costs):
                break
        elif idx == 0:
            if len(costs) == 0:
                break
        costs = costs[idx + 1 :]

    print("#" + str((test_case)) + " " + str(acount))
