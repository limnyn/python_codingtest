# https://www.acmicpc.net/problem/1005

'''
[목표]
    특정 건물을 가장 빨리 지을 때까지 걸리는 최소시간 출력

[접근]
    DAG(방향성 비순환 그래프) + 위상정렬을 이용하자

    [ 각 노드별로 건설 완료 시간을 어떻게 구할까? ]
        위상정렬 완료 된 시간을 다음 Task에 전달해 주고
        전달받은 Task는 그 시간부터 count 한다. 
        이 때, 가장 늦게 끝난 Task 까지 기다려야 한다
            -> 이전 Task 중에 마지막으로 끝난 Task의 완료 시간을 다음 Task의 시작 시간으로 지정해준다

'''

from collections import deque
import sys
input = sys.stdin.readline

def calc_build_time(w):
    '''
    Kahn 알고리즘을 통해 fan_in의 count를 통해 위상정렬을 수행한다
    이때, 이전 Task 중에 마지막으로 끝난 Task의 완료 시간을 다음 Task의 시작 시간으로 지정해준다
    '''
    dq = deque([])
    start_times = [0]*n
    for i in range(n):
        if fan_in[i] == 0:
            dq.append(i)

    while dq:
        node = dq.popleft()

        if node == w:
            return start_times[node] + build_times[node]

        for next in graph[node]:
            fan_in[next] -= 1
            if start_times[next] < start_times[node] + build_times[node]:
                start_times[next] = start_times[node] + build_times[node]

            if fan_in[next] == 0:
                dq.append(next)


if __name__ == "__main__":
    t = int(input())
    
    for _ in range(t):
        n, k = map(int, input().split())
        
        graph = [[] for _ in range(n)]
        fan_in = [0]*n
        
        build_times = list(map(int, input().split()))
        
        for _ in range(k):
            before, after = map(int, input().split())
            graph[before-1].append(after-1)
            fan_in[after - 1] += 1
        
        w = int(input())
        
        print(calc_build_time(w-1))


