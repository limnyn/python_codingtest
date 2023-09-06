# https://school.programmers.co.kr/learn/courses/30/lessons/172927

# dp문제

# 광물은 '주어진 순서대로' 캘 수 있다
# 사용할 수 있는 곡괭이 중 아무거나 하나를 선택해 광물을 캔다.
# 광물을 5개 캐면 사용할 수 없다.

# 한번 사용하기 시작하면 다 쓸 때까지 사용한다.
# 모든 광물을 다 캐거나, 곡괭이가 없을 때까지 캔다.

# 출력 : 최소한의 피로도로 clear


# # 다이아, 철, 돌 순서
# picks = [1, 3, 2]

# # 광물 순서
# minerals = ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]


picks = [1, 0, 0]
minerals = [
    "stone",
    "stone",
    "iron",
    "stone",
    "diamond",
    "diamond",
    "diamond",
    "diamond",
    "diamond",
    "diamond",
]


# 5개에 대해 d3 i2 처럼 식을 만든다
def cost_cal(next_minerals):
    lst = [0, 0, 0]
    for item in next_minerals:
        if item == "diamond":
            lst[0] += 1
        elif item == "iron":
            lst[1] += 1
        else:
            lst[2] += 1

    return lst


def solution(picks, minerals):
    answer = []

    if sum(picks) < len(minerals) // 5:
        for i in range(sum(picks)):
            answer.append(cost_cal(minerals[i * 5 : (i + 1) * 5]))
    else:
        for i in range((len(minerals) // 5) + 1):
            answer.append(cost_cal(minerals[i * 5 : (i + 1) * 5]))
    answer.sort(reverse=True)

    result = 0
    for pick in answer:
        if picks[0] != 0:
            result += sum(pick)
            picks[0] -= 1
            continue
        if picks[1] != 0:
            result += pick[0] * 5 + pick[1] + pick[2]
            picks[1] -= 1
            continue

        if picks[2] != 0:
            result += pick[0] * 25 + pick[1] * 5 + pick[2]
            picks[2] -= 1
            continue

        else:
            break
    return result


print(solution(picks, minerals))
