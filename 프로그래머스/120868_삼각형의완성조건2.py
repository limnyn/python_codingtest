# https://school.programmers.co.kr/learn/courses/30/lessons/120868

# 선분 세개로 삼각형을 만들기 위해서는 다음과 같은 조건을 만족해야 한다.
# - 가장 긴 변의 길이는 다른 두 변의 길이의 합보다 작아야 한다
# 두 변의 길이가 담긴 배열이 주어지면 나머지 한 변이 될 수 있는 정수의 개수를 return

# [a,b]일 때 c가 될수 있는 갯수는?


# case 1 : b가 제일 길 때 a
# case 2 : c가 제일 길 때 a - 1
def solution(sides):
    return 2 * min(sides) - 1


sides = [[1, 2], [3, 6], [11, 7]]
for side in sides:
    print(solution(side))
