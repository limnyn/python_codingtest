# https://www.acmicpc.net/problem/11657
'''
[목표]
    한 목적지에서 나머지 모든 도시로 가는 각각의 최소 비용을 출력하기
    만약 무한으로 시간(가중치)가 줄어든다면 -1 출력

[접근]
    1 <= N <= 500, 1 <= M <= 6000

    "음의 가중치"가 존재할 수 있는 경우의 single - source 최단경로 구하기
    -> 벨만-포드 알고리즘

[벨만 포드 알고리즘]
    대략 3 단계로 이루어진다.
        1. 노드 초기화
        2. 거리 측정
        3. 음수 사이클 체크 과정

    [음수 사이클을 체크 과정]
        2번 - 거리를 측정을 하고.
        한번 더 탐색을 했을 때 여전히 거리가 줄어든다면 음수 사이클이 존재한다는 뜻이다.
        -> 이미 한번 씩 탐색했는데 또 거리가 줄어들면 음수 사이클이 존재하기 때문이다.

[모듈 작성]
    def bellman_ford():

        # 1. 노드 초기화
        distance = [float("inf")]*n
        distance[0] = 0

        # 2.거리 측정
        for _ in range(n-1):
            for node in range(n):
                for end, cost in graph[node]:
                    if distance[end] > distance[node] + cost:
                        distance[end] = distance[node] + cost

        # 3. 음수 사이클 체크하기
        for node in range(n):
            for end, cost in graph[node]:
                if distance[end] > distance[node] + cost:
                    # 음수 사이클 존재 -> -1 출력
                    print(-1)
                    return

        # 음수 사이클이 없을 때 -> 결과 출력                
        for i in range(1, n):
            
            # 해당 노드로 가는 경로가 존재하지 않을 때 -1 출력
            if distance[i] == float('inf'):
                print(-1)
            else:
                print(distance[i])
'''
import sys
input = sys.stdin.readline


def bellman_ford():
    '''
    1. 노드 초기화
    2. 거리 측정
    3. 음수 사이클 체크 과정
    '''

    # 1. 노드 초기화
    distance = [float("inf")]*n
    distance[0] = 0

    # 2.거리 측정
    for _ in range(n-1):
        for node in range(n):
            for end, cost in graph[node]:
                if distance[end] > distance[node] + cost:
                    distance[end] = distance[node] + cost

    # 3. 음수 사이클 체크하기
    for node in range(n):
        for end, cost in graph[node]:
            if distance[end] > distance[node] + cost:
                # 음수 사이클 존재 -> -1 출력
                print(-1)
                return

    # 음수 사이클이 없을 때 -> 결과 출력                
    for i in range(1, n):
        
        # 해당 노드로 가는 경로가 존재하지 않을 때 -1 출력
        if distance[i] == float('inf'):
            print(-1)
        else:
            print(distance[i])


if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    for _ in range(m):
        start, end, cost = map(int, input().split())
        start -= 1
        end -= 1
        graph[start].append((end, cost))
    bellman_ford()


