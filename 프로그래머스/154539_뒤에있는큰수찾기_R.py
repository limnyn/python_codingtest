# https://school.programmers.co.kr/learn/courses/30/lessons/154539


numbers = [9, 1, 5, 3, 6, 2]

import heapq


# 스택 풀이
def solution(numbers):
    num_len = len(numbers)

    answer = [-1] * num_len
    stack = []
    for i in range(num_len):
        while stack and numbers[stack[-1]] < numbers[i]:
            answer[stack.pop()] = numbers[i]
        stack.append(i)

    return answer


# 힙을 사용한 풀이도 존재
# from heapq import heappop, heappush


# def solution(numbers):
#     answer = [-1 for _ in range(len(numbers))]
#     heap = [(numbers[0], 0)]
#     for i, n in enumerate(numbers[1:]):
#         while heap and heap[0][0] < n:
#             _, idx = heappop(heap)
#             answer[idx] = n
#         heappush(heap, (n, i + 1))
#     return answer


print(solution(numbers))
