# DFS == 깊이 우선 탐색

# 인접 행렬(Adjacency Matrix) : 2차원 배열로 그래프의 연결 관례를 표현하는 방식
# 인접 리스트(Adjacency List) : 리스트로 그래프의 연결 관계를 표현하는 방식

# 5-6.py 인접 행렬 방식 예제




INF = 999999999 # 무한
# 2차원 리스트를 이용해 인접 행렬 표현
graph = [
    [0, 7, 5],
    [7, 0 , INF],
    [5, INF, 0]
]
print(graph)

