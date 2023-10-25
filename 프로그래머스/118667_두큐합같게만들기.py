# https://school.programmers.co.kr/learn/courses/30/lessons/118667
# https://simsim231.tistory.com/273
from collections import deque


def solution(queue1, queue2):
    answer = 0
    q1 = deque(queue1)
    q2 = deque(queue2)
    k = 600000
    sum_total = sum(q1) + sum(q2)
    sum_q1 = sum(q1)
    sum_q2 = sum(q2)

    while q1 and q2 and k:
        k -= 1

        if sum_total % 2 == 1:
            return -1

        if sum_q1 < sum_q2:
            answer += 1
            tmp = q2.popleft()
            q1.append(tmp)
            sum_q1 += tmp
            sum_q2 -= tmp
        elif sum_q1 > sum_q2:
            answer += 1
            tmp = q1.popleft()
            q2.append(tmp)
            sum_q2 += tmp
            sum_q1 -= tmp

        else:
            return answer

    return -1
    # 만약 ij가 jk보다 크면
    # i, k를 +1
    # 만약 jk가 더 크면
    # j를 +1

    # i~k는 len(q1)*2 유지
    # 만약 i가 len(q1)*3일 때 결과가 안나오면 return -1
    # 결과가 나오면
    # i가 len(q1)이상일 경우에 cnt-len(q1)


# q1 = [3, 2, 7, 2]
# q2 = [4, 6, 5, 1]
# q1 = [101, 100]
# q2 = [102, 103]
q1 = [1, 1]
q2 = [1, 5]
print(solution(q1, q2))


# 11번 테스트케이스 에러
# def solution(queue1, queue2):
#     lst = queue1 + queue2 + queue1 + queue2
#     count = 0
#     i, j, k = 0, len(queue1), 2 * len(queue1)  # 0, 4, 8

#     # 만약 ik - ij == ij가 되면 count 출력
#     ik = sum(lst[i:k])
#     ij = sum(lst[i:j])
#     if ik % 2 == 1:
#         return -1

#     count = 0

#     while 1:
#         if i == len(queue1) * 3:
#             return -1
#         if 2 * ij == ik:  # 좌우가 같을 때
#             return count

#         elif 2 * (ik - ij) < ik:  # 만약 ij가 jk보다 크다면
#             count += 1
#             ij -= lst[i]
#             i += 1
#             k += 1
#         else:  # 만약 ij가 jk보다 작으면
#             count += 1
#             ij += lst[j]
#             j += 1
