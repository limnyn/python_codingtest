min_cycle = float('inf')
for start in range(n):
    if fan_in[start] == 0:  # 불필요한 연산을 줄이기 위해
        continue
    visited = [False] * n
    dq = deque([])
    dq.append((start, 0))
    
    while dq:
        node, cost = dq.popleft()
        
        for next_node in graph[node]:
            if next_node == start:  # 사이클이 형성된 경우
                min_cycle = min(min_cycle, cost + 1)
                dq = deque()  # 큐를 비워서 즉시 종료
                break
            if not visited[next_node]:
                visited[next_node] = True
                dq.append((next_node, cost + 1))
    
    visited[start] = True  # 현재 노드 시작의 방문 처리

if min_cycle == float('inf'):
    return 2

if min_cycle < n - 1:
    return min_cycle + 1

else:
    return -1

