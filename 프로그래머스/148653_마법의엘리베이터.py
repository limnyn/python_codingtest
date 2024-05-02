# https://school.programmers.co.kr/learn/courses/30/lessons/148653#
# 5678

# 2
# 5680
# 2
# 5700
# 3
# 6000
# 4
# 10000
# 1

storey = 5678
"""

if 5 초과
    올린다
elif 5일 때
    맨 앞자리가 아닐 때
        앞자리가 만약 5이상이면 올라가고
    맨앞자리면 내림 
else 5 미만일 때
    내린다
"""
from collections import deque


def solution(sotrey):
    count = 0
    dq = deque([int(x) for x in str(sotrey)])
    while dq:
        num = dq.pop()
        if num > 5:
            count += 10 - num
            if len(dq) != 0:
                dq[-1] += 1
            else:
                dq.appendleft(1)
            continue
        elif num == 5:
            if len(dq) != 0:
                if dq[-1] >= 5:
                    count += 10 - num
                    dq[-1] += 1
                    continue
        count += num

    return count


print(solution(storey))
