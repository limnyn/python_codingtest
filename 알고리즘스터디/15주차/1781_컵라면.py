# https://www.acmicpc.net/problem/1781
'''
[문제]
    문제, 데드라인, 컵라면 수가 존재한다.

    문제 수 1 <= N <= 200,000    
    데드라인 <= N

    1. 특정 시간까지 풀어야 하는 제한이 존재한다.
    2. 데드라인 까지 문제를 풀면 컵라면을 제공한다.
    3. 가장 많이 컵라면을 모아야 한다.

[접근]
    연료채우기 문제를 응용해보자]

    [정렬 + 우선순위 큐]
    1. 입력의 (데드라인, 컵라면) 쌍에 대해 (내림차순, 내림차순)으로 정렬한다.
        problem_list.sort(key=lambda x: (-x[0], -x[1]))

    2. 가장 마지막 시간부터 0초까지 각 시간별로 최대의 이익을 얻을 수 있는 방법을 선택한다.
        problem_hq = []
        result = 0
        idx = 0
        time = n # 최대 시간
        while time > 0:
            
            # 현재 시간 <= 데드라인 인 문제들을 heap에 넣는다
            while idx < n and problem_list[idx][1] >= time:
                deadline, cup_noodle = problem_list[idx]
                # 파이썬의 최소힙을 사용하기위해 부호 반전
                deadline *= -1
                cup_noodle *= -1
                heapq.heappush(problem_hq, (cup_noodle, deadline))
                idx += 1
            
            # 현재 time에서 가장 많은 컵라면을 얻을 수 있는 문제를 선택해 컵라면을 더한다.
            result -= heapq.heappop(problem_hq)[0]
            time -= 1


'''

import sys, heapq
input = sys.stdin.readline

def cup_noodle_calc():
    problem_hq = []
    result = 0
    idx = 0
    time = n # 최대 시간
    while time > 0:
        
        # 현재 시간 <= 데드라인 인 문제들을 heap에 넣는다
        while idx < n and problem_list[idx][0] >= time:
            deadline, cup_noodle = problem_list[idx]
            # 파이썬의 최소힙을 사용하기위해 부호 반전
            deadline *= -1
            cup_noodle *= -1
            heapq.heappush(problem_hq, (cup_noodle, deadline))
            idx += 1
        
        # 현재 time에서 가장 많은 컵라면을 얻을 수 있는 문제를 선택해 컵라면을 더한다.
        if problem_hq:
            result -= heapq.heappop(problem_hq)[0]
        time -= 1
    return result

if __name__ == "__main__":
    problem_list = []
    
    # 입력
    n = int(input())
    for _ in range(n):
        deadline, cup_noodle = list(map(int, input().split()))
        problem_list.append((deadline, cup_noodle))
    problem_list.sort(key=lambda x: (-x[0], -x[1]))

    print(cup_noodle_calc())
