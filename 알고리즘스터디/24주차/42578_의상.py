# https://school.programmers.co.kr/learn/courses/30/lessons/42578
def solution(clothes):
    closet = {}
    for cloth, cloth_type in clothes:
        if closet.get(cloth_type):
            closet[cloth_type] += 1
        else:
            closet[cloth_type] = 1
    answer = 1
    for key, value in closet.items():
        answer *= (value + 1)
    return answer - 1