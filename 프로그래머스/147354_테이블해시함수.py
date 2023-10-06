# https://school.programmers.co.kr/learn/courses/30/lessons/147354

"""
정렬
    1. col번째 값을 기준으로 튜플들을 오름차순 정렬,
    2. 만약 같다면 기본키(0번열)값을 기준으로 내림차순

r_b~r_e의 s_i에 대해
{4, 2, 9}, {2, 2, 6}, {1, 5, 10}, {3, 8, 3} 에 대해
S_i를 i번째 행의 튜플에 대해 각 컬럼의 값을 i로 나눈 나머지들의 합으로 정의
s_2 = 0+0+0 = 0
s_3 = 1+2+1 = 4

"""


def solution(data, col, row_begin, row_end):
    # 1. 정렬
    # data = sorted(sorted(data, key=(lambda x: -1 * x[0])), key=(lambda x: x[col - 1]))
    data = sorted(data, key=lambda x: (x[col - 1], -x[0]))

    # 2. s_i 계산
    s_i = []
    for i in range(row_begin, row_end + 1):
        s_i_sum = 0
        for d in data[i - 1]:
            s_i_sum += d % i
        s_i.append(s_i_sum)

    # 3. list 내부 bitwise연산
    answer = s_i[0]
    for s in s_i[1:]:
        answer ^= s

    return answer


data = [[2, 2, 6], [1, 5, 10], [4, 2, 9], [3, 8, 3]]
col = 2
row_b = 2
row_e = 3
print(solution(data, col, row_b, row_e))
