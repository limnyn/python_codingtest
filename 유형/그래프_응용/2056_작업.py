# https://www.acmicpc.net/problem/2056
"""
[문제]
작업들이 주어질 때, 작업간에 선행 관계가 존재한다.
모든 작업을 완료하기 위해 필요한 최소 시간을 구하여라.
서로 선행 관계가 없는 작업들은 동시에 수행 가능하다.

[접근]
위상정렬 + DP
BFS
"""
import sys
from collections import deque

def input(): return sys.stdin.readline().rstrip()

def main():
    n = int(input())

    indegree = [0] * (n + 1)  # 각 작업의 진입 차수 (선행 작업 수)
    work_time = [0] * (n + 1) # 각 작업 수행 시간
    graph = [[] for _ in range(n + 1)] # 선행 작업 리스트
    finish_time = [0] * (n + 1) # 최소 완료 시간 저장

    for i in range(1, n + 1):
        arr = list(map(int, input().split()))
        work_time[i] = arr[0]  # 현재 작업 소요 시간
        for pre in arr[2:]:  # 선행 작업이 존재하는 경우
            graph[pre].append(i)  # 선행 작업 -> 현재 작업 간선 추가
            indegree[i] += 1  # 진입 차수 증가

    # 위상 정렬 (BFS)
    q = deque()
    for i in range(1, n + 1):
        if indegree[i] == 0:  # 선행 작업이 없는 경우
            q.append(i)
            finish_time[i] = work_time[i]

    while q:
        cur = q.popleft()
        for next_task in graph[cur]:
            indegree[next_task] -= 1
            finish_time[next_task] = max(finish_time[next_task], finish_time[cur] + work_time[next_task])
            if indegree[next_task] == 0:
                q.append(next_task)

    print(max(finish_time))  # 전체 작업 완료 시간 중 최대값 출력

if __name__ == "__main__":
    main()
