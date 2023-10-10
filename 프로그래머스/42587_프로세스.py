# https://school.programmers.co.kr/learn/courses/30/lessons/42587


from collections import deque


def solution(priorities, location):
    # lst =[]
    # for i, p in enumerate(priorities):
    #     lst.append([p,i])
    dq = deque([[i, p] for i, p in enumerate(priorities)])
    i = 0
    result = []
    process = dq.popleft()
    while dq:
        if process[0] < max(dq)[0]:
            dq.append(process)
        else:
            result.append(process[1])
            i += 1
        process = dq.popleft()

    result.append(process[1])

    loc = result.index(location)

    return loc + 1
