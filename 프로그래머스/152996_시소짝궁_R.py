# https://school.programmers.co.kr/learn/courses/30/lessons/152996


# weights = [200, 200, 200, 300, 300, 600]
weights = [100, 200, 300, 400, 800, 600]  # 8

# {200: 1, 300: 1, 400: 2, 600: 2, 800: 2, 900: 1, 1200: 2, 1600: 1}
# 100 200 300 400

# 100 200 = 100:4 200:2  400
# 200 300 = 200:3 300:2  600
# 200 400 = 200:4 400:2  800
# 300 400 = 1200 1200    1200
# 400 800 = 1600 1600    1600
# 300 600 = 1200         1200
# 400 600 = 1200         1200


#     2   3    4
# 100 200 300  400
# 200 400 600  800
# 300 600 900  1200
# 400 800 1200 1600
# 800 1600 2400   /
# 600 1200 1800 2400

"""

"""


from collections import Counter


def solution(weights):
    answer = 0
    counter = Counter(weights)
    for w, c in counter.items():
        if c > 1:
            answer += c * (c - 1) // 2

    weights = list(set(weights))

    ratio = [1 / 2, 2 / 3, 3 / 4]
    for w in weights:
        for r in ratio:
            if w * r in weights:
                answer += counter[w * r] * counter[w]

    return answer


# def solution(weights):
#     answer = 0
#     count = Counter(weights)
#     for k, v in count.items():
#         print(k, v)
#         if v > 1:
#             answer += v * (v - 1) / 2  # nC2

#     # 같은거는 nc2로 계산
#     print(count)
#     weights = list(set(weights))
#     check = (3 / 4, 2 / 3, 1 / 2)
#     for w in weights:
#         for c in check:
#             if w * c in weights:
#                 print(w * c, w, c, count[w * c], count[w])
#                 answer += count[w] * count[w * c]

#     return answer


print(solution(weights))
