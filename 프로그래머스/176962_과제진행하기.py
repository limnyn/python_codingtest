# https://school.programmers.co.kr/learn/courses/30/lessons/176962


# 시작되기로 한 시각에 과제 시작
# 중단된 과제들 중 가장 최근에 멈춘 과제부터 시작

# 과제 계획을 담은 이차원 문자열 배열
plans = [["korean", "11:40", "30"], ["english", "12:10", "20"], ["math", "12:30", "40"]]
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
            # now_start = next_start
            # now_time = next_time
            # now_name = next_name

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
        # print(dq)
        # print(wait)

    answer.append(now_name)
    while wait:
        wait_time, wait_name = wait.pop()
        answer.append(wait_name)
    return answer


print(solution(plans))
