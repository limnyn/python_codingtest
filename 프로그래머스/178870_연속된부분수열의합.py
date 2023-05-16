# https://school.programmers.co.kr/learn/courses/30/lessons/178870
def solution(sequence, k):
    # return answer
    # 투 포인터로 풀어보자
    goal = 0
    min_set = [1e9, [0, 1e9]]
    l, r = 0, 0
    goal = 0
    while l < len(sequence) and r < len(sequence):
        goal += sequence[r]
        if goal == k:
            if r == l:
                return [l, r]
            elif min_set[0] > r - l:
                min_set = [r - l, [l, r]]
            goal -= sequence[l]
            l += 1
            r += 1
        elif goal < k:
            r += 1
        else:  # goal > k:
            goal -= sequence[l]
            goal -= sequence[r]
            l += 1
            if l > r:
                r += 1

    return min_set[1]
