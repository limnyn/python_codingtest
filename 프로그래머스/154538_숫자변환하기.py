# https://school.programmers.co.kr/learn/courses/30/lessons/154538


from collections import deque


def solution(x, y, n):
    dq = deque([])
    dq.append((y, 0))

    while dq:
        y, count = dq.popleft()

        if y == x:
            return count
        if y < x:
            continue

        count += 1
        if y % 3 == 0:
            dq.append((y // 3, count))
        if y % 2 == 0:
            dq.append((y // 2, count))
        dq.append((y - n, count))

    return -1


print(solution(10, 40, 5))
print(solution(10, 40, 30))
print(solution(2, 5, 4))
