# https://www.acmicpc.net/problem/2252
'''
[목표]
키 순서대로 줄을 세운다.
일부 학생들의 키를 비교한 결과가 주어졌을 때, 줄을 세워 출력

[접근]
우선순위가 존재하므로 위상정렬을 사용해 해결하자

'''
from collections import deque
import sys
input = sys.stdin.readline

def topological_sort(fan_in):
    '''
    1. fan in이 0인 노드들을 queue에 삽입
    
    2. queue에서 하나를 pop 하고 출력
    3. 인접노드들에 대해 fan_in[인접노드] -= 1
        3-1. 해당 fan_in[인접노드] == 0 인 경우 queue에 push
    
    2~3 반복
    '''
    
    dq = deque([])
    
    for i in range(n):
        if fan_in[i] == 0:
            dq.append(i)
    
    while dq:
        node = dq.popleft()
        print(node + 1, end=' ')

        for next in graph[node]:
            fan_in[next] -= 1
            if fan_in[next] == 0:
                dq.append(next)
    


if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    fan_in = [0] * n

    for _ in range(m):
        src, dst = map(int, input().split())
        src -= 1
        dst -= 1
        graph[src].append(dst)
        fan_in[dst] += 1
    topological_sort(fan_in)


    

