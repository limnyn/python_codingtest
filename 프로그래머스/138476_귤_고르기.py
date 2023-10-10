def solution(k, tangerine):
    from collections import Counter

    counter = Counter(tangerine).most_common()
    # [(3, 2), (2, 2), (5, 2), (1, 1), (4, 1)] 이런 형태로 반환

    # k에서 하나씩 제외
    answer = 0
    for _, count in counter:
        k -= count
        answer += 1
        if k <= 0:
            return answer


k = 6
tangerine = [1, 3, 2, 5, 4, 5, 2, 3]
print(solution(k, tangerine))
