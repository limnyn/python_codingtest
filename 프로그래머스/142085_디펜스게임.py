# https://school.programmers.co.kr/learn/courses/30/lessons/142085


import heapq


def solution(n, k, enemy):
    e = 0
    hq = []
    for i in range(len(enemy)):
        heapq.heappush(hq, -enemy[i])
        e += enemy[i]
        if n < e:
            if k == 0:
                return i
            k -= 1
            e += heapq.heappop(hq)
    return i + 1


enemy = [4, 2, 4, 5, 3, 3, 1]

print(solution(7, 3, enemy))

# """
# 진행하다가 막히면 이때까지 값 중에 가장 큰 값을 무적권 사용
# """

enemy = [3, 3, 3, 3]
print(solution(2, 4, enemy))
