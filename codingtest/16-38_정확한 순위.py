

# 입력 조건
#     첫째 줄에 학생들의 수 N(2<=N<=500)과 두 학생의 성적을 비교한 횟수 M(2<=M<=10000)이 주어집니다.
#     다음 M개의 각 줄에는 두 학생의 성적을 비교한 결과를 나타내는 두 양의 정수 A와 B가 주어집니다.
#     이는 A번 학생의 성적이 B번 학생보다 낮다는 것을 의미합니다.
# 출력 조건
#     첫째 줄에 성적 순위를 정확히 알 수 있는 학생이 몇 명인지 출력합니다

# 입력 예시
# 6 6
# 1 5
# 3 4
# 4 2
# 4 6
# 5 2
# 5 4

# 출력 예시
# 1


import sys
input = sys.stdin.readline

n, m = map(int, input().split())

print(n, m)

graph = [[0]* n for _ in range(n)]

for _ in range(m):
    start, end = map(int, input().split())
    
    graph[start-1][end-1] = 1
import pprint
pprint.pprint(graph)

for k in range(n):
    for a in range(n):
        for b in range(n):
            if a == b:
                graph[a][b] = 0
                continue
            if graph[a][k] and graph[k][b]:
                graph[a][b] = 1

pprint.pprint(graph)
sums = [0]*n
for i in range(n):
    for j in range(n):
        sums[i] += graph[i][j]
        sums[j] += graph[i][j]
count = 0
for x in sums:
    if x == n-1:
        count+=1        
print(count)
