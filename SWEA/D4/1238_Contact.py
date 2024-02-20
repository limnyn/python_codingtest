
from collections import deque
for t_c in range(1, 11):
    graph = [[] for _ in range(101)]
    n, start = map(int, input().split())
    line = list(map(int, input().split()))
    for i in range(0,n,2):
        s, e = line[i], line[i+1]
        graph[s].append(e)


    dq = deque([])
    dq.append([start,0])
    visited = [start]
    result = []
    while dq:
        sorc, time = dq.popleft()
        count = 0
        for dest in graph[sorc]:
            if dest not in visited:
                visited.append(dest)
                dq.append([dest, time+1])
                count += 1
        if count == 0:
            result.append([sorc, time])
            
    result.sort(key=lambda x: (-x[1], -x[0]))

    print(f'#{t_c} {result[0][0]}')
    