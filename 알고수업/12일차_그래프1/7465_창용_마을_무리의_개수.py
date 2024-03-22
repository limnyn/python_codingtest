'''
서로 집합에 속해있는지 비교하고, 
해당하는 집합의 개수를 세는 문제

1 <= m <= n <= 100
counting cells in blob 처럼 bfs를 돌며 
집합이 몇 개 있는 지 찾을 수 있을 것 같다.

두 정수 
'''
from collections import deque
def solution():
    n, m = map(int, input().split())
    visited = [False]* n
    grid = [[] for _ in range(n)] 
    for _ in range(m):
        i, j = map(int, input().split())
        grid[i-1].append(j-1)
        grid[j-1].append(i-1)

    cnt = 0

    for start in range(n):
        if visited[start]:
            continue
        

        dq = deque([])
        visited[start] = True
        dq.append(start)
        while dq:
            node = dq.popleft()
            for neigibor in grid[node]:
                if visited[neigibor] == False:
                    visited[neigibor] = True
                    dq.append(neigibor)
        
        cnt += 1

    return cnt

for t_c in range(1, int(input()) + 1):
    print(f"#{t_c} {solution()}")


