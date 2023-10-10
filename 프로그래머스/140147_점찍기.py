# https://school.programmers.co.kr/learn/courses/30/lessons/140107

"""
x,y에 대해
y = int((d**2 - x**2)**0.5)  // k + 1개
"""


def solution(k, d):
    count = 0
    for x in range(0, d + 1, k):
        y = int((d**2 - x**2) ** 0.5)  # (y,0)좌표 포함
        count += y // k + 1  # 0,y 좌표들을 포함하기 위해서 + 1
    return count


print(solution(1, 5))
