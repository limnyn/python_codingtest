# 3
# 3
# 10 7 6
# 3
# 3 5 9
# 5
# 1 1 3 1 2

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
from collections import deque


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
            # costs = costs[idx+1:]
        elif idx == 0:
            if len(costs) == 0:
                break
        costs = costs[idx + 1 :]

    print("#" + str((test_case)) + " " + str(acount))


# 10 6 7

# 1 1 3 1 2 1

# 3,2
# 2,5

# [1 1 2]
# [2]
# [1]
# -1
# -1
# -2
# 2 * 3 - 4 = 2
