# 경로 찾기
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 1 초	256 MB	37952	22478	16488	58.938%
# 문제
# 가중치 없는 방향 그래프 G가 주어졌을 때, 모든 정점 (i, j)에 대해서, i에서 j로 가는 경로가 있는지 없는지 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 정점의 개수 N (1 ≤ N ≤ 100)이 주어진다. 둘째 줄부터 N개 줄에는 그래프의 인접 행렬이 주어진다. i번째 줄의 j번째 숫자가 1인 경우에는 i에서 j로 가는 간선이 존재한다는 뜻이고, 0인 경우는 없다는 뜻이다. i번째 줄의 i번째 숫자는 항상 0이다.

# 출력
# 총 N개의 줄에 걸쳐서 문제의 정답을 인접행렬 형식으로 출력한다. 정점 i에서 j로 가는 경로가 있으면 i번째 줄의 j번째 숫자를 1로, 없으면 0으로 출력해야 한다.

# 예제 입력 1 
# 3
# 0 1 0
# 0 0 1
# 1 0 0
# 예제 출력 1 
# 1 1 1
# 1 1 1
# 1 1 1
# 예제 입력 2 
# 7
# 0 0 0 1 0 0 0
# 0 0 0 0 0 0 1
# 0 0 0 0 0 0 0
# 0 0 0 0 1 1 0
# 1 0 0 0 0 0 0
# 0 0 0 0 0 0 1
# 0 0 1 0 0 0 0
# 예제 출력 2 
# 1 0 1 1 1 1 1
# 0 0 1 0 0 0 1
# 0 0 0 0 0 0 0
# 1 0 1 1 1 1 1
# 1 0 1 1 1 1 1
# 0 0 1 0 0 0 1
# 0 0 1 0 0 0 0

import sys
input =sys.stdin.readline

def isConneted():
    #플로이드를 응용
    n = int(input())
    graph = []
    for _ in range(n):
        line = list(map(int, input().split()))
        graph.append(line)
    for k in range(n):
        for i in range(n):
            for j in range(n):                
                if graph[i][j] == 0:
                    graph[i][j] = 1 if (graph[i][k] and graph[k][j]) else 0
                #만약 i j가 연결 안되있을 때 i-k-j를 통해 연결되어있으면 1
    
    for g in graph:
        for i in range(len(g)-1):
            print(g[i], end=" ")
        print(g[n-1])
        


isConneted()
