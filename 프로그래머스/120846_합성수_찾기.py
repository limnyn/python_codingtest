# https://school.programmers.co.kr/learn/courses/30/lessons/120846


def solution(n):
    nums = [0] * 101
    for i in range(2, n):
        for j in range(2, n):
            if i * j <= 100:
                nums[i * j] = 1
            else:
                break
    if n < 4:
        return 0
    else:
        return sum(nums[4 : n + 1])
