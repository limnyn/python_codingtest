# https://school.programmers.co.kr/learn/courses/30/lessons/176962


# 시작되기로 한 시각에 과제 시작
# 중단된 과제들 중 가장 최근에 멈춘 과제부터 시작

# 과제 계획을 담은 이차원 문자열 배열
plans = [["aaa", "12:00", "20"], ["bbb", "12:10", "30"], ["ccc", "12:40", "10"]]
# 과제를 끝낸 순서대로 출력해야 한다.

# 시간을 전부 숫자로 변환한다면?

from collections import deque


def solution(plans):
    answer = []
    schedule = []

    # plans는 name, start, playtime으로 구성되어 있다.
    for name, start, playtime in plans:
        time = 60 * (int(start[:2])) + int(start[3:])
        schedule.append([time, int(playtime), name])
    schedule.sort()
    dq = deque(schedule)

    wait = []  # [시간, 과목명]

    now_start, now_time, now_name = dq.popleft()

    while dq:
        next_start, next_time, next_name = dq.popleft()
        temp = now_start + now_time

        # 과제가 끝났을 때, 새로시작되는 과제가 있다면 새로 시작해야하는 과제부터 진행
        if temp == next_start:
            answer.append(now_name)

        # 과제가 끝나고 시간이 남으면 멈춰둔 과제를 이어서 진행한다.
        elif temp < next_start:
            answer.append(now_name)
            exist_time = next_start - temp

            while wait:
                wait_time, wait_name = wait.pop()

                exist_time -= wait_time
                if exist_time > 0:
                    answer.append(wait_name)
                elif exist_time == 0:
                    # 바로 다음거로
                    answer.append(wait_name)
                    break
                elif exist_time < 0:
                    # 남은거 다시 넣기
                    wait.append([exist_time * (-1), wait_name])
                    break

        # 과제가 끝나기 전에 새로 시작되는 과제가 있다면
        else:
            wait_time = temp - next_start
            wait.append([wait_time, now_name])

        now_start = next_start
        now_time = next_time
        now_name = next_name

    answer.append(now_name)
    while wait:
        wait_time, wait_name = wait.pop()
        answer.append(wait_name)
    return answer


# def solution(plans):
#     plans = sorted(
#         map(lambda x: [x[0], int(x[1][:2]) * 60 + int(x[1][3:]), int(x[2])], plans),
#         key=lambda x: -x[1],
#     )
#     # 시작 시간 기준 내림차순

#     lst = []  # 과제들이 각각 끝나는 시간을 담을 리스트

#     while plans:
#         x = plans.pop()  # 가장 빠른 시작시간의 과제
#         for i, v in enumerate(lst):
#             if v[0] > x[1]:  # 만약 먼저 시작했던 과제의 끝나는 시간이, 지금 과제의 시작시간보다 크다면
#                 lst[i][0] += x[2]  # 먼저 시작한 과제들은 지금 과제가 끝날 때 까지 걸리는 시간만큼 더 늦게 끝나니까
#         lst.append([x[1] + x[2], x[0]])  # 이후 리스트에 현재 과제의 종료시간 추가
#     lst.sort()  # 오름차순 정렬

#     return list(map(lambda x: x[1], lst))


print(solution(plans))
